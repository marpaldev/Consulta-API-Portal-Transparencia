import pandas as pd
import logging
from typing import Optional


class LeitorCSV:
    def __init__(self, csv_file, logger: Optional[logging.Logger] = None):
        self.logger = logger or logging.getLogger(__name__)
        self.csv_file = csv_file

    def ler(self):
        self.logger.debug("Lendo arquivo CSV...")
        df = pd.read_csv(self.csv_file)
        if 'cpfs' not in df.columns:
            raise ValueError(f"Coluna 'cpfs' não encontrada em {self.csv_file}.")
        lista_cpfs = df['cpfs'].astype(str).tolist()
        lista_cpfs = sorted(set(lista_cpfs))
        return lista_cpfs
