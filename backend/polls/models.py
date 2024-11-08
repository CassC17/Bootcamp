from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date =models.DateField("published date")

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="choices") # supp tous les choix si on supp la player
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)
