from django.db import models
from users.models import User

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self) -> str: 
        return self.name

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blogs")
    title = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    content = models.TextField(max_length=255)
    tags = models.ManyToManyField(Tag, related_name="blogs")

    def __str__(self):
        return f"'{self.title}' | {self.date}"

