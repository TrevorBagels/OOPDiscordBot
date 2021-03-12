import os, time, random, sys, discord, datetime, math, JSON4JSON
from discord.ext import tasks, commands
from discord.ext.commands.core import command
from discord.utils import get
import importlib
class MainBot(commands.Bot):
	def __init__(self):
		j4j = JSON4JSON.JSON4JSON()
		j4j.load("config.json", "rules.json")
		self.config = j4j.data
		commands.Bot.__init__(self, command_prefix=self.config['prefix'])
		self.Commands = self.add_module("commands")
	
	def add_module(self, name):
		module = importlib.import_module(f".", f"cogs.{name}").Module
		module_instance = module(self)
		self.add_cog(module_instance)
		return module_instance


if __name__ == "__main__":
	bot = MainBot()
	try:
		bot.run(bot.config['token'])
	except:
		print("token not valid.")