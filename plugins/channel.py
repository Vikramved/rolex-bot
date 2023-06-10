from pyrogram import Client, filters
from info import CHANNELS
from database.ia_filterdb import save_file
import re

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

    

    # Check if caption exists and contains "@" symbol

    if message.caption and "@" in message.caption:

        # Split the caption by "@" symbol

        parts = message.caption.split("@", 1)

        

        # Replace the word after "@" symbol with "MovieBossTG"

        replaced_caption = parts[0] + "MovieBossTG" + (parts[1] if len(parts) > 1 else "")

        media.caption = replaced_caption

    else:

        media.caption = message.caption

    await save_file(media)

