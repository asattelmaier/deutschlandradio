from src.gui.menu_item_label import MenuItemLabel
from src.radio import Channel

channelLabelMap = {
    Channel.DEUTSCHLANDFUNK.value: MenuItemLabel.DEUTSCHLANDFUNK.value,
    Channel.DEUTSCHLANDFUNK_KULTUR.value: MenuItemLabel.DEUTSCHLANDFUNK_KULTUR.value,
    Channel.DEUTSCHLANDFUNK_NOVA.value: MenuItemLabel.DEUTSCHLANDFUNK_NOVA.value,
    Channel.DOKUMENTE_UND_DEBATTEN.value: MenuItemLabel.DOKUMENTE_UND_DEBATTEN.value,
    Channel.EMPTY.value: MenuItemLabel.QUIT.value,
}