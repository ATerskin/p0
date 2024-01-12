# GroupMe Bot With Math Functionality

## Functionality
1. The bot can reply to you and only you if you enter "Hello bot"
2. The bot can respond to other HUMAN users and to you if somebody says "Good morning" or "Good night"
3. The bot can solve basic arithmitic expressions by entering the command "Do math (expression)"
   - i.e: "Do math 4%2
   - i.e: "Do math 5x2-1/9x100

## Setup

1. Have Python3 installed
2. Have a GroupMe account
3. Drop an instance of a GroupMe bot following this API page: https://dev.groupme.com/tutorials/bots
   - **QUICK HINT** Use this curl command to drop a bot into a GroupMe Group of your choice:
   ```
   curl -X POST -d '{"bot": { "name": "(YOUR BOT'S NAME", "group_id": "(GROUP_ID TO ADD"}}' -H
   'Content-Type: application/json' "https://api.groupme.com/v3/bots?token=(YOUR ACCESS TOKEN)"
   ```
   - Access token can be found in the link above ^
4. Create a .env file with this template and fill out the corresponding fields:
   ```bash
   BOT_ID=""       # YOUR bot's ID in the group
   GROUP_ID=""     # Groups's id
   ACCESS_TOKEN="" # YOUR access token
   USER_ID=""      # YOUR personal GroupMe user_id. Needed so that the bot only responds to you in specific cases
   ```

## How To Run

```bash
# STEP 1:
# WITHIN THE p0 FOLDER
# create virtual environment (this creates a folder called venv)
python3 -m venv venv

# STEP 2:
# cd into groupme-bot folder
# activate virtual environment
source venv/bin/activate # for mac/linux
venv\Scripts\activate # for windows

# STEP 3:
# install dependencies
pip install -r requirements.txt

# STEP 4:
# run the bot.py program
python3 bot.py
