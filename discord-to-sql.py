import discord
import os
from dotenv import load_dotenv
import sqlite3

class DiscordClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # an attribute we can access from our task
        self.all_messages = []
        self.dbconn = sqlite3.connect(DB_FILENAME)
        self.cursor = self.dbconn.cursor()
        self.cursor.executescript(sql_template_script)
        self.dbconn.commit()


    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
        all_channels = discord.utils.get(self.get_all_channels())
        async for message in all_channels.history():
            self.cursor.execute("""
            INSERT INTO message VALUES (?,?,?)
            """,(message.id,message.author.id,message.content))
            self.cursor.execute("""
            INSERT OR IGNORE INTO user VALUES (?,?)
            """,(message.author.id,message.author.name))

        print("all messages scanned")
        self.dbconn.commit()
        print("db saved")

load_dotenv()
BOT_API_KEY = os.getenv('BOT_API_KEY')
DB_FILENAME = os.getenv('DB_FILENAME')
SQL_TEMPLATE_FILENAME = os.getenv('SQL_TEMPLATE_FILENAME')

with open(SQL_TEMPLATE_FILENAME, 'r') as sql_file:
    sql_template_script = sql_file.read()

client = DiscordClient(intents=discord.Intents.default())
client.run(BOT_API_KEY)
