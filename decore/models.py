"""
These are the development ready abstract models that are available inside decore package.
"""

from django.db import models
from django.template.defaultfilters import slugify


class TimeStamps(models.Model):
    """
    Abtract model that can be inherited to track when an object was created or 
    it was last updated.

    ``created_at`` stores the datetime in which the object was created

    ``updated_at`` stores the datetime in which the object was last updated

    Both these fields are auto updated with their values on object creation and updation.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UniqueSlug(models.Model):
    """
    Abstract model that can be inherited to have a unique slug field. The slug will be
    generated from the field name you provide in ``SLUG_FROM`` attribute.

    """
    SLUG_FROM = 'title'

    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    title = models.CharField(max_length=200)

    class Meta:
        abstract = True

    def _generate_slug(self):
        title = getattr(self, self.SLUG_FROM)

        if title:
            new_slug = slugify(title)

            if self.slug == new_slug:
                return

            slug_exists = self.__class__.objects.filter(slug=new_slug).exists()

            if slug_exists:
                new_slug = "{}-{}".format(new_slug, self.id)

            if self.slug != new_slug:
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
    title = models.CharField(max_length=200)

    class Meta:
        abstract = True

    def _generate_slug(self):
        title = getattr(self, self.SLUG_FROM)

        if title:
            new_slug = slugify(title)

            if self.slug != new_slug:
                self.slug = new_slug
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
