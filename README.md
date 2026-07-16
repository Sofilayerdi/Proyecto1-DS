# Proyecto 1 - Data Science
## Extracción y procesamiento de datos de centros educativos del MINEDUC Guatemala

## Descripción

Este proyecto automatiza la obtención de información pública de los centros educativos autorizados por el Ministerio de Educación de Guatemala (MINEDUC). Debido a que el portal únicamente permite descargar la información por departamento, se desarrolló un proceso automatizado utilizando Selenium que realiza la descarga de todos los departamentos, convierte los archivos a formato CSV y posteriormente genera un único conjunto de datos listo para su análisis.

---

## Tecnologías utilizadas

- Python 3.11
- Selenium
- Pandas
- WebDriver Manager
- Google Chrome

---

## Flujo del proyecto

### 1. Descarga automática

El script `descargar_mineduc.py`:

- Abre el portal del MINEDUC mediante Selenium.
- Recorre automáticamente los 22 departamentos.
- Selecciona el nivel educativo correspondiente.
- Ejecuta la búsqueda.
- Descarga el archivo generado.
- Renombra automáticamente cada archivo con el nombre del departamento.

Los archivos descargados se almacenan en:

```
data/raw/
```

---

### 2. Conversión a CSV

Aunque los archivos descargados poseen extensión `.xls`, realmente contienen tablas HTML.

El script `convertir_csv.py`:

- Lee las tablas HTML utilizando Pandas.
- Extrae la información de cada departamento.
- Convierte los datos a formato CSV.
- Guarda un archivo por departamento.

Salida:

```
data/interim/
```

---

### 3. Unión de todos los departamentos

El script `unir_csv.py`:

- Lee todos los CSV individuales.
- Une la información mediante `pd.concat()`.
- Genera un único dataset nacional.

Salida:

```
data/processed/centros_educativos_gt.csv
```

---

## Ejecución

### Instalar dependencias

```bash
pip install -r requirements.txt
```

### Descargar los datos

```bash
python src/descargar_mineduc.py
```

### Convertir a CSV

```bash
python src/convertir_csv.py
```

### Generar el dataset final

```bash
python src/unir_csv.py
```

---