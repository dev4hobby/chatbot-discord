# Simple Discord BOT

## Dependency

> Python 3.8.10

```bash
discord.py         1.7.
youtube-dl         2021.6.6
black              21.7b0
```

If you wanna use this as Music BOT
maybe need this step..

### Linux

```bash
apt-get update
apt-get install -y opus-tools ffmpeg
pip install -r requirements.txt
```

### OSX

```bash
brew install opus
brew install ffmpeg
pip install -r requirements.txt
```

## Deploy to heroku

### Procfile

```bash
worker: python ${your_bot_file.py}
```

upload your `Procfile` and enable Dyno

### Config Vars

```json
{
  "DISCORD_BOT_TOKEN": "your_bot_token"
}
```

Go to [Discord developer console > Bot](https://discord.com/developers/applications) and copy your Bot token.

### Aptfile

```bash
wget
```

### Buildpacks

`heroku/python`
`https://github.com/heroku/heroku-buildpack-apt.git`
`https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git`
`https://github.com/xrisk/heroku-opus.git`
