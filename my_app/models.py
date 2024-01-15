from django.db import models


class Coin(models.Model):
    is_eagle = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Сторона: {self.is_eagle}, время: {self.create_at}'

    @staticmethod
    def counter(n: int):
        coins = Coin.objects.order_by('-create_at')[: n]
        coins_dict = {'орел': 0, 'решка': 0}
        for coin in coins:
            if coin.is_eagle == 'орел':
                coins_dict['орел'] += 1
            else:
                coins_dict['решка'] += 1
        return coins_dict


class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.CharField(max_length=300)
    birthdate = models.DateField()

    def fullname(self):
        return f'{self.firstname} {self.lastname}'


class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    create_at = models.DateField(auto_now_add=True)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    count_views = models.IntegerField(default=0)
    is_published = models.BooleanField(default=False)
