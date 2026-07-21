from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent.parent

CARPETA_ENTRADA = ROOT / "data" / "interim"
CARPETA_SALIDA = ROOT / "data" / "interim_departamentos"
CARPETA_SALIDA.mkdir(parents=True, exist_ok=True)

departamentos = sorted({
    archivo.stem.rsplit("_", 1)[0]
    for archivo in CARPETA_ENTRADA.glob("*.csv")
})

print(f"Departamentos encontrados: {len(departamentos)}\n")

for departamento in departamentos:

    print(f"Uniendo {departamento}...")

    archivos = sorted(
        CARPETA_ENTRADA.glob(f"{departamento}_*.csv")
    )

    dfs = []

    for archivo in archivos:

        df = pd.read_csv(archivo)
        df = df.loc[:, ~df.columns.astype(str).str.contains("^Unnamed")]
        df = df.dropna(how="all")

        dfs.append(df)

    if not dfs:
        continue

    df_final = pd.concat(
        dfs,
        ignore_index=True
    )
    if "CODIGO" in df_final.columns:
        df_final = df_final.drop_duplicates(
            subset="CODIGO"
        )

    salida = CARPETA_SALIDA / f"{departamento}.csv"

    df_final.to_csv(
        salida,
        index=False,
        encoding="utf-8-sig"
    )
    print(f"   {len(df_final):,} registros")

print("\nDepartamentos agrupados correctamente.")