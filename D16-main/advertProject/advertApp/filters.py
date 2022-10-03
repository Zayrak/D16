import django_filters

from django.contrib.auth.models import User

from django_filters import FilterSet

from .models import Response, Advert


class ResponseFilter(FilterSet):
    id_user = django_filters.ModelChoiceFilter(label="Автор", queryset=User.objects.all())
    id_advert = django_filters.ModelChoiceFilter(label="Публикация", queryset=Advert.objects.all())

    class Meta:
        model = Response
        fields = ['id_user', 'id_advert']
