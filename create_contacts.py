from faker import Faker
from django.contrib.auth.models import User
from join.models import Color
import random

fake = Faker()

# Hole alle vorhandenen Farben aus der Datenbank
colors = Color.objects.all()

# Anzahl der zu erstellenden Kontakte
num_contacts = 30  # Passe die Zahl nach Bedarf an

for _ in range(num_contacts):
    # Zufällig generierte Daten für die Kontakte
    first_name = fake.first_name()
    last_name = fake.last_name()
    email = fake.email()
    avatar = f"{first_name[0].upper()}{last_name[0].upper()}"  # Avatar als erste Buchstaben
    color = random.choice(colors)

    # Benutzer erstellen
    User.objects.create_user(
        username=f"{first_name.lower()}{last_name.lower()}",
        email=email,
        first_name=first_name,
        last_name=last_name,
        password="password123",  # Ein Standardpasswort
        avatar=avatar,
        color=color
    )

print(f"{num_contacts} Kontakte wurden erstellt.")