# :camera_flash: ​Download de posts do Instagram 

Código em Python para fazer download de posts do Instagram (fotos, vídeos e metadatas) com a biblioteca `instaloader`.

São dois códigos. O `posts_instagram_data` é para fazer o download de posts de uma conta específica (pública) dentro de um intervalo de tempo especificado pelo usuário. O `posts_instagram_hashtag.py` é para fazer o download dos últimos posts públicos com uma determinada hashtag. O número de posts baixados é definido pelo usuário.

Ao fazer o download de posts, serão baixados fotos/vídeos, além de um arquivo de texto com a legenda do post e um arquivo `.json` com dados do post.

## Instruções

Primeiro é necessário instalar a biblioteca através de: `pip install instaloader`. Escolha um dos arquivos `.py` e abra.

### Para `posts_instagram_data`

Na linha `posts = instaloader.Profile.from_username(L.context, "instagram").get_posts()`, substitua `instagram` pela conta que deseja baixar os posts.

:rotating_light: A conta usada deve ser pública!

Troque os valores das variáveis `desde` e `ate` para as datas do intervalo desejado, onde `desde` é a data inicial e `ate` é a data final. O formato da data é ano, mês, dia (aaaa, mm, dd).

Na linha `L.download_post(post, "posts-instagram")`, substitua `posts-instagram` pelo nome que desejar para a pasta onde serão salvos os posts.

Agora é só rodar o código e esperar os downloads serem feitos

### Para `posts_instagram_hashtag`

As únicas alterações a serem feitas é na linha `L.download_hashtag(hashtag="selfie", max_count=10)` onde `selfie` pode ser substuído pela hashtag desejada e o valor de `max_count` pode ser trocado para o valor da quantidade de posts a serem baixados.

Após isso, é só rodar o código e os downloads serão feitos. Os posts serão salvos em uma pasta com o nome da hashtag escolhida.



# :envelope: Enviar mensagens pelo Instagram

Código em Python que faz login em uma conta e envia mensagens para outra através da biblioteca `instabot`.

## Instruções

Instale a biblioteca através de  `pip install instabot`. Abra o arquivo `instagram_send_message`. Em `username` e `password`, coloque o nome de usuário e senha da conta que vai enviar a mensagem. Substitua `Escreva a mensagem` pela mensagem a ser enviada, e `profile_name de destino` pelo nome de usuário de quem vai receber a mensagem. Em seguida, é só rodar o código e acompanhar as mensagens de logs para ver se a mensagem foi enviada.