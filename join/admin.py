from django.contrib import admin
from .models import Color, Profile, Category, Task, Subtask

class ProfileAdmin(admin.ModelAdmin):
    # Definiere die Felder, die im Admin-Panel angezeigt werden sollen
    readonly_fields = ['user', 'first_name', 'last_name']  # Ensure 'user' and 'first_name' are fields in the Profile model

    def first_name(self, obj):
        return obj.user.first_name
    first_name.short_description = 'First Name'
    def last_name(self, obj):
        return obj.user.last_name
    last_name.short_description = 'Last Name'
    list_display = ('user', 'avatar', 'color')
    # Hier wird das user-Feld unänderbar gemacht


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Color)
admin.site.register(Category)
admin.site.register(Task)
admin.site.register(Subtask)



# Register your models here.
