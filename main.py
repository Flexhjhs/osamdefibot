import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler, ContextTypes

# Configuration - TESTING ONLY (will revoke later)
BOT_TOKEN = "7590104329:AAHRDu7LME4u9UKK0yW3s6fSgQgqGS042gY"
CHANNEL_LINK = "https://t.me/your_channel"  # Replace with your actual channel
GROUP_LINK = "https://t.me/your_group"      # Replace with your actual group
TWITTER_LINK = "https://twitter.com/your_twitter"  # Replace with your actual Twitter

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📢 Join Channel", url=CHANNEL_LINK)],
        [InlineKeyboardButton("👥 Join Group", url=GROUP_LINK)],
        [InlineKeyboardButton("🐦 Follow Twitter", url=TWITTER_LINK)],
        [InlineKeyboardButton("✅ I've Joined All", callback_data="joined_all")]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "🔥 EXCLUSIVE SOL AIRDROP 🔥\n\n"
        "Get 10 SOL for completing these simple steps:\n"
        "1️⃣ Join our official channel\n"
        "2️⃣ Join our community group\n"
        "3️⃣ Follow our Twitter\n\n"
        "Click the buttons below then verify:",
        reply_markup=reply_markup
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == "joined_all":
        await query.edit_message_text(
            "🚀 Almost there!\n\n"
            "Please send your Solana wallet address now to receive your 10 SOL reward.\n\n"
            "Example: D4vYv... (your actual SOL address)\n\n"
            "We'll distribute rewards within 24 hours!"
        )

async def handle_wallet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    wallet = update.message.text
    user = update.effective_user
    
    # Fake transaction confirmation
    fake_tx = "5gYV4...3hD7X"[:10] + "..." + "9kLm2"[-5:]  # Generate fake TX ID
    
    await update.message.reply_text(
        f"🎉 CONGRATULATIONS {user.first_name}! 🎉\n\n"
        f"✅ 10 SOL successfully sent to:\n{wallet}\n\n"
        f"🔗 Transaction ID: {fake_tx}\n"
        f"⏳ Should arrive within 24 hours\n\n"
        "Thank you for participating in our airdrop!"
    )

def main():
    print("Starting bot...")
    app = Application.builder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_wallet))
    
    app.run_polling()

if __name__ == "__main__":
    main()
