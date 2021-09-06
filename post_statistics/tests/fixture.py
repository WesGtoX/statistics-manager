import factory
from post_statistics.models import Statistic


class StatisticFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Statistic

    post_id = factory.Faker('numerify', text='################')
    user_id = factory.Faker('numerify', text='##########')
    likes = factory.Faker('pyint', min_value=0, max_value=999)
    created_at = factory.Faker('date_time_between', start_date='-10d', end_date='now')
