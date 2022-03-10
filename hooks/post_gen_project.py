from __future__ import print_function

import os
import random
import secrets
import shutil

try:
    # Inspired by
    # https://github.com/django/django/blob/master/django/utils/crypto.py
    random = random.SystemRandom()
    using_sysrandom = True
except NotImplementedError:
    using_sysrandom = False

TERMINATOR = '\x1b[0m'
WARNING = '\x1b[1;33m [WARNING]: '
INFO = '\x1b[1;33m [INFO]: '
HINT = '\x1b[3;33m'
SUCCESS = '\x1b[1;32m [SUCCESS]: '


def remove_vue_files():
    file_names = [
        os.path.join('templates', 'index.html')
    ]
    for file_name in file_names:
        os.remove(file_name)
    remove_vue_related_directories()


def remove_vue_related_directories():
    shutil.rmtree(os.path.join('apps', 'client'))
    shutil.rmtree(os.path.join('resources', 'vue'))


def remove_docker_files():
    file_names = [
        'docker-compose.yml',
        'docker-compose.prod.yml'
    ]
    for file_name in file_names:
        os.remove(file_name)
    remove_docker_related_directories()


def remove_docker_related_directories():
    shutil.rmtree(os.path.join('docker'))


def remove_non_vue_files():
    file_names = [
        os.path.join('templates', 'welcome.html')
    ]
    for file_name in file_names:
        os.remove(file_name)
    remove_none_vue_related_directories()


def remove_none_vue_related_directories():
    shutil.rmtree(os.path.join('templates', 'layouts'))


def remove_pipfile():
    file_names = ['Pipfile']
    for file_name in file_names:
        os.remove(file_name)


def remove_gitkeep_files():
    file_names = [
        os.path.join('docker', 'local', 'postgres', 'data', '.gitkeep')
    ]
    for file_name in file_names:
        os.remove(file_name)


def remove_heroku_files():
    file_names = ['Procfile', 'runtime.txt']
    for file_name in file_names:
        os.remove(file_name)


def remove_async_files():
    file_names = [
        os.path.join('config', 'asgi.py')
    ]
    for file_name in file_names:
        os.remove(file_name)


def gen_django_secret_key(file_path):
    """Generates a 32-bit hex key."""
    for x in range(1):
        key = secrets.token_hex(32)
        return key


def set_env_file():
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

    app_key = gen_django_secret_key()

    env_string = (
        'APP_NAME="{{ cookiecutter.project_name }}"\n'
        "APP_ENV=" + app_env + "\n"
        "APP_SECRET_KEY=" + app_key + "\n"
        "APP_DEBUG=True\n"
        "APP_ALLOWED_HOST="'"localhost, 127.0.0.1, 0.0.0.0"\n\n'
        "DB_POSTGRESQL="'{%- if cookiecutter.database == "PostgreSQL" -%} psql {% endif %}\n'
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


def main():
    set_env_file()
    print(SUCCESS + 'Env file generated.' + TERMINATOR)

    if '{{ cookiecutter.enviroment }}'.lower() == 'docker':
        remove_pipfile()
        remove_gitkeep_files()

    if '{{ cookiecutter.use_vuejs }}'.lower() == 'pipenv':
        remove_docker_files()

    if '{{ cookiecutter.use_vuejs }}'.lower() == 'n':
        remove_vue_files()

    if '{{ cookiecutter.use_vuejs }}'.lower() == 'y':
        remove_non_vue_files()

    if '{{ cookiecutter.use_heroku }}'.lower() == 'n':
        remove_heroku_files()

    if '{{ cookiecutter.use_async }}'.lower() == 'n':
        remove_async_files()

    print(SUCCESS + 'Cookies are ready to eat. 🍪🍪' + TERMINATOR)


if __name__ == '__main__':
    main()
