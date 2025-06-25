"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    suma= 0
    with open('data.csv') as archivo_csv: 
        lineas = archivo_csv.readlines() 
        for linea in lineas:
            columnas = linea.split('\t')
            suma_seg_col = int(columnas[1])
            suma += suma_seg_col
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    return suma


def pregunta_02():
    conteo = {}
    with open('data.csv') as archivo_csv: 
        lineas = archivo_csv.readlines()
        for linea in lineas:
            columnas = linea.split('\t')
            letra = columnas[0]
            if letra in conteo:
                conteo[letra]+= 1
            else:
                conteo[letra]=1
                    
    conteo_ordenado = dict(sorted(conteo.items()))
    lista = [(letra, cuenta) for letra, cuenta in conteo_ordenado.items()]


    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    
    return lista


def pregunta_03():
    suma = {}
    with open('data.csv') as archivo_csv: 
        lineas = archivo_csv.readlines()
        for linea in lineas:
            columnas = linea.split('\t')
            suma_seg_col = int(columnas[1])
            letra = columnas[0]
            if letra in suma:
                suma[letra] += suma_seg_col
            else:
                suma[letra]= suma_seg_col
                             
    suma_ordenada = dict(sorted(suma.items()))
    lista = [(letra, sumar) for letra, sumar in suma_ordenada.items()]

    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    return lista


def pregunta_04():
    conteo = {}
    with open('data.csv') as archivo_csv: 
        lineas = archivo_csv.readlines()
        for linea in lineas:
            columnas = linea.split('\t')
            fechas = columnas[2]
            mes = fechas[5:7]
            if mes in conteo:
                conteo[mes]+= 1
            else:
                conteo[mes]=1
                    
    conteo_ordenado = dict(sorted(conteo.items()))
    lista = [(mes, cuenta) for mes, cuenta in conteo_ordenado.items()]
  
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    return lista


def pregunta_05():
    maximo_minimo = {}
    with open('data.csv') as archivo_csv: 
        lineas = archivo_csv.readlines()
        for linea in lineas:
            columnas = linea.split('\t')
            letra = columnas[0]
            valor = int(columnas[1])
            if letra in maximo_minimo:
                maximo, minimo = maximo_minimo[letra]
                maximo = max(valor, maximo)
                minimo = min(valor, minimo)
                maximo_minimo[letra] = (maximo, minimo)
            else: 
                maximo_minimo[letra] = (valor, valor)
    
    maximo_minimo_ordenado = dict(sorted(maximo_minimo.items()))    
    lista = [(letra,maximo,minimo) for letra, (maximo,minimo) in maximo_minimo_ordenado.items()]

    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    return lista


def pregunta_06():
    max_min = {}
    with open('data.csv') as archivo_csv: 
        lineas = archivo_csv.readlines()
        for linea in lineas:
            columnas = linea.split('\t')
            dicc = columnas[4]
            items_dicc = dicc.split(',')
            for llave_valor in items_dicc:
                llave, valor_str = llave_valor.split(':')
                valor=int(valor_str)
                if llave in max_min:
                    minimo, maximo = max_min[llave]
                    maximo = max(valor, maximo)
                    minimo = min(valor, minimo)
                    max_min[llave]= (minimo, maximo)
                else: 
                    max_min[llave]= (valor, valor)
    
    max_min_ordenado = dict(sorted(max_min.items()))
    lista = [(llave,minimo,maximo) for llave, (minimo, maximo) in max_min_ordenado.items()]

    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    return lista 


def pregunta_07():
    dicc = {}
    with open('data.csv') as archivo_csv: 
        lineas = archivo_csv.readlines()
        for linea in lineas:
            columnas = linea.split('\t')
            valor = int(columnas[1])
            letra = columnas[0]
            if valor in dicc:
                dicc[valor].append(letra)
            else:
                dicc[valor]= [letra]
    
    dicc_ordenado = dict(sorted(dicc.items()))
    lista_final = [(valor,lista) for valor, lista in dicc_ordenado.items()]
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    return lista_final


def pregunta_08():
    dicc = {}
    with open('data.csv') as archivo_csv: 
        lineas = archivo_csv.readlines()
        for linea in lineas:
            columnas = linea.split('\t')
            valor = int(columnas[1])
            letra = columnas[0]
            if valor in dicc:
                dicc[valor].append(letra)
            else:
                dicc[valor]= [letra]
    
    dicc_ordenado = dict(sorted(dicc.items()))
    lista_final = [(valor,sorted(list(set(lista)))) for valor, lista in dicc_ordenado.items()]

    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    return lista_final


def pregunta_09():
    dicc_final = {}
    with open('data.csv') as archivo_csv: 
        lineas = archivo_csv.readlines()
        for linea in lineas:
            columnas = linea.split('\t')
            dicc = columnas[4]
            items = dicc.split(',')
            for item in items: 
                llave, valor_str = item.split(':')
                if llave in dicc_final:
                    dicc_final[llave]+=1
                else:
                    dicc_final[llave]=1
    dicc_final_ordenado = dict(sorted(dicc_final.items()))
            
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    return dicc_final_ordenado


def pregunta_10():
    conteo = []
    with open('data.csv') as archivo_csv: 
        lineas = archivo_csv.readlines()
        for linea in lineas:
            columnas = linea.split('\t')
            letra = columnas[0]
            cant_elem_col4= len(columnas[3].split(','))
            cant_elem_col5 = len(columnas[4].split(','))
            conteo.append((letra,cant_elem_col4,cant_elem_col5))


    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    return conteo


def pregunta_11():
    suma = {}
    with open('data.csv') as archivo_csv:
        lineas = archivo_csv.readlines()
        for linea in lineas: 
            columnas = linea.split('\t')
            valores = int(columnas[1])
            lista_letras = columnas[3].split(',')
            for letra in lista_letras:
                if letra in suma:
                    suma[letra] += valores
                else:
                    suma[letra] = valores
    suma_ordenada = dict(sorted(suma.items()))

    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return suma_ordenada


def pregunta_12():
    respuesta = {}
    with open('data.csv') as archivo_csv: 
        lineas=archivo_csv.readlines()
        for linea in lineas: 
            columnas = linea.split('\t')
            letra = columnas[0]
            dicc = columnas[4].split(',')
            for items in dicc:
                llave, valor_str = items.split(':')
                valor = int(valor_str)
                if letra in respuesta:
                    respuesta[letra]+=valor
                else: 
                    respuesta[letra]=valor
    respuesta_ordenada = dict(sorted(respuesta.items()))   
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return respuesta_ordenada
