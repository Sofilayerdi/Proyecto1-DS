import pandas as pd
from pathlib import Path

ruta = Path("../data/raw")
dfs = []

for archivo in ruta.glob("*.xls"):
    df = pd.read_excel(archivo)
    df["departamento"] = archivo.stem
    dfs.append(df)

datos = pd.concat(dfs, ignore_index=True)
datos.to_csv(
    "../data/interim/establecimientos_unidos.csv",
    index=False
)
print(datos.shape)