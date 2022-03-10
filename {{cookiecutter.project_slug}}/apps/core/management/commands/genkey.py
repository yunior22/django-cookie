import secrets
import sys

from django.core.management import BaseCommand


class Command(BaseCommand):
    """Django command to generate a 32-bit hex key in the command line."""

    def handle(self, *args, **kwargs):
        for x in range(1):
            key = secrets.token_hex(32)
            sys.stdout.write('Key ' + str(x + 1) + ': ' + key + "\n")
