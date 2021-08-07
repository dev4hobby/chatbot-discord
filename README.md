# Simple Discord BOT

## 환경구성

**Python 3.8.10**

```bash
discord.py         1.7.
youtube-dl         2021.6.6
black              21.7b0
```
sound 모듈 사용시 `opus`, `ffmpeg`, `youtube-dl`에 의존해야함.

<details>
<summary>세부사항</summary>
<div markdown="1">

### Windows (확인 필요)
```
ffmpeg 설치  
https://ffmpeg.org/download.html#build-windows  

opus 설치
https://archive.mozilla.org/pub/opus/win32/opus-tools-0.2-opus-1.3.zip
```

### Linux
```
apt-get update
apt-get install -y opus-tools ffmpeg
pip install -r requirements.txt
```

### OSX
```
brew install opus
brew install ffmpeg
pip install -r requirements.txt
```

</div>