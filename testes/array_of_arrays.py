# Given an array of string, group the strings that are composed 
# by the same character, returning an array of arrays.

#  For example, given:
#  ["124", "412", "ab9", "241", "9ba", "abc", "2141"],
#     ^      ^             ^
#  Return:
#     [
#      ["124","412","241"], 
#      ["ab9","9ba"],
#      ["abc"],
#      ["2141"]
#     ]


#classe para criar os agrupamentos
class Grupo:
    def __init__(self, item):
        self._tamanho = len(item)
        self.arrays = [item]
        self._componentes = sorted(item)
        
    @property
    def componentes(self):
        return self._componentes
    
    #verifica a igualdade entre os elementos do grupo e outra string
    def __eq__(self, palavra):
        if (len(palavra) != self._tamanho):
            return False
        palavra = sorted(palavra)
        #se as duas strings ordenadas forem iguais, fazem parte do mesmo grupo
        return self._componentes == palavra
    


# Complexidade O (n^2 * z^2)
def verificar_agrupamentos(lista):
    estrutura = []
    
    if (len(lista) == 0):
        return estrutura

    #inicializa o primeiro elemento
    estrutura.append(Grupo(lista[0]))
    
    #percorre restante da lista passada exceto o primeiro
    for i in range(1,len(lista)):
        j = grupo_existente(estrutura,lista[i])
        if (j != -1):
            #se encontrou o grupo, inclui no existente
            estrutura[j].arrays.append(lista[i])
        else:
            #caso contrário cria um novo grupo
            estrutura.append(Grupo(lista[i]))
            
    #limpa estrutura
    retorno = []
    for item in estrutura:
        retorno.append(item.arrays)
    
    return retorno

#retorna indice do grupo ou -1 se não encontrou
def grupo_existente(superarray,item):
    for k in range(len(superarray)):
        #verifica a igualdade do grupo e do novo item
        if (superarray[k] == item):
            return k
        
    return -1
    

#caso de teste expandido
resultado = verificar_agrupamentos(["124", "412", "ab9", "241", "9ba", "abc", "2141", '112', '221'])

print(resultado)
