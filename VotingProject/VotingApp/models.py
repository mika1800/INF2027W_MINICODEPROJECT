from django.db import models
from .DatabaseConnection import database

Question_collection = database['Questions']
Choice_collection = database['Choices']

#Creation of Question Class
class Question(models.Model):
    question_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField ('Date Published')

def __str__(self):
    return self.question_text



#Creation of Choice Class
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    choice_text = models.CharField(max_length = 250)
    votes = models.IntegerField(default=0)

def __str__(self):
        return self.choice_text