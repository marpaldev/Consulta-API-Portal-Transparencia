import logging
from ControladorAplicacao import ControladorAplicacao


def log_init():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%d-%b-%y %H:%M:%S",
        filename="logfile.log",
    )
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.getLogger("requests").setLevel(logging.WARNING)

if __name__ == "__main__":
    log_init()
    api_key = ControladorAplicacao.obterChaveApi()
    app = ControladorAplicacao(api_key, "cpfs.csv", "dados.csv")
    app.executar()
    logger = logging.getLogger(__name__)
    logger.info("Programa finalizado com sucesso!")
