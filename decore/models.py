"""
This file contains all the abstract models that can make
a django developers work easy.
"""

from django.db.signals import post_save
from django.db import models
from django.dispatch import receiver
from django.template.defaultfilters import slugify


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


class UniqueSlug(AbstractModel):
    """
    Abstract model that can be inherited to have a unique slug field
    in the model.

    When inhertied will check for slug_from attribute in the model,
    by default slug_from will have value title.

    """
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta(AbstractModel.Meta):
        slug_from = 'title'

    def _generate_slug(self):
        title = getattr(self, self.Meta.slug_from)

        if title:
            new_slug = slugify(title)
            slug_exists = self.__class__.objects.filter(slug=new_slug).exists()

            if slug_exists:
                new_slug = "{}-{}".format(new_slug, self.id)

            self.slug = new_slug
            self.save()


class Slug(AbstractModel):
    """
    Abstract model that can be inherited to have a slug field
    in the model.

    When inhertied will check for slug_from attribute in the model,
    by default slug_from will have value title.

    """
    slug = models.SlugField(max_length=200, db_index=True)

    class Meta(AbstractModel.Meta):
        slug_from = 'title'

    def _generate_slug(self):
        title = getattr(self, self.Meta.slug_from)

        if title:
            self.slug = slugify(title)
            self.save()
