from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=64)
    content=models.TextField()

    def __str__(self):
        return "标题：{}，字数：{}，概要：{}".format(self.title,len(self.content),self.content[:18])
