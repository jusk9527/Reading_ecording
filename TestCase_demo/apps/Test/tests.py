from django.test import TestCase

# Create your tests here.

class Demo(TestCase):
    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown')

    def test_demo(self):
        print('test_demo')

    def test_demo_2(self):
        print('test_demo2')



from django.urls import reverse
class HelloTestCase(TestCase):
    def setUp(self):
        self.name = 'Django'

    def test_hello_test_case(self):
        url = '/hello_test_case'
        # urls = reverse('hello_test_case')
        # print(urls)
        # Input: print(resolve(url))
        # Output: ResolverMatch(func=development_of_test_habits.views.hello_test_case.HelloTestCase, args=(), kwargs={}, url_name=hello_test_case, app_names=[], namespaces=[])




        # 不带参数
        response = self.client.get(url)


        self.assertEqual(response.status_code, 200)  # 期望的Http相应码为200
        data = response.json()
        self.assertEqual(data['msg'], 'Hello , I am a test Case')  # 期望的msg返回结果为'Hello , I am a test Case'


        # 带参数
        response = self.client.get(url, {'name': self.name})
        self.assertEqual(response.status_code, 200)  # 期望的Http相应码为200
        data = response.json()
        self.assertEqual(data['msg'], 'Hello Django I am a test Case')  # 期望的msg返回结果为'Hello Django I am a test Case'




from django.contrib.auth.models import User
from apps.Test import models
from mixer.backend.django import mixer
class HomeWorkAPITestCase(TestCase):
    def setUp(self):
        self.user = mixer.blend(User)

        self.random_home_works = [
            mixer.blend(models.HomeWork)
            for _ in range(11)
        ]

    def test_home_works_list_api(self):
        url = reverse('home_works_list')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

        self.client.force_login(self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data), len(self.random_home_works))

        data_fields = [key for key in data[0].keys()]

        self.assertIn('school_name', data_fields)
        self.assertIn('class_name', data_fields)
        self.assertIn('student_name', data_fields)
        self.assertIn('name', data_fields)
