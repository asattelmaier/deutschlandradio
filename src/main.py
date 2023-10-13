import argparse
import gui
import radio
from event_bus import EventBus
from src.logger import Logger


def main() -> None:
    current_channel = radio.Channel.DEUTSCHLANDFUNK
    event_bus = EventBus()

    radio.create(event_bus, current_channel)
    gui.create(event_bus)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--log-level", help="Set the log level (DEBUG)")
    parser.add_argument("--version", action="version", version="rundfunk version 2.1.1")
    args = parser.parse_args()
    Logger.setup(args.log_level)

    main()
