from rest_framework import serializers
from join.models import Category, Task, Subtask, User, Color, TaskHistory, Profile

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'name', 'code']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    color = ColorSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'initials', 'color']

class CategorySerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    color = ColorSerializer()

    class Meta:
        model = Category
        fields = ['id', 'name', 'color', 'users']

class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = ['id', 'name', 'done']

class TaskHistorySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = TaskHistory
        fields = ['id', 'user', 'timestamp', 'change_description']

class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubtaskSerializer(many=True)
    history = TaskHistorySerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'duedate', 'category', 'status', 'subtasks', 'history']

    def create(self, validated_data):
        subtasks_data = validated_data.pop('subtasks')
        user = self.context['request'].user
        task = Task.objects.create(**validated_data)
        for subtask_data in subtasks_data:
            Subtask.objects.create(task=task, **subtask_data)
        TaskHistory.objects.create(task=task, user=user, change_description='Task created')
        return task

    def update(self, instance, validated_data):
        subtasks_data = validated_data.pop('subtasks')
        user = self.context['request'].user
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.duedate = validated_data.get('duedate', instance.duedate)
        instance.category = validated_data.get('category', instance.category)
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        for subtask_data in subtasks_data:
            subtask_id = subtask_data.get('id')
            if subtask_id:
                subtask = Subtask.objects.get(id=subtask_id, task=instance)
                subtask.name = subtask_data.get('name', subtask.name)
                subtask.done = subtask_data.get('done', subtask.done)
                subtask.save()
            else:
                Subtask.objects.create(task=instance, **subtask_data)

        TaskHistory.objects.create(task=instance, user=user, change_description='Task updated')
        return instance