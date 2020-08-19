import gifs
import config
import discord
import random
import logging
import discord.ext
from discord.ext import commands
from outsources import functions

logger = logging.getLogger('discord')


logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


bot = commands.Bot(command_prefix=["p!", "?"])  # sets the bot prefix
bot.remove_command('help')  # removes the default discord.py help command


@bot.event  # sets the bot status and prints when it has started in console with stats, stats include: The amount of users that are in the total amount of guilds and the discord.py version
async def on_ready():
    activity = discord.Game(name="in TPK | p!help", type=1)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print('ProtoPaw has started successfully')
    print('-----------')
    print('guilds:')
    print(len(bot.guilds))
    print('-----------')
    print('users:')
    print(len(bot.users))
    print('-----------')
    print('version:')
    print(discord.__version__)
    print('-----------')


@bot.command(name="ping", aliases=["pong", "latency"], brief="shows the bot's latency.")  # the ping command, simply shows the latency in an embed
async def latency(ctx):
    embed = discord.Embed(title="ProtoPaw latency", color=config.color)
    embed.add_field(name="ping", value=f'**{bot.latency:.2f}**s')
    await ctx.send(embed=embed)


@bot.command()  # the help command, displays all the commands and the developers in an embed
async def help(ctx):
    embed = discord.Embed(title='commands | `?`, `p!`', color=config.color)
    embed.add_field(name="**🔨 moderation**", value="`ban` `unban` `kick` `softban`", inline=True)
    embed.add_field(name="**🤖 bot related**", value="`help` `ping` `invite` `stats` `links` `info`", inline=True)
    embed.add_field(name="**🏗️ Utils**", value="`get_id` `avatar` `serverinfo` `random` `poll` `decide`", inline=True)
    embed.add_field(name="**🤝 Social**", value="`hug` `snuggle` `boop`\n `kiss` `pat` `honk`\n `cuddle` `askproto` `lick` `blush` `feed`\n`glomp` `happy`\n`highfive` `wag`", inline=True)
    embed.add_field(name="**❔ Others**", value="`say` `say2`", inline=True)
    embed.add_field(name="**Developers**", value="`BluewyFurGame#5108`\n`ChosenFate#5108`", inline=True)
    embed.set_thumbnail(url="https://www.dropbox.com/s/yx7z6iefnx0q576/Icon.jpg?dl=1")
    embed.set_footer(text="Thank you, " + ctx.message.author.name + ", for using ProtoPaw!")
    await ctx.send(embed=embed)


@bot.command(name="invite", aliases=["inv", "oauth"], brief="Shows the bot ouath link")  # shows the bot invite with hyperlink in an embed
async def invite(ctx):
    embed = discord.Embed(title="ProtoPaw invite link", color=config.color)
    embed.add_field(name="Invite ProtoPaw here", value="[Add ProtoPaw to your server](https://discord.com/api/oauth2/authorize?client_id=620990340630970425&permissions=806218999&scope=bot)")
    await ctx.send(embed=embed)


@bot.command(name="stats", aliases=["statistics"], brief="shows bot statistics.")  # shows the bot statistics (total amount of users in total amount of guilds) in an embed
async def statistics(ctx):
    embed = discord.Embed(title="Statistics ProtoPaw:", description="Global Bot Statistics", color=config.color)
    embed.add_field(name="Total Guilds", value=len(bot.guilds), inline=False)
    embed.add_field(name="Total users", value=len(bot.users), inline=False)
    await ctx.send(embed=embed)


@bot.command()  # retrieves the ID of a member. Argument can be an ID, just the user's name or the user mention
async def get_id(ctx, member: discord.Member):
    user_id = member.id
    await ctx.send('The user ID is %d.' % user_id)


@bot.command(aliases=['av'])  # shows the mentioned user's avatar in an embed
async def avatar(ctx, *, user: discord.Member = None):
    if user is None:
        user = ctx.author
    else:
        user = user
        eA = discord.Embed(title='Avatar', color=config.color)
        eA.set_author(name=user, icon_url=user.avatar_url)
        eA.set_image(url=user.avatar_url)
        await ctx.send(embed=eA)


@bot.command(name='links', brief='Discord related links')  # shows the links related to ProtoPaw in an embed
async def links(ctx):
    embed = discord.Embed(title='Protopaw Links', color=config.color)
    embed.add_field(name='Support/community discord Server:', value="https://discord.gg/k64tAer\nhttps://discord.gg/bcjdqyn\nhttps://discord.me/thepawkingdom\nhttps://discord.st/thepawkingdom", inline=True)
    embed.add_field(name="Contact", value="ChosenFate#5108\nBluewytheRenegade#2923")
    embed.add_field(name="Social media:", value="Twitter | https://twitter.com/furrycontentuvs", inline=False)
    embed.set_thumbnail(url="https://www.dropbox.com/s/yx7z6iefnx0q576/Icon.jpg?dl=1")
    embed.set_footer(text="Thank you, " + ctx.message.author.name + ", for using ProtoPaw!")
    await ctx.send(embed=embed)


