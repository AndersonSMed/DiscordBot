# EducaBot
A discord bot created to allow some useful commands to both professors and students

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
python -m app
```

# Running tests
Before running tests, you'll need to install the required test dependencies. To do so, run the following commands inside your environment:
```bash
pip install -r test_requirements.txt
```
After that, you can finally run the application's tests using the following command:
```bash
python -m pytest
```

# Contributing guidelines
First of all, thanks for the interest. If you want to contribute on this project, you will need to setup your environment first. To do so, follow up the next steps.
## Code Style
- Install pre-commit in your machine, you can find how to do it inside [pre-commit homepage](https://pre-commit.com/).
- After that, install the git hooks, as showed in [installing git hook scripts](https://pre-commit.com/#3-install-the-git-hook-scripts).
- This project also uses the [google python style guide](https://google.github.io/styleguide/pyguide.html), therefore, take a read on it before start coding.