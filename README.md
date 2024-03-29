# EducaBot
A discord bot created to allow some useful commands to server management

# Setting up Application
First of all, make sure you have a valid Discord Bot Token, you can find it in the link [How to Get a Discord Bot Token](https://www.writebots.com/discord-bot-token/).

Once you have a valid token, you need to export it in your environment, as following:

```bash
export DISCORD_BOT_TOKEN=<your_discord_bot_token>
```

After that, you need to install the project dependencies to finish setting everything up, as showed below.

```bash
python -m venv .env
. .env/bin/activate
pip install -r requirements.txt
```

# Running application
```bash
make run
```

# Setting up tests
```bash
pip install -r test_requirements.txt
```

# Running tests
```bash
make test
```

# List of Supported commands

| Command Name | Action |
| ------------ | ------ |
| $ping | Prints the phrase "Pong!" on the channel |
