'''
assc = str(open("cod_assc.txt", "r").read())
listac = assc.split('\n')
with open("Chat.txt", 'w') as file:
    file.write('\nINSERT INTO #TEMP VALUES ')
    for i in listac:
        if (listac.index(i))%50 == 0:
            file.write('\n')
        elif (listac.index(i))%500 == 0:
            file.write(';\n\nINSERT INTO #TEMP VALUES '+'('+i+'),')
        else:
            file.write('('+i+'),')

print('pronto')
file.close()
'''
'''
assc = str(open("cod_assc.txt", "r").read())

listac = assc.split('\n')

print(len(listac))

with open("base 116490.txt", 'w+') as file:
    file.write('\nINSERT INTO #TEMP VALUES ')
    for i in listac:
        if (listac.index(i)+1)%500 == 0:
            file.write(';\n\nINSERT INTO #TEMP VALUES '+'('+i+'),')
        elif (listac.index(i)+1)%50 == 0:
            file.write('\n')
            file.write('('+i+'),')
        else:
            file.write('('+i+'),')

print('pronto')
file.close()
'''


baseorig = "cod_assc.txt" #base de origem em txt
nometxt = "base resultado.txt" #base que será gerada
nometabela = "#NOME" #nome da base no sql
nomecampos = ["CAMPO1", "CAPO2", "..."] #colunas da base
tiposdados = "TIPOCAMPO1-TIPOCAMPO2-ETC" #tipo de dados de cada coluna


assc = str(open(baseorig, "r").read())
listac = assc.split('\n')
qtdlinhas = str(len(listac))

def createtable(nometabela, campos, tipos):
    tipos = tipos.split('-')
    create = "CREATE TABLE "+nometabela+" ("
    for campo in campos:
        indexcampo = campos.index(campo)
        if indexcampo != 0:
            create = create+', '+campo+' '+tipos[indexcampo]
        else:
            create = create+' '+campo+' '+tipos[indexcampo]
    return create+")"

def formatar(campos, tipos):
    tipos = tipos.split('-')
    campos = campos.split('\t')
    insert = '('
    for i in campos:
        indexcampo = campos.index(i)
        tipoi = tipos[indexcampo]
        if indexcampo != 0:
            if tipoi == 'INT':
                insert = insert+','+campos[indexcampo]
            if tipoi == 'DATE':
                insert = insert+", '"+campos[indexcampo]+"'"
        else:
            if tipoi == 'INT':
                insert = insert+campos[indexcampo]
            if tipoi == 'DATE':
                insert = insert+"'"+campos[indexcampo]+"'"
    insert = insert+")"
    return insert
                
print('aquivo origem: '+baseorig)
print('aquivo gerado: '+nometxt)
print('quantidade linhas: '+qtdlinhas)



with open(nometxt, 'w+') as file:
    file.write(createtable(nometabela, nomecampos, tiposdados))
    file.write('\n\nINSERT INTO '+nometabela+' VALUES ')
    print("processando...")
    for campo in listac:
        indexcampo = listac.index(campo)
        campos = formatar(campo, tiposdados)
        if (indexcampo+1)%500 == 0:
            file.write(';\n\nINSERT INTO #TEMP VALUES '+campos+',')
        elif (indexcampo+1)%50 == 0:
            file.write('\n')
            file.write(campos+',')
        else:
            file.write(campos+',')

print('pronto')
file.close()




