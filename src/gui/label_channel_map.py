from src.gui.menu_item_label import MenuItemLabel
from src.radio import Channel

labelChannelMap = {
    MenuItemLabel.DEUTSCHLANDFUNK.value: Channel.DEUTSCHLANDFUNK,
    MenuItemLabel.DEUTSCHLANDFUNK_KULTUR.value: Channel.DEUTSCHLANDFUNK_KULTUR,
    MenuItemLabel.DEUTSCHLANDFUNK_NOVA.value: Channel.DEUTSCHLANDFUNK_NOVA,
    MenuItemLabel.DOKUMENTE_UND_DEBATTEN.value: Channel.DOKUMENTE_UND_DEBATTEN,
    MenuItemLabel.QUIT.value: Channel.EMPTY,
}