
import discord

class RPG_Event:
    def __init__(self, date, time, host, channel):
        self.date = date
        self.time = time
        self.host = host
        self.channel = channel

    def __repr__(self):
        rep = 'RPG EVENT\n'
        rep += ('\t- {}\n' * 4).format(self.date, self.time, self.host, self.channel)
        return rep

    def get_remind_message(self):
        return 'Remider @PC, an RPG session hosted by {} will begin in 30 minutes.'.format(self.host.user)

if __name__ == '__main__':
    event = RPG_Event()