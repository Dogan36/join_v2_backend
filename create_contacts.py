from faker import Faker
from django.contrib.auth.models import User
from join.models import Color, Profile
import random

# Initialisieren Sie Faker
fake = Faker()

# Hole alle vorhandenen Farben aus der Datenbank
colors = Color.objects.all()

# Sicherstellen, dass Farben vorhanden sind
if not colors:
    print("Keine Farben in der Datenbank gefunden!")
else:
    # Anzahl der zu erstellenden Kontakte
    num_contacts = 30  # Passen Sie die Zahl nach Bedarf an

    # Starten Sie die Erstellung von Kontakten
    for _ in range(num_contacts):
        # Zufällig generierte Daten für die Kontakte
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        avatar = f"{first_name[0].upper()}{last_name[0].upper()}"  # Avatar aus den ersten Buchstaben
        color = random.choice(colors)

        try:
            # Benutzer erstellen
            user = User.objects.create_user(
                username=f"{first_name.lower()}{last_name.lower()}",
                email=email,
                first_name=first_name,
                last_name=last_name,
                password="password123",  # Ein Standardpasswort
            )

            # UserProfile wird automatisch durch das Signal erstellt, aber falls es manuell erstellt werden soll:
            profile = Profile.objects.create(
                user=user,  # Verknüpft das UserProfile mit dem Benutzer
                avatar=avatar,
                color=color  # Wählt eine zufällige Farbe aus den vorhandenen Farben
            )

            print(f"Kontakt für {first_name} {last_name} wurde erstellt.")

        except Exception as e:
            print(f"Fehler bei der Erstellung des Kontakts {first_name} {last_name}: {e}")

    print(f"{num_contacts} Kontakte wurden erstellt.")
