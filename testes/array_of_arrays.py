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

# obj.elementos {key: value, key: value}
# obj.elementos = [1, 2, 4]

# estrutura =
# [
#     {tamanho: 3, arrays: ['124', "412"], elementos: '124'}, 
#     
# ]
#  i = 1

class Elemento:
    def __init__(self, item):
        self.tamanho = len(item)
        self.arrays = [item]
        #self.elementos = item
        
    @property
    def componentes(self):
        return self.arrays[0]


# O (n^2 * z^2)
def verificar_agrupamentos(lista):
    estrutura = []
    
    if (len(lista) == 0):
        return estrutura

    #inicializa o primeiro elemento
    estrutura.append(Elemento(lista[0]))
    
    #percorre restante da lista passada exceto o primeiro
    # i = 2
    # j = 0
    for i in range(1,len(lista)):
        j = grupo_existente(estrutura,lista[i])
        if (j != False):
            estrutura[j].arrays.append(lista[i])
        else:
            estrutura.append(Elemento(lista[i]))
            
    #limpa estrutura
    retorno = []
    for item in estrutura:
        retorno.append(item.arrays)
    
    return retorno

def grupo_existente(superarray,item):
    for k in range(len(superarray)):
        if (superarray[k].tamanho == len(item)):
            if (mesmo_elementos(superarray[k].componentes, item)):
                return k
        
    return False
    
# elementos = 124
# item = 412
# [True, True, True]
def mesmo_elementos(elementos, item):
    verificado = [False]*len(item)
    i = 0
    # i = 3
    # c = 2
    for c in item: # 112 x 221 => 
        # e = 2
        for e in elementos:
            if (e == c):
                verificado[i]=True
                break
        i += 1
        
    for achou in verificado:
        if not achou: 
            return False
    
    return True


resultado = verificar_agrupamentos(["124", "412", "ab9", "241", "9ba", "abc", "2141"])

print(resultado)
