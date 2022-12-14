import discord
import os
from dotenv import load_dotenv
import sqlite3
import sys
import asyncio

class DiscordClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # an attribute we can access from our task
        self.message_counter = 0
        self.dbconn = sqlite3.connect(DB_FILENAME)
        self.cursor = self.dbconn.cursor()
        self.cursor.executescript(sql_template_script)
        self.dbconn.commit()

    async def setup_hook(self) -> None:
        self.status_checker = self.loop.create_task(self.check_status())

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
        all_channels = discord.utils.get(self.get_all_channels())
        async for message in all_channels.history(limit=None):
            self.cursor.execute("""
            INSERT INTO message VALUES (?,?,?)
            """,(message.id,message.author.id,message.content))
            self.cursor.execute("""
            INSERT OR IGNORE INTO user VALUES (?,?)
            """,(message.author.id,message.author.name))

            for react in message.reactions: 
                self.cursor.execute("""
                INSERT OR IGNORE INTO react VALUES (?,?,?)
                """,(message.id, str(react.emoji),react.count))
            self.dbconn.commit()
            self.message_counter += 1
        print("scrape complete")

    async def check_status(self):
        while not self.is_closed():
            print(self.message_counter)
            await asyncio.sleep(10)


load_dotenv()
BOT_API_KEY = os.getenv('BOT_API_KEY')
DB_FILENAME = os.getenv('DB_FILENAME')
SQL_TEMPLATE_FILENAME = os.getenv('SQL_TEMPLATE_FILENAME')

with open(SQL_TEMPLATE_FILENAME, 'r') as sql_file:
    sql_template_script = sql_file.read()

client = DiscordClient(intents=discord.Intents.default())
client.run(BOT_API_KEY)
