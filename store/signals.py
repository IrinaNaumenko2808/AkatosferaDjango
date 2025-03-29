from django.db.models.signals import post_migrate
from django.core.management import call_command
from django.dispatch import receiver
import os

@receiver(post_migrate)
def load_fixtures_after_migrate(sender, **kwargs):
    fixture_file = os.path.join('fixtures.json')
    if os.path.exists(fixture_file):
        print(" Загрузка фикстур из файла fixtures.json...")
        try:
            call_command('loaddata', fixture_file)
        except Exception as e:
            print(f"Ошибка загрузки fixtures: {e}")