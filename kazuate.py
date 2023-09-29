import discord
import random

TOKEN = 'ここにbotのトークンを入れる'
DISCORD_SERVER_IDS = ここにサーバーのidを入れる

client = discord.Bot(intents=discord.Intents.all())

@client.slash_command(name="kazuate", description="数当てゲーム", guild_ids=[DISCORD_SERVER_IDS])
async def on_message(message: discord.Message):
    ans = random.randint(1,100)
    max_count = 5
    kazulist = list(range(1, 101))
    await message.respond(f"1~100の数字の中から一つ選んだよ。\nその数字を{max_count}回以内に当ててね。")

    def kazuatecheck(m):
        return (m.author == message.author) and (m.content in [str(n) for n in kazulist])

    for i in range(1,max_count+1):
        await message.channel.send(f"{i}回目、いくつかな？")
        reply = await client.wait_for("message", check=kazuatecheck)
        if int(reply.content) == ans:
            await message.channel.send("当たり！")
            break
        elif i == max_count:
            pass
        elif int(reply.content) > ans:
            await message.channel.send("もっと下だよ")
        else:
            await message.channel.send("もっと上だよ")
    else:
        await message.channel.send(f"残念～正解は{ans}でした")

  client.run(TOKEN)
