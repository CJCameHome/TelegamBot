from telegram import Update
from telegram.ext import ContextTypes

async def test_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /test is issued."""
    await update.message.reply_text("Bayot si CJ")