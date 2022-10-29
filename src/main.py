import gui
import radio
from event_bus import EventBus


def main() -> None:
    current_channel = radio.Channel.DEUTSCHLANDFUNK
    event_bus = EventBus()

    radio.create(event_bus, current_channel)
    gui.create(event_bus)


if __name__ == "__main__":
    main()
