class MenuBuilder:
    def __init__(self, gimp_toolkit, menu):
        self._gimp_toolkit = gimp_toolkit
        self._menu = menu

    @staticmethod
    def create(gimp_toolkit):
        menu = gimp_toolkit.Menu()

        return MenuBuilder(gimp_toolkit, menu)

    def add_item(self, label, handler):
        item = self._gimp_toolkit.CheckMenuItem(label)

        item.set_draw_as_radio(True)
        item.connect('activate', self._create_item_handler(handler))
        self._add_to_menu(item)

        return self

    def add_separator(self):
        item = self._gimp_toolkit.SeparatorMenuItem()

        self._add_to_menu(item)

        return self

    def build(self):
        self._menu.show_all()

        return self._menu

    @property
    def _menu_items(self):
        return filter(self._is_menu_item, self._menu)

    @staticmethod
    def _disable_items(items):
        for item in items:
            item.set_active(False)

    def _is_menu_item(self, item):
        return isinstance(item, self._gimp_toolkit.CheckMenuItem)

    def _add_to_menu(self, item):
        self._menu.append(item)

    def _create_item_handler(self, handler):
        return lambda item: self._item_handler(item, handler)

    def _item_handler(self, item, handler):
        handler()

        # TODO: Move this logic to make it simple testable
        if item.get_active():
            items = self._filter_menu_item(item)
            MenuBuilder._disable_items(items)

    def _filter_menu_item(self, item_to_filter):
        return filter(lambda item: item is not item_to_filter, self._menu_items)
