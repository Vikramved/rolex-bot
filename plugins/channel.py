from pyrogram import Client, filters

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

    

    # Remove specific text from the caption

    caption = message.caption

    if caption is not None:

        unwanted_text = "╔════ ᴊᴏɪɴ ᴡɪᴛʜ ᴜs ═════╗\n𝐂𝐡✯𝐧𝐧𝐞𝐥 :- @MovieUpdates_Mr2\n𝐂𝐡✯𝐧𝐧𝐥𝐥 :- @TeamMovieRockerzz_mr"

        caption = caption.replace(unwanted_text, "")

    media.caption = caption

    await save_file(media)