@bot.command(name="serverinfo", aliases=["servinfo", "sinfo"])  # shows info about the server the command was executed, in an embed. Still being worked on.
async def serverinfo(ctx):
    embed = discord.Embed(title="Server information", color=config.color)
    embed.add_field(name="Info:", value="Membercount:\nRegion:\n", inline=True)
    embed.add_field(name="Value", value=str(len(ctx.guild.members)) + "\n" + str(ctx.guild.region) + "\n", inline=True)
    embed.set_author(name=ctx.guild.name + " Statistics", url="https://cdn.discordapp.com/icons/" + str(ctx.guild.id) + "/" + str(ctx.guild.icon) + ".webp?size=1024", icon_url="https://cdn.discordapp.com/icons/" + str(ctx.guild.id) + "/" + str(ctx.guild.icon) + ".webp?size=1024")
    await ctx.send(embed=embed)


@bot.command(name='variable', brief='test variables')  # to test things. Currently a way to bully people who arent a fan of furries.
async def variables(ctx):
    embed = discord.Embed(title='variable tests', color=config.color)
    embed.add_field(name='test:', value="Teh fitnyessgwam pacew test is a muwtistage aewobic capacity test that pwogwessivewy gets mowe difficuwt as it continyues. Teh 20 metew pacew test wiww begin owo in 30 seconds. Wine up at teh stawt. Teh wunnying speed stawts swowwy~ but gets fastew each minyute aftew chu heaw dis signyaw. A singwe wap shouwd be compweted each time chu heaw dis sound. Uwu wemembew uwu to wun owo in a gay winye~ and wun as wong as possibwe. Teh second time chu faiw uwu to compwete a wap befowe teh sound~ ur test is ovew. Teh test wiww begin on teh wowd stawt. On ur mawk~ get weady~ stawt.", inline=False)
    embed.set_thumbnail(url="https://www.dropbox.com/s/yx7z6iefnx0q576/Icon.jpg?dl=1")
    embed.set_author(name="The Paw Kingdom Links", url="https://www.dropbox.com/s/yx7z6iefnx0q576/Icon.jpg?dl=1", icon_url="https://www.dropbox.com/s/yx7z6iefnx0q576/Icon.jpg?dl=1")
    await ctx.send(embed=embed)


@bot.command(name='snuggle', brief='Snuggling, how sweet')  # interaction command - snuggle someone. gifs are random!
async def snuggle(ctx, members: commands.Greedy[discord.Member], *, reason="being adorable"):
    await functions.interactions(ctx, members, reason, "snuggle", "how cute", "snuggled")


@bot.command(name='hug', brief='Fandom hug!')  # interaction command - hug someone. gifs are random!
async def hug(ctx, members: commands.Greedy[discord.Member], *, reason="being adorable"):
    await functions.interactions(ctx, members, reason, "hug", "how lovely", "hugged")


@bot.command(name='pat', brief='Pats, wholesome!')  # interaction command - pat someone. gifs are random!
async def pat(ctx, members: commands.Greedy[discord.Member], *, reason="being adorable"):
    await functions.interactions(ctx, members, reason, "pat", "how beautiful", "pat")


@bot.command(name='boop', aliases=['bp'], brief='Boop!')  # interaction command - boop someone. gifs are random!
async def boop(ctx, members: commands.Greedy[discord.Member], *, reason="being adorable"):
    await functions.interactions(ctx, members, reason, "boop", "so soft", "booped")


@bot.command(name='kiss', aliases=['smooch'], brief='Smooch!')  # interaction command - kiss someone. gifs are random!
async def kiss(ctx, members: commands.Greedy[discord.Member], *, reason="being adorable"):
    await functions.interactions(ctx, members, reason, "smooch", "lovely", "smooched")


@bot.command(name="lick", brief='Licking, lol')  # interaction command - lick someone. gifs are random!
async def lick(ctx, members: commands.Greedy[discord.Member], *, reason="being adorable"):
    await functions.interactions(ctx, members, reason, "lick", "tasty", "licked")


@bot.command(name="bellyrub")  # interaction command - bellyrub someone. gifs are random!
async def bellyrub(ctx, members: commands.Greedy[discord.Member], *, reason="being adorable"):
    await functions.interactions(ctx, members, reason, "bellyrub", "lovely", "bellyrubbed")


