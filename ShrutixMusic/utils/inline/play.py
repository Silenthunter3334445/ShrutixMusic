import math
import random

import config
from pyrogram import enums
from pyrogram.types import InlineKeyboardButton

from ShrutixMusic import nand as app
from ShrutixMusic.utils.formatters import time_to_seconds


STYLES = [
    enums.ButtonStyle.PRIMARY,
    enums.ButtonStyle.SUCCESS,
    enums.ButtonStyle.DANGER,
]


def _get_style(style_val):
    if getattr(config, "BUTTON_COLOUR", False):
        return {"style": style_val}
    return {}


def autoplay_markup(chat_id: int, mode: bool):
    status = "ON ✅" if mode else "OFF ❌"
    return [
        InlineKeyboardButton(
            text=f"Autoplay: {status}",
            callback_data=f"autoplay {chat_id}",
        )
    ]


def track_markup(_, videoid, user_id, channel, fplay):
    r1, r2 = random.choices(STYLES, k=2)
    return [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
                **_get_style(r1),
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
                **_get_style(r1),
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
                **_get_style(r2),
            )
        ],
    ]


def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)

    remaining_sec = max(0, duration_sec - played_sec)
    remaining = f"{remaining_sec // 60:02d}:{remaining_sec % 60:02d}"

    percentage = (played_sec / duration_sec) * 100 if duration_sec else 0
    umm = math.floor(percentage)

    if 0 < umm <= 10:
        bar = "|♬—————————|-"
    elif umm < 20:
        bar = "|—♬————————|-"
    elif umm < 30:
        bar = "|——♬———————|-"
    elif umm < 40:
        bar = "|———♬——————|-"
    elif umm < 50:
        bar = "|————♬—————|-"
    elif umm < 60:
        bar = "|—————♬————|-"
    elif umm < 70:
        bar = "|——————♬———|-"
    elif umm < 80:
        bar = "|———————♬——|-"
    elif umm < 95:
        bar = "|————————♬—|-"
    else:
        bar = "|—————————♬|-"

    r1, r2, r3, r4 = random.choices(STYLES, k=4)

    return [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {remaining}",
                url=f"https://t.me/{app.username}?startgroup=true",
                **_get_style(r1),
            )
        ],
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
                **_get_style(r2),
            ),
            InlineKeyboardButton(
                text="II",
                callback_data=f"ADMIN Pause|{chat_id}",
                **_get_style(r2),
            ),
            InlineKeyboardButton(
                text="↻",
                callback_data=f"ADMIN Replay|{chat_id}",
                **_get_style(r2),
            ),
            InlineKeyboardButton(
                text="‣‣I",
                callback_data=f"ADMIN Skip|{chat_id}",
                **_get_style(r2),
            ),
            InlineKeyboardButton(
                text="▢",
                callback_data=f"ADMIN Stop|{chat_id}",
                **_get_style(r2),
            ),
        ],
        [
            InlineKeyboardButton(
                text="💬 sᴜᴘᴘᴏʀᴛ",
                url=config.SUPPORT_CHAT,
                **_get_style(r3),
            ),
            InlineKeyboardButton(
                text="📢 ᴄʜᴀɴɴᴇʟ",
                url=config.SUPPORT_CHANNEL,
                **_get_style(r3),
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
                **_get_style(r4),
            )
        ],
    ]


def stream_markup(_, chat_id):
    r1, r2, r3 = random.choices(STYLES, k=3)

    return [
        [
            InlineKeyboardButton(
                text="▷",
                callback_data=f"ADMIN Resume|{chat_id}",
                **_get_style(r1),
            ),
            InlineKeyboardButton(
                text="II",
                callback_data=f"ADMIN Pause|{chat_id}",
                **_get_style(r1),
            ),
            InlineKeyboardButton(
                text="↻",
                callback_data=f"ADMIN Replay|{chat_id}",
                **_get_style(r1),
            ),
            InlineKeyboardButton(
                text="‣‣I",
                callback_data=f"ADMIN Skip|{chat_id}",
                **_get_style(r1),
            ),
            InlineKeyboardButton(
                text="▢",
                callback_data=f"ADMIN Stop|{chat_id}",
                **_get_style(r1),
            ),
        ],
        [
            InlineKeyboardButton(
                text="💬 sᴜᴘᴘᴏʀᴛ",
                url=config.SUPPORT_CHAT,
                **_get_style(r2),
            ),
            InlineKeyboardButton(
                text="📢 ᴄʜᴀɴɴᴇʟ",
                url=config.SUPPORT_CHANNEL,
                **_get_style(r2),
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
                **_get_style(r3),
            )
        ],
    ]


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    r1, r2 = random.choices(STYLES, k=2)

    return [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"SIMPLEPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
                **_get_style(r1),
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"SIMPLEPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
                **_get_style(r1),
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
                **_get_style(r2),
            )
        ],
    ]


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    r1, r2 = random.choices(STYLES, k=2)

    return [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
                **_get_style(r1),
            )
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
                **_get_style(r2),
            )
        ],
    ]


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = str(query)[:20]
    r1, r2 = random.choices(STYLES, k=2)

    return [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
                **_get_style(r1),
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
                **_get_style(r1),
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
                **_get_style(r2),
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
                **_get_style(r2),
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
                **_get_style(r2),
            ),
        ],
    ]
