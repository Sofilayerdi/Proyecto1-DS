from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent

RAW_FOLDER = ROOT / "data" / "raw"
INTERIM_FOLDER = ROOT / "data" / "interim"
INTERIM_FOLDER.mkdir(parents=True, exist_ok=True)

COLUMNAS_ESPERADAS = {
    "CODIGO",
    "DISTRITO",
    "DEPARTAMENTO",
    "MUNICIPIO",
    "ESTABLECIMIENTO"
}

archivos = sorted(RAW_FOLDER.glob("*.xls"))

print(f"Se encontraron {len(archivos)} archivos.\n")

for archivo in archivos:
    print(f"Convirtiendo {archivo.name}...")
    try:
        tablas = pd.read_html(
            archivo,
            encoding="windows-1252"
        )
        df = None
        for tabla in tablas:
            columnas = {
                str(c).strip().upper()
                for c in tabla.columns
            }
            if COLUMNAS_ESPERADAS.issubset(columnas):
                df = tabla
                break
        if df is None:
            df = max(
                tablas,
                key=lambda t: t.shape[0] * t.shape[1]
            )
        df = df.dropna(how="all")
        salida = INTERIM_FOLDER / f"{archivo.stem}.csv"
        df.to_csv(
            salida,
            index=False,
            encoding="utf-8-sig"
        )
        print(f"✓ {salida.name} ({len(df)} filas)\n")

    except Exception as e:
        print(f"✗ Error con {archivo.name}")
        print(e)
        print()
print("Conversión finalizada.")