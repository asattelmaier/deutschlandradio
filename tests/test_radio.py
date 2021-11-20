import unittest
from unittest.mock import MagicMock, call

from radio import Radio, Channel


class TestRadio(unittest.TestCase):
    def test_creation(self):
        """
        Test that a Radio instance will be created.
        """
        audio_player = MagicMock()

        radio = Radio.create(audio_player)

        self.assertIsInstance(radio, Radio)

    def test_default_channel(self):
        """
        Test that "Deutschlandfunk" will be the default channel.
        """
        audio_player = MagicMock()

        audio_player.is_playing = True
        radio = Radio.create(audio_player)
        radio.update_channel(Channel.DEUTSCHLANDFUNK)

        audio_player.stop.assert_called_once()

    def test_change_channel(self):
        """
        Test that the channel will be changed.
        """
        audio_player = MagicMock()
        channel = MagicMock()

        channel.value = 'some-channel-value'
        audio_player.is_playing = True
        radio = Radio.create(audio_player)
        radio.update_channel(channel)

        audio_player.set_uri.assert_has_calls([
            call(Channel.DEUTSCHLANDFUNK.value),
            call('some-channel-value')
        ])

    def test_play_updated_channel(self):
        """
        Test that the updated channel will be played directly.
        """
        audio_player = MagicMock()
        channel = MagicMock()

        channel.value = 'some-channel-value'
        audio_player.is_playing = True
        radio = Radio.create(audio_player)
        radio.update_channel(channel)

        audio_player.play.assert_called_once()

    def test_stop_player(self):
        """
        Test that the player will be stopped if the provided
        channel is already playing.
        """
        audio_player = MagicMock()
        channel = MagicMock()

        channel.value = 'some-channel-value'
        radio = Radio.create(audio_player)
        radio.update_channel(channel)
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

        channel.value = 'some-channel-value'
        radio = Radio.create(audio_player)
        radio.update_channel(channel)
        audio_player.is_playing = False
        radio.update_channel(channel)

        audio_player.play.assert_has_calls([call(), call()])
