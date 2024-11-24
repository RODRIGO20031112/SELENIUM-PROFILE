import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
import time

# Caminho do diretório de dados do usuário e perfil
user_data_dir = "C:/Users/USER/AppData/Local/Google/Chrome/User Data"
profile_directory = "Profile 1"

# Configurar as opções do Chrome
chrome_options = Options()
chrome_options.add_argument(f"user-data-dir={user_data_dir}")  # Diretório de dados do usuário
chrome_options.add_argument(f"profile-directory={profile_directory}")  # Nome do perfil
chrome_options.add_argument("--no-sandbox")  # Outra opção para melhorar a compatibilidade
chrome_options.add_argument("--disable-dev-shm-usage")  # Evita problemas com o Docker (se aplicável)

# Inicializar o driver com undetected-chromedriver
driver = uc.Chrome(options=chrome_options)

# Abra uma página para testar
driver.get("https://www.google.com")

# Espera por 5 segundos
time.sleep(5)

# Depois de 5 segundos, navega para o outro site
driver.get("https://piratenation.game/")

time.sleep(1000)

# O navegador será aberto com o perfil específico
