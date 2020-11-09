import embeds

data = None


async def reset(guild, json_data):
    global data
    data = json_data

    bot_commands_channel = guild.get_channel(data['channels']['management']['bot_commands'])

    async for message in bot_commands_channel.history():
        await message.delete()

    embed, file = embeds.embeds['help']()
    await bot_commands_channel.send(file=file, embed=embed)
    embed, file, reactions = embeds.embeds['global_mute']()

    message = await bot_commands_channel.send(file=file, embed=embed)

    for reaction in reactions:
        await message.add_reaction(reaction)

    return message


async def set_game_code(guild, code):
    game_code_channel = guild.get_channel(data['channels']['game']['game_code'])
    chat_channel = guild.get_channel(data['channels']['game']['chat'])

    embed, file = embeds.embeds['game-code'](code)

    if code is not None:
        await game_code_channel.edit(name='Game Code: {}'.format(code))
        await chat_channel.send(file=file, embed=embed)
    else:
        await game_code_channel.edit(name='Game Code: {}'.format('XXXXXX'))


commands = {
    'reset': lambda message, args: reset(message.guild),
    'code': lambda message, args: set_game_code(message.guild, args[0])
}


