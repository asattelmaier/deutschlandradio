import unittest
from unittest.mock import MagicMock, call

from radio import Radio


class TestRadio(unittest.TestCase):
    def test_creation(self):
        """
        Test that a Radio instance will be created.
        """
        audio_player = MagicMock()
        channel = MagicMock()

        radio = Radio.create(audio_player, channel)

        self.assertIsInstance(radio, Radio)

    def test_current_channel(self):
        """
        Test that the current channel will be set.
        """
        audio_player = MagicMock()
        channel = MagicMock()

        channel.value = 'some-channel'
        audio_player.is_playing = True
        Radio.create(audio_player, channel)

        audio_player.set_uri.assert_called_once_with('some-channel')

    def test_change_channel(self):
        """
        Test that the channel will be changed.
        """
        audio_player = MagicMock()
        channel = MagicMock()
        other_channel = MagicMock()

        channel.value = 'some-channel'
        other_channel.value = 'some-other-channel'
        audio_player.is_playing = True
        radio = Radio.create(audio_player, channel)
        radio.update_channel(other_channel)

        audio_player.set_uri.assert_has_calls([
            call('some-channel'),
            call('some-other-channel')
        ])

    def test_play_updated_channel(self):
        """
        Test that the updated channel will be played directly.
        """
        audio_player = MagicMock()
        channel = MagicMock()
        other_channel = MagicMock()

        radio = Radio.create(audio_player, channel)
        radio.update_channel(other_channel)

        audio_player.play.assert_called_once()

    def test_stop_player(self):
        """
        Test that the player will be stopped if the provided
        channel is already playing.
        """
        audio_player = MagicMock()
        channel = MagicMock()

        radio = Radio.create(audio_player, channel)
        audio_player.is_playing = True
        radio.update_channel(channel)

        audio_player.stop.assert_called_once()

    def test_play_player(self):
        """
        Test that the player will be played if the provided
        channel is stopped.
        """
        audio_player = MagicMock()
        channel = MagicMock()
        other_channel = MagicMock()

        radio = Radio.create(audio_player, channel)
        radio.update_channel(other_channel)
        audio_player.is_playing = False
        radio.update_channel(other_channel)

        audio_player.play.assert_has_calls([call(), call()])
