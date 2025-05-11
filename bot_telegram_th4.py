import telebot

# Substitui pelo teu token real
TOKEN = '7845048247:AAE8nAczgS60hV2Owtuwl7h47UAAJq-L3rk'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome_message(message):
    bot.send_message(
        message.chat.id,
        "Olá! 👋 Bem-vindo ao *Kz Dicas Diárias*!\n"
        "Aqui, você receberá dicas práticas e simples para começar a ganhar dinheiro com baixo investimento.\n"
        "Use o menu abaixo para explorar as opções disponíveis.\n"
        "💡 Comece agora e transforme seu tempo livre em renda!",
        parse_mode="Markdown"
    )

@bot.message_handler(commands=['dica'])
def send_dica(message):
    bot.send_message(
        message.chat.id,
        "💡 *Dica do Dia:*\n"
        "Explore oportunidades de renda extra utilizando habilidades que você já possui. "
        "Pense em como transformar seu conhecimento em um serviço ou produto digital.",
        parse_mode="Markdown"
    )

@bot.message_handler(commands=['ebook'])
def send_ebook(message):
    bot.send_message(
        message.chat.id,
        "📘 *E-books Disponíveis:*\n"
        "1. \"Comece a Ganhar com o que Você Sabe\"\n"
        "2. \"Transforme Seu Tempo Livre em Renda\"\n\n"
        "Para adquirir, visite: wa.me/244958905453",
        parse_mode="Markdown"
    )

@bot.message_handler(commands=['premium'])
def send_premium(message):
    bot.send_message(
        message.chat.id,
        "🚀 *Acesso Premium:*\n"
        "Obtenha estratégias exclusivas, suporte personalizado e atualizações frequentes.\n"
        "Saiba mais em: wa.me/244958905453",
        parse_mode="Markdown"
    )

@bot.message_handler(commands=['suporte'])
def send_support(message):
    bot.send_message(
        message.chat.id,
        "🤝 *Suporte:*\n"
        "Para dúvidas ou assistência, entre em contato conosco através do e-mail: storemy067@gmail.com",
        parse_mode="Markdown"
    )

bot.infinity_polling()
