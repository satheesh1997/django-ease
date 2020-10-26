"""
This file contains all the abstract models that can make
a django developers work easy.
"""

from django.db import models


class AbstractModel(models.Model):
    """
    Abstract model base that can be inherited to create an
    abstract model.
    """
    class Meta:
        abstract = True


class TimeStamps(AbstractModel):
    """
    Abstract model that can be inherited to have the timestamp
    fields (created_at & updated_at) in the model.

    The created_at field gives the datetime in which the object
    is added.
    The updated_at field gives the datetime is which the object
    is last updated.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
