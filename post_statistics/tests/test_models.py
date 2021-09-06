from django.test import TestCase
from post_statistics.models import Statistic


class StatisticModelTestCase(TestCase):

    def test_create_statistic(self) -> None:
        """
        Test to create a successful Statistic model.
        """
        data = {
            'post_id': '10213575510851840',
            'user_id': '1808970598',
            'likes': 21,
            'created_at': '2021-09-05'
        }
        statistic = Statistic.objects.create(**data)

        self.assertEqual(data.get('post_id'), statistic.post_id)
        self.assertEqual(data.get('user_id'), statistic.user_id)
        self.assertEqual(data.get('likes'), statistic.likes)
        self.assertEqual(data.get('created_at'), statistic.created_at)
        self.assertEqual(
            statistic.__str__(),
            f'User ID: {data.get("user_id")}, Post ID: {data.get("post_id")}, Likes: {data.get("likes")}'
        )

    def test_update_statistic(self) -> None:
        """
        Test to update a Statistic model.
        """
        data = {
            'post_id': '10213575510851123',
            'user_id': '1808970598',
            'likes': 5,
            'created_at': '2021-09-05'
        }
        Statistic.objects.create(**data)

        statistic = Statistic.objects.get(post_id='10213575510851123', user_id='1808970598')
        self.assertEqual(statistic.likes, 5)

        statistic.likes = 10
        statistic.save()

        self.assertEqual(statistic.likes, 10)

    def test_delete_statistic(self) -> None:
        """
        Test to delete a Statistic model.
        """
        data = {
            'post_id': '10213575510401212',
            'user_id': '1808970598',
            'likes': 5,
            'created_at': '2021-09-05'
        }
        Statistic.objects.create(**data)

        statistic = Statistic.objects.get(post_id='10213575510401212', user_id='1808970598')

        statistic.delete()
        self.assertFalse(Statistic.objects.filter(post_id='10213575510401212', user_id='1808970598').exists())
