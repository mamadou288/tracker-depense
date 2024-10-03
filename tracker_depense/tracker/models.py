from django.db import models
from django.contrib.auth.models import User

class Depense(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    categorie = models.CharField(max_length=255)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f"{self.utilisateur.username} - {self.montant} le {self.date}"
