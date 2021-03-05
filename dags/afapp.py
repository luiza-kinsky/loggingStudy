import logging
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

#O objeto DAG irá guardar as tasks
dag = DAG(
    'afapp',
    default_args=default_args,
    description='Demonstrando logs em forma humana e de máquina',
    schedule_interval=timedelta(days=1),
    start_date=days_ago(2),
    tags=['example'],
)

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


def collect(primeiro_nome, segundo_nome, debug=False, retries=5):
    try:
        return True, add(primeiro_nome, segundo_nome)
    except Exception:
        if retries > 0:
            return collect(primeiro_nome, segundo_nome, debug, retries - 1)
        return False, []

def print_context():
    primeiro_nome = "Luiza"
    segundo_nome = "Kinsky"
    
    data = collect(primeiro_nome, segundo_nome)
    print(data)

    return True


run_this = PythonOperator(
    task_id='print_the_context',
    python_callable=print_context,
    dag=dag,
)

#add('Luiza', 'Kinsky')
#add('Luiza', True)