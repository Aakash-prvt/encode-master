from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Translation(object):

    START_TEXT = """
<b>Hey</b><b> {} </b>

<b>I am Telegram Video Encoder Bot</b>

<b>I can Encode Any File or Video</b>

<b>Use Help Command to Know How to Use me</b>

<b>Made With 💕 By</b><b> @Tellybots_4u</b>
"""
    HELP_TEXT = """
<b>Media or File</b>
➠ <b>Just Send telegram file or media to get started.</b>

<b>Set Thumbnail</b>
➠ <b>Reply With /sthumb With Photo To Save Thumbnail.</b>

<b>Deleting Thumbnail</b>
➠ Send /dthumb to delete thumbnail.</b>

<b>Made With 💕 By</b><b> @Tellybots_4u</b>
"""
    ABOUT_TEXT = """
 **🤖 <b>Bot :** Video-Encoder</b>\n
 **👲 <b>Developer :** [Tellybots_4u](https://telegram.me/tellybots_4u)</b>\n
 **👥 <b>Channel :** [Tellybots_4u](https://telegram.me/tellybots_4u)</b>\n
 **❄️ <b>Credits :** Everyone in this journey</b>\n
 **🍴 <b>Source :** [Click here](https://t.me/tellybots_digital)</b>\n
 **📝 <b>Language :** [Python3](https://python.org)</b>\n
 **📚 <b>Library :** [Pyrogram v1.2.0](https://pyrogram.org)</b>\n
 **🌟 <b>Server :** [Heroku](https://heroku.com)</b>\n
"""
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤖 Update Channel', url='https://telegram.me/tellybots_4u'),
        InlineKeyboardButton('💬 Support Group', url='https://telegram.me/tellybots_support')
        ],[
        InlineKeyboardButton('❔ Help', callback_data='help'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('👲 About', callback_data='about'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 Home', callback_data='home'),
        InlineKeyboardButton('❔ Help', callback_data='help'),
        InlineKeyboardButton('⛔ Close', callback_data='close')
        ]]
    )
    
