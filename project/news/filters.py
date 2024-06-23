from django_filters import FilterSet
from .models import News


class NewsFilter(FilterSet):
    class Meta:
        model = News
        fields = (
            'title': ['icontains'],
            'author': ['exact'],
            'time_in': ['gt',],
        )
