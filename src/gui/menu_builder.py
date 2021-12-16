from __future__ import annotations
from typing import Type
from src.g_object import GimpToolkit, Menu
from .menu_handler import MenuHandler


class MenuBuilder:
    def __init__(self, gimp_toolkit: Type[GimpToolkit], menu: Menu, menu_handler: MenuHandler):
        self._gimp_toolkit = gimp_toolkit
        self._menu = menu
        self._menu_handler = menu_handler

    @staticmethod
    def create(gimp_toolkit: Type[GimpToolkit], menu_handler: MenuHandler):
        menu = gimp_toolkit.Menu()

        return MenuBuilder(gimp_toolkit, menu, menu_handler)

    def add_item(self, label, handler):
        item = self._gimp_toolkit.CheckMenuItem(label)

        item.set_draw_as_radio(True)
        item.connect('activate', self._menu_handler.create_item_handler(handler))
        self._menu_handler.add_item(item, handler)
        self._add_to_menu(item)

        return self

    def add_separator(self):
        item = self._gimp_toolkit.SeparatorMenuItem()

        self._add_to_menu(item)

        return self

    def build(self):
        self._menu.show_all()

        return self._menu

    def _add_to_menu(self, item):
        self._menu.append(item)
