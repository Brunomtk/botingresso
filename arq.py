import webbrowser
import time
import pygame
import chromedriver_autoinstaller

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from datetime import datetime

# Instala automaticamente o ChromeDriver compatível
chromedriver_autoinstaller.install()

# Caminho do áudio (corrigido com raw string e extensão)
audio = r"C:\Users\bruno\Downloads\arq\arq\audio\AUD-20211005-WA0108.mp3"

# URL da página a ser monitorada
url = "https://www.ingressolive.com/2806-arq-da-agrarias-60326"

# Configurações do Chrome
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Opcional: rodar em segundo plano
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Inicializa o Pygame para tocar o áudio
pygame.mixer.init()

def verificar_ingressos():
    # Inicia o navegador com as opções configuradas
    driver = webdriver.Chrome(service=Service(), options=chrome_options)
    driver.get(url)

    try:
        while True:
            try:
                # Tenta encontrar o botão de compra
                botao_compra = driver.find_element(By.CLASS_NAME, "ingresso-quantidade")

                # Se encontrou, significa que há ingressos
                print("🎉 Ingressos disponíveis!")
                pygame.mixer.music.load(audio)
                pygame.mixer.music.play()
                webbrowser.open(url)

                time.sleep(30)  # Tempo de aviso
                pygame.mixer.music.stop()
                break

            except Exception:
                print(f"[{datetime.now().strftime('%H:%M:%S')}] Ingressos esgotados, recarregando...")
                time.sleep(10)
                driver.refresh()

    except KeyboardInterrupt:
        print("❌ Execução interrompida pelo usuário.")

    finally:
        driver.quit()

if __name__ == "__main__":
    verificar_ingressos()
