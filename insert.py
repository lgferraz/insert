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
import re


baseorig = "cod_assc.txt" #base de origem em txt ex: "cod_assc.txt"
orig = str(open(baseorig, "r").read()).split("####")

nometxt = re.search("nometxt:.+", orig[0]).group(0).split(":")[1] #base que será gerada ex: "base resultado.txt"
nometabela = re.search("nometabela:.+", orig[0]).group(0).split(":")[1] #nome da base no sql ex: "#NOME"
nomecampos = re.search("campos:.+", orig[0]).group(0).split(":")[1].replace(" ", "").split(",") #colunas da base ex: ["CAMPO1", "CAPO2", "..."]
tiposdados = re.search("tipos:.+", orig[0]).group(0).split(":")[1].replace(" ", "").split(",") #tipo de dados de cada coluna ex: "TIPOCAMPO1-TIPOCAMPO2-ETC"

assc = orig[1]
listac = assc.split('\n')
listac.pop(0)
qtdlinhas = str(len(listac))

def createtable(nometabela, campos, tipos):
    create = "CREATE TABLE "+nometabela+" ("
    for campo in campos:
        indexcampo = campos.index(campo)
        if indexcampo != 0:
            create = create+', '+campo+' '+tipos[indexcampo]
        else:
            create = create+' '+campo+' '+tipos[indexcampo]
    return create+")"

def formatar(campos, tipos):
    insert = '('
    campos = campos.split()
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

file.close()

final = str(open(nometxt, 'r').read()).replace(",;",";")
with open(nometxt, 'w+') as file:
        file.write(final)
file.close()
print('pronto')




