from django.forms import ModelForm
from models import Poll


class FilmForm(ModelForm):
    class Meta:
        model = Poll
        readonly = 'start_poll_date'
