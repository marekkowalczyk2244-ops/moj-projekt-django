from django.test import TestCase


class SanityTests(TestCase):
    def test_true_is_true(self):
        self.assertTrue(True)

from core.tasks import add


class CeleryTaskTests(TestCase):
    def test_add_task(self):
        result = add.apply(args=(2, 3))
        self.assertEqual(result.get(), 5)