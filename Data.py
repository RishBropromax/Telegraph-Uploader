from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
ðHello {}

I can upload media to telegra.ph and give you back the link with ease. Try sending multiple media, and it still won't stop me.
I can also be used in groups !!
To see `Supported Media Types` tap the related button below.
Use the other buttons to know more about me and my usage.

â¨Powerd By : @EmoBotDevolopers & @SDBOTs_inifinity
    """

    # Help Message
    HELP = """
ð**HOW TO USE ME**ð

See `Supported Media Types` by clicking that related button below.

ð**How to use me here?**ð
Just send the media and leave rest on me. 

ðº**How to use in group?**ðº
Add to me the group.
Then reply to a media with /telegraph to get the telegra.ph link.

âï¸**Commands**âï¸

>> /t
>> /tg
>> /telegraph

More features in development. Keep track by joining @SDBOTS_Inifinity.
    """

    # About Message
    ABOUT = """
âï¸**About This Bot**âï¸

ð Bot created by @SDBOTS_Inifinity & @EmoBotDevolopers

ð¦ Source Code : [Click Here](https://github.com/RishBropromax/Telegraph-Uploader)

âï¸ Framework : [Pyrogram](docs.pyrogram.org)

ð° Language : [Python](www.python.org)

ð¨âð» Developer : @ImRishmika

ðSupport : [SD Bá´á´s CÊá´á´ â¡ï¸](https://t.me/+RiZlGUJfgBM3NjQ1) or [Emo Bot Support ð¥](t.me/EmoBotSupport)
    """

    SUPPORTED_MEDIA_TYPES = """
â **SUPPORTED MEDIA TYPES** â 

1) Image
2) Sticker
3) Gifs or Animation
4) Video
5) Video Note
6) Document (Video/Photo/Gif)

Note : Telegraph has a size limit of 5 MB.
    """

    # Home Button
    home_buttons = [
        [
            InlineKeyboardButton("â¡ï¸SD Bá´á´sâ¡ï¸", url="https://t.me/SDBOTs_inifinity"),
        ],
        [
            InlineKeyboardButton("</> ÑÐ¼Ï Ð²ÏÑ âÑÎ½ÏâÏÏÑÊÑ", url="https://t.me/EmoBotDevolopers"),
        ],
        [InlineKeyboardButton("ð§© Supported Media Types ð§©", callback_data="supported_media_types")],
        [InlineKeyboardButton("ð Close ð", callback_data="close")],
        [InlineKeyboardButton(text="ð  Return Home ð ", callback_data="home")],
    ]

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("â¡ï¸SD Bá´á´sâ¡ï¸", url="https://t.me/SDBOTs_inifinity")
        ],
        [
            InlineKeyboardButton("</> ÑÐ¼Ï Ð²ÏÑ âÑÎ½ÏâÏÏÑÊÑ", url="https://t.me/EmoBotDevolopers"),
        ],
        [InlineKeyboardButton("ð§© Supported Media Types ð§©", callback_data="supported_media_types")],
        [
            InlineKeyboardButton("How to Use â", callback_data="help"),
            InlineKeyboardButton("ð¥ About ð¥", callback_data="about")
        ],
        [InlineKeyboardButton("Close ð", callback_data="close")]
    ]

    # Supported Media Buttons
    supported_media_buttons = [
        [InlineKeyboardButton("â¡ï¸SD Bá´á´sâ¡ï¸", url="https://t.me/SDBOTs_inifinity")],
        [InlineKeyboardButton("</> ÑÐ¼Ï Ð²ÏÑ âÑÎ½ÏâÏÏÑÊÑ", url="https://t.me/EmoBotDevolopers")],
        [InlineKeyboardButton("Close ð", callback_data="close")],
        [InlineKeyboardButton(text="ð  Return Home ð ", callback_data="home")]
    ]
