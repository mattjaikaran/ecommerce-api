from django.core.management import BaseCommand

# Description for command here
class Command(BaseCommand):
    help = ''
    print(f'>>> python manage.py create_test_data')
    print(f'>>> {help}')

    def handle(self, *args, **options):

        print('>>> create_test_data.py successfully ran')
