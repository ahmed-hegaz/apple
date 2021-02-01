from django.db import models

class Apple(models.Model):  
    title = models.CharField(max_length=100)
    text = models.ForeignKey('Text', related_name='apple', on_delete=models.CASCADE)


    def __str__(self):
        return self.title


class Text(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)

    def __str__(self):
            return self.title    