@bot.command(name="cuddle")  # interaction command - cuddle someone. gifs are random!
async def cuddle(ctx, members: commands.Greedy[discord.Member], *, reason="being adorable"):
    await functions.interactions(ctx, members, reason, "cuddle", "heartwarming", "cuddled")


@bot.command(name="rawr")  # interaction command - rawr at someone. gifs are random!
async def rawr(ctx, members: commands.Greedy[discord.Member], *, reason="Rawr!"):
    GIFlist = gifs.rawr
    GIF = random.choice(GIFlist)
    if not (members):
        embed = discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**rawred, cute!**\nFor: " + reason))
        embed.set_image(url=GIF)
        await ctx.send(embed=embed)
        return
    embed = discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**rawred at**" + " " + '**,** '.join(x.mention for x in members) + "**, cute!**\nFor: " + reason))
    embed.set_image(url=GIF)
    await ctx.send(embed=embed)


@bot.command(name="awoo")  # interaction command - awoo at someone. gifs are random!
async def awoo(ctx, members: commands.Greedy[discord.Member], *, reason="Awoo!"):
    GIFlist = gifs.awoo
    GIF = random.choice(GIFlist)
    if not (members):
        embed = discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**awoo'd, chilling!**\nFor: " + reason))
        embed.set_image(url=GIF)
        await ctx.send(embed=embed)
        return
    embed = discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**awoo'd at**" + " " + '**,** '.join(x.mention for x in members) + "**, chilling!**\nFor: " + reason))
    embed.set_image(url=GIF)
    await ctx.send(embed=embed)


@bot.command(name="blush")  # interaction command - blush (because of) someone. gifs are random!
async def blush(ctx, members: commands.Greedy[discord.Member], *, reason="Makes them kyooter!"):
    GIFlist = gifs.blush
    GIF = random.choice(GIFlist)
    if not (members):
        embed = discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**blushed**\nFor: " + reason))
        embed.set_image(url=GIF)
        await ctx.send(embed=embed)
        return
    embed = discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**blushed because of**" + " " + '**,** '.join(x.mention for x in members) + "**, kyoot!**\nFor: " + reason))
    embed.set_image(url=GIF)
    await ctx.send(embed=embed)


@bot.command(name="feed")  # interaction command - feed someone. gifs are random!
async def feed(ctx, members: commands.Greedy[discord.Member], *, reason="Hungwy boy"):
    GIFlist = gifs.feed
    GIF = random.choice(GIFlist)
    embed = discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**feeds**" + " " + '**,** '.join(x.mention for x in members) + "**, chilling!**\nFor: " + reason))
    embed.set_image(url=GIF)
    await ctx.send(embed=embed)


@bot.command(name="glomp")  # interaction command - glomp someone. gifs are random!
async def glomp(ctx, members: commands.Greedy[discord.Member], *, reason="Love!"):
    GIFlist = gifs.glomp
    GIF = random.choice(GIFlist)
    embed = discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**glomped on**" + " " + '**,** '.join(x.mention for x in members) + "**, chilling!**\nFor: " + reason))
    embed.set_image(url=GIF)
    await ctx.send(embed=embed)


@bot.command(name="happy")  # interaction command - be happy (because of someone). gifs are random!
async def happy(ctx, members: commands.Greedy[discord.Member], *, reason="Vibing"):
    GIFlist = gifs.happy
    GIF = random.choice(GIFlist)
    if not (members):
        embed = discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**Is happy**\nFor: " + reason))
        embed.set_image(url=GIF)
        await ctx.send(embed=embed)
        return
    embed = discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**Is happy because of**" + " " + '**,** '.join(x.mention for x in members) + "**, kyoot!**\nFor: " + reason))
    embed.set_image(url=GIF)
    await ctx.send(embed=embed)


@bot.command(name="highfive")  # interaction command - highfive someone. Gifs are random
async def highfive(ctx, members: commands.Greedy[discord.Member], *, reason="being adorable"):
    await functions.interactions(ctx, members, reason, "highfive", "awesome!", "high fived")


@bot.command(name="wag")  # interaction command - wag (because of someone). gifs are random!
async def wag(ctx, members: commands.Greedy[discord.Member], *, reason="Rawr!"):
    GIFlist = gifs.wag
    GIF = random.choice(GIFlist)
    if not (members):
        embed = discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**wags their tail, kyoot!**\nFor: " + reason))
        embed.set_image(url=GIF)
        await ctx.send(embed=embed)
        return
    embed = discord.Embed(title="", color=config.color, description=(ctx.message.author.mention + " " + "**wags their tail because of**" + " " + '**,** '.join(x.mention for x in members) + "**, cute!**\nFor: " + reason))
    embed.set_image(url=GIF)
    await ctx.send(embed=embed)


