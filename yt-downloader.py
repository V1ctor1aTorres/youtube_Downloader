import youtube_dl
#Baixar vídeos do YouTube e de outros sites semelhantes

url = str(input('Digite a url do vídeo aqui: \n'))
#Cria um objeto YoutubeDL usando o gerenciador de contexto with
with youtube_dl.YoutubeDL() as ydl:
    #Usa o método download do objeto YoutubeDL para baixar o vídeo
    #A URL do vídeo é passada como uma lista [url]
    ydl.download([url])
