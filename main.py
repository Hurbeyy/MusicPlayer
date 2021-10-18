#MIT License

#Copyright (c) 2021 SUBIN

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.
try:
    import asyncio
    from pyrogram import Client, idle, filters
    import os
    from config import Config
    from utils import mp, USERNAME, FFMPEG_PROCESSES
    from pyrogram.raw import functions, types
    import os
    import sys
    from time import sleep
    from threading import Thread
    from signal import SIGINT
    import subprocess
    
except ModuleNotFoundError:
    import os
    import sys
    import subprocess
    file=os.path.abspath("requirements.txt")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', file, '--upgrade'])
    os.execl(sys.executable, sys.executable, *sys.argv)


CHAT=Config.CHAT
bot = Client(
    "Musicplayer",
    Config.API_ID,
    Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins=dict(root="plugins")
)
if not os.path.isdir("./downloads"):
    os.makedirs("./downloads")
async def main():
    async with bot:
        await mp.start_radio()
def stop_and_restart():
    bot.stop()
    os.system("git pull")
    sleep(10)
    os.execl(sys.executable, sys.executable, *sys.argv)


bot.run(main())
bot.start()

@bot.on_message(filters.command(["restart", f"restart@{USERNAME}"]) & filters.user(Config.ADMINS) & (filters.chat(CHAT) | filters.private))
async def restart(client, message):
    await message.reply_text("🔄 Güncelleniyor ve Yeniden Başlatılıyor...")
    await asyncio.sleep(3)
    try:
        await message.delete()
    except:
        pass
    process = FFMPEG_PROCESSES.get(CHAT)
    if process:
        try:
            process.send_signal(SIGINT)
        except subprocess.TimeoutExpired:
            process.kill()
        except Exception as e:
            print(e)
            pass
        FFMPEG_PROCESSES[CHAT] = ""
    Thread(
        target=stop_and_restart
        ).start()    


bot.send(
    functions.bots.SetBotCommands(
        commands=[
            types.BotCommand(
                command="başlat",
                description="Botun canlı olup olmadığını kontrol edin"
            ),
            types.BotCommand(
                command="yardım",
                description="Yardım iletisini gösterir"
            ),
            types.BotCommand(
                command="oynat",
                description="Youtube/audiofile'dan şarkı çalma"
            ),
            types.BotCommand(
                command="soynat",
                description="JioSaavn'dan şarkı çal, bir albüm çalmak için bayrak kullan."
            ),
            types.BotCommand(
                command="coynat",
                description="Bir kanaldan müzik dosyalarını çalma."
            ),
            types.BotCommand(
                command="yoynat",
                description="Youtube çalma listesinden müzik dosyalarını çalar."
            ),
            types.BotCommand(
                command="çalanşarkı",
                description="Geçerli çalma şarkısını denetimlerle gösterir"
            ),
            types.BotCommand(
                command="oynatmalistesi",
                description="Çalma listesini gösterir"
            ),
            types.BotCommand(
                command="listeyitemizle",
                description="Geçerli çalma listesini temizler"
            ),
            types.BotCommand(
                command="karıştır",
                description="Çalma listesini karıştırma"
            ),
            types.BotCommand(
                command="ihracat",
                description="Geçerli çalma listesini ileride kullanmak üzere json dosyası olarak dışa aktarma."
            ),
            types.BotCommand(
                command="ithalat",
                description="Önceden verilen çalma listesini içeri aktarma."
            ),
            types.BotCommand(
                command="upload",
                description="Geçerli çalma şarkısını ses dosyası olarak karşıya yükle."
            ),
            types.BotCommand(
                command="atla",
                description="Geçerli şarkıyı atla"
            ),           
            types.BotCommand(
                command="katıl",
                description="VC'ye Katıl"
            ),
            types.BotCommand(
                command="ayrıl",
                description="VC'den ayrıl"
            ),
            types.BotCommand(
                command="vc",
                description="VC birleştirilirse Ckeck"
            ),
            types.BotCommand(
                command="dur",
                description="Çalmayı Durdurur"
            ),
            types.BotCommand(
                command="radyo",
                description="Alem Fm Canlı Radio"
            ),
            types.BotCommand(
                command="radyodur",
                description="Radyo/Canlı yayını durdurur"
            ),
            types.BotCommand(
                command="tekraroynat",
                description="Baştan tekrarla"
            ),
            types.BotCommand(
                command="temizlik",
                description="RAW dosyalarını temizler"
            ),
            types.BotCommand(
                command="duraklat",
                description="Şarkıyı duraklatma"
            ),
            types.BotCommand(
                command="devamet",
                description="Duraklatılan şarkıya devam etme"
            ),
            types.BotCommand(
                command="sessizlik",
                description="VC'de Sessize Alma"
            ),
            types.BotCommand(
                command="ses",
                description="Bass Ses ayarlama 0-200"
            ),
            types.BotCommand(
                command="sesiaç",
                description="VC'de sesi aç"
            ),
            types.BotCommand(
                command="tekrarbaşlat",
                description="Botu güncelleştirme ve yeniden başlatma"
            )
        ]
    )
)

idle()
bot.stop()
