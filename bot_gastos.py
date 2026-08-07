import os
from datetime import datetime
import telebot
import pandas as pd

# Cole aqui o Token que você recebeu do @BotFather
TOKEN = os.environ.get("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)

NOME_ARQUIVO = "planilha_gastos.xlsx"


def salvar_no_excel(item, valor):
    # Captura a data atual automaticamente
    data_atual = datetime.now().strftime("%d/%m/%Y")

    novos_dados = {"Data": [data_atual], "Item": [item], "Valor (R$)": [valor]}
    df_novo = pd.DataFrame(novos_dados)

    # Se o arquivo já existir, adiciona a linha. Se não, cria um novo.
    if os.path.exists(NOME_ARQUIVO):
        df_antigo = pd.read_excel(NOME_ARQUIVO)
        df_final = pd.concat([df_antigo, df_novo], ignore_index=True)
    else:
        df_final = df_novo

    # Salva no arquivo Excel
    df_final.to_excel(NOME_ARQUIVO, index=False)


@bot.message_handler(commands=["start", "ajuda"])
def enviar_boas_vindas(message):
    texto = (
        "Olá! Eu sou seu assistente de gastos.\n\n"
        "Para registrar uma compra, envie no formato:\n"
        "**Item - Valor**\n\n"
        "Exemplo: `Supermercado - 150.50`\n"
        "Exemplo: `Gasolina - 80`"
    )
    bot.reply_to(message, texto, parse_mode="Markdown")


@bot.message_handler(func=lambda message: True)
def processar_gasto(message):
    try:
        # Divide a mensagem usando o traço "-" como separador
        texto = message.text
        if "-" not in texto:
            bot.reply_to(
                message, "Formato incorreto. Use: **Item - Valor**", parse_mode="Markdown"
            )
            return

        partes = texto.split("-")
        item = partes[0].strip()
        # Substitui vírgula por ponto para evitar erros em números decimais
        valor_texto = partes[1].strip().replace(",", ".")
        valor = float(valor_texto)

        # Salva na planilha
        salvar_no_excel(item, valor)

        bot.reply_to(
            message, f"✅ Registrado!\n📌 {item}\n💰 R$ {valor:.2f}"
        )

    except ValueError:
        bot.reply_to(
            message,
            "Erro no valor. Certifique-se de usar apenas números (Ex: 15.50).",
        )
    except Exception as e:
        bot.reply_to(message, "Ocorreu um erro ao processar sua mensagem.")


# Mantém o bot rodando
print("Bot de gastos iniciado...")
bot.infinity_polling()