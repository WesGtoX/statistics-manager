from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from post_statistics.tests.fixture import StatisticFactory

from faker import Faker

faker = Faker()


class StatisticViewSetTests(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()

    def test_perform_create(self) -> None:
        """
        Test creating a Statistic model per rest request.
        """
        data = {
            'post_id': '10213570010851840',
            'user_id': '1808970597',
            'likes': 21,
            'created_at': '2021-09-05 00:00'
        }
        response = self.client.post(reverse('statistic-list'), data=data)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)
        self.assertEqual(data.get('post_id'), response.data.get('post_id'))
        self.assertEqual(data.get('user_id'), response.data.get('user_id'))
        self.assertEqual(data.get('likes'), response.data.get('likes'))
        self.assertEqual('2021-09-05T00:00:00Z', response.data.get('created_at'))

    def test_get_latest_statistics_by_post_id(self) -> None:
        """
        Test to get latest statistics for a specific post id, via rest request.
        """
        date = faker.date_between(start_date='-35d', end_date='-31d')
        StatisticFactory.create_batch(2, post_id='1779375071376586', user_id='4110778024')
        StatisticFactory.create_batch(2, post_id='1779375071376586', user_id='4110778024', created_at=date)
        data = {
            'post_id': '1779375071376586',
            'latest': 3,
        }
        response = self.client.get(reverse('statistic-post'), data=data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(3, len(response.data))

    def test_get_latest_statistics_by_user_id(self) -> None:
        """
        Test to get latest statistics for all posts of a specific user id, via rest request.
        """
        date = faker.date_between(start_date='-35d', end_date='-31d')
        StatisticFactory.create_batch(3, post_id='166937525776586', user_id='4110778024')
        StatisticFactory.create_batch(3, post_id='177937525776586', user_id='4110778024')
        StatisticFactory.create_batch(2, post_id='188937525776586', user_id='4110778024', created_at=date)
        StatisticFactory.create_batch(1, post_id='199937525776586', user_id='4110778024', created_at=date)
        data = {
            'user_id': '4110778024',
            'latest': 4,
        }

        response = self.client.get(reverse('statistic-user'), data=data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(4, len(response.data))

    def test_get_average_number_of_likes_per_day_by_user_id(self):
        """
        Test to get average number of likes per day for a specific user id, via rest request.
        """
        date = faker.date_time_between(start_date='-35d', end_date='-31d')
        StatisticFactory.create_batch(2, user_id='9150721021', likes=10)
        StatisticFactory.create_batch(2, user_id='9150721021', likes=15)
        StatisticFactory.create_batch(2, user_id='9150721021', likes=20)
        StatisticFactory.create_batch(5, user_id='9150721021', created_at=date, likes=30)

        response = self.client.get(reverse('statistic-average', args=['9150721021']))
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(15.0, response.data.get('likes_average'))
