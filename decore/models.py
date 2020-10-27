"""
This file contains all the abstract models that can make
a django developers work easy.
"""

from django.db import models
from django.template.defaultfilters import slugify


class TimeStamps(models.Model):
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

    class Meta:
        abstract = True


class UniqueSlug(models.Model):
    """
    Abstract model that can be inherited to have a unique slug field
    in the model.

    When inhertied will check for slug_from attribute in the model,
    by default SLUG_FROM will have value title.

    """
    SLUG_FROM = 'title'
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        abstract = True

    def _generate_slug(self):
        title = getattr(self, self.SLUG_FROM)

        if title:
            new_slug = slugify(title)
            slug_exists = self.__class__.objects.filter(slug=new_slug).exists()

            if slug_exists:
                new_slug = "{}-{}".format(new_slug, self.id)

            self.slug = new_slug
            self.save()


class Slug(models.Model):
    """
    Abstract model that can be inherited to have a slug field
    in the model.

    When inhertied will check for slug_from attribute in the model,
    by default SLUG_FROM will have value title.

    """
    SLUG_FROM = 'title'

    slug = models.SlugField(max_length=200, db_index=True)

    class Meta:
        abstract = True

    def _generate_slug(self):
        title = getattr(self, self.SLUG_FROM)

        if title:
            self.slug = slugify(title)
            self.save()


class Hidden(models.Model):
    """
    Abstact model that can be inhertied to have hide functionality
    in a model using is_hidden field.

    Use .hide() to hide and .unhide() to unhide an object.
    """
    is_hidden = models.BooleanField(default=False, db_index=True)

    class Meta:
        abstract = True

    def hide(self):
        """
        hides the object if its not hidden
        """
        if not self.is_hidden:
            self.is_hidden = True
            self.save()

    def unhide(self):
        """
        unhide the objects if its hidden
        """
        if self.is_hidden:
            self.is_hidden = False
            self.save()
