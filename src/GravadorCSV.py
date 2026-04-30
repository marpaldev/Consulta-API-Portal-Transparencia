import pandas as pd
import os
import logging

from typing import Optional


class GravadorCSV:
    def __init__(self, csv_saida, logger: Optional[logging.Logger] = None):
        self.csv_saida = csv_saida
        self.logger = logger or logging.getLogger(__name__)

    def gravar(self, dados):
        registro = [dados] if isinstance(dados, dict) else dados
        df = pd.DataFrame(registro)
        arquivo_existe = os.path.exists(self.csv_saida)
        if arquivo_existe:
            self.logger.debug(
                f"Reescrevendo {self.csv_saida}"
            )
            df.to_csv(self.csv_saida, index=False, header=False, encoding="utf-8", mode="a")
        else:
            self.logger.debug(
                f"Criando o arquivo de saída... {self.csv_saida}"
            )
            df.to_csv(self.csv_saida, index=False, encoding="utf-8", mode="w")
            self.logger.info(
                f"O arquivo {self.csv_saida} criado com sucesso."
            )
