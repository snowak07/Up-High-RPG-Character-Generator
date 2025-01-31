# INSTALLATION
python version >= 3.10 required.

For OpenAI integration you need the following additional setup:\
- Environment variable called OPENAI_API_KEY set to your own api key.\
- openai package installed e.g. `pip3 install openai`\
NOTE: Might need to setup a python venv to install openai if you used Homebrew to install python.\
NOTE: Use `source myenv/bin/activate` with each new terminal instance if you needed above step.

# USAGE
Run the following to start the character generator.
```python3 char-gen.py```

### Parameters
- `print=true` Prints the output to a txt file with your character name.
- `summary=true` Adds a GPT summary of the character's backstory to the end of the output.
- `load_backstory=true` Loads a already created character file and appends a GPT summary to the end of the same file. Below parameter also required with this option.
- `path/to/character/file` File path to your character file used in conjunction with the above parameter.

### Examples
```
python3 char-gen.py print=true summary=true
python3 char-gen.py load_backstory=true ./path/to/file
```