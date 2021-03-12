import logging
from pythonjsonlogger import jsonlogger

# Função que determina o json
def setup_logging(log_level, log_format):
    logger = logging.getLogger()
    logger.setLevel(log_level)
    logHandler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter(log_format)
    logHandler.setFormatter(formatter)
    logger.addHandler(logHandler)

'''
   A formatação abaixo permite personalizar
   a forma como o log será mostrado
'''
# DateTime:Level:Arquivo:Mensagem
log_format = '%(asctime)s:%(levelname)s:%(filename)s:%(message)s'
log_level = logging.DEBUG
setup_logging(log_level, log_format)
'''
   Aqui as configurações do modulo são definidas

   filename = 'nome do arquivo em que ficará salvar a mensagem do log.'
   filemode = 'a forma em que o arquivo será gravado.'
   level = 'level em que o log atuará'
   format = 'formatação da mensagem do log'
'''
logging.basicConfig(filename='soma.log',
                    # w -> sobrescreve o arquivo a cada log
                    # a -> não sobrescreve o arquivo
                    filemode='w',
                    level=logging.DEBUG,
                    format=log_format)

'''
   O objeto getLogger() permite o retorno de
   varias instancias de logs.
'''
# Instancia do objeto getLogger()
logger = logging.getLogger('root')

def add(x, y):
    """
        Essa função recebe o primeiro nome e o segundo nome de uma pessoa e retorna o nome completo dela
    """
    if isinstance(x, int) and isinstance(y, int):
        soma = x+y
        logger.info(soma)
        #self.logger.info(x,y)
        return x + y
    else:
        logger.error(
            f'{x} type: {type(x)} - {y} type: {type(y)}'
        )

add(5, 10)
add('Luiza', True)