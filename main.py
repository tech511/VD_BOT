import logging,shutil
import asyncio
from pyrogram import Client
from config import API_ID,API_HASH,BOT_TOKEN,QUEUE_LIMIT,DOWNLOAD_ROOT
from database.connection import connect_database
from core.task_manager import manager
from core.state import sessions
from cleanup import cleanup_old_downloads
from utils.logging import setup_logging
from callback import setup_callback
from commands import setup_commands
from logic.ban import setup_ban
from handlers.thumbnail_handler import setup_thumbnail

log=setup_logging()
app=Client('VD_BOT',api_id=API_ID,api_hash=API_HASH,bot_token=BOT_TOKEN)

def dependency_check():
    missing=[]
    if not API_ID or not API_HASH or not BOT_TOKEN: missing.append('API_ID/API_HASH/BOT_TOKEN')
    if not shutil.which('ffmpeg'): missing.append('ffmpeg')
    if missing: raise RuntimeError('Missing runtime dependencies/config: '+', '.join(missing))

async def maintenance():
    while True:
        try:
            sessions.cleanup(); cleanup_old_downloads()
        except Exception: log.exception('Maintenance failed')
        await asyncio.sleep(300)

async def main():
    dependency_check(); connect_database()
    setup_commands(app); setup_callback(app); setup_ban(app); setup_thumbnail(app)
    await app.start(); await manager.start(); maint=asyncio.create_task(maintenance())
    me=await app.get_me(); log.info('Bot online as @%s | workers=%s | download_dir=%s',me.username,QUEUE_LIMIT,DOWNLOAD_ROOT)
    try: await asyncio.Event().wait()
    finally:
        maint.cancel(); await asyncio.gather(maint,return_exceptions=True); await manager.stop(); await app.stop()

if __name__=='__main__': asyncio.run(main())
