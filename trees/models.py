from django.db import models


class Category(models.Model):
    """
    categories of trees
    """
    class Meta:
        """
        helper class to improve the way categories display in admin
        in plural form
        """
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    # friendly_name is optional
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    def get_friendly_name(self):
        """
        returns the name of the category
        """
        return self.friendly_name


class ExtaFeature(models.Model):
    """
    extra features that make tree stand out
    """

    name = models.CharField(max_length=254)
    # friendly_name is optional
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    def get_friendly_name(self):
        """
        returns the name of the category
        """
        return self.friendly_name


class Enviroment(models.Model):
    """
    general clasification where the tree should be kept
    """

    name = models.CharField(max_length=254)
    # friendly_name is optional
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    def get_friendly_name(self):
        """
        returns the name of the category
        """
        return self.friendly_name


class Size(models.Model):
    """
    size of the tree with description
    """

    name = models.CharField(max_length=254)
    # friendly_name is optional
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    # the smaller value - the smaler the tree, 
    # this will allow to sort the trees by their size
    number = models.IntegerField(max_length=1, null=False, blank=False)

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
    name = models.CharField(max_length=254, null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    extra_feature = models.ForeignKey('ExtraFeature', null=True, blank=True, on_delete=models.SET_NULL)
    enviroment = models.ForeignKey('Enviroment', null=True, blank=True, on_delete=models.SET_NULL)
    size = models.ForeignKey('Size', null=True, blank=True, on_delete=models.SET_NULL)