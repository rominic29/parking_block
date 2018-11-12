from django.test import (
    Client,
    TestCase,
)

from .forms import SignUpForm
from .models import (
    Car,
    User,
)


class TestBase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_superuser(
            email='usuario@email.com',
            password='usuario1234',
        )
        login = self.client.login(
            username='usuario@email.com', password='usuario1234')
        return login


class ModelsTest(TestBase):
    def test_create_user(self):
        User.objects.create_user(
            email='prueba@prueba.com',
            password='prueba1234',
        )
        user = User.objects.get(email='prueba@prueba.com')
        self.assertEqual(user.email, 'prueba@prueba.com')

    def test_create_user_not_email(self):
        self.assertRaises(
            ValueError,
            User.objects.create_user,
            email=None,
            password='prueba1234',
        )

    def test_create_super_user(self):
        User.objects.create_superuser(
            email='superprueba@prueba.com',
            password='prueba1234',
        )
        user = User.objects.get(email='superprueba@prueba.com')
        self.assertEqual(user.email, 'superprueba@prueba.com')

    def test_create_super_user_error_1(self):
        self.assertRaises(
            ValueError,
            User.objects.create_superuser,
            email='super1@email.com',
            password='prueba1234',
            is_staff='true',
        )

    def test_create_super_user_error_2(self):
        self.assertRaises(
            ValueError,
            User.objects.create_superuser,
            email='super1@email.com',
            password='prueba1234',
            is_superuser='true',
        )

    def test_create_car(self):
        car1 = Car.objects.create(user=self.user, license_plate='AEO608')
        car2 = Car.objects.create(
            user=self.user,
            license_plate='AA608ABC',
            description='an example',
        )
        self.assertEqual(car1.license_plate, 'AEO608')
        self.assertEqual(car1.description, '')
        self.assertEqual(car2.license_plate, 'AA608ABC')
        self.assertEqual(car2.description, 'an example')


class FormTest(TestBase):
    def test_SignUp_Form(self):
        form = SignUpForm({
            'password1': 'password27',
            'password2': 'password27',
            'email': 'juan@ejemplo.com',
        })
        form.save()
        user = User.objects.get(email='juan@ejemplo.com')
        self.assertEqual(user.email, 'juan@ejemplo.com')
