import os
import asyncio
import discord
import random
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
import typing
import aiohttp
import requests
import urllib.request
import json
import time
import datetime
import platform
import sys
import logging
from pyfiglet import figlet_format, FontNotFound




logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

ROLE = ('noobie')
TOKEN = ('NzU4OTc0NDM2NTUyMjEyNDgw.X22wBg.Zrgd7Y_605lSc2L14FJm1G8ovYA')
GUILD = ('Cyl Development')
KEY = ('AIzaSyD3dYpq8cxTcHK8t0HeXnESHgcRC74ohns')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)
client = Bot('!')

@bot.event #o que mostra na consola quando o bot inicia
async def on_ready():
    guild = discord.utils.find(lambda g: g.name == GUILD, bot.guilds)
    print("Bot esta Online!\n")
    print("Discord.py API versao:", discord.__version__)
    print("Versao do Python:", platform.python_version())
    print("Iniciado em:", platform.system(), platform.release(), "(" + os.name + ")")
    print("versao do Cyl 3.0, nome de codigo Maxx")
    print("Nome : {}".format(bot.user.name))
    print("ID do cliente : {}".format(bot.user.id))
    print("Ativo em " + str(len(bot.guilds)) + " servidor(es).\n")
    for guild in bot.guilds:
        for member in guild.members:
            print(member)
    activity = discord.Activity(name='Temporada 2020 da terra parte 2', type=discord.ActivityType.watching)
    await bot.change_presence(activity=activity)

@bot.event #o que acontece quando um membro se junta ao servidor 
async def on_member_join(ctx, member):
    await ctx.send(f'{member.name.mention}, bem vindo ao servidor. Escreve !help para mais comandos.')

