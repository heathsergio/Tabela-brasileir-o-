import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

# URL MODELO do Globo Esporte (GE) para a Tabela do Brasileirão
# Esta URL deve ser ajustada para a temporada de 2025 quando o campeonato começar.
DATA_SOURCE_URL = "https://ge.globo.com/futebol/brasileirao-serie-a/"
OUTPUT_FILE = "data.json"

def get_brasileirao_data():
    """
    Tenta coletar dados da tabela e artilharia do Brasileirão 2025 usando o GE como modelo.
    
    NOTA: Como o Brasileirão 2025 não começou, os dados reais serão simulados.
    A lógica de raspagem está comentada, mas serve como modelo para quando a URL
    de 2025 estiver no ar.
    """
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Tentando coletar dados...")
    
    tabela = []
    artilharia = []

    try:
        # -----------------------------------------------------------------
        # Lógica de Raspagem (Modelo para 2025)
        # -----------------------------------------------------------------
        # response = requests.get(DATA_SOURCE_URL)
        # response.raise_for_status()
        # soup = BeautifulSoup(response.content, 'html.parser')
        
        # # Exemplo de como seria a raspagem da tabela (pode variar)
        # tabela_html = soup.find('table', class_='tabela__body')
        # if tabela_html:
        #     for i, linha in enumerate(tabela_html.find_all('tr')):
        #         colunas = linha.find_all('td')
        #         if len(colunas) > 8:
        #             tabela.append({
        #                 "pos": i + 1,
        #                 "time": colunas[1].text.strip(),
        #                 "pts": int(colunas[2].text.strip()),
        #                 # ... (continuar extraindo as outras colunas)
        #             })
            
        # # Exemplo de como seria a raspagem da artilharia (pode variar)
        # # ...
        # -----------------------------------------------------------------
        
        # Dados simulados para desenvolvimento e teste (serão substituídos pela raspagem em 2025)
        tabela = [
            {"pos": 1, "time": "Flamengo", "pts": 75, "jogos": 38, "v": 22, "e": 9, "d": 7, "gp": 65, "gc": 35},
            {"pos": 2, "time": "Palmeiras", "pts": 70, "jogos": 38, "v": 20, "e": 10, "d": 8, "gp": 60, "gc": 30},
            {"pos": 3, "time": "Atlético-MG", "pts": 68, "jogos": 38, "v": 19, "e": 11, "d": 8, "gp": 55, "gc": 32},
            {"pos": 4, "time": "Botafogo", "pts": 65, "jogos": 38, "v": 18, "e": 11, "d": 9, "gp": 58, "gc": 40},
            {"pos": 17, "time": "Vasco da Gama", "pts": 45, "jogos": 38, "v": 12, "e": 9, "d": 17, "gp": 40, "gc": 55},
        ]
        
        artilharia = [
            {"pos": 1, "jogador": "Gabigol", "time": "Flamengo", "gols": 25},
            {"pos": 2, "jogador": "Hulk", "time": "Atlético-MG", "gols": 20},
            {"pos": 3, "jogador": "Tiquinho Soares", "time": "Botafogo", "gols": 18},
        ]
        
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a fonte de dados: {e}")
        return None, None
        
    return tabela, artilharia

def save_data(tabela, artilharia):
    """
    Salva os dados coletados em um arquivo JSON.
    """
    if not tabela or not artilharia:
        print("Dados inválidos, abortando salvamento.")
        return

    data = {
        "tabela": tabela,
        "artilharia": artilharia,
        "ultima_atualizacao": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }

    try:
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Dados salvos com sucesso em {OUTPUT_FILE}")
    except IOError as e:
        print(f"Erro ao salvar o arquivo JSON: {e}")

if __name__ == "__main__":
    tabela_data, artilharia_data = get_brasileirao_data()
    save_data(tabela_data, artilharia_data)

