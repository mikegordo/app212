from django.core.management.base import BaseCommand

from app212.models import *

SUPERUSER_TOKEN = '0admin0abcd0192837465abcd657483929abcd44'


class Command(BaseCommand):
    help = 'Populate dev database'

    def handle(self, *args, **options):
        self.stdout.write("Creating users...")
        self.create_superuser()
        self.stdout.write("Creating tokens...")
        self.create_tokens()
        self.stdout.write("Done.")

    @staticmethod
    def create_superuser():
        User.objects.create_superuser('admin', '', 'admin')

    @staticmethod
    def create_tokens():
        user = User.objects.get(is_superuser=True, username='admin')
        if not user:
            raise Exception('Superuser not found. Cannot create admin token.')
        Token.objects.create(user=user, key=SUPERUSER_TOKEN)
