from django.db import models

class Destination(models.Model):
    continent = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    highlights = models.TextField()
    les_destinations = models.CharField(max_length=250)
    price_include = models.TextField()
    price_exclude = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    photo = models.ImageField(upload_to="media", blank=True, null=True)

    def __str__(self):
        return f"{self.pays} - {self.continent}"

class DayItinerary(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='itineraries')
    day_number = models.PositiveIntegerField()
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField()  # Détails du jour (activités, lieux visités, etc.)
    photo = models.ImageField(upload_to="media", blank=True, null=True)
    photo2 = models.ImageField(upload_to="media", blank=True, null=True)

    class Meta:
        ordering = ['day_number']  # Tri par ordre des jours

    @property
    def duration(self):
        # Nombre total de jours pour les itinéraires associés
        return self.itineraries.count()

    def __str__(self):
        return f"{self.destination} - Day {self.day_number}: {self.title}"

