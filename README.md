# loggingStudy

## Gerando logs com Python
1. Criar uma página para armazenar o código;
2. Criar um arquivo .py (nesse caso coloquei app.py).

### Iniciando o código
- Importar o módulo logging:
```
import logging
```
- Definir a formatação do log:
```
'''
   A formatação abaixo permite personalizar
   a forma como o log será mostrado
'''
# DateTime:Level:Arquivo:Mensagem
log_format = '%(asctime)s:%(levelname)s:%(filename)s:%(message)s'
```
- Definir as configurações do log e sua instância:
```
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
```
O módulo contém varios tipos de niveis de mensagens. São elas:
|__Level__ |__Numeric Level__|
|----------|-----------------|
|  CRITICAL|       50        |
|  ERROR   |       40        |
|  WARNING |       30        |
|  INFO    |       20        |
|  DEBUG   |       10        |
|  NOTSET  |       0         |
Até aqui, as configurações do log já foram definidas.
### Colocar em prática
- Fazer uma função que receba o primeiro_nome e o segundo_nome de uma pessoa e retorne o log no nosso arquivo exemplo.log (definido acima):
```
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
```
### Resultado
O retorno desse código ficará dentro do arquivo exemplo.log no mesmo caminho do arquivo app.py e terá a seguinte forma:
```

```