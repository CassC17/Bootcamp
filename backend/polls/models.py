from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=200)
    pub_date =models.DateField("published date")

class Game(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="games") # supp tous les choix si on supp la player
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
