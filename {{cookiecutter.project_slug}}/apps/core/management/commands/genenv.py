import secrets
import sys

from django.core.management import BaseCommand


def gen_key():
    """Generates a 32-bit hex key."""
    for x in range(1):
        key = secrets.token_hex(32)
        return key


class Command(BaseCommand):
    """Django command generates a .env file with django specific environment variables."""

    def handle(self, *args, **kwargs):
        file_name = input('Enter a .env file name [defaults to .env] : ')
        if file_name == '':
            file_name = '.env'

        while True:
            q1 = input('Do you want file for: A) development B) production [A/b]? : ')
            if q1 == 'A' or 'a' or '':
                app_env = 'development'
                break
            elif q1 == 'B' or 'b':
                app_env = 'production'
                break

        f = open(file_name, 'w')

        app_key = gen_key()

        env_string = (
            'APP_NAME="Django"\n'
            "APP_ENV=" + app_env + "\n"
            "APP_SECRET_KEY=" + app_key + "\n"
            "APP_DEBUG=False\n"
            "APP_ALLOWED_HOST="'"localhost, 127.0.0.1, 0.0.0.0"\n\n'
            "DB_POSTGRESQL=psql\n"
            "DB_HOST=psql\n"
            "DB_PORT=5432\n"
            "DB_DATABASE=django_db\n"
            "DB_USERNAME=postgres\n"
            "DB_PASSWORD=secret\n\n"
            "REDIS_HOST=redis\n"
            "REDIS_PASSWORD=secret\n"
            "REDIS_PORT=6379\n\n"
            "MAIL_MAILER=smtp\n"
            "MAIL_HOST=smtp.mailtrap.io\n"
            "MAIL_PORT=2525\n"
            "MAIL_USERNAME=null\n"
            "MAIL_PASSWORD=null\n"
            "MAIL_ENCRYPTION=null\n"
            "MAIL_FROM_ADDRESS=null\n"
            "MAIL_FROM_NAME=Django\n"
        )
        f.write(env_string)
        f.close()

        self.stdout.write(self.style.SUCCESS("File " + file_name + " successfully created."))

