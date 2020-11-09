import time

import discord
from discord import Message

import commands
import embeds
import json
import os

intents = discord.Intents.all()
client = discord.Client(intents=intents)
global_mute_message = None

server_guild = None  # Server Guild ID

mute_listeners = []  # A list of Members which mute the Game Call when they mute themselves
force_muted = []  # All Members that ara forcefully muted by the Bot
self_mute = []  # A List of all Members which have muted themselves
muted = False  # If the Game Call is muted

with open('config.json') as config:
    data = json.load(config)


@client.event
async def on_ready():
    global server_guild
    global global_mute_message

    server_guild = client.get_guild(773213583982460939)
    global_mute_message = await commands.reset(server_guild, data)

    await commands.set_game_code(server_guild, None)

    print("Bot online")


@client.event
async def on_message(message):
    if message.content.startswith('!') and message.channel.id == data['channels']['management']['bot_commands']:
        content = message.content.split(' ')
        command = content[0][1::]
        args = content[1::]

        if command in commands.commands:
            result = await commands.commands[command](message, args)

            if type(result) == Message:
                global global_mute_message
                global_mute_message = result
        else:
            embed, file = embeds.embeds['unknown_command'](command)
            msg = await message.channel.send(file=file, embed=embed)
            await msg.delete(delay=10)
        await message.delete()
    elif message.channel.id == data['channels']['management']['bot_commands'] \
            and not message.author.bot:
        await message.delete()


async def update_mute(channel, mute):
    global muted
    muted = mute

    for member in channel.members:
        if (member in force_muted) != mute:
            if mute:
                force_muted.append(member)
            else:
                force_muted.remove(member)

            await member.edit(mute=muted)


@client.event
async def on_reaction_add(reaction, member):
    if reaction.emoji == '🔇' and reaction.message == global_mute_message and member.roles and member.voice:
        await update_mute(member.voice.channel, True)
    elif reaction.emoji == '📻' and reaction.message == global_mute_message and member.roles and member.voice:
        mute_listeners.append(member)
    elif not member.voice and not member.bot:
        await reaction.message.remove_reaction(reaction.emoji, member)


@client.event
async def on_reaction_remove(reaction, member):
    if reaction.emoji == '🔇' and reaction.message == global_mute_message and member.roles:
        await update_mute(member.voice.channel, False)
    elif reaction.emoji == '📻' and reaction.message == global_mute_message and member.roles and member.voice:
        mute_listeners.remove(member)


@client.event
async def on_voice_state_update(member, before, after):
    if after.self_mute and not before.self_mute and member not in self_mute:
        self_mute.append(member)
    elif not after.self_mute and before.self_mute and member in self_mute:
        self_mute.remove(member)

    if member in mute_listeners:
        if after.channel is None and before.channel is not None:
            await global_mute_message.remove_reaction('🔇', member)
            await global_mute_message.remove_reaction('📻', member)

            mute_listeners.remove(member)

            if len(mute_listeners) == 0:
                await update_mute(member.voice.channel, False)
                return

        for mute in self_mute:
            if mute not in mute_listeners:
                continue
            else:
                await update_mute(member.voice.channel, True)
                return

        await update_mute(member.voice.channel, False)

client.run(os.environ['AMONG_US_BOT_TOKEN'])
