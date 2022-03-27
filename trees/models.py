"""
models for trees app.
"""

import string
import random
from django.db import models
from django.template.defaultfilters import slugify

LEAVES_OR_NEEDLES_CHOICES = [
    ('coniferous', 'Coniferous'),
    ('deciduous', 'Deciduous'),
]

IMG_DISCLAIMER_CHOICES = [
        ('standarised', 'This is an image of a typical tree \
                        of this size and shape. We grow and \
                        sell many nearly identical specimen. \
                        The product that you will purchase will be \
                        very similar to the one on the photograph.'),
        ('unique', 'This is an image of the specimen that is being for sale'),
]


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
    # trunk circumference
    # these columns are required
    name = models.CharField(max_length=254, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True, editable=False)
    height_in = models.DecimalField(max_digits=9, decimal_places=2)
    trunk_circumference = models.DecimalField(max_digits=9, decimal_places=2)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    current_stock = models.IntegerField(null=True, blank=True)
    # these columns are optional
    leaves_or_needles = models.CharField(
            max_length=254, choices=LEAVES_OR_NEEDLES_CHOICES,
            default='coniferous', null=True, blank=True)
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_alt = models.CharField(max_length=254, null=True, blank=True)
    image_disclaimer = models.CharField(
            max_length=254, choices=IMG_DISCLAIMER_CHOICES,
            default='standarised',  null=True, blank=True
            )
    feature = models.ManyToManyField(
                'Feature', blank=True)
    enviroment = models.ForeignKey(
                'Enviroment', null=True, blank=True, on_delete=models.SET_NULL)
    # unique slug solution found on:
    # https://www.geeksforgeeks.org/add-the-slug-field-inside-django-model/

    def random_string_generator(self,
                                size=10,
                                chars=string.ascii_lowercase + string.digits):
        """
        generates a string of characters consisting of
        lowercase letters and digits, lenght is set to 10
        """
        return ''.join(random.choice(chars) for _ in range(size))

    def save(self, *args, **kwargs):
        """
        automaticaly generates slug field
        """
        if not self.slug:
            name_string = slugify(self.name)
            random_characters = self.random_string_generator()
            slug = f'{name_string}-{random_characters}'
            # checks if this slug is already in the column slug
            if slug in self.slug:
                random_characters = self.random_string_generator()
                new_slug = f'{name_string}-{random_characters}'
                self.slug = new_slug
            else:
                self.slug = slug
        super(Tree, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'
