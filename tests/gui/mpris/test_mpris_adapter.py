import unittest
from unittest.mock import MagicMock
from mpris_server.base import PlayState
from src.gui import MprisAdapter
from src.radio import OnPlay, Play, OnStop, Stop
from tests.mocks.event_bus_mock import EventBusMock


class TestMprisAdapter(unittest.TestCase):
    def test_on_playpause_call_on_play_subscription(self):
        """
        Test that `on_playpause()` gets called on play.
        """
        event_bus = EventBusMock()
        current_channel = MagicMock()
        event_adapter = MagicMock()
        event = MagicMock()
        mpris_adapter = MprisAdapter.create(event_bus, current_channel)

        mpris_adapter.set_event_adapter(event_adapter)
        event_bus \
            .get_subscription(OnPlay) \
            .notify(event)

        event_adapter.on_playpause.assert_called()

    def test_playstate_on_play_subscription(self):
        """
        Test that the play state is `PLAYING` after on play subscription.
        """
        event_bus = EventBusMock()
        current_channel = MagicMock()
        event_adapter = MagicMock()
        event = MagicMock()
        mpris_adapter = MprisAdapter.create(event_bus, current_channel)

        mpris_adapter.set_event_adapter(event_adapter)
        event_bus \
            .get_subscription(OnPlay) \
            .notify(event)
        playstate = mpris_adapter.get_playstate()

        self.assertEqual(PlayState.PLAYING, playstate)

    def test_current_channel_on_play_subscription(self):
        """
        Test that the event channel will be published on play.
        """
        event_bus = EventBusMock()
        current_channel = MagicMock()
        event_adapter = MagicMock()
        event = MagicMock()
        mpris_adapter = MprisAdapter.create(event_bus, current_channel)

        event.channel = MagicMock()
        mpris_adapter.set_event_adapter(event_adapter)
        event_bus \
            .get_subscription(OnPlay) \
            .notify(event)
        mpris_adapter.play()
        play_event = event_bus \
            .get_event(Play)

        self.assertEqual(play_event.channel, event.channel)

    def test_on_playpause_call_on_stop_subscription(self):
        """
        Test that `on_playpause()` gets called on stop.
        """
        event_bus = EventBusMock()
        current_channel = MagicMock()
        event_adapter = MagicMock()
        event = MagicMock()
        mpris_adapter = MprisAdapter.create(event_bus, current_channel)

        mpris_adapter.set_event_adapter(event_adapter)
        event_bus \
            .get_subscription(OnStop) \
            .notify(event)

        event_adapter.on_playpause.assert_called()

    def test_playstate_on_stop_subscription(self):
        """
        Test that the play state is `STOPPED` after on stop subscription.
        """
        event_bus = EventBusMock()
        current_channel = MagicMock()
        event_adapter = MagicMock()
        event = MagicMock()
        mpris_adapter = MprisAdapter.create(event_bus, current_channel)

        mpris_adapter.set_event_adapter(event_adapter)
        event_bus \
            .get_subscription(OnStop) \
            .notify(event)
        playstate = mpris_adapter.get_playstate()

        self.assertEqual(playstate, PlayState.STOPPED)

    def test_current_channel_on_stop_subscription(self):
        """
        Test that the event channel will be published on stop.
        """
        event_bus = EventBusMock()
        current_channel = MagicMock()
        event_adapter = MagicMock()
        event = MagicMock()
        mpris_adapter = MprisAdapter.create(event_bus, current_channel)

        event.channel = MagicMock()
        mpris_adapter.set_event_adapter(event_adapter)
        event_bus \
            .get_subscription(OnStop) \
            .notify(event)
        mpris_adapter.pause()
        stop_event = event_bus \
            .get_event(Stop)

        print(event_bus._events)

        self.assertEqual(stop_event.channel, event.channel)