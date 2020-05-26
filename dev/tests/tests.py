from __future__ import print_function, absolute_import

from django.test import TestCase as _TestCase, Client

from django.contrib.auth.models import User

from tests.models import UnlimitedExample


class TestCase(_TestCase):
    """Compatibility fix"""
    if not hasattr(_TestCase, 'assertRegex'):
        assertRegex = _TestCase.assertRegexpMatches
    if not hasattr(_TestCase, 'assertNotRegex'):
        assertNotRegex = _TestCase.assertNotRegexpMatches


class ModuleTest(TestCase):
    def setUp(self):
        """Sets the test environment"""
        self.user = User.objects.create(username='user', is_superuser=True, is_staff=True)
        self.user.set_password('password')
        self.user.save()

        self.example = UnlimitedExample.objects.create(name='name123name', code='code')

    def test_001_basic(self):
        """Check for basic functionality"""
        c = Client()
        c.login(username='user', password='password')

        response = c.get('/admin/tests/unlimitedexample/%s/change/' % self.example.pk)
        self.assertEqual(response.status_code, 200)
        self.assertIn('name123name', response.content.decode('utf8'))

        response = c.post('/admin/tests/unlimitedexample/%s/change/' % self.example.pk, data={'name': 'test123test', 'code': 'test', '_continue': 'continue'})
        self.assertEqual(response.status_code, 302)

        self.example.refresh_from_db()
        self.assertEqual(self.example.name, 'test123test')
        self.assertEqual(self.example.code, 'test')

        response = c.get('/admin/tests/unlimitedexample/%s/change/' % self.example.pk)
        self.assertEqual(response.status_code, 200)
        self.assertIn('test123test', response.content.decode('utf8'))

    def test_002_unlimited_values(self):
        """Check for unlimited length processing"""

        verylongname = 'x' * 10000
        verylongcode = 'y' * 10000
        self.example.name = verylongname
        self.example.save()

        self.example.refresh_from_db()
        self.assertEqual(self.example.name, verylongname)

        self.example.code = verylongcode
        self.example.save()

        self.example.refresh_from_db()
        self.assertEqual(self.example.code, verylongcode)

        c = Client()
        c.login(username='user', password='password')

        response = c.get('/admin/tests/unlimitedexample/%s/change/' % self.example.pk)
        self.assertEqual(response.status_code, 200)
        self.assertIn(verylongname, response.content.decode('utf8'))
        self.assertIn(verylongcode, response.content.decode('utf8'))

        self.example.name = 'name123name'
        self.example.code = 'code123code'
        self.example.save()

        response = c.get('/admin/tests/unlimitedexample/%s/change/' % self.example.pk)
        self.assertEqual(response.status_code, 200)
        self.assertIn('name123name', response.content.decode('utf8'))
        self.assertIn('code123code', response.content.decode('utf8'))

        response = c.post('/admin/tests/unlimitedexample/%s/change/' % self.example.pk, data={
            'name': verylongname, 'code': 'empty23empty', '_continue': 'continue'
        })
        self.assertEqual(response.status_code, 302)

        self.example.refresh_from_db()
        self.assertEqual(self.example.name, verylongname)
        self.assertEqual(self.example.code, 'empty23empty')

        response = c.post('/admin/tests/unlimitedexample/%s/change/' % self.example.pk, data={
            'name': 'empty23empty', 'code': verylongcode, '_continue': 'continue'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Ensure this value has at most', response.content.decode('utf8'))

        self.example.refresh_from_db()
        self.assertEqual(self.example.name, verylongname)
        self.assertEqual(self.example.code, 'empty23empty')
