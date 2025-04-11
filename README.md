# INSTALLATION
python version >= 3.10 required.

To run the discord bot you need the Discord Bot Token for the Character Generator bot from the Discord developer portal (link below). Set an environment variable to DISCORD_PYTHON_API_KEY
- Warning! You have to reset the bot token to reveal it on the console. Doing so will disable existing environment variables.
- https://discord.com/developers/applications

For OpenAI integration you need the following additional setup:\
- openai package installed e.g. `pip3 install openai`\
- Environment variable called OPENAI_API_KEY set to your own api key.\
NOTE: Might need to setup a python venv to install openai if you used Homebrew to install python.\
NOTE: Use `source myenv/bin/activate` with each new terminal instance if you needed above step.

# DISCORD BOT USAGE
Run the following to start the character generator.
```
python3 discord_bot.py
```

# CLI USAGE
Run the following to start the character generator.
```
python3 character_generator_controller.py
```

### Parameters
- `print=true` Prints the output to a txt file with your character name.
- `summary=true` Adds a GPT summary of the character's backstory to the end of the output.
- `load_backstory=true` Loads a already created character file and appends a GPT summary to the end of the same file. Below parameter also required with this option.
- `path/to/character/file` File path to your character file used in conjunction with the above parameter.

### Examples
```
python3 character_generator_controller.py print=true summary=true
python3 character_generator_controller.py load_backstory=true ./path/to/file
```