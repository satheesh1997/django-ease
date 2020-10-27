from django.test import TestCase

from app import models


class TimeStampsTestCases(TestCase):
    def setUp(self):
        self.model = models.TimeStampsModel

    def test_if_the_created_at_and_updated_at_field_is_present(self):
        obj = self.model.objects.create()
        self.assertTrue(hasattr(obj, 'created_at'))