import logging
import sys

# Configuración del logger
logger = logging.getLogger("my_custom_logger")
logger.setLevel(logging.DEBUG)  # Captura logs desde DEBUG en adelante

# Formato de los logs
formatter = logging.Formatter(
    '%(levelname)s: ->  [%(filename)s:%(lineno)d] msg:" %(message)s " %(asctime)s',
    datefmt="%H:%M:%S"
)

# Configuración del handler para la consola
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Configuración opcional: Guardar logs en un archivo !!! Descomentar para usar

# file_handler = logging.FileHandler("app.log", encoding="utf-8")
# file_handler.setFormatter(formatter)
# logger.addHandler(file_handler)

# Evita duplicados de logs si se reinicia la configuración
logger.propagate = False
