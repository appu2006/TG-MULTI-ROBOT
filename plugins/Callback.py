from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton                              
from pyrogram.types import CallbackQuery
import asyncio


@Client.on_callback_query()
async def callback(bot, msg):
   data = msg.data
   if data == "help":
       await msg.message.edit(       
           text="""HEY HERE YOU CAN FIND THE BASIC COMMANDS OF MINE.IF YOU DON'T KNOW HOW TO USE COMMAND JOIN SUPPORT GROUP AND ASK.

<b><u>COMMANDS</u></b>

β send channel last message with
  forwerd tag to get the channel id π―

β /id - your tg id & info

β /telegraph - reply to below 5Mb media
  to get telegraph linkπ―

β /stickerid - Reply To Any Sticker to get sticker id

To Make Logo - /logo Your Name
To Make Square Logo -  /logosq Your Name

β»οΈ Example:
/logo BETAs
/logosq MKN

π€©THANKS FOR USING MEπ
""",       
           reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("π€ ππ ππππ", callback_data="botz")
                  ],[
                  InlineKeyboardButton("β©οΈ ππππ", callback_data="start"),
                  InlineKeyboardButton("π πππππ", callback_data="close")
                  ]]
                  )
           )
   elif data == "about":
         await msg.message.edit(
             text=f""" 
ββββββ° πΌππ»ππΈ π±πΎπ β±ββ
ββ­ββββββββββββββββ£
ββ£βͺΌπ€α΄Κ Ι΄α΄α΄α΄ : {bot.mention}
ββ£βͺΌπ¦α΄α΄α΄  1 : <a href=https://t.me/JP_Jeol_org>α΄α΄α΄Κ</a>
ββ£βͺΌπ¨βπ»α΄α΄α΄  2 : <a href=https://t.me/mr_MKN>α΄Κ.α΄α΄Ι΄ α΄Ι’</a>
ββ£βͺΌβ£οΈsα΄α΄Κα΄α΄ α΄α΄α΄ : <a href=https://github.com/Jeolpaul/TG-MULTI-BOT>α΄Ι’-α΄α΄Κα΄Ιͺ-Κα΄α΄</a>
ββ£βͺΌπ‘Κα΄sα΄α΄α΄ α΄Ι΄ : <a href=https://dashboard.heroku.com>Κα΄Κα΄α΄α΄</a>
ββ£βͺΌπ£οΈΚα΄Ι΄Ι’α΄α΄Ι’α΄ : <a href=https://www.python.org>α΄Κα΄Κα΄Ι΄3</a>
ββ£βͺΌπΚΙͺΚΚα΄ΚΚ : <a href=https://github.com/pyrogram>α΄ΚΚα΄Ι’Κα΄α΄</a> 
ββ£βͺΌποΈα΄ α΄ΚsΙͺα΄Ι΄ : 1.0.3  
ββ°ββββββββββββββββ£
ββββββββββββββββββββ """,
              disable_web_page_preview = True,
              reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("β©οΈ ππππ", callback_data="start"),
                  InlineKeyboardButton("π πππππ", callback_data="close")
                  ]]
                  )
         )        
   elif data == "start":
         await msg.message.edit(
             text=f"Hello {msg.from_user.mention}ππ»\nI'am A Multi use Bot with many usefull features.\neg:- Telegarph, Channel ID, User ID, Fun, Group Id etc...\nYou can see My commands by below button... \n\nβ send channel last message with forwerd tag to get the channel id π―",          
             reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("β£οΈ πππππππ", url="https://t.me/BETA_BOTSUPPORT"),
                  InlineKeyboardButton("π’ πππππππ", url="https://t.me/BETA_UPDATES")
                  ],[            
                  InlineKeyboardButton("βΉοΈ ππππ", callback_data="help"),
                  InlineKeyboardButton("π πππ", callback_data="fun")
                  ],[
                  InlineKeyboardButton("π¨βπ» ππππ π¨βπ» ", callback_data="devs"),
                  InlineKeyboardButton("π€ πππππ", callback_data="about")
                  ]]
                  )
             )
   elif data == "devs":
         await msg.message.edit(
             text=f"This Bot will be made @JP_Jeol & @mr_MKN ",
             reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("π¨βπ» ππππ 1", url="https://t.me/JP_Jeol_org"),
                  InlineKeyboardButton("π¨βπ» ππππ 2", url="https://t.me/mr_MKN")
                  ],[
                  InlineKeyboardButton("β£οΈ ππππππ ππππ β£οΈ", url="https://github.com/Jeolpaul/TG-MULTI-BOT"),
                  ],[
                  InlineKeyboardButton("β©οΈ ππππ", callback_data="start"),
                  InlineKeyboardButton("π πππππ", callback_data="close")
                  ]]
                  )
             )
   elif data == "fun":
         await msg.message.edit(
             text=f"""<b><u>JUS TEST THIS COMMANDS π</u></b>

β /runs         
β /ikka      
β /dice     
β /arrow    
β /goal    
β /luck    
β /throw     
β /bowling  
β /tenpins    
""",      
             reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("β©οΈ ππππ", callback_data="start"),
                 InlineKeyboardButton("π πππππ", callback_data="close")
                 ]]
                 )
             )
   elif data == "botz":
         await msg.message.edit(
             text="π€ This is My botz π",
                 reply_markup=InlineKeyboardMarkup( [[
                     InlineKeyboardButton("βΉοΈ πππππ πππ", url="https://t.me/GeorgeMalarobot"),
                     InlineKeyboardButton("π΅ πππππ πππ", url="https://t.me/SK_MUSIC_ROBOT")
                     ],[
                     InlineKeyboardButton("ποΈ πππππ πππππππ ποΈ", url="https://t.me/MKN_GROUPMANAGEROBOT")
                     ],[                   
                     InlineKeyboardButton("β©οΈ ππππ", callback_data="start"),
                     InlineKeyboardButton("π πππππ", callback_data="close")
                     ]]
                     )
                 )
   elif data == "close":
        await msg.message.delete()
        try:
            await msg.message.reply_to_message.delete()
        except:
            pass
























