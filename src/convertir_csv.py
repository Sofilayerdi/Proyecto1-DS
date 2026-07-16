from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent

RAW_FOLDER = ROOT / "data" / "raw"
INTERIM_FOLDER = ROOT / "data" / "interim"
INTERIM_FOLDER.mkdir(parents=True, exist_ok=True)

archivos = list(RAW_FOLDER.glob("*.xls"))

if not archivos:
    print("No se encontraron archivos .xls en data/raw")
    raise SystemExit

print(f"Se encontraron {len(archivos)} archivos.\n")

# Columnas que identifican la tabla de establecimientos
COLUMNAS_ESPERADAS = {"CODIGO", "DISTRITO", "DEPARTAMENTO", "MUNICIPIO", "ESTABLECIMIENTO"}

for archivo in archivos:
    print(f"Convirtiendo {archivo.name}...")
    try:
        # encoding='windows-1252' evita que se corrompan tildes y ñ
        tablas = pd.read_html(archivo, encoding="windows-1252")

        df_correcto = None
        for t in tablas:
            columnas = {str(c).strip().upper() for c in t.columns}
            if COLUMNAS_ESPERADAS.issubset(columnas):
                df_correcto = t
                break

        if df_correcto is None:
            # Respaldo: la tabla con más celdas (filas x columnas)
            df_correcto = max(tablas, key=lambda t: t.shape[0] * t.shape[1])

        # Quitar filas completamente vacías (la fila de "relleno" final)
        df_correcto = df_correcto.dropna(how="all")

        nombre_csv = archivo.stem + ".csv"
        salida = INTERIM_FOLDER / nombre_csv
        df_correcto.to_csv(salida, index=False, encoding="utf-8-sig")
        print(f"{nombre_csv} creado correctamente. ({len(df_correcto)} filas)\n")

    except Exception as e:
        print(f"Error con {archivo.name}")
        print(e)
        print()

print("Conversión finalizada.")