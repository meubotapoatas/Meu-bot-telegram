# 🤖 Bot de Palpites no Telegram

Bot de Telegram que envia palpites de futebol usando **The Odds API** com odds mínimas de 1.8, pré-match + in-play.

## 🚀 Como rodar no Render

1. Crie um novo Web Service no [Render](https://render.com/).
2. Conecte seu repositório GitHub.
3. Em "Environment Variables", adicione:
   - `BOT_TOKEN` → Token do seu bot no Telegram.
   - `ODDS_API_KEY` → Chave da The Odds API.
   - `TELEGRAM_CHAT_ID` → ID do seu chat no Telegram.
4. Deploy e pronto.

Comando para iniciar no Render:
