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

    if message.caption:

        caption = message.caption

        # Find the word after the "@" symbol

        match = re.search(r'@(\w+)', caption)

        if match:

            word_to_replace = match.group(1)

            # Replace the word with "MovieBossTG"

            new_caption = caption.replace(f"@{word_to_replace}", "MovieBossTG")

            media.caption = new_caption

        else:

            media.caption = caption

    await save_file(media)

