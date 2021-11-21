class MenuBuilder:
    def __init__(self, menu, gimp_toolkit):
        self._menu = menu
        self._gimp_toolkit = gimp_toolkit

    @staticmethod
    def create(gimp_toolkit):
        menu = gimp_toolkit.Menu()

        return MenuBuilder(menu, gimp_toolkit)

    def add_item(self, label, handler):
        item = self._gimp_toolkit.MenuItem(label)

        item.connect('activate', handler)
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
