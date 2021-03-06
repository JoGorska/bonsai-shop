"""
models for questions app
"""

from django.db import models
from django.contrib.auth.models import User


STATUS_CHOICES = ((0, "Draft"), (1, "Published"))
NEWSLETTER_CHOICES = ((0, "Not Interested"), (1, "Sign me up"))


class Question(models.Model):
    """
    Model to record user's questions for FAQ page
    """
    header = models.CharField(max_length=254)
    detail = models.TextField()
    answer = models.TextField(blank=True)

    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    image_alt = models.CharField(max_length=254, null=True, blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="questions")
    created_on = models.DateTimeField(auto_now=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True, editable=False)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    class Meta:
        """
        orders the questions by date when it was created,
        the most recent first
        """
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.status} {self.header}"
