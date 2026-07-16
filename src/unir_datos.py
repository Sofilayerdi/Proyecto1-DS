from pathlib import Path
import pandas as pd

CARPETA = Path("data/interim")
SALIDA = Path("data/processed")
SALIDA.mkdir(exist_ok=True)

archivos = sorted(CARPETA.glob("*.csv"))
dfs = []

for archivo in archivos:
    print(f"Leyendo {archivo.name}")
    dfs.append(pd.read_csv(archivo))
df = pd.concat(
    dfs,
    ignore_index=True
)

print(f"\nTotal de registros: {len(df):,}")

df.to_csv(
    SALIDA / "centros_educativos_gt.csv",
    index=False,
    encoding="utf-8-sig"
)

print("Archivo final creado.")