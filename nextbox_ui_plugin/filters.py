import django_filters
from dcim.models import Device, Site, Region
from django.conf import settings
from packaging import version

NETBOX_CURRENT_VERSION = version.parse(settings.VERSION)

if NETBOX_CURRENT_VERSION >= version.parse("2.11.0"):
    from dcim.models import Location
else:
    from dcim.models import RackGroup as Location

from django.utils.translation import gettext_lazy as _

class TopologyFilterSet(django_filters.FilterSet):

    device_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Device.objects.all(),
        to_field_name='id',
        field_name='id',
        label=_('Device (ID)'),
    )
    location_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Location.objects.all(),
        label=_('Location (ID)'),
    )
    site_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Site.objects.all(),
        label=_('Site (ID)'),
    )
    region_id = django_filters.ModelMultipleChoiceFilter(
        queryset=Region.objects.all(),
        field_name='site__region',
        label=_('Region (ID)'),
    )

    class Meta:
        model = Device
        fields = ['id', 'name', ]