@bot.command(name='random', brief='Randomness!')  # Let protoPaw choose for you!
async def randomchoice(ctx, arg1, arg2):
    Arglist = [arg1, arg2]
    await ctx.send(random.choice(Arglist))


@bot.command(name="info")  # Gives information about the mentioned command
async def info(ctx, arg):
    embed = discord.Embed(title='Help menu - Prefixes `p!` | `?`', color=config.color)
    embed.add_field(name=arg, value=getattr(cmds, arg), inline=True)
    embed.add_field(name="Syntax of " + arg, value=getattr(syntax, arg), inline=True)
    embed.add_field(name="Developers:", value="`-` ChosenFate#5108\n`-` BluewyFurGame#5108", inline=False)
    embed.set_thumbnail(url="https://www.dropbox.com/s/yx7z6iefnx0q576/Icon.jpg?dl=1")
    embed.set_footer(text="Thank you, " + ctx.message.author.name + ", for using ProtoPaw!")
    await ctx.send(embed=embed)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please fill in all the required arguments.')  # Shows the command isn't completed
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have the sufficient permissions.")  # Shows that you dont have the needed permission for this command


@bot.command(name="askprotopaw", aliases=["askpp", "askproto"])  # Lets you ask something to ProtoPaw, he will answer with a random answer listed in gifs.py
async def askprotopaw(ctx, *, arg):
    answers = gifs.AskProtopaw
    answer = random.choice(answers)
    embed = discord.Embed(title=f"{arg} - Proto says {answer}", color=config.color)
    await ctx.send(embed=embed)


@bot.command(name="ban")  # Permanently bans the user that was mentioned (user must be in guild)
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    if member == ctx.message.author:
        await ctx.send("You can't ban yourself, derp!")
        return
    if reason is None:
        await ctx.send(f"Make sure you provide a reason with this command {ctx.author.mention}.")
        return
    else:
        messageok = f"You have been banned from **{ctx.guild.name}** | Reason: `{reason}`"
        await member.send(messageok)
        await member.ban(reason=f"{ctx.message.author}: {reason}")
        embed = discord.Embed(title=f"{member} has been casted from {ctx.guild.name}!", color=config.color)
        embed.set_image(url="https://media1.tenor.com/images/b90428d4fbe48cc19ef950bd85726bba/tenor.gif?itemid=17178338")
        embed.set_footer(text=f"Reason: {reason}\nModerator: {ctx.message.author}")
        await ctx.send(embed=embed)


@bot.command(name='unban')  # Unbans user with a given ID
@commands.has_permissions(ban_members=True)
async def _unban(ctx, id: int):
    user = await bot.fetch_user(id)
    await ctx.guild.unban(user)
    clearname = str(user).split("#")
    embed = discord.Embed(title=f"Unbanned {clearname[0]}", color=config.color)
    embed.set_footer(text=user)
    await ctx.send(embed=embed)


@bot.command(name="kick")  # Kicks the mentioned user from the guild
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    if member == ctx.message.author:
        await ctx.send("You can't kick yourself, derp!")
        return
    if reason is None:
        await ctx.send(f"Make sure you provide a reason with this command {ctx.author.mention}.")
        return
    else:
        messageok = f"You have been kicked from **{ctx.guild.name}** | Reason: `{reason}`"
        await member.send(messageok)
        await member.kick(reason=f"{ctx.message.author}: {reason}")
        embed = discord.Embed(title=f"{member} has been kicked from {ctx.guild.name}!", color=config.color)
        embed.set_image(url="https://media1.tenor.com/images/b90428d4fbe48cc19ef950bd85726bba/tenor.gif?itemid=17178338")
        embed.set_footer(text=f"Reason: {reason}\nModerator: {ctx.message.author}")
        await ctx.send(embed=embed)


@bot.command(name="softban")  # bans and immediately unbans the user mentioned
@commands.has_permissions(ban_members=True)
async def softban(ctx, member: discord.Member, *, reason=None):
    if member == ctx.message.author:
        await ctx.send("You can't softban yourself, derp!")
        return
    if reason is None:
        await ctx.send(f"Make sure you provide a reason with this command {ctx.author.mention}.")
        return
    else:
        messageok = f"You have been softbanned from **{ctx.guild.name}** | Reason: `{reason}`"
        await member.send(messageok)
        await member.ban(reason=f"{ctx.message.author}: {reason}")
        await member.unban()
        embed = discord.Embed(title=f"{member} has been softcasted from {ctx.guild.name}!", color=config.color)
        embed.set_image(url="https://media1.tenor.com/images/b90428d4fbe48cc19ef950bd85726bba/tenor.gif?itemid=17178338")
        embed.set_footer(text=f"Reason: {reason}\nModerator: {ctx.message.author}")
        await ctx.send(embed=embed)


