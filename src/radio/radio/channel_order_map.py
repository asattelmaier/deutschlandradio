from src.radio.radio import Channel


class ChannelOrderMap:
    _map = {
        Channel.DEUTSCHLANDFUNK.value: {
            'previous': Channel.DOKUMENTE_UND_DEBATTEN,
            'next': Channel.DEUTSCHLANDFUNK_KULTUR,
        },
        Channel.DEUTSCHLANDFUNK_KULTUR.value: {
            'previous': Channel.DEUTSCHLANDFUNK,
            'next': Channel.DEUTSCHLANDFUNK_NOVA,
        },
        Channel.DEUTSCHLANDFUNK_NOVA.value: {
            'previous': Channel.DEUTSCHLANDFUNK_KULTUR,
            'next': Channel.DOKUMENTE_UND_DEBATTEN,
        },
        Channel.DOKUMENTE_UND_DEBATTEN.value: {
            'previous': Channel.DEUTSCHLANDFUNK_NOVA,
            'next': Channel.DEUTSCHLANDFUNK,
        },
    }

    @staticmethod
    def next(channel: Channel) -> Channel:
        return ChannelOrderMap._map[channel.value]['next']

    @staticmethod
    def previous(channel: Channel) -> Channel:
        return ChannelOrderMap._map[channel.value]['previous']
