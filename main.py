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
    await message.reply_text("???? G??ncelleniyor ve Yeniden Ba??lat??l??yor...")
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
                command="start",
                description="Botun canl?? olup olmad??????n?? kontrol edin"
            ),
            types.BotCommand(
                command="help",
                description="Yard??m iletisini g??sterir"
            ),
            types.BotCommand(
                command="play",
                description="Youtube/audiofile'dan ??ark?? ??alma"
            ),
            types.BotCommand(
                command="splay",
                description="JioSaavn'dan ??ark?? ??al, bir alb??m ??almak i??in bayrak kullan."
            ),
            types.BotCommand(
                command="cplay",
                description="Bir kanaldan m??zik dosyalar??n?? ??alma."
            ),
            types.BotCommand(
                command="yplay",
                description="Youtube ??alma listesinden m??zik dosyalar??n?? ??alar."
            ),
            types.BotCommand(
                command="player",
                description="Ge??erli ??alma ??ark??s??n?? denetimlerle g??sterir"
            ),
            types.BotCommand(
                command="playlist",
                description="??alma listesini g??sterir"
            ),
            types.BotCommand(
                command="clearplaylist",
                description="Ge??erli ??alma listesini temizler"
            ),
            types.BotCommand(
                command="shuffle",
                description="??alma listesini kar????t??rma"
            ),
            types.BotCommand(
                command="export",
                description="Ge??erli ??alma listesini ileride kullanmak ??zere json dosyas?? olarak d????a aktarma."
            ),
            types.BotCommand(
                command="import",
                description="??nceden verilen ??alma listesini i??eri aktarma."
            ),
            types.BotCommand(
                command="upload",
                description="Ge??erli ??alma ??ark??s??n?? ses dosyas?? olarak kar????ya y??kle."
            ),
            types.BotCommand(
                command="skip",
                description="Ge??erli ??ark??y?? atla"
            ),           
            types.BotCommand(
                command="join",
                description="VC'ye Kat??l"
            ),
            types.BotCommand(
                command="leave",
                description="VC'den ayr??l"
            ),
            types.BotCommand(
                command="vc",
                description="VC birle??tirilirse Ckeck"
            ),
            types.BotCommand(
                command="stop",
                description="??almay?? Durdurur"
            ),
            types.BotCommand(
                command="radio",
                description="Alem Fm Canl?? Radio"
            ),
            types.BotCommand(
                command="stopradio",
                description="Radyo/Canl?? yay??n?? durdurur"
            ),
            types.BotCommand(
                command="replay",
                description="Ba??tan tekrarla"
            ),
            types.BotCommand(
                command="clean",
                description="RAW dosyalar??n?? temizler"
            ),
            types.BotCommand(
                command="pause",
                description="??ark??y?? duraklatma"
            ),
            types.BotCommand(
                command="resume",
                description="Duraklat??lan ??ark??ya devam etme"
            ),
            types.BotCommand(
                command="mute",
                description="VC'de Sessize Alma"
            ),
            types.BotCommand(
                command="volume",
                description="Bass Ses ayarlama 0-200"
            ),
            types.BotCommand(
                command="unmute",
                description="VC'de sesi a??"
            ),
            types.BotCommand(
                command="restart",
                description="Botu g??ncelle??tirme ve yeniden ba??latma"
            )
        ]
    )
)

idle()
bot.stop()