@bot.command() #mostra citações da serie brooklyn 99
async def brook(ctx: commands.Context):
    """
    Citações de brooklyn99
    """
        
    brooklyn_99_quotes = [
        'Sou a versao humana deste emoji 💯 .',
        'Bingpot!',
        (
            'Fixe. fixe fixe fixe fixe fixe fixe fixe, '
            'Sem duvidas sem duvidas sem duvidas.'
        ),
        'Sargento, com todo o respeito, vou ignorar tudo o que acabou de dizer',
        'Eu comi uma vagem. Sabia a vomito de peixe. Nunca mais.',
        'A linguagem Inglesa nao e capaz de capturar a profundidade dos meus pensamentos, logo vou passar a usar emojis tambem para me exprimir melhor. Winky face.',
        'Um sitio onde toda a gente sabe o teu nome é inferno. Tas a descreber o inferno.',
        'Se eu morrer, transforma os meus tweets num livro.',
        'Ta bem, mas tou a protestar. Vou andar ate la extremamente lentamente!',
        'Jake, porque é que nao fazes a coisa certa e saltas da janela abaixo?',

    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(aliases=["8ball"]) #e so 8ball
async def boladeperguntas(ctx: commands.Context):
    """
    responde a perguntas!
    """
    roll_ball_quotes = [
        'Sim.',
        'Nao.',
        'Talvez.',
        'Nao posso confirmar nem negar',
        'No meu ver, sim.',
        'Pergunta novamente mais tarde.',
        'Melhor nao dizer agora.',
        'Impossivel de prever.',
        'Concentra-te e pergunta novamente.',
        'Nao contes nisso.',
        'E certo.',
        'Certamente que sim.',
        'Probabelmente.',
        'A minha resposta é nao.',
        'As minhas fontes dizem nao.',
        'O resultado nao parece bom.',
        'Resultado bom.',
        'Estou confuso, pergunta outra vez.',
        'Tudo ponta para sim.',
        'Muito duvidosamente.',
        'Sem duvidas.',
        'Sim - definitivamente.',
        'Podess contar com isso.',

    
    ]

    response = random.choice(roll_ball_quotes)
    await ctx.send(response)

@bot.command() #da id do canal
async def get_channel(ctx, *, given_name):
    """
    Tira id do canal. apenas desenvolvedor
    """
    for channel in ctx.guild.channels:
        if channel.name == given_name:
            wanted_channel_id = channel.id

    await ctx.send(wanted_channel_id)


@bot.command()
async def boasvindas(ctx,member: discord.Member):
    """
    Da boas vindas.
    """
    await ctx.send(f'bem vindo a familia, {member.mention}')

@bot.command() #manda no chat a lista do servidores
async def servidores(ctx: commands.Context):
    """
    Da lista de servidores
    """
    _servers = "\n".join(guild.name for guild in bot.guilds)

    await ctx.send(f"Sou parte destes servidores:\n```{_servers}```")

@bot.command(pass_context = True) #ajuda a fazer decisoes
async def moeda(ctx):
    '''Cara ou coroa'''
    flip_options = ['Cara','Coroa']
    flip_response = random.choice(flip_options)
    await ctx.send(flip_response)

@bot.command()
async def abracar(ctx, *, member: discord.Member = None):
    """Abraca outro membro no servidor <3"""
    try:
        if member is None:
            await ctx.send(ctx.message.author.mention + " foi abraçado!")
        else:
            if member.id == ctx.message.author.id:
                await ctx.send(ctx.message.author.mention + " abraçou-se a si mesma!")
            else:
                await ctx.send(member.mention + " foi abraçado por " + ctx.message.author.mention + "!")

    except:
        await print('error')

@bot.command(aliases=["fancy"])
async def embelezar(ctx, *, text):
    """Faz texto bonito!"""
    try:
        def strip_non_ascii(string):
            """manda a string sem ASCII characters."""
            stripped = (c for c in string if 0 < ord(c) < 127)
            return ''.join(stripped)

        text = strip_non_ascii(text)
        if len(text.strip()) < 1:
            return await ctx.send(":x: apenas caracters ASCII, por favor!")
        output = ""
        for letter in text:
            if 65 <= ord(letter) <= 90:
                output += chr(ord(letter) + 119951)
            elif 97 <= ord(letter) <= 122:
                output += chr(ord(letter) + 119919)
            elif letter == " ":
                output += " "
        await ctx.send(output)

    except:
        await print('error')

@bot.command()
async def plataformabot(ctx):
    """Mostra o sistema operativo onde o bot esta ligado."""
    try:
        await ctx.send("O bot esta ligado em: ```" + str(platform.platform()) + "```")
    except:
        await print('error')

@bot.command(aliases=['user'])
async def informacao(ctx, member: discord.Member):
    """Da informacao de um utilizador"""
    try:
        embed = discord.Embed(title="Perfil utilizador: " + member.name, colour=member.colour)
        embed.add_field(name="Nome:", value=member.name)
        embed.add_field(name="ID:", value=member.id)
        embed.add_field(name="Estado:", value=member.status)
        embed.add_field(name="Papel mais alto:", value=member.top_role)
        embed.add_field(name="Juntou-se:", value=member.joined_at)
        created_at = member.created_at.strftime("%b %d, %Y")
        embed.add_field(name="Criou a conta em:", value=created_at)
        embed.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed=embed)
    except:
        await print('error')

