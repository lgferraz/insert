# Insert

Script para gerar código de tabelas temporárias, com base em dados já existentes, do SQL Server
## Arquivo *cod_assc.txt*
No arquivo *cod_assc.txt* você irá inserir tanto os parâmetros para gerar os inserts, quanto os próprios dados da tabela, separados pelo identificador *####*

## Parâmetros da tabela
Dentro do *cod_assc.txt* haverá os seguintes parâmetros a serem preenchidos
**nometxt:** referente ao nome do arquivo final com os inserts
**nometabela:** referente ao nome da tabela dos inserts (pode ser temp ou não)
**campos:** referente ao nome dos campos dos inserts da tabela
**tipos:** referente ao tipo de dado de cada campo na tabela, e deve ser preenchido de forma respectiva à ordem dos campos
### A área de parâmetros deve ser algo assim:

    nometxt:exemplo.txt
    nometabela:#tabelaexemplo
    campos:campo1, campo2, etc
    tipos:INT, INT, INT
    ####


## Preenchendo com campos
Os campos (informações a serem inseridas com insert) devem ser colocados no arquivo após  "*####*", separando as colunas por *tab* de forma respectiva à ordem dos nomes dos campos

# ⚠️ Alertas
*🚨Apagar espaços em branco entre (no inicio e no final) os campos a serem inseridos*

*🚨No último insert o último campo terminará com ",", lembrar de trocar essa vírgula por ponto e vírgula ";"*
