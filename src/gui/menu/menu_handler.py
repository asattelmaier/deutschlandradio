from typing import Callable

from src.event_bus import EventBus
from src.gui.menu.menu_item import MenuItemLabel, MenuItem, MenuItemLabelChannelMap
from src.radio import Channel, OnPlay, Play, OnStop, Stop
from ..g_object import CheckMenuItem


class MenuHandler:
    def __init__(self, event_bus: EventBus, quit_handler: Callable):
        self._items: [MenuItem] = []
        self._event_bus: EventBus = event_bus
        self._quit_handler: Callable = quit_handler

    @staticmethod
    def create(event_bus: EventBus, quit_handler: Callable):
        menu_handler = MenuHandler(event_bus, quit_handler)

        event_bus.subscribe(OnPlay(menu_handler._activate_item))
        event_bus.subscribe(OnStop(menu_handler._disable_item))

        return menu_handler

    def add_item(self, item: CheckMenuItem) -> None:
        channel = MenuItemLabelChannelMap.get_channel(item.get_label())

        return self._items.append(MenuItem(item, channel))

    def item_handler(self, item: CheckMenuItem) -> None:
        label = item.get_label()

        if label == MenuItemLabel.QUIT.value:
            return self._quit_handler()

        self._item_handler(self._get_item_by_label(label))

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
