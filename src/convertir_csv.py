from pathlib import Path
import pandas as pd

# Rutas del proyecto
ROOT = Path(__file__).resolve().parent.parent

RAW_FOLDER = ROOT / "data" / "raw"
INTERIM_FOLDER = ROOT / "data" / "interim"
INTERIM_FOLDER.mkdir(parents=True, exist_ok=True)

# Buscar todos los archivos .xls
archivos = list(RAW_FOLDER.glob("*.xls"))

if len(archivos) == 0:
    print("No se encontraron archivos .xls en data/raw")
    exit()
print(f"Se encontraron {len(archivos)} archivos.\n")

for archivo in archivos:
    print(f"Convirtiendo {archivo.name}...")
    try:
        df = pd.read_excel(archivo)
        nombre_csv = archivo.stem + ".csv"
        salida = INTERIM_FOLDER / nombre_csv
        df.to_csv(
            salida,
            index=False,
            encoding="utf-8-sig"
        )
        print(f"{nombre_csv} creado correctamente.\n")
    except Exception as e:
        print(f"Error con {archivo.name}")
        print(e)
        print()
print("Conversión finalizada.")