from django.test import TestCase
from base.models import Galaxy, System, Planet, Owner, Rocket


class TestModels(TestCase):
    """
    This class contains tests for models: Galaxy, System and Planet
    """

    def setUp(self) -> None:
        """
        Initializes the test data
        """
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

        self.system1 = System.objects.create(
            id=1,
            name="Test System",
            description="Simple text",
            age="700 billion years",
            mass="8000 billion tones",
            number_of_stars=1,
            star="Sun",
            satellites="Moon",
            number_of_satellites=1,
            galaxy=self.galaxy1
        )

        self.planet1 = Planet.objects.create(
            id=1,
            name="Test Planet",
            description="Simple text",
            age="100 billions years",
            star="Sun",
            number_of_stars=1,
            orbital_period="365 d",
            satellites="Moon",
            number_of_satellites=1,
            mean_radius="4000 km",
            mass="8999 tones",
            surface_gravity="10 m/s^2",
            surface_temp_min="-30 Celsius degree",
            surface_temp_max="50 Celsius degree",
            surface_temp_mean="25 Celsius degree",
            galaxy=self.galaxy1,
            system=self.system1
        )
        self.owner1 = Owner.objects.create(
            id=1,
            name="SpaceX",
            description="Cheap starts",
            founded="2002-03-14",
            founder="Elon Musk",
            website="www.spacex.com",
            country="USA"
        )
        self.rocket1 = Rocket.objects.create(
            id=1,
            name='Falcon 9',
            description="Good rocket",
            country="USA",
            cost_per_launch="100 mln $",
            height="100 meter",
            mass="100 t",
            stages=2,
            owner=self.owner1
        )

    def test_galaxy_model(self) -> None:
        """
        Test that the Galaxy object has the correct attributes
        """
        self.assertEqual(self.galaxy1.name, 'Test Galaxy')
        self.assertEqual(self.galaxy1.id, 1)
        self.assertEqual(self.galaxy1.description, "Simple text")
        self.assertEqual(self.galaxy1.number_of_stars, 10)

    def test_system_model(self) -> None:
        """
        Test that the System object has the correct attributes
        """
        self.assertEqual(self.system1.name, "Test System")
        self.assertEqual(self.system1.description, "Simple text")
        self.assertEqual(self.system1.number_of_stars, 1)
        self.assertEqual(self.system1.number_of_satellites, 1)

    def test_system_relation_with_galaxy(self) -> None:
        """
        Test that the System object is related to the correct Galaxy object
        """
        self.assertEqual(self.system1.galaxy, self.galaxy1)

    def test_planet_model(self) -> None:
        """
        Test that the Planet object has the correct attributes
        """
        self.assertEqual(self.planet1.name, "Test Planet")
        self.assertEqual(self.planet1.description, "Simple text")
        self.assertEqual(self.planet1.number_of_stars, 1)
        self.assertEqual(self.planet1.number_of_satellites, 1)

    def test_planet_relation_with_galaxy(self) -> None:
        """
        Test that the Planet object is related to the correct Galaxy object.
        """
        self.assertEqual(self.planet1.galaxy, self.galaxy1)

    def test_planet_relation_with_system(self) -> None:
        """
        Test that the Planet object is related to the correct System object
        """
        self.assertEqual(self.planet1.system, self.system1)

    def test_owner_model(self) -> None:
        """
        Test that the Owner object has the correct attributes.
        """
        self.assertEqual(self.owner1.name, "SpaceX")
        self.assertEqual(self.owner1.description, "Cheap starts")
        self.assertEqual(self.owner1.founder, "Elon Musk")

    def test_rocket_model(self) -> None:
        """
        Test that the Rocket object has the correct attributes
        """
        self.assertEqual(self.rocket1.name, "Falcon 9")
        self.assertEqual(self.rocket1.description, "Good rocket")
        self.assertEqual(self.rocket1.stages, 2)

    def test_rocket_relation_with_owner(self) -> None:
        """
        Test that the Rocket object is related to the correct Owner object
        """
        self.assertEqual(self.rocket1.owner, self.owner1)


class TestModelsRequiredData(TestCase):
    """
    This class contains tests for models: Galaxy, System and Planet
    This is testing only required values without values that can be null
    """

    def setUp(self) -> None:
        """
        Initializes the test data
        """
        self.galaxy1 = Galaxy.objects.create(
            id=1,
            name='Test Galaxy',
            description='Simple text',
        )

        self.system1 = System.objects.create(
            id=1,
            name="Test System",
            description="Simple text",
            galaxy=self.galaxy1
        )

        self.planet1 = Planet.objects.create(
            id=1,
            name="Test Planet",
            description="Simple text",
            galaxy=self.galaxy1,
            system=self.system1
        )

    def test_galaxy_null_values(self) -> None:
        """
        Tests that the age, number_of_stars fields of the Galaxy model
        are null
        """
        self.assertIsNone(self.galaxy1.age)
        self.assertIsNone(self.galaxy1.number_of_stars)

    def test_system_null_values(self) -> None:
        """
        Tests that the age, number_of_stars, number_of_satellites
        fields of the System model are null
        """
        self.assertIsNone(self.system1.age)
        self.assertIsNone(self.system1.number_of_stars)
        self.assertIsNone(self.system1.number_of_satellites)

    def test_planet_null_values(self) -> None:
        """
        Tests that the number_of_stars, number_of_stars
        fields of the Planet model are null
        """
        self.assertIsNone(self.planet1.number_of_satellites)
        self.assertIsNone(self.planet1.number_of_stars)