# 🌟 Telegram Quote Bot

*Spread daily inspiration with automated motivational quotes!*

[![Python](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Telegram](https://img.shields.io/badge/Telegram-Bot-blue.svg)](https://core.telegram.org/bots)

## ✨ Features

- 🤖 **Automated Delivery**: Send daily quotes to multiple Telegram chats
- 📚 **Custom Quote Library**: Use your own collection of inspiring quotes
- 🔄 **Smart Rotation**: Cycles through quotes sequentially, never repeating
- 🎨 **Beautiful Formatting**: Markdown formatting with rotating emojis
- 🛡️ **Error Handling**: Robust retry mechanism and comprehensive logging
- 📊 **Progress Tracking**: Keeps track of current quote position
- 🔧 **Easy Configuration**: Simple environment-based setup

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- A Telegram Bot Token ([Get one from @BotFather](https://t.me/botfather))
- Chat IDs where you want to send quotes

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/NorthFi/telegram-quote-bot-py.git
   cd telegram-quote-bot-py
   ```

2. **Install dependencies**
   ```bash
   pip install requests python-dotenv
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   BOT_TOKEN=your_bot_token_here
   CHAT_IDS=chat_id_1,chat_id_2,chat_id_3
   QUOTES_FILE=quotes.txt
   INDEX_FILE=current_index.txt
   ```

4. **Create your quotes file**
   
   Create a `quotes.txt` file with one quote per line:
   ```
   The only way to do great work is to love what you do. - Steve Jobs
   Innovation distinguishes between a leader and a follower. - Steve Jobs
   Stay hungry, stay foolish. - Steve Jobs
   ```

5. **Run the bot**
   ```bash
   python telegram-quote-bot-py.py
   ```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `BOT_TOKEN` | Your Telegram bot token | `YOUR_BOT_TOKEN` |
| `CHAT_IDS` | Comma-separated list of chat IDs | `YOUR_CHAT_IDS` |
| `QUOTES_FILE` | Path to your quotes file | `quotes.txt` |
| `INDEX_FILE` | File to track current quote position | `current_index.txt` |

### Getting Chat IDs

To find your chat ID:
1. Add your bot to the chat
2. Send a message to the chat
3. Visit `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
4. Look for the `chat.id` field in the response

## 📋 Usage Examples

### Manual Execution
```bash
python telegram-quote-bot-py.py
```

### Automated with Cron
Add to your crontab for daily execution at 9 AM:
```bash
0 9 * * * /usr/bin/python3 /path/to/telegram-quote-bot-py/telegram-quote-bot-py.py
```

### Docker Usage
```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["python", "telegram-quote-bot-py.py"]
```

## 📁 Project Structure

```
telegram-quote-bot-py/
├── telegram-quote-bot-py.py      # Main bot script
├── quotes.txt                 # Your quote collection
├── current_index.txt          # Tracks current position
├── .env                       # Environment variables
├── requirements.txt           # Python dependencies
├── README.md                  # This file
└── telegram-quote-bot-py.log     # Log file (generated)
```

## 🎨 Message Format

The bot sends beautifully formatted messages:

```
🌟 Inspiration of the Day:

"The only way to do great work is to love what you do." - Steve Jobs
```

Available emojis: 🌟 🔥 ✨ 💡 🌈 ⚡

## 🔍 Logging

The bot creates detailed logs in `telegram-quote-bot-py.log`:
- Message delivery status
- Error tracking
- Quote progression
- Retry attempts

## 🛠️ Troubleshooting

### Common Issues

**Bot not sending messages?**
- Verify your bot token is correct
- Ensure the bot is added to target chats
- Check chat IDs are properly formatted

**Quotes not advancing?**
- Check file permissions for `current_index.txt`
- Verify quotes file exists and is readable
- Review logs for error messages

**Message formatting issues?**
- Ensure quotes don't contain unescaped markdown characters
- Check the escape_markdown_v2 function handles your content

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Ideas for Contributions

- [ ] Add support for different quote categories
- [ ] Implement time zone support
- [ ] Add quote search functionality
- [ ] Create a web interface for quote management
- [ ] Add support for images/GIFs
- [ ] Implement quote submission via Telegram

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Telegram Bot API](https://core.telegram.org/bots/api) for the amazing platform
- All the quote contributors who inspire us daily
- The Python community for excellent libraries

## 📞 Support

Having issues? Here's how to get help:

- 📖 Check the [documentation](https://github.com/NorthFi/telegram-quote-bot-py/wiki)
- 🐛 Report bugs via [GitHub Issues](https://github.com/NorthFi/telegram-quote-bot-py/issues)
- 💬 Join our [Telegram Group](https://t.me/quote_bot_support)
- ⭐ Star the repo if you find it useful!

---

*Made with ❤️ for spreading daily inspiration*
