import os, time, random, sys, discord, datetime
from discord.ext import commands
from discord.ext.commands.core import command
from discord.utils import get
from utils import pluralize, mention
class Module(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.test = 'hello world'
	
	@commands.command(brief='pings a person')
	async def ping(self, ctx, target: discord.Member):
		pings = random.randrange(1, 4)
		await ctx.channel.send(f"Pinging {mention(target.id)} {pluralize('time', pings, n=True, pref=' more ')}")
		for x in range(pings): await ctx.channel.send(target.mention)
