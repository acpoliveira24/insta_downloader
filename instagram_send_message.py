from instabot import Bot


bot = Bot()

bot.login(username="profile_name", password="password")
bot.send_message("Escreva a mensagem", ["profile_name de destino"])
