'''

   TT  TT TT  TT     OOOOOOOOO          LL                    YY    YY
      TTTT         OO         OO        LL                       YY 
       T TT          OO          OO       LL                     YY
       TT          OO          OO       LL                       YY
       TT          OO           OO      LL                       YY    
       TT           OO         OO        LL LL LL LL  LL          YY
                    OOOO  OO OO  OO        
                                Version 1.0
Hello,
I created this bot for my project, which is called "Узник Узника Python'а ", i think that you'll like it. When i developed it, i wanted created the Multifunctional discord bot
And i added a comments for this project, for your convenience
I used a new library for python - it's called 'Disnake', you can get to know it here:
:link: https://docs.disnake.dev/en/stable/ :link:
Also you can join to disnake-community for this link:
:link: https://discord.gg/disnake :link:
You can edit name of all, but here i'll give a name to all buttons etc
'''
# let's start
import disnake
from disnake.ext import commands
from disnake.enums import ButtonStyle
bot = commands.Bot(
    command_prefix = "p.",
    intents        = disnake.Intents().all()
)
modsroleslist = [
    1031970576526479480, # STAFF modsroleslist[0]
    1031967292793307207, # Тех. Часть modsroleslist[1]
    1031970471836647464, # Куратор modsroleslist modsroleslist[2]
    ]
class RoleButtons(disnake.ui.View):# create buttons object for autoroles-embed
    def __init__(self):
        super().__init__(timeout=None)

    # Creates a row of buttons and when one of them is pressed, it will send a message with the number of the button.
    @disnake.ui.button(label="ГАЙДЫ", style=ButtonStyle.grey)
    async def rguide_button1(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.defer()
        message = await interaction.original_message()
        role = interaction.guild.get_role(1033740441423712396)
        if role:
            if role in interaction.user.roles:
                await interaction.send(embed=disnake.Embed(description=f':x: Роль *{role.name}* убрана.'),ephemeral=True)
                await interaction.user.remove_roles(role)
            else:
                await interaction.send(embed=disnake.Embed(description=f':white_check_mark: Роль *{role.name}* добавлена'),ephemeral=True)
                await interaction.user.add_roles(role)

    @disnake.ui.button(label="Junior Developer", style=ButtonStyle.blurple)
    async def role_button1(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.defer()
        message = await interaction.original_message()
        role = interaction.guild.get_role(1031975356061716541)
        if role:
            if role in interaction.user.roles:
                await interaction.send(embed=disnake.Embed(description=f':x: Роль *{role.name}* убрана.'),ephemeral=True)
                await interaction.user.remove_roles(role)
            else:
                await interaction.send(embed=disnake.Embed(description=f':white_check_mark: Роль *{role.name}* добавлена'),ephemeral=True)
                await interaction.user.add_roles(role)  

    @disnake.ui.button(label="Middle Developer", style=ButtonStyle.red)
    async def role_button2(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.defer()
        message = await interaction.original_message()
        role = interaction.guild.get_role(1031975161227923657)
        if role:
            if role in interaction.user.roles:
                await interaction.send(embed=disnake.Embed(description=f':x: Роль *{role.name}* убрана.'),ephemeral=True)
                await interaction.user.remove_roles(role)
            else:
                await interaction.send(embed=disnake.Embed(description=f':white_check_mark: Роль *{role.name}* добавлена'),ephemeral=True)
                await interaction.user.add_roles(role)
    
    @disnake.ui.button(label="Senior Developer", style=ButtonStyle.grey)
    async def role_button3(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.defer()
        message = await interaction.original_message()
        role = interaction.guild.get_role(1031975041144983552)
        if role:
            if role in interaction.user.roles:
                await interaction.send(embed=disnake.Embed(description=f':x: Роль *{role.name}* убрана.'),ephemeral=True)
                await interaction.user.remove_roles(role)
            else:
                await interaction.send(embed=disnake.Embed(description=f':white_check_mark: Роль *{role.name}* добавлена'),ephemeral=True)
                await interaction.user.add_roles(role)
    
    @disnake.ui.button(label='Убрать все роли', style=ButtonStyle.green)
    async def deleteroles_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.defer()
        message = await interaction.original_message()
        role1 = interaction.guild.get_role(1031975356061716541)
        role2 = interaction.guild.get_role(1031975161227923657)
        role3 = interaction.guild.get_role(1031975041144983552)
        if role1:
            if role1 or role2 or role3 in interaction.user.roles:
                await interaction.send(embed=disnake.Embed(description=f':x: Роли убраны.'),ephemeral=True)
                await interaction.user.remove_roles(role1)
                await interaction.user.remove_roles(role2)
                await interaction.user.remove_roles(role3)
            else:
                await interaction.send(embed=disnake.Embed(description=f':white_check_mark: У вас нет ни одной из ролей'),ephemeral=True)

class RoleLangButtons(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    # Creates a row of buttons and when one of them is pressed, it will send a message with the number of the button.


    @disnake.ui.button(label="Java", style=ButtonStyle.gray)
    async def role_java(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.defer()
        message = await interaction.original_message()
        role = interaction.guild.get_role(1033421160668479488)
        if role:
            if role in interaction.user.roles:
                await interaction.send(embed=disnake.Embed(description=f':x: Роль *{role.name}* убрана.'),ephemeral=True)
                await interaction.user.remove_roles(role)
            else:
                await interaction.send(embed=disnake.Embed(description=f':white_check_mark: Роль *{role.name}* добавлена'),ephemeral=True)
                await interaction.user.add_roles(role)  

    @disnake.ui.button(label="JS", style=ButtonStyle.gray)
    async def role_js(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.defer()
        message = await interaction.original_message()
        role = interaction.guild.get_role(1033416860034682960)
        if role:
            if role in interaction.user.roles:
                await interaction.send(embed=disnake.Embed(description=f':x: Роль *{role.name}* убрана.'),ephemeral=True)
                await interaction.user.remove_roles(role)
            else:
                await interaction.send(embed=disnake.Embed(description=f':white_check_mark: Роль *{role.name}* добавлена'),ephemeral=True)
                await interaction.user.add_roles(role)
    
    @disnake.ui.button(label="PHP", style=ButtonStyle.grey)
    async def role_php(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.defer()
        message = await interaction.original_message()
        role = interaction.guild.get_role(1033416904938885170)
        if role:
            if role in interaction.user.roles:
                await interaction.send(embed=disnake.Embed(description=f':x: Роль *{role.name}* убрана.'),ephemeral=True)
                await interaction.user.remove_roles(role)
            else:
                await interaction.send(embed=disnake.Embed(description=f':white_check_mark: Роль *{role.name}* добавлена'),ephemeral=True)
                await interaction.user.add_roles(role)
    
    @disnake.ui.button(label="Python", style=ButtonStyle.grey)
    async def role_python(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.defer()
        message = await interaction.original_message()
        role = interaction.guild.get_role(1033416897259122728)
        if role:
            if role in interaction.user.roles:
                await interaction.send(embed=disnake.Embed(description=f':x: Роль *{role.name}* убрана.'),ephemeral=True)
                await interaction.user.remove_roles(role)
            else:
                await interaction.send(embed=disnake.Embed(description=f':white_check_mark: Роль *{role.name}* добавлена'),ephemeral=True)
                await interaction.user.add_roles(role)
    
    @disnake.ui.button(label="C#", style=ButtonStyle.grey)
    async def role_cs(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.defer()
        message = await interaction.original_message()
        role = interaction.guild.get_role(1033416961176109106)
        if role:
            if role in interaction.user.roles:
                await interaction.send(embed=disnake.Embed(description=f':x: Роль *{role.name}* убрана.'),ephemeral=True)
                await interaction.user.remove_roles(role)
            else:
                await interaction.send(embed=disnake.Embed(description=f':white_check_mark: Роль *{role.name}* добавлена'),ephemeral=True)
                await interaction.user.add_roles(role)
    
    @disnake.ui.button(label="C/C++", style=ButtonStyle.grey)
    async def role_C(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.defer()
        message = await interaction.original_message()
        role = interaction.guild.get_role(1033417022412968057)
        if role:
            if role in interaction.user.roles:
                await interaction.send(embed=disnake.Embed(description=f':x: Роль *{role.name}* убрана.'),ephemeral=True)
                await interaction.user.remove_roles(role)
            else:
                await interaction.send(embed=disnake.Embed(description=f':white_check_mark: Роль *{role.name}* добавлена'),ephemeral=True)
                await interaction.user.add_roles(role)
    
    @disnake.ui.button(label='Убрать все роли', style=ButtonStyle.green)
    async def deleteroles_button(
        self, button: disnake.ui.Button, interaction: disnake.MessageInteraction
    ):
        await interaction.response.defer()
        message = await interaction.original_message()
        role1 = interaction.guild.get_role(1033417022412968057)
        role2 = interaction.guild.get_role(1033416961176109106)
        role3 = interaction.guild.get_role(1033416904938885170)
        role4 = interaction.guild.get_role(1033416897259122728)
        role5 = interaction.guild.get_role(1033416860034682960)
        role6 = interaction.guild.get_role(1033421160668479488)
        if role1:
            if role1 or role2 or role3 or role4 or role5 or role6 in interaction.user.roles:
                await interaction.send(embed=disnake.Embed(description=f':x: Роли убраны.'),ephemeral=True)
                await interaction.user.remove_roles(role1)
                await interaction.user.remove_roles(role2)
                await interaction.user.remove_roles(role3)
                await interaction.user.remove_roles(role4)
                await interaction.user.remove_roles(role5)
                await interaction.user.remove_roles(role6)
            else:
                await interaction.send(embed=disnake.Embed(description=f':white_check_mark: У вас нет ни одной из ролей'),ephemeral=True)

class events:
    @bot.event
    async def on_ready(): # event starting when bot is ready:
    #console ready-mark
        print(f'''
        Bot: {bot.user.display_name}
        Статус: {bot.status}
        ''')
    #autorole-embed
        mainembed = disnake.Embed(color = 0x303136, description = f"")
        mainembed.add_field(name=f"Роли FoxFord", value="Для получения интересующей вас роли \nВам достаточно нажать на кнопку и вам будет выдана роль.")
        mainembed.set_image(url='https://support.discord.com/hc/article_attachments/360013500032/nitro_gif.gif')
    #second autorole-embed
        langembed = disnake.Embed(color = 0x303136, description = f"")
        langembed.add_field(name=f"Роли FoxFord(Языки Программирования)", value="Для получения интересующей вас роли \nВам достаточно нажать на кнопку и вам будет выдана роль.")
        langembed.set_image(url='https://media.tenor.com/cKgOapMuyWcAAAAC/coding-developer-code.gif')  
        channel = bot.get_channel(1033398087936397343)
        await channel.purge(limit=20)
        await channel.send(embed=mainembed, view=RoleButtons()) 
        await channel.send(embed=langembed, view=RoleLangButtons())   

    

    @bot.event
    async def on_raw_reaction_add(payload): #event starting when somebody add reaction to message
        """ 
        $ if someone adds a reaction not in the channel "channelid", the bot ignores it.
        $ Otherwise, if someone adds a reaction to a message in the channel "channelid", the bot starts a new check:
        $ If member wich added role not MOD(Here MOD - only 3 members, and not definite mod-role), bot delete this reaction
        """
        channelid = payload.channel_id
        user = payload.member
        messageid = payload.message_id
        if channelid == 1031911925690417253:
            channel = bot.get_channel(channelid)
            message = await channel.fetch_message(messageid)
            if payload.member.mention == "<@788591270712574014>":
                pass
            elif payload.member.mention == "<@1031891517838737408>":
                pass
            elif payload.member.mention == "<@1018723024700199025>":
                pass
            else:
                for reaction in message.reactions:
                    await reaction.remove(user)
        else:
            return


    

    @bot.event #event starting when somebody join to our guild
    async def on_member_join(member):
        channel__welcome = bot.get_channel(1031971102106320916)
        embed = disnake.Embed(
            title = f"{member.name} добро пожаловать на сервер!", 
        )
        date_format = "%a, %b %d, %Y | %I:%M %p" 
        embed.add_field(name="Member name: ",value=f'`{member}`',inline=False)
        embed.add_field(name="Member id",value=f"`{member.id}`",inline=False)
        embed.add_field(name="Date of join",value=f'`{member.joined_at.strftime(date_format)}`',inline=True)
        embed.add_field(name='Date of create',value=f'`{member.created_at.strftime(date_format)}`',inline=True)
        await channel__welcome.send(f'{member.mention}')
        await channel__welcome.send(embed = embed)
        await member.send('Доброго времени суток!\nВы зашли в discord-сообщество FoxFord по курсу веб-разработки.\nЧто бы получить доступ к каналам, нажмите на кнопку в канале: <#1033398087936397343>')
        await member.send('https://media.tenor.com/rr7TAKrxAaIAAAAM/boom.gif')
        message = await member.send(embed=embed)
        await message.edit('Тех.часть')
    @bot.event
    async def on_member_remove(member):
        channel_welcome = bot.get_channel(1031971102106320916)
        embed = disnake.Embed(
            title = f"{member.name} покинул наш сервер!", 
        )
        date_format = "%a, %b %d, %Y | %I:%M %p" 
        embed.add_field(name="Member name: ",value=f'`{member}`',inline=False)
        embed.add_field(name="Member id",value=f"`{member.id}`",inline=False)
        embed.add_field(name='Date of create',value=f'`{member.created_at.strftime(date_format)}`',inline=True)
        await channel_welcome.send(f'{member.mention}')
        await channel_welcome.send(embed = embed)

class slash_commands:
    @bot.slash_command(name="mod") #base case for command
    async def moderator(inter):
        pass

    @moderator.sub_command(name='ban',description='Blacklist')
    @commands.has_any_role(modsroleslist[0],modsroleslist[1],modsroleslist[2])
    async def ban(
        inter: disnake.CommandInteraction,
        member: disnake.Member,
        reason: str
        ):
        commands_log = inter.author.guild.get_channel(1031971076877598750)
        banembed = disnake.Embed(title="Blacklist",description=f"{member}... Now. He's on Blacklist")
        banembed.add_field(name='Причина наказания BAN:',value=f'{reason}')
        banembed.add_field(name='Модератор:',value=f'{inter.author.mention}')
        banembed.add_field(name='STATICID Модератора:',value=f"{inter.author.id}")
        banembed.add_field(name='Наказанный:',value=f'{member.mention}')
        banembed.add_field(name='STATICID Наказанного:',value=f"{member.id}")

        personalembed = disnake.Embed(title=f"Вы были наказанны на {inter.author.guild.name} системой BAN",description=f'По причине {reason}')
        personalembed.add_field(name='Модератор:',value=f'{inter.author}')

        await inter.send(embed=banembed)
        message = await commands_log.send(embed=banembed)
        await message.edit(member.mention)
        await member.send(embed=personalembed)
        await member.send('`Если вы считаете что вас наказали не честно. Можете обратиться к следящей за Модераторами адмнистрацией: toly#8788, I\'m toly#8788`')

        await member.ban(reason=reason)

    @moderator.sub_command(name='kick',description='Get out of here[Moderate]')
    @commands.has_any_role(modsroleslist[0],modsroleslist[1],modsroleslist[2])
    async def kick(
        inter: disnake.CommandInteraction,
        member: disnake.Member,
        reason: str
        ):
        guild = bot.get_guild(1013797936716595230)
        commands_log = guild.get_channel(1031971076877598750)
        banembed = disnake.Embed(title="Наказание системой KICK",description=f"{member}... Now. He's on Blacklist")
        banembed.add_field(name='Причина наказания KICK:',value=f'{reason}')
        banembed.add_field(name='Модератор:',value=f'{inter.author.mention}')
        banembed.add_field(name='STATICID Модератора:',value=f"{inter.author.id}")
        banembed.add_field(name='Наказанный:',value=f'{member.mention}')
        banembed.add_field(name='STATICID Наказанного:',value=f"{member.id}")

        personalembed = disnake.Embed(title=f"Вы были наказанны на {guild.name} системой KICK",description=f'По причине {reason}')
        personalembed.add_field(name='Модератор:',value=f'{inter.author}')

        await inter.send(embed=banembed)
        message = await commands_log.send(embed=banembed)
        await message.edit(member.mention)
        await member.send(embed=personalembed)
        await member.send('`Если вы считаете что вас наказали не честно. Можете обратиться к следящей за Модераторами адмнистрацией: toly#8788, I\'m toly#8788`')

        await member.kick(reason=reason)

    @moderator.sub_command(name="get-info",description='Getting info about user[Mod]')
    @commands.has_any_role(modsroleslist[0],modsroleslist[1],modsroleslist[2])
    async def gi(inter: disnake.CommandInteraction, member: disnake.Member):
        if member.voice is None:
            voiceid = "None"
        else:
            voiceid = f"<#{member.voice.channel.id}>"
        statval = member.status.value
        if statval == 'dnd':
            statval = "💓Не беспокоить"
        elif statval == 'online':
            statval = "💚Online"
        elif statval == 'idle':
            statval = "💛Не активен"
        else:
            statval = member.status.value
        date_format = "%a, %b %d, %Y | %I:%M %p" 
        embed = disnake.Embed(description=f"Модератор {inter.author} запросил info о пользователе")
        embed.add_field(name='UID|SID',value=f'`{member.id}`')
        embed.add_field(name='Server name',value=f'`{member.display_name}`')
        embed.add_field(name='Name',value=f'`{member.name}`')
        embed.add_field(name='Top role',value=f'`||`{member.top_role.mention}`||`')
        embed.add_field(name="Date of join",value=f'`{member.joined_at.strftime(date_format)}`',inline=True)
        embed.add_field(name='Date of create',value=f'`{member.created_at.strftime(date_format)}`',inline=True)

        embed.add_field(name='Status',value=f'`{statval}`',inline=True)
        embed.add_field(name='Activity Status',value=f'`{member.activity}`',inline=True)
        embed.add_field(name='Name and discriminator',value=f'`{member}`',inline=True)
        embed.add_field(name='Voice Channel',value=f'{voiceid}',inline=True)
        embed.set_thumbnail(url=member.display_avatar.url)
        await inter.send(embed=embed,ephemeral=True)
    @moderator.sub_command(name="report",description='Report the administrator')
    async def report(
                    inter: disnake.CommandInteraction, 
                    administrator: disnake.Member,суть_жалобы: str, 
                    доказательства
        ):
        guild = inter.author.guild
        moderator = guild.get_role(modsroleslist[0])
        spmod = guild.get_role(modsroleslist[1])
        stAdmin = guild.get_role(modsroleslist[2])
        if not 'http' in доказательства:
            await inter.send('Не удалось распознать ссылку на доказательства!',ephemeral=True)
        else:
            if not moderator in administrator.roles:
                if not spmod in administrator.roles:
                    if not stAdmin in administrator.roles:
                        await inter.send('Выбранный вами пользователь не является модреатором/администратором')
                    else:
                        embed = disnake.Embed(title="New Report",description="Complaint against the administrator")
                        embed.add_field(name="Отправитель:",value=f"{inter.author.mention}")
                        embed.add_field(name="Администратор:",value=f"{administrator.mention}")
                        embed.add_field(name="Суть жалобы:",value=f'{суть_жалобы}')
                        repcha = bot.get_channel(1031911925690417253)
                        await inter.send('Репорт отправлен.',ephemeral=True)
                        message = await repcha.send(embed=embed)
                        await message.edit(administrator.mention)
                        await message.reply(f'{доказательства}')
                        await message.add_reaction('✅')
                        await message.add_reaction('⌛')
                        await message.add_reaction('❌')
                else:
                    embed = disnake.Embed(title="New Report",description="Complaint against the administrator")
                    embed.add_field(name="Отправитель:",value=f"{inter.author.mention}")
                    embed.add_field(name="Администратор:",value=f"{administrator.mention}")
                    embed.add_field(name="Суть жалобы:",value=f'{суть_жалобы}')
                    repcha = bot.get_channel(1031971157341122560)
                    await inter.send('Репорт отправлен.',ephemeral=True)
                    message = await repcha.send(embed=embed)
                    await message.edit(administrator.mention)
                    await message.reply(f'{доказательства}')
                    await message.add_reaction('✅')
                    await message.add_reaction('⌛')
                    await message.add_reaction('❌')
            else:
                embed = disnake.Embed(title="New Report",description="Complaint against the administrator")
                embed.add_field(name="Отправитель:",value=f"{inter.author.mention}")
                embed.add_field(name="Администратор:",value=f"{administrator.mention}")
                embed.add_field(name="Суть жалобы:",value=f'{суть_жалобы}')
                repcha = bot.get_channel(1031971157341122560)
                await inter.send('Репорт отправлен.',ephemeral=True)
                message = await repcha.send(embed=embed)
                await message.edit(administrator.mention)
                await message.reply(f'{доказательства}')
                await message.add_reaction('✅')
                await message.add_reaction('⌛')
                await message.add_reaction('❌')
#Command for Only One use
    #@bot.slash_command()
    async def rules(inter: disnake.CommandInteraction):
        embed = disnake.Embed(title=f"""Правила сообщества {inter.author.guild.name} 
        На соблюдение нижеописанных правил Вы даете согласие при подключении к Discord - серверу. Незнание данных Правил не освобождает отответственности.""",description=f"Соблюдайте условия использования Discord.")
        embed.add_field(name='Общие правила.', value="""*1.Относитесь ко всем с уважением. На сервере категорически запрещены домогательства, преследования, сексизм, расизм и разжигание ненависти.
        2.Запрещается публиковать непристойные материалы, а также контент с ограничениями по возрасту. Данное правило распространяется на тексты, изображения или ссылки, содержащие или описывающие сцены секса, наготу, сцены насилия или другой шокирующий контент.
        3.Запрещается любое будь то косвенное или прямое упоминание родных.
        4.Запрещается распространение SCAM программ или другого вредоносного ПО.*
        """)
        rulcha = bot.get_channel(inter.author.guild.rules_channel.id)
        await rulcha.send(embed=embed)
        await inter.send("Successfully",ephemeral=True)
    @bot.slash_command(name="ownews",description='news using the command[Own role]')
    @commands.has_any_role(modsroleslist[1],modsroleslist[2])
    async def onews(
        inter: disnake.CommandInteraction,
        txt: str,
        channel: disnake.TextChannel, 
        mention: str = commands.Param(choices=[
            disnake.Localized("Everyone", key="OPTION_EN"),
            disnake.Localized("False", key="OPTION_FS"),])
        ):
        guild = inter.author.guild
        await channel.send(txt)
        if mention == 'Everyone':
            allowed_mentions = disnake.AllowedMentions(everyone = True)
            await inter.send("Successfully",ephemeral=True)
            await channel.send(content = "@everyone", allowed_mentions = allowed_mentions)
        elif mention == 'False':
            await inter.send("Successfully",ephemeral=True)
    @bot.slash_command(description='Эта команда регулируется исключительно кодом[Не использовать]')
    @commands.has_any_role(1031967292793307207)
    async def news(inter: disnake.CommandInteraction, channel: disnake.TextChannel, default: int):
        if default == 1:
            embed = disnake.Embed(title='Новый пост!', description='Бесплатные ресурсы для изучение каких-либо сфер программирования. \n  Для некоторых сурсов в свою очередь нужны знания английского(Но вы можете либо найти уже переведенную версию, или перевести вручную)')
            embed.add_field(name='Аббривиатуры:', value='''
FAQ - Частозадаваемые вопросы
            ''',inline=False)
            embed.add_field(name='Ресурсы:', value='''
FAQ по изучению программирования: https://inlnk.ru/1PDBNO
"Как делать заметки как программист": https://inlnk.ru/DB5RkQ
Изучение C++: https://inlnk.ru/JjMl2B
Изучение Python: https://inlnk.ru/NDMN9P
Ныне живые ресурсы по программированию: https://inlnk.ru/XOMVQ1
Как создать X: https://inlnk.ru/Pm2D58
FAQ Python: https://inlnk.ru/dn6eYn
Все лекции по Computer Since: https://inlnk.ru/JjMl5p
Гайд от OSSU: https://inlnk.ru/Pm2D5L
Сленг: https://inlnk.ru/voDOeP
Курс Learning How To Learn: https://inlnk.ru/YAMvgK
Gnurian гайд по Python: https://inlnk.ru/AKkZ6V
Roadmap по BackEnd Python: https://inlnk.ru/kX6MG6
            ''')
            embed.add_field(name='Задачи и челленджи:',value='''
Задачки: https://www.codewars.com/
Задачи из книг: https://inlnk.ru/ageLGP
Олимпиадные задачи: https://www.eolymp.com/ru/
Челлендж по использованию python: https://www.pythonchallenge.com/
            ''')
            await inter.send("Successfully", ephemeral=True)
            await channel.send(embed=embed)
            await channel.send('Ресурсы были предоставлены: <@853933989081776128> \n Отредактировано: <@788591270712574014> \n Скажем им спасибо и поставим реакцию))')
        elif default == 2:
            await channel.send('''
                                        `CSS Part-1`
**1. Планвый скролл**
Раньше, для оснащения страницы плавной прокруткой, требовалось задействовать несколько строк JS-кода. 
А теперь эта задача может быть решена исключительно средствами CSS. Ну не замечательно ли это? 
Теперь воспользоваться плавной прокруткой можно, прибегнув к CSS-свойству scroll-behavior.
Пример: 
html {
        scroll-behavior: smooth;
}
пример на CodePen - https://inlnk.ru/XOMVK0
**2. Закрепление элементов**
Закрепление элементов — это одна из моих любимых возможностей CSS. 
Речь идёт о том, что соответствующие элементы не исчезают из области просмотра при прокрутке страниц.
Теперь для закрепления элементов на страницах нет нужды прибегать к offsetTo и window.scrollY в JS. 
В наши дни можно просто воспользоваться CSS-свойством position: sticky:
header {
        position: sticky;
        top: 0;
}
проект на CodePen, 
в котором приведён пример использования свойства position: sticky - https://inlnk.ru/LAMaJJ
**3. Обрезка текста**
CSS даёт в наше распоряжение два чудесных свойства: text-overflow и line-clamp.
Они позволяют обрезать тексты, аккуратно обращаясь со словами,
и при этом избавляют нас от необходимости использовать для решения подобных задач JavaScript или какие-то другие сложные методы. 
Оба свойства не новы, но крайне полезны.
Пример на CodePen - https://inlnk.ru/em6wXK```
''')
            await channel.send('''
                                `CSS Part-2`
**4 Пользовательские CSS-свойства: CSS-переменные**
В JavaScript-мире препроцессоры CSS — это очень полезные и популярные технологии. 
Но современным веб-дизайнерам доступны мощные стандартные возможности CSS, известные как пользовательские CSS-свойства или CSS-переменные.
CSS-переменные помогают поддерживать приложения в единообразном состоянии, способствуют реализации принципа DRY. 
Они облегчают разработку и поддержку тем оформления приложений. Подобные возможности - одна из главных причин успеха препроцессоров. 
Подробнее об этом можете почитать здесь - https://inlnk.ru/voDOYj
Использование стандартных возможностей CSS означает, что для создания переменных препроцессоры больше не нужны.
Переменные, как и другие любимые нами стандартные возможности CSS, работают по каскадному принципу.
Для объявления переменной достаточно поставить два тире (--) перед её именем.
После этого, там, где нужно значение переменной, вызывают функцию var(), передавая ей созданную ранее переменную в качестве аргумента. 
:root {
  --base: #ffc600;
  --spacing: 10px;
  --blur: 10px;
}
img {
  padding: var(--spacing);
  background: var(--base);
  -webkit-filter: blur(var(--blur));
  filter: blur(var(--blur));
}
.hl {
  color: var(--base);
}
CSS-переменными можно управлять из JavaScript.
пример на CodePen,показано использование CSS-переменных и управление ими из JS-кода - https://inlnk.ru/84ZNGv

<@&1033740441423712396>
            ''')
        elif default == 3:
            firstembed = disnake.Embed(title='Новый пост! JS Part-1', description='Меня попросили сделать фишечки HTML,CSS,JS\nЛовите))',color=disnake.Color.red())
            firstembed.add_field(name='JS',value='''
**1.Переменные Let и Const**
В JavaScript
Ключевые слова let и const дают более предсказуемые переменные, чем те, что объявлены через var.
У них блочная область видимости: такие переменные существуют только в пределах участка кода, ограниченного фигурными скобками. 
Такой подход позволяет избежать конфликта переменных, делая код более предсказуемым.
let используется для переменных, которые нужно переназначить после создания. Переменные, объявленные с помощью const, невозможно переназначить или изменить.  
В React
let и const — предпочтительные ключевые слова для объявления переменных в React, поскольку их поведение предсказуемо.
Как и в JS, переменные, которые планируется переназначить, объявляют с помощью let, а те, которые не нужно переназначать, — const.          
            ''')
            firstembed.add_field(name='JS',value='''
**2.Шаблонные строки**
В JavaScript
Шаблонные строки намного динамичнее базового типа String в JS, получаемого с помощью одинарных или двойных кавычек. С их помощью гораздо проще интерполировать и вставлять значения в строки.
Достаточно использовать синтаксис ${}, чтобы вставить допустимое в JS выражение. 
Для конкатенации и комбинирования строк не нужен оператор «+», проще писать многострочные объекты типа String, 
поскольку не нужно создавать новые строки с помощью символа новой строки (\n) или возврата каретки (\r).
Кроме того, в шаблонных строках можно использовать вложенные кавычки (одинарные и двойные), не опасаясь ошибок.            
В React
Шаблонные строки используют, чтобы создавать сложные объекты класса String, 
а также динамически вычислять стили элементов в зависимости от условий. 
Можно вставлять значения переменных, операторы, вызовы функций и т. д.
            ''')
            thirdembed = disnake.Embed(title='Новый пост! JS Part-2', description='Меня попросили сделать фишечки HTML,CSS,JS\nЛовите))',color=disnake.Color.green())
            thirdembed.add_field(name='JS',value='''
**3.Стрелочные функции**
В JavaScript
Со стрелочными функциями можно использовать сокращённый синтаксис. Это делает весь код короче. 
Можно заменить ключевое слово return (возврат происходит по умолчанию, если нет фигурных скобок) и тело функции (фигурные скобки) большой стрелкой (=>).
Проще работать с объектами и классами через ключевое слово this. Кроме того, можно удалить скобки вокруг одиночного параметра.
В React
Если в JavaScript можно создать стандартную функцию, можно создать и стрелочную. Как правило, второй вариант предпочтительнее, потому что синтаксис проще.
Чаще всего стрелочные функции используют для создания компонентов, а также для методов массивов высшего порядка, таких как .map() или .filter().
            ''')
            thirdembed.add_field(name='JS',value='''
**4.Методы массивов .map(), .filter(), .reduce(), и т. д.**
В JavaScript 
Так же, как и цикл for, методы массивов map, filter и reduce позволяют перебирать элементы массива:
.map() — позволяет преобразовать каждый элемент массива;
.filter() — создаёт новый массив со всеми элементами, которые прошли проверку, заданную в функции;
.reduce() — позволяет преобразовать весь массив в соответствии с нашими нуждами (даже в другой тип данных).
Указанные методы короче и читаются легче, чем цикл for. Комбинируя эти методы и стрелочные функции, можно ещё больше сократить код.
В React
Методы .map(), .filter(), .reduce() можно использовать для преобразования данных. 
Обычно их применяют для динамического отображения элементов и компонентов с помощью .JSX,
поскольку эти методы можно связывать в цепочки для последовательных трансформаций.
            ''')
            await channel.send(embed=firstembed)
            await channel.send(embed=thirdembed)
            await channel.send('<@&1033740441423712396>,\nСурсы брал с этого сайта,там вы и найдете остальные приколюхи по JS.')
        elif default == 4:
            embed = disnake.Embed(title='Новый пост!',description='Краткое объяснение выученного за последние два занятия')
            embed.add_field(name='Теги',value='''
**<h1>-<h6>...</h1>-</h6>** - простой заголовок, цифра влияет на размер(чем больше цифра в теге, тем меньше текст)
**<a href='ссылка'>...</a>** - тег позволяющий создать гиперссылку(href - сайт на который будет ссылать наш текст)
**<p>...</p>** - простой абзац
**<span>...</span>** - тег позволяющий сделать отступ текста от заголовка
**<div class/id = '...'>...<div>** - Структурный тег, в котором группируются другие теги, проще говоря Контейнер.
**<em>...</em>** - делает текст курсивным
**<br>** - разрыв строки(Enter)
**<img src='' alt=''>** - тег добавляющий изображение в наш html файл, src - где хранится изображение(Может быть как путь к файлу на пк, так и ссылкой на изображение), alt = Альтернативный текст, который будет отображаться в случае, если картинка не загрузится
**<video src='' width='' height=''>...</video>** - тег добавляющий видео в наш html файл, src работает так же, как и в img, widht и height - ширина и высота отображаемого видео
            ''')

            embed.add_field(name='Теория',value='''
**body** - тег хранящий в себе весь контент html документа
**head** - тег хранящий в себе тех.теги по типу(title, расположение css файла и т.п.)
**title** - тег дающей имя самой вкладке в браузере
**<!DOCTYPTE html>** - Элемент <!DOCTYPE> предназначен для указания типа текущего документа(C этого тега стоит начинать все html документы)
            ''')
            await channel.send(embed=embed)
            await channel.send('<@&1033740441423712396>\n Вот вам краткий конспектик, надеюсь все написал\n Накидайте реакций)')
        elif default == 5:
            embed = disnake.Embed(title='Новый пост!',description='Краткий конспект по теме последнего урока')
            embed.add_field(name='Теги',value='''
**<table>...</table>** - создает сам объект таблицы, в который мы будем подгружать информацию следующими тегами.
**<tr>...</tr>** - создает строку(расшифровывается как table row - табличная строка) в таблице.
**<td>...</td>** - создает колонку
**<thead>...</thead>** - работает по принципу head в основном html файле(Верхняя часть)
**<tbody>...</tbody>** - работает по принципу body в основном html файле(Основной контент)
**<tfoot>...</tfoot>** - работает по принципу footer в основном html файле(Нижняя часть, т.е. подвал)
`Возможно я упустил какие-то теги`
            ''')
            embed.add_field(name='Теория', value='''
**HTML-таблицы** упорядочивают и выводят на экран данные с помощью строк или столбцов. Таблицы состоят из ячеек, образующихся при пересечении строк и столбцов. 
Ячейки таблиц могут содержать любые HTML-элементы, такие как заголовки, списки, текст, изображения, элементы форм, а также другие таблицы.
**К таблицам,** так же как и ко всем html тегам можно применять стили, как внешние(CSS), так и внутренние(HTML).
P.S.
**Если хотите более подробно ознакомиться с материалом, можете пересмотреть вебинар, я лишь собрал ту информацию которую нашел и посчитал нужной**
**Так же итоговый файл урока можно посмотреть здесь:** <#1035225365544718366>
            ''')
            embed.set_thumbnail(url=inter.author.display_avatar.url)
            await channel.send(embed=embed)
            await channel.send('<@&1033740441423712396>, вот краткий конспект, если есть ошибки, тегайте в общем чате, исправлю')
    @moderator.sub_command(name="givespecmod",description='giving special modearetor for user[st.Mod]')
    async def givespecmod(inter: disnake.CommandInteraction, member: disnake.Member):
        await inter.send(embed=disnake.Embed(description=":white_check_mark:Successfully"),ephemeral=True)
        guild = bot.get_guild(1013797936716595230)
        role1 = guild.get_role(1013798595583021137)
        role2 = guild.get_role(1013800980145524837)
        role3 = guild.get_role(1013800680282136679)
        commands_log = guild.get_channel(1031971076877598750)

        embed = disnake.Embed(description=f"Administrator {inter.author} give a special moderator {member}")
        await inter.send("Обрабатываю информацию о пользователе",ephemeral=True)
        await commands_log.send(embed=embed)
        date_format = "%a, %b %d, %Y | %I:%M %p" 
        embed = disnake.Embed(description=f"Модератор {inter.author} запросил info о пользователе")
        embed.add_field(name='UID|SID',value=f'`{member.id}`')
        embed.add_field(name='Server name',value=f'`{member.display_name}`')
        embed.add_field(name='Name',value=f'`{member.name}`')
        embed.add_field(name='Top role',value=f'`||`{member.top_role.mention}`||`')
        embed.add_field(name="Date of join",value=f'`{member.joined_at.strftime(date_format)}`',inline=True)
        embed.add_field(name='Date of create',value=f'`{member.created_at.strftime(date_format)}`',inline=True)

        embed.add_field(name='Status',value=f'`{member.status}`',inline=True)
        embed.add_field(name='Activity Status',value=f'`{member.activity}`',inline=True)
        embed.add_field(name='Name and discriminator',value=f'`{member}`',inline=True)
        embed.set_thumbnail(url=member.display_avatar.url)
        await commands_log.send(embed=embed)
        await gi(inter, member)
        await member.add_roles(role1,role2,role3)

    @moderator.sub_command(name="warn",description="Give Warn[moderate]")
    @commands.has_any_role(modsroleslist[0],modsroleslist[1],modsroleslist[2])
    async def mwarn(inter: disnake.CommandInteraction,member: disnake.Member ,reason):
        gui = bot.get_guild(1031958999572164649)   
        warn1 = gui.get_role(1033408718928367727)
        warn2 = gui.get_role(1033408752042397796)
        commands_log = gui.get_channel(1031971076877598750)
        if inter.author == member:
            await inter.send('Вы не можете выдать варн сам себе.',ephemeral=True)
        else:
            if not warn2 in member.roles:
                if not warn1 in member.roles:
                    await member.add_roles(warn1)
                    embed = disnake.Embed(description=f"Модератор выдал первое предупреждение предупреждение пользователю {member}")
                    embed.add_field(name='Причина:',value=f'{reason}')
                    embed.add_field(name='Модератор:',value=inter.author.mention)
                    embed.add_field(name='Наказанный:',value=member)
                    await member.send("Вам было выдано первое предупреждение!")
                    await member.send(embed=embed)
                    await inter.send(embed=embed,ephemeral=True)
                    await commands_log.send(embed=embed)
                    print(member.roles)
                elif warn1 in member.roles:
                    await member.add_roles(warn2)
                    embed = disnake.Embed(description=f"Модератор выдал второе предупреждение предупреждение пользователю {member}")
                    embed.add_field(name='Причина:',value=f'{reason}')
                    embed.add_field(name='Модератор:',value=inter.author.mention)
                    embed.add_field(name='Наказанный:',value=member)
                    await member.send("Вам было выдано второе предупреждение!\n При последующем нарушении вы будете изгнаны из нашего сообщества! \n ||Если считаете, что наказание выдано не верно, используйте /mod report .||")
                    await member.send(embed=embed)
                    await inter.send(embed=embed,ephemeral=True)
                    await commands_log.send(embed=embed)
            elif warn2 in member.roles:
                embed = disnake.Embed(description="Участник был кикнут из-за слишком большого количества предупреждений")
                embed.set_image(url='https://i.gifer.com/1UDY.gif')
                embed.add_field(name='Пользователь', value=member.mention)
                await commands_log.send(embed=embed)
                await inter.send(embed=embed,ephemeral=True)
                await member.kick(reason='warn')
            else:
                await inter.send("Ошибка: Code W1")

    @moderator.sub_command(name='unwarn',description='unwarn user[moderate]')
    @commands.has_any_role(modsroleslist[1],modsroleslist[2])
    async def unwarn(inter: disnake.CommandInteraction, member: disnake.Member, reason: str):
        gui = bot.get_guild(1031880847026036776)   
        warn1 = gui.get_role(1033408718928367727)
        warn2 = gui.get_role(1033408752042397796)
        commands_log = gui.get_channel(1031971076877598750)

        if inter.author.mention == member.mention:
            await inter.send('Вы не можете снять варн сам себе.',ephemeral=True)
        else:
            if not warn2 in member.roles:
                if not warn1 in member.roles:
                    await inter.send(embed=disnake.Embed(description=":white_check_mark:У пользователя нет предупреждений"),ephemeral=True)
                elif warn1 in member.roles:
                    await member.remove_roles(warn1)
                    embed = disnake.Embed(description=f"Модератор амнистировал первое предупреждение предупреждение пользователя {member}")
                    embed.add_field(name='Причина:',value=f'{reason}')
                    embed.add_field(name='Модератор:',value=inter.author.mention)
                    embed.add_field(name='Амнистированый:',value=member)
                    await member.send("Вам было амнистировано первое предупреждение!\n Больше не нарушайте \n")
                    await member.send(embed=embed)
                    await inter.send(embed=embed,ephemeral=True)
                    await commands_log.send(embed=embed)
            elif warn2 in member.roles:
                    await member.remove_roles(warn2)
                    embed = disnake.Embed(description=f"Модератор амнистировал второе предупреждение предупреждение пользователя {member}")
                    embed.add_field(name='Причина:',value=f'{reason}')
                    embed.add_field(name='Модератор:',value=inter.author.mention)
                    embed.add_field(name='Амнистированый:',value=member)
                    await member.send("Вам было амнистировано второе предупреждение!\n Больше не нарушайте \n")
                    await member.send(embed=embed)
                    await inter.send(embed=embed,ephemeral=True)
            else:
                await inter.send("Ошибка: Code W1")

    @bot.slash_command(name='server')
    async def server(inter):
        pass

    @server.sub_command_group(name='get')
    async def serverget(inter):
        pass

    @serverget.sub_command(name='roles')
    async def gar(inter: disnake.CommandInteraction):
        rollist = inter.author.guild.roles
        embed = disnake.Embed(description=f'Полный список ролей {inter.author.guild.name}')
        embed.add_field(name='Роли:', value=f"\n".join([f'{str(r.mention)} |  {str(r.id)}' for r in reversed(rollist)]))
        await inter.send(embed=embed,ephemeral=True)
    @serverget.sub_command(name='members')
    async def gam(inter: disnake.CommandInteraction):
        rollist = inter.author.guild.members
        embed = disnake.Embed(description=f'Полный список пользователей {inter.author.guild.name} || всего {inter.author.guild.member_count} ||')
        embed.add_field(name='Участники:', value=f"\n".join([f'{str(r.mention)} |  {str(r.id)}' for r in reversed(rollist)]))
        await inter.send(embed=embed,ephemeral=True)
    @serverget.sub_command(name='voices')
    async def gv(inter: disnake.CommandInteraction):
        rollist = inter.author.guild.voice_channels
        embed = disnake.Embed(description=f'Полный список голосовых комнат {inter.author.guild.name} || всего {len(rollist)} ||')
        embed.add_field(name='Каналы:', value=f"\n".join([f'{str(r.mention)} | {r.category}'for r in reversed(rollist)]))
        await inter.send(embed=embed,ephemeral=True)
    @serverget.sub_command(name='tchannel')
    async def gtch(inter: disnake.CommandInteraction):
        rollist = inter.author.guild.text_channels
        embed = disnake.Embed(description=f'Полный список текстовых каналов {inter.author.guild.name} || всего {len(rollist)} ||')
        embed.add_field(name='Каналы:', value=f"\n".join([f'{str(r.mention)} | {r.category}'for r in reversed(rollist)]))

        await inter.send(embed=embed,ephemeral=True)

    @serverget.sub_command(name="profile",description='Getting info about you[All]')
    async def gyourselfprofile(inter: disnake.CommandInteraction):
        if inter.author.voice is None:
            voiid = "None"
        else:
            voiid = f"<#{inter.author.voice.channel.id}>"
        statval = inter.author.status.value
        if statval == 'dnd':
            statval = "💓Не беспокоить"
        elif statval == 'online':
            statval = "💚Online"
        elif statval == 'idle':
            statval = "💛Не активен"
        else:
            statval = inter.author.status.value
        date_format = "%a, %b %d, %Y | %I:%M %p" 
        embed = disnake.Embed(description=f"Пользователь {inter.author} запросил info о себе")
        embed.add_field(name='UID|SID',value=f'`{inter.author.id}`')
        embed.add_field(name='Server name',value=f'`{inter.author.display_name}`')
        embed.add_field(name='Name',value=f'`{inter.author.name}`')
        embed.add_field(name='Top role',value=f'`||`{inter.author.top_role.mention}`||`')
        embed.add_field(name="Date of join",value=f'`{inter.author.joined_at.strftime(date_format)}`',inline=True)
        embed.add_field(name='Date of create',value=f'`{inter.author.created_at.strftime(date_format)}`',inline=True)

        embed.add_field(name='Status',value=f'`{statval}`',inline=True)
        embed.add_field(name='Activity Status',value=f'`{inter.author.activity}`',inline=True)
        embed.add_field(name='Name and discriminator',value=f'`{inter.author}`',inline=True)
        embed.add_field(name='Voice Channel',value=f'{voiid}',inline=True)
        embed.set_thumbnail(url=inter.author.display_avatar.url)
        await inter.send(embed=embed)


token = 'your token'
bot.run(token)