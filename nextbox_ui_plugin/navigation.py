from extras.plugins import PluginMenuItem
from django.utils.translation import gettext_lazy as _

menu_items = (
    PluginMenuItem(
        link='plugins:nextbox_ui_plugin:topology',
        link_text=_('Topology Viewer'),
        buttons=()
    ),
)