@bot.command(name="poll")  # Makes a poll with up to 10 options, seperate choices with ,
async def poll(ctx, *, arg):
    await ctx.message.delete()
    choice = str(arg).split(",")
    n = 1
    reactionlist = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣", "7️⃣", "8️⃣", "9️⃣", "🔟"]
    embed = discord.Embed(title="Poll", color=config.color)
    for x in choice:
        embed.add_field(name="Option " + reactionlist[n-1], value=f"{x}", inline=False)
        n = n+1
    embed.set_footer(text=f"Poll cast by {ctx.message.author}")
    botmsg = await ctx.send(embed=embed)
    en = 1
    for emoji in reactionlist:
        await botmsg.add_reaction(emoji)
        en = en+1
        if en >= n:
            break


@bot.command(name="decide")  # Let people vote for something
async def decide(ctx, *, arg):
    await ctx.message.delete()
    embed = discord.Embed(title=arg, color=config.color)
    embed.set_footer(text=f"Asked by {ctx.message.author}")
    botmsg = await ctx.send(embed=embed)
    await botmsg.add_reaction("✅")
    await botmsg.add_reaction("❌")


@bot.command(name="revive")  # Tags the role that was given with a message.
@commands.has_permissions(manage_messages=True)
async def revive(ctx):
    await ctx.message.delete()
    await ctx.send("<@&738356235841175594>! The chat is dead, we need you now!")


@bot.command()  # In an embed repeats what you said and deletes the original command
async def say(ctx, *, sentence):
    await ctx.message.delete()
    embed = discord.Embed(title=sentence, color=config.color)
    embed.set_footer(text=f"Executed by {ctx.message.author}")
    await ctx.send(embed=embed)


@bot.command()  # Repeats what you said and deletes the original command
async def say2(ctx, *, sentence2):
    await ctx.message.delete()
    await ctx.send(f"{ctx.author.mention} said:\n{sentence2}")
 
   
@bot.command()
async def purge(ctx, amount=0):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'Successfully deleted **{amount}** messages with the purge command.')


class cmds:
    hug = "Hugs the pinged person, kyoot!"
    snuggle = "Snuggles the pinged persons, kyoot!"
    boop = "Boops the pinged persons, boop!"
    kiss = "Smooches the pinged persons :*"
    pat = "Pats the pinged persons, good boy!"
    ping = "Displays the latency of the bo -connection lost"
    invite = "Displays the invite link to invite TPKP to your server"
    stats = "Shows some neat stats about TPKP"
    get_id = "Gets a users Discord ID"
    av = "Gets and posts avatar of the pinged person / ID works too"
    links = "Displays some links to get to The Paw Kingdom, this bots home!"
    random = "Can't make a choice? Use the random command! Only 2 options possible at this point"
    info = "You already know what this does, derp"
    honk = "HONK"
    askprotopaw = "Ask ProtoPaw, and he shall give you an answer"
    unban = "Unbans the given user"
    lick = "Licks the pinged persons, yum!"
    ban = "Bans the mentioned person"
    kick = "Kicks the specified person"
    softban = "Softbans (bans and unbans) the specified"
    poll = "Cast a poll if you can't agree about something!"
    decide = "Casts a simple yes / no poll"
    cuddle = "Cuddle the pinged persons"


class syntax:
    hug = "`?hug @user1 @user2...`"
    snuggle = "`?snuggle @user1 @user2...`"
    boop = "`?boop @user1 @user2...`"
    kiss = "`?kiss  @user1 @user2...`"
    pat = "`?pat  @user1 @user2...!`"
    invite = "`?invite`"
    get_id = "`?get_id @user`"
    links = "`links`"
    info = "`?info`"
    honk = "`?honk`"
    askproto = "`?askreggie <Question>`"
    lick = "`?lick @user1 @user2..."
    ban = "`?ban @user | ID Reason`"
    kick = "`?kick @user | ID reason`"
    softban = "`?softban @user | ID reason"
    poll = "`?poll choice1, choice2, choice3 [...]`"
    decide = "`?decide <question>"
    cuddle = "?cuddle @user1 @user2...`"


bot.run(config.token)
