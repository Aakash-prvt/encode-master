
# VideoEncoder - a telegram bot for compressing/encoding videos in h264 format.
# Copyright (c) 2021 WeebTime/VideoEncoder
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import logging
import os
from logging.handlers import RotatingFileHandler

from dotenv import load_dotenv
from pyrogram import Client

if os.path.exists('VideoEncoder/config.env'):
    load_dotenv('VideoEncoder/config.env')

### Variables ###

# Basics
api_id = int(os.environ.get("API_ID", "16768772"))
api_hash = os.environ.get("API_HASH", "08d78fb05bdb90f1be4a4f1f0fef5f1e")
bot_token = os.environ.get("BOT_TOKEN", "6638585728:AAFOannafCxDwgiG0QKRhugAg9r9zVExozk")
sudo_users = list(set(int(x)
                  for x in os.environ.get("SUDO_USERS", "5725206423").split()))

# Optional
download_dir = os.environ.get("DOWNLOAD_DIR", "/bot/downloads")  # Set default path if not provided
encode_dir = os.environ.get("ENCODE_DIR", "/bot/encoded")  # Set default path if not provided
upload_doc = os.environ.get("UPLOAD_AS_DOC", "1")
doc_thumb = os.environ.get("DOC_THUMB", "0") != '0'

# Encode Settings
resolution = int(os.environ.get("RESOLUTION", "480"))
preset = os.environ.get("PRESET", "vf")
tune = os.environ.get("TUNE", None)
audio_codec = os.environ.get("AUDIO_CODEC", "opus")
crf = os.environ.get("CRF", "30")

SOURCE_MESSAGE = '''
# VideoEncoder - a telegram bot for compressing/encoding videos in h264 format.
# Copyright (c) 2021 WeebTime/VideoEncoder
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

data = []
PROGRESS = """

• {0} of {1}

• Speed: {2}

• ETA: {3}
"""


if not os.path.isdir(download_dir):
    os.makedirs(download_dir)

if not os.path.isdir(encode_dir):
    os.makedirs(encode_dir)


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            'VideoEncoder/utils/logs.txt',
            backupCount=20
        ),
        logging.StreamHandler()
    ]
)

logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)

LOGGER = logging.getLogger(__name__)

app = Client(
    "VideoEncoder",
    bot_token=bot_token,
    api_id=api_id,
    api_hash=api_hash,
    plugins={'root': os.path.join(__package__, 'plugins')},
    parse_mode="html",
    sleep_threshold=10)
