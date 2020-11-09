import embeds
import time

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

    print('Code: ' + str(code))

    if code is not None:
        print('k')
        start = time.time()
        #await game_code_channel.edit(name='Game Code: {}'.format(code))
        mid = time.time()
        print('Mid: {}'.format(mid - start))
        await chat_channel.send(file=file, embed=embed)
        end = time.time()
        print('End: {}'.format(end - mid))
        print('Total: {}'.format(end - start))
    else:
        await game_code_channel.edit(name='Game Code: {}'.format('XXXXXX'))


commands = {
    'reset': lambda message, args: reset(message.guild),
    'code': lambda message, args: set_game_code(message.guild, args[0])
}


