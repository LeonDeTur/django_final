from django.core.management.base import BaseCommand
from my_app.models import Author, Article


class Command(BaseCommand):
    help = "Generate fake authors and posts."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')

        for i in range(1, count + 1):
            author = Author(firstname=f'firstname{i}', lastname=f'lastname{i}', email=f'email{i}@mail.ru',
                            biography=f'biography{i}', birthdate=f'2000-11-23')
            author.save()
            for j in range(1, count + 1):
                article = Article(title=f'Title{j}', description=f'description{j}', author_id=author,
                                  category=f'category{i}')
                article.save()
