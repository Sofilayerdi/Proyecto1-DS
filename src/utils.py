import shutil
import time
from pathlib import Path

def esperar_descarga(carpeta, timeout=60):
    carpeta = Path(carpeta)
    inicio = time.time()
    while time.time() - inicio < timeout:
        archivo = carpeta / "establecimiento.xls"
        if archivo.exists():
            return archivo
        time.sleep(1)
    raise TimeoutError("No terminó la descarga.")


def renombrar_archivo(origen, nuevo_nombre):
    destino = origen.parent / nuevo_nombre
    if destino.exists():
        destino.unlink()
    shutil.move(origen, destino)
    return destino