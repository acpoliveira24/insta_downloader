from datetime import datetime
import instaloader


# Carrega a biblioteca e seleciona uma conta para baixar os posts
L = instaloader.Instaloader()
posts = instaloader.Profile.from_username(L.context, "instagram").get_posts()

# Define o intervalo da data
desde = datetime(2021, 4, 1)
ate = datetime(2021, 6, 30)

# Seleciona os posts dentro da data definida e faz o download na pasta criada posts-instagram
for post in posts:
    if (post.date >= desde) and (post.date <= ate):
        print(post.date)
        L.download_post(post, "posts-instagram")
