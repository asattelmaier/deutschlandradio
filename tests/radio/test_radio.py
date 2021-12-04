import unittest
from unittest.mock import MagicMock

from src.radio import Radio, Stop, Play, ChangeChannel
from src.radio.subscriptions import OnUpdateChannel
from tests.mocks.event_bus_mock import EventBusMock


class TestRadio(unittest.TestCase):
    def test_current_channel(self):
        """
        Test that the current channel will be set.
        """
        audio_player = MagicMock()
        event_bus = MagicMock()
        channel = MagicMock()

        channel.value = 'some-channel'
        audio_player.is_playing = True
        Radio.init(audio_player, event_bus, channel)

        audio_player.set_uri.assert_called_once_with('some-channel')

    def test_change_channel(self):
        """
        Test that the channel will be changed.
        """
        audio_player = MagicMock()
        event_bus = EventBusMock()
        channel = MagicMock()
        update_channel_event = MagicMock()

        channel.value = 'some-channel'
        update_channel_event.channel.value = 'some-other-channel'
        audio_player.is_playing = True
        Radio.init(audio_player, event_bus, channel)
        event = event_bus \
            .get_subscription(OnUpdateChannel) \
            .notify(update_channel_event) \
            .get_event(ChangeChannel)

        self.assertIs(event.channel, update_channel_event.channel)

    def test_change_channel_audio_player_call_order(self):
        """
        Test the audio player call order:
          1. stop player
          2. set new uri
          3. start player
        The order is important, otherwise the new
        channel will not be played immediately after
        channel switch.
        """
        audio_player = MagicMock()
        event_bus = EventBusMock()
        channel = MagicMock()
        update_channel_event = MagicMock()

        channel.value = 'some-channel'
        update_channel_event.channel.value = 'some-other-channel'
        audio_player.is_playing = True
        Radio.init(audio_player, event_bus, channel)
        events = event_bus \
            .get_subscription(OnUpdateChannel) \
            .notify(update_channel_event) \
            .events

        self.assertIsInstance(events[0], Stop)
        self.assertIsInstance(events[1], ChangeChannel)
        self.assertIsInstance(events[2], Play)

    def test_play_updated_channel(self):
        """
        Test that the updated channel will be played directly.
        """
        audio_player = MagicMock()
        event_bus = EventBusMock()
        channel = MagicMock()
        update_channel_event = MagicMock()

        Radio.init(audio_player, event_bus, channel)
        events = event_bus \
            .get_subscription(OnUpdateChannel) \
            .notify(update_channel_event) \
            .events

        self.assertIsInstance(events[2], Play)

    def test_stop_player(self):
        """
        Test that the player will be stopped if the provided
        channel is already playing.
        """
        audio_player = MagicMock()
        event_bus = EventBusMock()
        channel = MagicMock()
        update_channel_event = MagicMock()

        Radio.init(audio_player, event_bus, channel)
        audio_player.is_playing = True
        events = event_bus \
            .get_subscription(OnUpdateChannel) \
            .notify(update_channel_event) \
            .events

        self.assertIsInstance(events[0], Stop)
