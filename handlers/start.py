from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAIp9mBtwBBZGywWEmV-WC8gcMArjusuAAKMAgACTp1xV6m-mtC1YTfoHgQ")
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!
\nI can play music in your group's voice chat
Maintained by @Imteyaz_king  ❤
\nTo add in your group contact us at @Awesome_support .
\nUse the buttons below to know more about me.
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🌍 FRIENDS FOREVER", url="https://t.me/FRIENDS_FOREVER_OFFICIAL_CHAT",
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/Awesome_support"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/Awesome_Lists"
                    ),
                    InlineKeyboardButton(
                        "💾 Source code", url="https://github.com/QueenArzoo/VCPlayBot"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "➕ Add To Your Group ➕", url="https://t.me/VC_Imteyaz_bot?startgroup=true"
                    )
                ]
            ]
        )
    )

@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
