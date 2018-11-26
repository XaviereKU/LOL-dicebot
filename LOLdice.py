import asyncio
import discord
import random

client = discord.Client()

token = "NDYxODc3NzgyMTUwOTA1ODY2.DhZtIA.ZJSnDpUiGWcz32sBo3T8IxqJdIo"

@client.event
async def on_ready():
	print("Logged in as ")
	print(client.user.name)
	# print(client.user.id)
	print("===========")
	await client.change_presence(game=discord.Game(name="A Bot", type=1))

@client.event

@client.event
async def on_message(message):
	if message.author.bot:
		return None
	
	channel = message.channel

	if message.content == '/주사위' or message.content == '/ㅈㅅㅇ' or message.content == '/wtd':
		dicenum = random.randrange(1,100)
		await client.send_message(channel, '주사위 숫자 : {}'.format(dicenum))

	if message.content == '/rd' or message.content == '/rw' or message.content == '/구인'  or message.content == '/구직' or message.content == '/ㄱㅇ'  or message.content == '/ㄱㅈ':
		member = message.author
		voice = message.author.voice.voice_channel

		if voice == None:
			fmt = '@everyone {0.display_name} 구직합니다!'
			await client.send_message(channel, fmt.format(member))
		else:
			members = voice.voice_members
			if message.server.id == '381380340939227136':
				if voice.name.startswith('내전'):
					cnt = max(10-len(members),0)
					if cnt > 0:						
						fmt = '@here {0.name}에서 ' + cnt.__str__()+ ' 명 구인합니다!'			
					else:
						fmt = '{0.name} 풀방입니다!'
				else:
					cnt = max(5 - len(members), 0)            
					if cnt > 0:
						fmt = '@here {0.name}에서 ' + cnt.__str__() + ' 명 구인합니다!'
					else:
						fmt = '{0.name}풀방입니다!'
			else:
				cnt = max(4 - len(members), 0)            
				if cnt > 0:
					fmt = '@here {0.name}에서 ' + cnt.__str__() + ' 명 구인합니다!'
				else:
					fmt = '{0.name} 풀방입니다!'
			await client.send_message(channel, fmt.format(voice))
        
client.run(token)