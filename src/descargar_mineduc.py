from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time
from config import *
from utils import *

options = webdriver.ChromeOptions()

prefs = {
    "download.default_directory": DOWNLOAD_FOLDER,
    "download.prompt_for_download": False,
    "download.directory_upgrade": True
}

options.add_experimental_option("prefs", prefs)
options.add_argument("--headless=new")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

wait = WebDriverWait(driver, 20)

NIVELES = {
    "45": "basico",
    "46": "diversificado",
    "42": "parvulos",
    "41": "preprimaria_bilingue",
    "43": "primaria",
    "44": "primaria_adultos"
}

for codigo_dep, nombre_dep in DEPARTAMENTOS.items():
    print(nombre_dep.upper())

    for codigo_nivel, nombre_nivel in NIVELES.items():
        print(f"Nivel: {nombre_nivel}")
        driver.get(URL)
        try:
            Select(
                wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.ID,
                            "_ctl0_ContentPlaceHolder1_cmbDepartamento"
                        )
                    )
                )
            ).select_by_value(codigo_dep)

            time.sleep(2)
            wait.until(
                EC.presence_of_element_located(
                    (
                        By.ID,
                        "_ctl0_ContentPlaceHolder1_cmbMunicipio"
                    )
                )
            )

            Select(
                wait.until(
                    EC.element_to_be_clickable(
                        (
                            By.ID,
                            "_ctl0_ContentPlaceHolder1_cmbNivel"
                        )
                    )
                )
            ).select_by_value(codigo_nivel)

            driver.find_element(
                By.ID,
                "_ctl0_ContentPlaceHolder1_IbtnConsultar"
            ).click()

            # Esperar Exportar (máximo 5 segundos)
            exportar = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable(
                    (
                        By.ID,
                        "_ctl0_ContentPlaceHolder1_btnExportar"
                    )
                )
            )

            exportar.click()
            archivo = esperar_descarga(DOWNLOAD_FOLDER)
            renombrar_archivo(
                archivo,
                f"{nombre_dep}_{nombre_nivel}.xls"
            )
            print("   ✓ Descargado")
        except TimeoutException:
            print("   ⚠ Sin establecimientos")
        except Exception as e:
            print(f"   ✗ Error: {e}")

driver.quit()

print("\nProceso terminado.")