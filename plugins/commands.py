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
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
from utils import USERNAME, mp
from config import Config
U=USERNAME
CHAT=Config.CHAT
msg=Config.msg
HOME_TEXT = "<b>Helo, [{}](tg://user?id={})\n\nIam MusicPlayer 2.0 which plays music in Channels and Groups 24*7.\n\nI can even Stream Youtube Live in Your Voicechat.\n\nDeploy Your Own bot from source code below.\n\nHit /help to know about available commands.</b>"
HELP = """

<b>
Bir ses dosyasına veya youtube bağlantısına yanıt olarak /play <şarkı adı> kullanın veya /play'i kullanın.

Bir youtube çalma listesindeki tüm şarkıları çalmak için /yplay'i kullanın.

Jio Saavn'dan bir şarkı çalmak için <code>/splay şarkı adı</code>'nı veya bir jiosaavn albümündeki veya /cplay <kanalındaki tüm şarkıları çalmak için <code>/splay -a albüm adı</code>'nı da kullanabilirsiniz. kullanıcı adı veya kanal kimliği> bir telgraf kanalından müzik çalmak için.</b>

**Ortak Komutlar**:

**/oynat** Oynatmak için bir ses dosyasını veya YouTube bağlantısını yanıtlayın veya /oynat <sarkı adı> kullanın.
**/soynat** Jio Saavn'dan müzik çalın, Bu albümdeki tüm şarkıları çalmak için <song adı> veya <code> /splay -bir albüm adı</code> kullanın.
**/çalanşarkı** Çalmakta olan şarkıyı göster.
**/upload** Çalmakta olan şarkıyı ses dosyası olarak yükler.
**/yardım** Komutlar için yardım göster
**/çalmalistesi** Çalma listesini gösterir.

**Yönetici Komutları**:
**/atla** [n] ... Akımı atla veya n burada n >= 2.
**/coynat** Bir kanalın müzik dosyalarından müzik çalın.
**/yoynat** Bir youtube oynatma listesinden müzik çalın.
**/katıl** Sesli sohbete katılın.
**/ayrıl** Mevcut sesli sohbetten çık
**/karıştır** Çalma Listesini Karıştır.
**/vc** Hangi VC'nin birleştirildiğini kontrol edin.
**/dur** Oynatmayı bırak.
**/radyo** Radyoyu Başlat.
**/radyodur** Radyo Akışını durdurur.
**/listeyitemizle** Çalma listesini temizleyin.
**/ihracat** Mevcut çalma listesini ileride kullanmak üzere dışa aktarın.
**/ithalat** Daha önce dışa aktarılan bir oynatma listesini içe aktarın.
**/tekraroynat** Baştan oynatın.
**/temizlik** Kullanılmayan RAW PCM dosyalarını kaldırın.
**/duraklat** Oynatmayı duraklatın.
**/devamet** Oynatmaya devam edin.
**/ses** Sesi değiştir (0-200).
**/sessizlik** VC'de sessize alma.
**/sesiaç** VC'de sesi aç.
**/tekrarbaşlat** Bot'u günceller ve yeniden başlatır.
"""




@Client.on_message(filters.command(['start', f'start@{U}']))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton('᭄☠️ Korsan🍂👣🍂', url='https://t.me/korsanfed'),
        InlineKeyboardButton('᭄☠️ Botunu Yapmak İçin', url='https://t.me/Alem_Sohbet'),
    ],
    [
        InlineKeyboardButton('᭄☠️ Yardım', url='https://t.me/Alem_Sohbet'),
        
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    m=await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)
    await mp.delete(m)
    await mp.delete(message)



@Client.on_message(filters.command(["help", f"help@{U}"]))
async def show_help(client, message):
    buttons = [
        [
        InlineKeyboardButton('᭄☠️ Korsan🍂👣🍂', url='https://t.me/korsanfed'),
        InlineKeyboardButton('᭄☠️ Botunu Yapmak İçin', url='https://t.me/Alem_Sohbet'),
    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    if msg.get('help') is not None:
        await msg['help'].delete()
    msg['help'] = await message.reply_text(
        HELP,
        reply_markup=reply_markup
        )
    await mp.delete(message)
