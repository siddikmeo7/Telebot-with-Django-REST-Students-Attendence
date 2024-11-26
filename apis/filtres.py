import django_filters
from .models import Attendens

class AttendensFilterOmad(django_filters.FilterSet):
    omad = django_filters.BooleanFilter(field_name='omad', lookup_expr='exact', initial=True)
    class Meta:
        model = Attendens
        fields = ["omad",]


class AttendensFilterRaft(django_filters.FilterSet):
    raft = django_filters.BooleanFilter(field_name='raft', lookup_expr='exact', initial=True)
    class Meta:
        model = Attendens
        fields = ["raft"]



class AttendensFilterDercard(django_filters.FilterSet):
    dercard = django_filters.BooleanFilter(field_name='dercard', lookup_expr='exact', initial=True)
    class Meta:
        model = Attendens
        fields = ["dercard"]


class AttendensFilterNaomad(django_filters.FilterSet):
    naomad = django_filters.BooleanFilter(field_name='naomad', lookup_expr='exact', initial=True)
    class Meta:
        model = Attendens
        fields = ["naomad"]


