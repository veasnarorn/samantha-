import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise RuntimeError("TOKEN not found. Add TOKEN in Railway Variables.")


def main_menu():
    keyboard = [
        [
            InlineKeyboardButton(
                "🤖 BOT",
                callback_data="bot"
            )
        ],
        [
            InlineKeyboardButton(
                "📢 CANAL OFICIAL",
                callback_data="channel"
            )
        ],
        [
            InlineKeyboardButton(
                "📷 INSTAGRAM",
                callback_data="instagram"
            )
        ],
        [
            InlineKeyboardButton(
                "💬 SUPORTE",
                callback_data="support"
            )
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "✨ *Bem-vindo à Equipe Samantha!*\n\n"
        "Escolha uma opção abaixo:"
    )

    await update.message.reply_text(
        text=text,
        parse_mode="Markdown",
        reply_markup=main_menu(),
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "bot":
        keyboard = [[
            InlineKeyboardButton(
                "🤖 Abrir Bot",
                url="https://t.me/samanthaequipe_bot"
            )
        ]]

        await query.message.reply_text(
            "🤖 *Bot Oficial*\n\n"
            "Clique abaixo para abrir:",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    elif query.data == "channel":
        keyboard = [[
            InlineKeyboardButton(
                "📢 Abrir Canal",
                url="https://t.me/samanthaequipeganhos"
            )
        ]]

        await query.message.reply_text(
            "📢 *Canal Oficial*\n\n"
            "Acesse nosso canal:",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    elif query.data == "instagram":
        keyboard = [[
            InlineKeyboardButton(
                "📷 Abrir Instagram",
                url="https://www.instagram.com/888equipe.top"
            )
        ]]

        await query.message.reply_text(
            "📷 *Instagram Oficial*\n\n"
            "Siga nosso Instagram:",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )

    elif query.data == "support":
        keyboard = [[
            InlineKeyboardButton(
                "💬 Abrir Suporte",
                url="https://cf.dot01bx.cfd/chat/index?channelId=0fce0c9e5a984c169ae0a373ef9e72c3"
            )
        ]]

        await query.message.reply_text(
            "💬 *Suporte Oficial*\n\n"
            "Clique abaixo para falar com o suporte:",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(keyboard),
        )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("✅ Samantha Equipe Bot Online")

    app.run_polling(drop_pending_updates=True)


if name == "__main__":
    main()
