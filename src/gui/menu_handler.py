from __future__ import annotations
from src.event_bus import EventBus
from src.radio import Channel, OnPlay, Play, OnStop, Stop
from src.g_object import CheckMenuItem
from .menu_item import MenuItem
from .menu_item_label import MenuItemLabel


class MenuHandler:
    def __init__(self, event_bus: EventBus):
        self._items: [MenuItem] = []
        self._event_bus: EventBus = event_bus

    @staticmethod
    def create(event_bus: EventBus) -> MenuHandler:
        menu_handler = MenuHandler(event_bus)

        event_bus.subscribe(OnPlay(menu_handler._activate_item))
        event_bus.subscribe(OnStop(menu_handler._disable_item))

        return menu_handler

    def add_item(self, item: CheckMenuItem) -> None:
        label = item.get_label()

        if label == MenuItemLabel.DEUTSCHLANDFUNK.value:
            return self._items.append(MenuItem(item, Channel.DEUTSCHLANDFUNK))
        if label == MenuItemLabel.DEUTSCHLANDFUNK_KULTUR.value:
            return self._items.append(MenuItem(item, Channel.DEUTSCHLANDFUNK_KULTUR))
        if label == MenuItemLabel.DEUTSCHLANDFUNK_NOVA.value:
            return self._items.append(MenuItem(item, Channel.DEUTSCHLANDFUNK_NOVA))
        if label == MenuItemLabel.DOKUMENTE_UND_DEBATTEN.value:
            return self._items.append(MenuItem(item, Channel.DOKUMENTE_UND_DEBATTEN))
        if label == MenuItemLabel.QUIT.value:
            return self._items.append(MenuItem(item, Channel.EMPTY))

    def item_handler(self, item: CheckMenuItem) -> None:
        self._item_handler(self._get_item_by_label(item.get_label()))

    @staticmethod
    def _disable_items(items: [MenuItem]) -> None:
        for item in items:
            if item.is_active:
                item.disable()

    def _get_item_by_channel(self, channel: Channel) -> MenuItem:
        for item in self._items:
            if item.channel.value == channel.value:
                return item

    def _get_item_by_label(self, label: str) -> MenuItem:
        for item in self._items:
            if item.label == label:
                return item

    def _item_handler(self, item: MenuItem) -> None:
        # This is a workaround because if `set_active`
        # is called on `CheckMenuItem` the `activate`
        # event of `CheckMenuItem` will be called and
        # we will run into a endless loop.
        if item.is_updating:
            return item.update_done()

        if not item.is_active:
            return self._event_bus.publish(Stop(item.channel))

        return self._event_bus.publish(Play(item.channel))

    def _filter_item(self, item_to_filter: MenuItem) -> [MenuItem]:
        return filter(lambda item: item is not item_to_filter, self._items)

    def _activate_item(self, event: Play) -> None:
        item = self._get_item_by_channel(event.channel)

        if not item.is_active:
            item.activate()

        items = self._filter_item(item)
        MenuHandler._disable_items(items)

    def _disable_item(self, event: Stop) -> None:
        item = self._get_item_by_channel(event.channel)

        if item.is_active:
            item.disable()
