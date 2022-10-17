from django.db import models


class rand(models.Model):
    CATEGORY_FOOD = (
        ('pork', 'pork'),
        ('chicken', 'chicken'),
        #('beef', 'beef'),
        #('fish', 'fish'),
        ('vegetarian', 'vegetarian')
    )
    DIFFICULTY_FOOD = (
        ('easy', 'easy'),
        ('moderate', 'moderate'),
        ('hard', 'hard')
    )
    CUISINE_FOOD = (
        ('american', 'american'),
        ('australian', 'australian'),
        #('chinese', 'chinese'),
        ('european', 'european')
    )
    title = models.CharField(max_length=50)
    method = models.TextField()
    ingredients = models.TextField()
    source_url = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    category = models.CharField(max_length=100,choices=CATEGORY_FOOD)
    difficulty = models.CharField(max_length=100,choices=DIFFICULTY_FOOD)
    cuisine = models.CharField(max_length=100,choices=CUISINE_FOOD)

    def __str__(self):
        return self.title

class Comment(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name