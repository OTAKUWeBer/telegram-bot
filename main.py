import telepot
import yt_dlp
from time import sleep
import os

# Use Your BOT token here
TOKEN = os.getenv('BOT_TOKEN')  # Replace "os.getenv('BOT_TOKEN')" with your actual bot token
bot = telepot.Bot(TOKEN)

def extract_video_url(url):
    ydl_opts = {
        'format': 'best',
        'noplaylist': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)  # Set download to False
        video_url = info.get('url')  # Extract the direct video URL
        title = info.get('title', 'Video')
        return video_url, title

def handle(msg):
    username = msg.get('from', {}).get('username', 'Unknown')
    chat_type = msg.get('chat', {}).get('type', 'Unknown')
    text = msg.get('text', 'No text')
    
    print(f"Username: {username}, Type: {chat_type}, Text: {text}")
    
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        command = msg['text'].strip()
        
        if command.startswith('yt '):
            url = command[3:]  # Extract the URL after "yt "
            bot.sendMessage(chat_id, "Extracting YouTube video link...")
            try:
                video_url, title = extract_video_url(url)
                bot.sendMessage(chat_id, f"Here is the video/download link for <a href='{video_url}'>{title}</a>.", parse_mode='HTML')
            except Exception as e:
                bot.sendMessage(chat_id, f"An error occurred: {str(e)}")
        
        elif command.startswith('fb '):
            url = command[3:]  # Extract the URL after "fb "
            bot.sendMessage(chat_id, "Extracting Facebook video link...")
            try:
                video_url, title = extract_video_url(url)
                bot.sendMessage(chat_id, f"Here is the video/download link for <a href='{video_url}'>{title}</a>.", parse_mode='HTML')
            except Exception as e:
                bot.sendMessage(chat_id, f"An error occurred: {str(e)}")
        
        elif command.startswith('ig '):
            url = command[3:]  # Extract the URL after "ig "
            bot.sendMessage(chat_id, "Extracting Instagram video link...")
            try:
                video_url, title = extract_video_url(url)
                bot.sendMessage(chat_id, f"Here is the video/download link for <a href='{video_url}'>{title}</a>.", parse_mode='HTML')
            except Exception as e:
                bot.sendMessage(chat_id, f"An error occurred: {str(e)}")
        
        elif command == '/help':
            help_message = (
                "Available commands:\n"
                "/help - Show this help message\n"
                "yt <YouTube URL> - Get a link to the YouTube video\n"
                "fb <Facebook URL> - Get a link to the Facebook video\n"
                "ig <Instagram URL> - Get a link to the Instagram video\n\n"
                "Check my GitHub for more information: https://github.com/OTAKUWeBer"
            )
            bot.sendMessage(chat_id, help_message)
            
        else:
            other_msgs = "/help - To check the available commands\n"
            bot.sendMessage(chat_id, other_msgs)

# Set the bot to listen for messages
bot.message_loop(handle)

print('Listening for messages...')
while True:
    sleep(10)
