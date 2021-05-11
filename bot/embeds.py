import discord


def command_help(german):
    if german:
        embed = discord.Embed(title='**Hilfe zu allen Befehlen**',
                              description='Hier stehen alle Befehle zusammen mit ihrer Erklärung\n\n'
                                          '**!set-game-code [Game-Code]**'
                                          '     Ändert den aktuellen Game Code',
                              color=0x72A7CF)
        file = discord.File('./images/info.png', filename='info.png')
        embed.set_thumbnail(url='attachment://info.png')

        return embed, file
    else:
        embed = discord.Embed(title='**Help to all commands**',
                              description='Here are all commands with their summary\n\n'
                                          '**!set-game-code [game code]**'
                                          '     Changes the current game code',
                              color=0x72A7CF)
        file = discord.File('./images/info.png', filename='info.png')
        embed.set_thumbnail(url='attachment://info.png')

        return embed, file


def global_mute(german):
    if german:
        embed = discord.Embed(title='**Global Mute**',
                              description='Wenn jemand mit :mute: reagiert werden alle im Game Call stummgeschalten'
                                          'Wenn jemand mit :radio: reagiert werden alle im Game Call stummgeschalten, '
                                          'sobald man sich selbst stummschaltet',
                              color=0xFF8E00)
        file = discord.File('./images/mute.png', filename='mute.png')
        embed.set_thumbnail(url='attachment://mute.png')

        return embed, file, ['🔇', '📻']
    else:
        embed = discord.Embed(title='**Global Mute**',
                              description='Once someone reacts with :mute: all users in the game call get muted'
                                          'Once somenoe reacts with :radio: all user in the game call get muted, '
                                          'once you mute yourself.',
                              color=0xFF8E00)
        file = discord.File('./images/mute.png', filename='mute.png')
        embed.set_thumbnail(url='attachment://mute.png')

        return embed, file, ['🔇', '📻']

def maps():
    embed = discord.Embed(title='**Maps**',
                          color=0xFF8E00)

    skeld = discord.File('./images/skeld.jpg', filename='mute.png')
    mira_hq = discord.File('./images/mirahq.jpg', filename='mute.png')
    polus = discord.File('./images/polus.jpg', filename='mute.png')

    embed.set_thumbnail(url='attachment://mute.png')


def unknown_command(command, german):
    if german:
        embed = discord.Embed(title='**Unbekannter Befehl:** {}'.format(command),
                              description='Dieser Befehl existiert nicht\nBitte überprüfe nochmal ob die Schreibweise '
                                          'korrekt ist.',
                              color=0xFE2121)
        file = discord.File('./images/close.png', filename='close.png')
        embed.set_thumbnail(url='attachment://close.png')
    else:
        embed = discord.Embed(title='**Unknown command:** {}'.format(command),
                              description='This command doesn\'t exist\nPlease check if you spelled it correct ',
                              color=0xFE2121)
        file = discord.File('./images/close.png', filename='close.png')
        embed.set_thumbnail(url='attachment://close.png')

    return embed, file


def game_code(code, german):
    if german:
        embed = discord.Embed(title='Aktueller Game Code: **`{}`**'.format(code),
                              color=0xFF4141)
        file = discord.File('./images/cover.png', filename='cover.png')
        embed.set_image(url='attachment://cover.png')

        return embed, file
    else:
        embed = discord.Embed(title='Current game code: **`{}`**'.format(code),
                              color=0xFF4141)
        file = discord.File('./images/cover.png', filename='cover.png')
        embed.set_image(url='attachment://cover.png')

        return embed, file

embeds = {
    'help': command_help,
    'global_mute': global_mute,
    'maps': maps,
    'unknown_command': unknown_command,
    'game-code': game_code
}