@bot.command()
async def insultar(ctx, member: discord.Member = None):
    """Insulta alguem."""
    insults = ["Se o riso é o melhor remedio, a tua cara deve estar a curar o mundo.", "E melhor deixar alguem pensar que es um idiota do que abrires a boca e prova-lo.", "Se eu tivesse uma cara como a tua, eu punha os meus pais em tribunal.", "Es tao feio que quando a tua mae te deixou na escola ela foi multada por deitar lixo fora.", "Se eu quisesse cometer suicidio, trepava ao teu ego e saltava para o teu QI.", "Cerebro nao e tudo, no teu caso ele nao e nada.", "Es sempre assim tao estupido ou hoje é uma ocasiao especial?", "Como e que chegaste aqui? Alguem deixou-te a gaiola aberta?", "Eu queria ver coisas do teu ponto de vista mas nao sou capaz de meter a minha cabeça assim tao dentro do meu proprio cu.", "Tens ido as compras? Eles tem andado a vender vidas, devias ir buscar uma.", "A ultima vez que eu vi algo como tu, eu puchei o autoclismo.", "Se a estupidez fosse medida em tijolos serias a Grande Muralha da China.", "Queres um insulto? Olha-te ao espelho!", "A historia da tua vida e mais insultante que alguma coisa que eu tenha a dizer.",  "E  melhor te esconderes, o homem do lixo ta a chegar.", "Eu tenho um ficheiro de texto maior que o teu cerebro na minha base de dados, ocupa 1KB", "Es velhos suficiente para te lembrares quando emojis eram chamados 'hieroglyfos.'", "Eu nao entro em combate mental com pessoas desarmadas.", "Sera que o teu cu tem inveja da quantidade de merda que sai da tua boca?", "A tua cara parece que pegou fogo e alguem tentou apaga-lo com um garfo.", "Hey, tens uma coisa no teu terceiro queixo.", "Tenho inveja das pessoas que nao te conhecem.", "Tu trazes felicidade a toda a gente, quando sais da sala.", "Se tu vais ter duas caras, pelo menos faz uma delas bonita.", "Algures la fora ha uma arvore, sempre a produzir oxigenio para tu respirares. Acho que lhe deves pedir desculpa.", "Eu nao te odeio, mas se tivesses a pegar fogo e eu tivesse agua, eu bebia-a.", "Se tivesses na televisao eu mudava o canal.", "Tens diarreia da boca e constipação das ideias.", "Se ser feio fosse um crime, terias uma sentença eterna.", "Nao ha vacina para a estupidez. Tenho pena de ti.", "Os teus pais alguma vez te pediram para fujires de casa?", "Alguma similaridade entre ti e um ser humano e apenas coincidencia.", "Continua a falar - tenho a certeza que um dia destes vais dizer alguma coisa inteligente.", "Como e que amas a natureza depois de ela ter feito uma coisa assim tao horrivel?", "Se tivesses estudado mais, eu tenho a certeza que terias qualificaçoes suficientes para seres limpador de sanitas no McDonalds.", "Nao devia dizer nada para te chatear, eu sei que e o teu tempo do mes.", "Nao percebo como puderam dar uma coisa tao feia uma forma fisica."]
    await ctx.send(member.mention + " " + random.choice(insults))  # Menciona o utilizador e diz o insulto

@bot.command(aliases=['ud'])
async def urban(ctx, *msg):
    """Procura definicao no Urban Dictionary."""
    try:
        word = ' '.join(msg)
        api = "http://api.urbandictionary.com/v0/define"
        # Envia um pedido para a API do urban dictionary e guarda informação
        response = requests.get(api, params=[("term", word)]).json()
        embed = discord.Embed(description="Sem resultados!", colour=0xffd1dc)
        if len(response["list"]) == 0:
            return await ctx.send(embed=embed)
        # Adiciona resultado a resposta do commando
        embed = discord.Embed(title="palavra", description=word, colour=embed.colour)
        embed.add_field(name="Definição:", value=response['list'][0]['definition'])
        embed.add_field(name="Exemplos:", value=response['list'][0]['example'])
        await ctx.send(embed=embed)
    except:
        await print('error')

@bot.command(aliases=['say'])
async def diz(ctx, *msg):
    """Faz o bot dizer alguma coisa."""
    try:
        say = ' '.join(msg)
        await ctx.send(say)
    except:
        await print('error')
 
@bot.command()
@commands.has_any_role("Devotee","Priest") #troca com o nome de papel do moderador no teu servidor
async def banir(ctx, member:discord.User=None, reason =None):
    """banir pessoas"""

    if member == None or member == ctx.message.author:
        await ctx.channel.send("Nao te podes banir a ti mesmo!")
        return
    if reason == None:
        reason = "FALTA DE RESPEITO"
    message = f"Foste banido de {ctx.guild.name} por {reason}"
    await member.send(message)
    await ctx.guild.ban(member, reason=reason)
    await ctx.channel.send(f"{member} foi banido!")

@bot.command()
@commands.has_any_role("Devotee","Priest")
async def avisar(ctx, member: discord.Member):
    """Avisar pessoas!"""

    await ctx.send(f"Por favor nao desrespeites as regras ou seras castigado! {member.mention}")

@bot.command()
async def ping(ctx):
    t = await ctx.send('Pong!')
    ms = (t.timestamp-ctx.timestamp).total_seconds() * 1000
    await ctx.send(':ping_pong:Pong! O meu ping é', ms)


bot.run(TOKEN)  