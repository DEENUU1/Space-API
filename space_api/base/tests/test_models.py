from django.test import TestCase
from base.models import Galaxy, System, Planet


class TestModels(TestCase):
    """
    This class contains tests for models: Galaxy, System and Planet
    """
    def setUp(self) -> None:
        self.galaxy1 = Galaxy.objects.create(
            id=1,
            name='Test Galaxy',
            description='Simple text',
            age="1000 billion years",
            constellation="Not known",
            distance="10000 ly",
            type="BCC23",
            mass="9239329 bilion tones",
            number_of_stars=10,
            size="100 ly"
        )

    def test_galaxy_model(self) -> None:
        """
        Test that the Galaxy object has the correct attributes
        """
        self.assertEqual(self.galaxy1.name, 'Test Galaxy')
        self.assertEqual(self.galaxy1.id, 1)
        self.assertEqual(self.galaxy1.description, "Simple text")
        self.assertEqual(self.galaxy1.number_of_stars, 10)
