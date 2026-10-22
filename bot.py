
import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ["BOT_TOKEN"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to Instagram Service Store!\n\n"
        "/services - Services dekhein\n"
        "/help - Help"
    )

async def services(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📱 Instagram Services\n\n"
        "1. Instagram Likes\n"
        "2. Instagram Views\n"
        "3. Instagram Followers\n\n"
        "Order ke liye admin se contact karein."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Commands:\n/start - Start bot\n/services - Services dekhein"
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("services", services))
app.add_handler(CommandHandler("help", help_command))
app.run_polling()
