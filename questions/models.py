"""
models for questions app
"""

from django.db import models
from django.contrib.auth.models import User


STATUS_CHOICES = ((0, "Draft"), (1, "Published"))


class Question(models.Model):
    """
    Model to record user's questions for FAQ page
    """
    header = models.CharField(max_length=254)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name="questions")
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    class Meta:
        """
        orders the questions by date when it was created,
        the most recent first
        """
        ordering = ['-created_on']

    def __str__(self):
        return f"{self.status} {self.header}"
