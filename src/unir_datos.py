from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
CARPETA = ROOT / "data" / "interim_departamentos"
SALIDA = ROOT / "data" / "processed"
SALIDA.mkdir(parents=True, exist_ok=True)

archivos = sorted(
    CARPETA.glob("*.csv")
)

print(f"Departamentos encontrados: {len(archivos)}\n")

dfs = []

for archivo in archivos:
    print(f"Leyendo {archivo.name}")
    df = pd.read_csv(archivo)
    df = df.loc[:, ~df.columns.astype(str).str.contains("^Unnamed")]
    df = df.dropna(how="all")
    dfs.append(df)

df_final = pd.concat(
    dfs,
    ignore_index=True
)

if "CODIGO" in df_final.columns:
    df_final = df_final.drop_duplicates(
        subset="CODIGO"
    )

print(f"\nTotal de registros: {len(df_final):,}")

df_final.to_csv(
    SALIDA / "centros_educativos_gt.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nArchivo final creado correctamente.")