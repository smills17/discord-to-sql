# discord-to-sql
Scrapes the entire post history of a discord server into a SQL database
## Prereqs
* copy the file `.env.sample` in the root directory and name it `.env`
### Discord
* Make an application [here](https://discord.com/developers/applications)  and name it `discord-to-sql`.
* navigate to `bot` and enable it, and save the resulting `secret token` in `.env` for `BOT_API_KEY`
* Click on Oauth2 -> url generator, and check only the top `bot` box, then `administrator` for the other one, as pictured [here](https://user-images.githubusercontent.com/1500566/207491958-07e31957-ec04-456c-ba0d-1a06b6955433.png)
4. Use the generated url to invite this bot to a server where you have permissions to do so
### Local Database
## Run
### Full Scrape / Initial DB Build
### Update
