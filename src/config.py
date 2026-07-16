from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_RAW = BASE_DIR / "data" / "raw"
DOWNLOAD_FOLDER = str(DATA_RAW)
URL = "http://www.mineduc.gob.gt/BUSCAESTABLECIMIENTO_GE/"


DEPARTAMENTOS = {
    "16": "alta_verapaz",
    "15": "baja_verapaz",
    "04": "chimaltenango",
    "20": "chiquimula",
    "00": "ciudad_capital",
    "02": "el_progreso",
    "05": "escuintla",
    "01": "guatemala",
    "13": "huehuetenango",
    "18": "izabal",
    "21": "jalapa",
    "22": "jutiapa",
    "17": "peten",
    "09": "quetzaltenango",
    "14": "quiche",
    "11": "retalhuleu",
    "03": "sacatepequez",
    "12": "san_marcos",
    "06": "santa_rosa",
    "07": "solola",
    "10": "suchitepequez",
    "08": "totonicapan",
    "19": "zacapa"
}