from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pathlib import Path
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

wait = WebDriverWait(driver,20)
driver.get(URL)

for codigo, nombre in DEPARTAMENTOS.items():
    print(f"Descargando {nombre}...")
    print("Seleccionando departamento...")
    time.sleep(2)

    departamento = wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "_ctl0_ContentPlaceHolder1_cmbDepartamento"
            )
        )
    )
    Select(departamento).select_by_value(codigo)
    time.sleep(2)

    print("Esperando municipios...")

    wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "_ctl0_ContentPlaceHolder1_cmbMunicipio"
            )
        )
    )

    time.sleep(2)
    print("Seleccionando nivel...")
    Select(
        wait.until(
            EC.element_to_be_clickable(
                (
                    By.ID,
                    "_ctl0_ContentPlaceHolder1_cmbNivel"
                )
            )
        )
    ).select_by_value("46")

    print("Buscando...")

    driver.find_element(
        By.ID,
        "_ctl0_ContentPlaceHolder1_IbtnConsultar"
    ).click()

    print("Exportando...")

    wait.until(
        EC.presence_of_element_located(
            (
                By.ID,
                "_ctl0_ContentPlaceHolder1_btnExportar"
            )
        )
    )
    driver.find_element(
        By.ID,
        "_ctl0_ContentPlaceHolder1_btnExportar"
    ).click()
    archivo = esperar_descarga(DOWNLOAD_FOLDER)
    renombrar_archivo(
        archivo,
        f"{nombre}.xls"
    )
    driver.find_element(
        By.ID,
        "_ctl0_ContentPlaceHolder1_btnLimpiar"
    ).click()
driver.quit()