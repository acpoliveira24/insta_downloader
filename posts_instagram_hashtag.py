import instaloader


# Carrega a biblioteca
L = instaloader.Instaloader()

# Faz o download dos 10 útlimos posts com a hashtag selfie
L.download_hashtag(hashtag="selfie", max_count=10)
