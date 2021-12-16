from __future__ import annotations
from typing import Callable
from src.event_bus import EventBus
from src.radio import Channel
from src.g_object import CheckMenuItem
from .menu_item import MenuItem
from .menu_item_label import MenuItemLabel


class MenuHandler:
    _items: [MenuItem] = []

    def __init__(self, even_bus: EventBus):
        self._event_bus = even_bus

    @staticmethod
    def create(event_bus: EventBus) -> MenuHandler:
        return MenuHandler(event_bus)

    def add_item(self, item: CheckMenuItem, handler: Callable) -> None:
        label = item.get_label()

        if label == MenuItemLabel.DEUTSCHLANDFUNK.value:
            return self._items.append(MenuItem(item, Channel.DEUTSCHLANDFUNK, handler))
        if label == MenuItemLabel.DEUTSCHLANDFUNK_KULTUR.value:
            return self._items.append(MenuItem(item, Channel.DEUTSCHLANDFUNK_KULTUR, handler))
        if label == MenuItemLabel.DEUTSCHLANDFUNK_NOVA.value:
            return self._items.append(MenuItem(item, Channel.DEUTSCHLANDFUNK_NOVA, handler))
        if label == MenuItemLabel.DOKUMENTE_UND_DEBATTEN.value:
            return self._items.append(MenuItem(item, Channel.DOKUMENTE_UND_DEBATTEN, handler))
        if label == MenuItemLabel.QUIT.value:
            return self._items.append(MenuItem(item, Channel.EMPTY, handler))

    def create_item_handler(self, handler: Callable) -> Callable:
        return lambda item: self._item_handler(self._get_item(item), handler)

    @staticmethod
    def _disable_items(items: [MenuItem]) -> None:
        for item in items:
            if item.is_active:
                item.disable()

    def _get_item(self, check_menu_item: CheckMenuItem) -> MenuItem:
        for item in self._items:
            if item.label == check_menu_item.get_label():
                return item

    def _item_handler(self, item: MenuItem, handler: Callable) -> None:
        if item.is_active:
            items = self._filter_item(item)
            MenuHandler._disable_items(items)

        handler()

    def _filter_item(self, item_to_filter: MenuItem) -> [MenuItem]:
        return filter(lambda item: item is not item_to_filter, self._items)
