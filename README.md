# discord-to-sql
Scrapes the entire post history of a discord server into a SQL database
## Prereqs
* copy the file `.env.sample` in the root directory and name it `.env`
### Discord
1. Make an application [here](https://discord.com/developers/applications)  and name it `discord-to-sql`.
2. Navigate to `bot` and enable it, and save the resulting "secret token" into the `.env` you made earlier, for the variable `BOT_API_KEY` on line 1
3. Click on Oauth2 -> url generator, and check only the top `bot` box, then `administrator` for the other one, as pictured [here](https://user-images.githubusercontent.com/1500566/207491958-07e31957-ec04-456c-ba0d-1a06b6955433.png)
4. Use the generated url to invite this bot to a server where you have permissions to do so
### Local Database
By default sqlite3 creates a database in `discord.db` in the root directory, using the file `discord.sql` as a template to set up the tables.
## Run
`pip3 install discord.py python-dotenv`

`python3 discord-to-sql.py`

Every time it runs it will attempt to build an initial db at the `DB_FILENAME` location specified in `.env` if it does not exist.

After logging into the server(s) where its authed, it will download every message from every channel, filling the tables.

## Planned features

* Currently when you run it, it only gathers the messages up to the moment you started the script.  Can be expanded to also actively gather messages in real time
