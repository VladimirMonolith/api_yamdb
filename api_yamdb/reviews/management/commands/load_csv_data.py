import csv
import subprocess as sub

from django.core.management.base import BaseCommand
from reviews.models import Category, Comment, Genre, Review, Title
from users.models import User


class Command(BaseCommand):
    """Проводит миграции и загружает тестовые данные
    в базу из csv файлов,которые располагаются в директории /static/data/."""

    def handle(self, *args, **options):
        self.migreate_sqlite()
        self.import_users()
        self.import_category()
        self.import_genre()
        self.import_titles()
        self.import_review()
        self.import_comments()
        self.import_genre_title()

        print('Загрузка тестовых данных завершена.')

    def migreate_sqlite(self):
        cmd_makemigrations = 'python manage.py makemigrations'.strip().split()
        cmd_migrate = 'python manage.py migrate'.strip().split()
        sub.call(cmd_makemigrations)
        sub.call(cmd_migrate)

    def import_category(self, file='category.csv'):
        print(f'Загрузка {file}...')
        file_path = f'static/data/{file}'
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                status, created = Category.objects.update_or_create(
                    id=row['id'],
                    name=row['name'],
                    slug=row['slug']
                )

    def import_genre(self, file='genre.csv'):
        print(f'Загрузка {file}...')
        file_path = f'static/data/{file}'
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                status, created = Genre.objects.update_or_create(
                    id=row['id'],
                    name=row['name'],
                    slug=row['slug']
                )

    def import_titles(self, file='titles.csv'):
        print(f'Загрузка {file}...')
        file_path = f'static/data/{file}'
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                status, created = Title.objects.update_or_create(
                    id=row['id'],
                    name=row['name'],
                    year=row['year'],
                    category_id=row['category_id'],
                    genre_id=row['genre_id'],
                )

    def import_review(self, file='review.csv'):
        print(f'Загрузка {file}...')
        file_path = f'static/data/{file}'
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                status, created = Review.objects.update_or_create(
                    id=row['id'],
                    author_id=row['author_id'],
                    text=row['text'],
                    score=row['score'],
                    pub_date=row['pub_date'],
                    title_id=row['title_id']
                )

    def import_comments(self, file='comments.csv'):
        print(f'Загрузка {file}...')
        file_path = f'static/data/{file}'
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                status, created = Comment.objects.update_or_create(
                    id=row['id'],
                    author_id=row['author_id'],
                    text=row['text'],
                    pub_date=row['pub_date'],
                    review_id=row['review_id']
                )

    def import_genre_title(self, file='genre_title.csv'):
        print(f'Загрузка {file}...')
        file_path = f'static/data/{file}'
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                status, created = Title.genre.through.objects.update_or_create(
                    id=row['id'],
                    genre_id=row['genre_id'],
                    title_id=row['title_id']
                )

    def import_users(self, file='users.csv'):
        print(f'Загрузка {file}...')
        file_path = f'static/data/{file}'
        with open(file_path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                status, created = User.objects.update_or_create(
                    id=row['id'],
                    username=row['username'],
                    email=row['username'],
                    first_name=row['first_name'],
                    last_name=row['last_name'],
                    bio=row['bio'],
                    role=row['role']
                )
