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
   BOT_ID=""
   GROUP_ID="" 
   ACCESS_TOKEN=""
   USER_ID=""
   ```

## How To Run

```bash
**# STEP 1:**
# WITHIN THE p0 FOLDER
# create virtual environment (this creates a folder called venv)
python3 -m venv venv

**# STEP 2:**
# cd into groupme-bot folder
# activate virtual environment
source venv/bin/activate # for mac/linux
venv\Scripts\activate # for windows

**# STEP 3:**
# install dependencies
pip install -r requirements.txt

**# STEP 4: **
# run the bot.py program
python3 bot.py

```bash
BOT_ID=""
GROUP_ID="98324520" # our GroupMe chat id
ACCESS_TOKEN="" 
```

- `BOT_ID` is the id of your bot, you can find this on the [dev page](https://dev.groupme.com/bots)
- This is file is what is loaded in [`bot.py`](./groupme-bot/bot.py#L7) via the `load_dotenv()` function

```bash
# clone the **forked** repo to your local machine and cd into it 
git clone https://github.com/<your-username>/p0.git && cd p0

# create virtual environment (this creates a folder called venv)
python3 -m venv venv

# activate virtual environment
source venv/bin/activate # for mac/linux
venv\Scripts\activate # for windows


# install dependencies
pip install -r requirements.txt
```

To deactivate the virtual environment, run `deactivate`

## Tasks

We have provided you with an outline of the bot in [`bot.py`](./groupme-bot/bot.py) that is able to read/send messages to the GroupMe chat. Your task is to implement the following features:

- [ ] respond to you
  - you should be able to run your script and send a message in the GroupMe chat and have your bot respond to you and **only you**, meaning that if someone else sends the same message, **even with the same name**, your bot should not respond to them
    - hint: look at the [`sample.json`](./groupme-bot/sample.json) that shows what other fields you can extract from a response (i.e. `sender_id`)
    - you can view the contents of a response itself by printing `response.json().get("response", {})` located [here](./groupme-bot/bot.py#L31)(this is what is inside the `response` field of the `sample.json` file)
- [ ] good morning/good night
  - if *anyone* says good morning/good night, your bot should respond with a good morning/good night with their name
    - i.e. if someone says "good morning", your bot should respond with "good morning, <name>"
    - think about how you're going to stop your bot from responding to itself and the other bots in the chat
    - **caution:** if you start spamming the chat, please `ctrl+c` your script to stop it
    - feel free to mute the chat, we will use piazza for any important announcements
- [ ] create 1 (or more, for extra-credit) additional features that you think would be cool
  - you may incorporate other API's (i.e. [Giphy](https://developers.giphy.com/docs/api/endpoint#search))
  - you can have the bot perhaps have tell the weather of a particular city
- [ ] create a doc (markdown, `*.md` file) that outlines the features of your bot, how to run it
  - please put this file in the [`groupme-bot`](./groupme-bot) folder and name it `README.md`
  - refer to markdown syntax [here](https://www.markdownguide.org/basic-syntax/)

## Running

```bash
# activate virtual environment
source venv/bin/activate # for mac/linux
venv\Scripts\activate # for windows

# run bot
python3 bot.py
```

- you *may* additionally add flags that can be added to the `bot.py` script
  - i.e. `python3 bot.py --debug` should run the bot in debug mode and print out more information if something goes wrong
  - i.e. `python3 bot.py --help` should print out a help message that shows what flags are available
    - your TAs will appreciate this

## Submission

as you complete tasks, edit **this** markdown file to reflect your progress. if you have completed something just put an "x" in the checkbox. here's an example:

- [ ] respond to you (not done)
- [x] respond to you (done)

once you are done, commit your changes and push to your forked repo

```bash
# adds all files that have been changed in the current directory
git add .
# commit changes with message "completed p0" (you can change this to whatever you want)
git commit -m "completed p0"
# if this is your first time pushing, you'll need to set the upstream branch
git push --set-upstream origin main
# otherwise, you can just push
git push
```

then, on gradescope submit a `submission.txt` file that has the following contents:

```
username
repo
```

where `username` is your github username and `repo` is the name of your forked repo (i.e. `p0`)
