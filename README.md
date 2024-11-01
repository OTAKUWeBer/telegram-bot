# Telegram Video Downloader Bot

A simple Telegram bot that allows users to get direct links to download or stream videos from YouTube, Facebook, and Instagram by sending a URL. The bot utilizes the [yt-dlp](https://github.com/yt-dlp/yt-dlp) library to extract video links.

## Features

- Extract direct streaming/download links from:
  - YouTube
  - Facebook
  - Instagram
- Easy-to-use commands
- No file downloads; links are provided directly

## Commands

- `/help`: Show available commands
- `yt <YouTube URL>`: Get a link to a YouTube video
- `fb <Facebook URL>`: Get a link to a Facebook video
- `ig <Instagram URL>`: Get a link to an Instagram video

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/OTAKUWeBer/telegram-bot.git
   cd telegram-bot
   ```

2. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your Telegram Bot:**
   - Create a new bot using [BotFather](https://core.telegram.org/bots#botfather) and get the token.
   - Replace the `TOKEN` variable in `main.py` with your bot token.

## Usage

1. Run the bot:

   ```bash
   python main.py
   ```

2. Open your Telegram app and search for your bot. Start a chat and use the commands listed above.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## Acknowledgments

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) for the video link extraction functionality.
- [Telepot](https://github.com/nickoala/telepot) for the Telegram bot framework.# telegram-bot
