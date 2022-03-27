"""
models for trees app.
"""

import string
import random
from django.db import models
from django.template.defaultfilters import slugify


class Feature(models.Model):
    """
    Features of trees
    """
    name = models.CharField(max_length=254)
    # friendly_name and icon is optional
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    icon_fontawsome = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    def get_friendly_name(self):
        """
        returns the name of the feature
        """
        return self.friendly_name


class Enviroment(models.Model):
    """
    general clasification where the tree should be kept
    """

    name = models.CharField(max_length=254)
    # friendly_name and icon is optional
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    icon_fontawsome = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    def get_friendly_name(self):
        """
        returns the name of the category
        """
        return self.friendly_name


class Tree(models.Model):
    """
    class that creates trees table to hold products that
    will be sold by the store
    """
    # these columns are required
    name = models.CharField(max_length=254, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    height_in = models.DecimalField(max_digits=9, decimal_places=2)
    trunk_width_in = models.DecimalField(max_digits=9, decimal_places=2)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    current_stock = models.IntegerField(null=True, blank=True)
    # these columns are optional
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_description = models.CharField(max_length=254, null=True, blank=True)
    image_disclaimer = models.TextField()
    feature = models.ManyToManyField(
                'Feature', blank=True)
    enviroment = models.ForeignKey(
                'Enviroment', null=True, blank=True, on_delete=models.SET_NULL)
    # unique slug solution found on:
    # https://www.geeksforgeeks.org/add-the-slug-field-inside-django-model/

    def random_string_generator(self, size=10, chars=string.ascii_lowercase + string.digits):
        """
        generates a string of characters
        """
        return ''.join(random.choice(chars) for _ in range(size))

    def save(self, *args, **kwargs):
        if not self.slug:
            name_string = slugify(self.name)
            random_characters = self.random_string_generator(size=6)
            slug = f'{name_string}-{random_characters}'
            if slug in self.slug:
                random_characters = self.random_string_generator(size=6)
                slug = f'{name_string}-{random_characters}'
            else:
                self.slug = slug
        super(Tree, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'
