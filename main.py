import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

client = MyClient
client.run('OTA0NzE3MjAyNzY1MjY3MDE2.YX_ljQ.Q3wv5Ry4toIeZMxFRX1vMqEM8R8')
