from pyrogram import Client, filters

import re

from info import CHANNELS

from database.ia_filterdb import save_file

media_filter = filters.document | filters.video | filters.audio

@Client.on_message(filters.chat(CHANNELS) & media_filter)

async def media(bot, message):

    """Media Handler"""

    for file_type in ("document", "video", "audio"):

        media = getattr(message, file_type, None)

        if media is not None:

            break

    else:

        return

    media.file_type = file_type

    media.caption = message.caption

    # Remove words mentioned with "@" symbol from the caption

    caption_words = re.findall(r'@(\w+)', media.caption)

    for word in caption_words:

        media.caption = media.caption.replace(f"@{word}", "")

    await save_file(media)

