from django.test import TestCase

from app import models


class TimeStampsTestCases(TestCase):
    def setUp(self):
        self.model = models.TimeStampsModel

    def test_if_the_created_at_and_updated_at_attributes_are_present(self):
        obj = self.model.objects.create()
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))

    def test_if_created_at_is_having_a_datetime_after_creation(self):
        obj = self.model.objects.create()
        self.assertIsNotNone(obj.created_at)

    def test_if_updated_is_getting_updated_on_each_save(self):
        obj = self.model.objects.create()
        last_updated_at = obj.updated_at

        self.assertIsNotNone(obj.updated_at)
        obj.save()
        self.assertNotEqual(obj.updated_at, last_updated_at)


class HiddenTestCases(TestCase):
    def setUp(self):
        self.model = models.HiddenModel

    def test_if_is_hidden_attribute_is_present(self):
        obj = self.model.objects.create()
        self.assertTrue(hasattr(obj, 'is_hidden'))

    def test_if_hide_is_marking_is_hidden_to_true(self):
        obj = self.model.objects.create()
        self.assertFalse(obj.is_hidden)

        obj.hide()
        self.assertTrue(obj.is_hidden)

    def test_if_unhide_is_marking_is_hidden_to_false(self):
        obj = self.model.objects.create(is_hidden=True)
        self.assertTrue(obj.is_hidden)

        obj.unhide()
        self.assertFalse(obj.is_hidden)


class SlugTestCases(TestCase):
    def setUp(self):
        self.model = models.SlugModel

    def test_if_slug_attribute_is_present(self):
        obj = self.model.objects.create()
        self.assertTrue(hasattr(obj, 'slug'))

    def test_if_default_slug_from_is_title(self):
        self.assertEqual(self.model.SLUG_FROM, 'title')

    def test_if_the_field_denoted_in_slug_from_is_present(self):
        obj = self.model.objects.create()
        self.assertTrue(hasattr(obj, self.model.SLUG_FROM))

    def test_if_the_slug_is_getting_generated(self):
        obj = self.model.objects.create(title='Satheesh Kumar')
        self.assertIsNotNone(obj.slug)


class UniqueSlugTestCases(SlugTestCases):
    def setUp(self):
        self.model = models.UniqueSlugModel

    def test_if_slug_generated_is_unqiue(self):
        obj = self.model.objects.create(title='Satheesh Kumar')
        self.assertIsNotNone(obj.slug)

        duplicate_obj = self.model.objects.create(title='Satheesh Kumar')
        self.assertIsNotNone(duplicate_obj.slug)

        self.assertNotEqual(obj.slug, duplicate_obj.slug)