from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images')
    url = models.URLField(blank=True)
    github_repo = models.URLField(blank=True)
    date = models.DateField()
    tags = models.ManyToManyField(Category)

    class Meta:
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.project_name



