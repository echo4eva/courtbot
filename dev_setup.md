# Setting up a Discord Bot
[source of tutorial](https://youtu.be/xc1VpbRd4is)

# 1. Virtual Environment

**How to create a virtual environment**

- command in terminal

```python
py -m venv env
```

- `py` → prefix to state we’re using python
- `-m` → locates the current location being used
- `venv` → creates a virtual environment
- `env` → the name of the environment folder

---

**How to activate the virtual environment**

```python
.\env\Scripts\activate
```

- `.` → locates the current location being used
- `\env\Scripts\activate` → the location and what we want to use, the activate file.
- once activated, will see “(env)”

---

**Issue with activating**

- get an error saying that running a script is disabled

---

**To get around the issue above**

[source](https://www.stanleyulili.com/powershell/solution-to-running-scripts-is-disabled-on-this-system-error-on-powershell/)

1. open up powershell as an admin
2. do this command

```python
set-executionpolicy remotesigned
```

1. say “Y”
2. now you can activate by going through “how to activate the virtual environment”

# 2. Hikari Library

It’s a better version of discord.py I guess. 

[source](https://www.hikari-py.dev/)

**How to install the hikarai library**

1. once activated the environment, install the library in VSCode’s terminal

```python
python -m pip install -U hikari
# Windows users may need to run this instead...
py -3 -m pip install -U hikari
```

1. restart VSCode
2. installed, but if there’s an issue

---

**A possible issue**

- since we are using a virtual environment, VSCode might not run the virtual environment, therefore not detecting the hikari library
- when doing `import hikari` at the top of a python file, it wont detect hikari even though installed in venv

---

**Troubleshooting then issue**

[source](https://youtu.be/5ud9Y2uB4PY)

1. go to View > Command Palette (ctrl+shift+p)
2. type in “python: select interpreter”
3. choose the one with “\env\” folder path
4. now vscode detects hikari!

# 3. .gitignore + venv

Not sure if this step is necessary since I already put it in the main branch.

**How to get a .gitignore file**

[source](https://youtu.be/qSnjgEU6VwQ)

- just watch the video bruh, probably wont need because it’s already in repository. but possibly useful info

---

**.gitignore**

- allows us to ignore some files and folders when committing
- if we don’t use this, then we have to uncheck stuff all the time, just do it

---

**Virtual environment**

- since we made a virtual environment folder, git will detect everything in the \env\ folder when we don’t want it to, so that’s why we add it to .gitignore, kinda like it’s a text file on its own line

```python
env/
```

- `env/` → is the folder name within the project, blocking everything in the folder

# 4. .env (not mistakened for venv folder!)

.env is a type of file that we can use to make things hidden such as variable names, in this case, the token of the discord bot. If someone has the token of the discord bot, they’re able to hack it without our permission, so it’s good to keep it hidden from the public.

The only reason we’re doing this is because our repository is out in the public, we will use “3. .gitignore + venv” in this step too.

There are many ways to make things hidden from the public, but we will follow this video because it was a good tutorial.

[source tutorial](https://youtu.be/YdgIWTYQ69A)

[source github repository](https://github.com/theskumar/python-dotenv)

**dotenv**

- name of the library
- install it by in VSCode’s terminal while venv is activated!

```python
pip install python-dotenv
```

---

**Ignoring it in git**

- add it to the .gitignore list

```python
.env
```

- ignore it so it doesn’t get added to the repository, cuz it’s secret! duh!

---

**etc.**

- just watch the video bruh, im done explaining tbh (to be honest).