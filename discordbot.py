#/usr/bin/env python3
# discord.py code adapted from https://discordpy.readthedocs.io/

import re

import discord

# This token can be found on the Bot page for your application
DISCORD_TOKEN = ''

class RegexBot(discord.Client):
    """Bot that responds to chat messages on Discord."""

    def make_reply(self, text, author):
        """The function where you do your regular expression work!
        
        Arguments:
            text (string): The text of the message sent
            author (string): The display name of the user who sent it
        """
        # Current just echoes the message sent with the author name
        reply = author + " just said: " + text
        return reply

    async def on_ready(self):
        # Runs when successfully connected to the server
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        # This passes the message's text and author name as 
        reply = self.make_reply(message.content, message.author.name)
        if reply:
            await message.channel.send(reply)


if __name__ == "__main__":
    client = RegexBot()
    client.run(DISCORD_TOKEN)

# Discover NLP course materials authored by Julie Medero, Xanda Schofield, and Richard Wicentowski
# This work is licensed under a Creative Commons Attribution-ShareAlike 2.0 Generic License# https://creativecommons.org/licenses/by-sa/2.0/
