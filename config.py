import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent
DOWNLOAD_ROOT = Path(os.getenv('DOWNLOAD_DIR', str(BASE_DIR / 'downloads'))).expanduser().resolve()
DOWNLOAD_ROOT.mkdir(parents=True, exist_ok=True)

API_ID = int(os.getenv('API_ID', '0'))
API_HASH = os.getenv('API_HASH', '')
BOT_TOKEN = os.getenv('BOT_TOKEN', '')
OWNER_ID = int(os.getenv('OWNER_ID', '0'))
MONGO_URL = os.getenv('MONGO_URL', '')

CHANNEL_URL = os.getenv('CHANNEL_URL', 'https://t.me/AniWorld_Bots_Hub')
PROGRESS_REFRESH_RATE = float(os.getenv('PROGRESS_REFRESH_RATE', '3'))
QUEUE_LIMIT = max(1, int(os.getenv('QUEUE_LIMIT', '3')))
SESSION_TTL = int(os.getenv('SESSION_TTL', '600'))
CLEANUP_INTERVAL = int(os.getenv('CLEANUP_INTERVAL', '300'))
MAX_DOWNLOAD_BYTES = int(os.getenv('MAX_DOWNLOAD_BYTES', str(2 * 1024**3)))
MIN_FREE_DISK_BYTES = int(os.getenv('MIN_FREE_DISK_BYTES', str(512 * 1024**2)))

START_IMAGE = os.getenv('START_IMAGE', 'https://i.ibb.co/JW2cgsHr/x.jpg')
HELP_IMAGE = os.getenv('HELP_IMAGE', 'https://i.ibb.co/BKYDfS6y/x.jpg')
DETAILS_IMAGE = os.getenv('DETAILS_IMAGE', 'https://i.ibb.co/m5TsCfcq/x.jpg')
COMMANDS_IMAGE = os.getenv('COMMANDS_IMAGE', 'https://i.ibb.co/JW2cgsHr/x.jpg')
ANALYSIS_IMAGE = os.getenv('ANALYSIS_IMAGE', 'https://graph.org/file/c74667250166f8b66ad1a-4efcd88181cb81688d.jpg')
ERROR_IMAGE = os.getenv('ERROR_IMAGE', 'https://i.ibb.co/BKYDfS6y/x.jpg')
DASHBOARD_IMAGE = os.getenv('DASHBOARD_IMAGE', 'https://graph.org/file/f9d1876922cc67008ee22-2c3eb24f1485dbbf20.jpg')
DOWNLOAD_COMPLETE_IMAGE = os.getenv('DOWNLOAD_COMPLETE_IMAGE', 'https://i.ibb.co/JW2cgsHr/x.jpg')

START_TEXT = '''〔 🤖 ᴠɪᴅᴇᴏ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ 〕\n\n👋 ʜᴇʟʟᴏ {first_name}!!\n━━━━━━━━━━━━━━━━━━━━\nɪ ᴄᴀɴ ᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏꜱ ᴀɴᴅ ᴀᴜᴅɪᴏ ꜰʀᴏᴍ ꜱᴜᴘᴘᴏʀᴛᴇᴅ ꜰᴏʀᴍᴀᴛꜱ.\n\n🚀 ꜱᴇɴᴅ ᴍᴇ ᴀ ᴠɪᴅᴇᴏ ʟɪɴᴋ ᴛᴏ ʙᴇɢɪɴ.\n━━━━━━━━━━━━━━━━━━━━\nᴘᴏᴡᴇʀᴇᴅ ʙʏ: @AniWorld_Bots_Hub'''
HELP_TEXT = '📥 Send a supported video URL.\n\n🔎 I will analyze it and show available video/audio options.\n\nFor playlists, you can select the items you want before starting.'
DETAILS_TEXT = '╭━━━〔 🗃️ ᴅᴇᴛᴀɪʟs 〕━━━╮\n│\n│ 🤖 Bot: VD BOT\n│ ⚙️ Engine: yt-dlp\n│ 🔤 Language: Python\n│ 🗄️ Database: MongoDB\n│ 🚦 Queue: enabled\n│\n╰━━━━━━━━━━━━━━━━━━━━╯'
COMMANDS_TEXT = '━━━〔 📢 ᴄᴏᴍᴍᴀɴᴅꜱ 〕━━━\n\n/start — start the bot\n/settings — user settings\n/database — owner database dashboard\n/ban <id> — owner ban\n/unban <id> — owner unban\n\nSend a media URL to begin.'
RENAME_PROMPT_TEXT = '╭━━━〔 ✏️ ʀᴇɴᴀᴍᴇ ꜰɪʟᴇ 〕━━━╮\n\nSend the new filename.\n\n╰━━━━━━━━━━━━━━━━━━━━╯'
