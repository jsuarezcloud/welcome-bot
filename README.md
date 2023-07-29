# Discord-Welcome-Bot
This is a simple app for running a Discord Welcome Bot within your server

# App Configuration
To use this app, you'll need to add some specific entries in the **.env** file

Here are the following fields listed in the **.env** file:
* **DISCORD_TOKEN**: This field requires the token generated on the Discord Developer Portal for the Bot created
* **DISCORD_GUILD**: This field requires the guild/server name where the Discord Bot will be hosted on
* **DISCORD_SERVER_LIST**: This field is only used if this Discord Bot will run on multiple servers, which requires 
the guild's/server's name of all associated guilds/servers 
  * to use this field you'll need to add a comma with no spaces between each server name; there is a comma delimiter set
  within the **welcome_bot.py** module which if you want to use more than one server, you'll need to remove the comment
  on line **12**
  * **.env file EX:** ***DISCORD_SERVER_LIST=server1,server2***

This application does have two packages required, those being **discord** package and the **python-dotenv** package

When the project is installed locally and if you're running the project on an IDE/Editor, the IDE/Editor should prompt 
you to install those requirements