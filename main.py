import discord, os
from discord.ext import commands
from colorama import Fore, init
from dotenv import load_dotenv

load_dotenv()
init(convert=True)
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!",help_command=None,intents=intents)

hoistingTags = ['!','?','$',',','.']

@bot.event
async def on_ready():
	print(f"{Fore.LIGHTGREEN_EX}------------------------------------------")
	print("Bot is ready!!")
	print(f"Logged in as {bot.user.name}#{bot.user.discriminator}")
	print("Bot made by !Not Aypro#8261")
	print(f"------------------------------------------{Fore.RESET}")

@bot.command()
async def start(ctx):
	changedCount = 0
	totalCount = 0
	guild = ctx.guild
	for member in guild.members:
		if list(member.display_name)[0] in hoistingTags:
			totalCount += 1
			try:
				await member.edit(nick="No hoisting!")
				print(f"{Fore.LIGHTGREEN_EX}Found {member.display_name}#{member.discriminator} hoisting, changing their nickname...{Fore.RESET}")
				changedCount += 1
			except discord.Forbidden:
				print(f"{Fore.LIGHTRED_EX}Missing permissions to change nickname of the user {member.display_name}#{member.discriminator}")
	await ctx.send(f"Successfully changed **{changedCount}/{totalCount}** users name")


@bot.event
async def on_member_update(before,after):
	if list(after.display_name)[0] in hoistingTags:
		try:
			await after.edit(nick="No hoisting!")
			print(f"{Fore.LIGHTGREEN_EX}Found {after.display_name}#{after.discriminator} hoisting, changing their nickname...{Fore.RESET}")
		except discord.Forbidden:
			print(f"{Fore.LIGHTRED_EX}Missing permissions to change nickname of the user {after.display_name}#{after.discriminator}")

bot.run(TOKEN)