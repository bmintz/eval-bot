#!/usr/bin/env python3
# encoding: utf-8

import logging

import discord
from discord.ext import commands

logging.basicConfig(level=logging.WARNING)  # prevent annoying startup messages from discord
logger = logging.getLogger('bot')
logger.setLevel(logging.INFO)

class Bot(commands.Bot):
	def __init__(self):
		super().__init__(command_prefix='')
		self.remove_command('help')
		self.load_extension('jishaku')

	async def is_owner(self, user):
		return True  # :Think:

	async def on_ready(self):
		logger.info('Logged in as: %s', self.user)

bot = Bot()

def main():
	import os
	bot.run(os.environ['discord_bot_token'])

if __name__ == '__main__':
	main()
