from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import UniqueSlug, Slug


@receiver(post_save)
def generate_slug_on_post_save_of_slug_models(sender, instance, **kwargs):
    if issubclass(sender, UniqueSlug) or issubclass(sender, Slug):
        instance._generate_slug()