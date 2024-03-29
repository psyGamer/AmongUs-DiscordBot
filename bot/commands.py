import embeds

data = None

async def reset(guild, json_data):
    global data
    data = json_data

    bot_commands_channel = guild.get_channel(data['channels']['chat_for_admins'])

    async for message in bot_commands_channel.history():
        await message.delete()

    embed, file = embeds.embeds['help'](data['use_german'])
    await bot_commands_channel.send(file=file, embed=embed)
    embed, file, reactions = embeds.embeds['global_mute'](data['use_german'])

    message = await bot_commands_channel.send(file=file, embed=embed)

    for reaction in reactions:
        await message.add_reaction(reaction)

    return message


async def set_game_code(guild, code):
    game_code_channel = guild.get_channel(data['channels']['call_to_display_game_code'])
    chat_channel = guild.get_channel(data['channels']['chat_for_game_code'])

    embed, file = embeds.embeds['game-code'](code, data['use_german'])

    if code is not None:
        await game_code_channel.edit(name='Game Code: {}'.format(code))
        await chat_channel.send(file=file, embed=embed)
    else:
        await game_code_channel.edit(name='Game Code: {}'.format('XXXXXX'))


commands = {
    'reset': lambda message, args: reset(message.guild),
    'code': lambda message, args: set_game_code(message.guild, args[0])
}


