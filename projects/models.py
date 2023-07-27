from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to='images', blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    

class Project(models.Model):
    project_name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    url = models.URLField(blank=True)
    github_repo = models.URLField(blank=True)
    date = models.DateField(null=True)
    tags = models.ManyToManyField(Category, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.project_name

