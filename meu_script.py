from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import time

# Configurações
API_KEY = 'SUA_API_KEY'  # Substitua com sua chave de API
SEARCH_QUERY = 'musica '  # Pode ser qualquer tipo de música ou artista
BASE_URL = 'https://www.googleapis.com/youtube/v3/search'

# Função para buscar vídeos usando a API do YouTube
def buscar_videos(query):
    params = {
        'part': 'snippet',
        'q': query,
        'key': API_KEY,
        'maxResults': 5,
        'type': 'video'  # Garantir que apenas vídeos sejam retornados
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erro ao buscar vídeos: {response.status_code}")
        return {}

# Função principal
def main():
    # Busca vídeos
    resultados = buscar_videos(SEARCH_QUERY)
    
    if 'items' in resultados:
        # Imprime os títulos e URLs dos vídeos encontrados
        for item in resultados['items']:
            video_title = item['snippet']['title']
            video_id = item['id']['videoId']
            print(f'Título: {video_title}')
            print(f'URL: https://www.youtube.com/watch?v={video_id}')
            print()
    else:
        print("Deu certo")
    
    # Inicia o WebDriver
    driver = webdriver.Chrome()  # ou use outro navegador, se preferir
    driver.get('https://www.youtube.com')

    # Localiza a barra de pesquisa e envia a consulta
    search_box = driver.find_element(By.NAME, 'search_query')
    search_box.send_keys(SEARCH_QUERY)  # Digita o termo de busca
    search_box.send_keys(Keys.RETURN)  # Pressiona "Enter"

    # Aguarda os resultados carregarem
    time.sleep(5)  # Aguarda 5 segundos (ajuste conforme necessário)
    

    # Aguarda um pouco antes de fechar
    input("Pressione Enter para fechar...")
    driver.quit()

if __name__ == '__main__':
    main()
