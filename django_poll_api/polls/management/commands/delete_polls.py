from django.core.management.base import BaseCommand
from polls.models import *


class Command(BaseCommand):
    help = 'Start scrape-parse Function'

    def handle(self, *args, **options):
        polls_all = Poll.objects.all()
        for poll in polls_all:
            poll.delete()