import logging

'''
   A formatação abaixo permite personalizar
   a forma como o log será mostrado
'''
# DateTime:Level:Arquivo:Mensagem
log_format = '%(asctime)s:%(levelname)s:%(filename)s:%(message)s'

'''
   Aqui as configurações do modulo são definidas

   filename = 'nome do arquivo em que ficará salvar a mensagem do log.'
   filemode = 'a forma em que o arquivo será gravado.'
   level = 'level em que o log atuará'
   format = 'formatação da mensagem do log'
'''
logging.basicConfig(filename='exemplo.log',
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

def add(primeiro_nome: str, segundo_nome: str) -> str:
    """
        Essa função recebe o primeiro nome e o segundo nome de uma pessoa e retorna o nome completo dela
    """

    # Aqui, é verificado se os parametros passados são do tipo string (str)
    if isinstance(primeiro_nome, str) and isinstance(segundo_nome, str):
        logger.info(f'{primeiro_nome} {segundo_nome}')
        return primeiro_nome + segundo_nome
    else:
        logger.error(
            f'{primeiro_nome} type: {type(primeiro_nome)} - {segundo_nome} type: {type(segundo_nome)}'
        )

add('Luiza', 'Kinsky')
add('Luiza', True)