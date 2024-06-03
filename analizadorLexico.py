import re

def analizar_codigo(codigo):
    reservadas = ["program", "int", "read", "printf", "end"]
    operadores = ["+", "=", "*", "/", "-"]
    parentesis_abre = ["("]
    parentesis_cierra = [")"]
    llaves_abre = ["{"]
    llaves_cierra = ["}"]
    punto_coma = [";"]
    coma = ","
    Numero = ["0-9"]

    tokens_totales = []
    lineas = codigo.split("\n")

    for num_linea, linea in enumerate(lineas, start=1):
        tokens_linea = []

        # Buscar palabras reservadas
        for token in reservadas:
            matches = re.findall(r"\b{}\b".format(token), linea)
            for match in matches:
                tokens_linea.append((num_linea, match, "Palabra reservada"))

        # Buscar operadores
        for token in operadores:
            matches = linea.count(token)
            for _ in range(matches):
                tokens_linea.append((num_linea, token, "Operador"))

        # Buscar paréntesis izquierdos
        for token in parentesis_abre:
            matches = linea.count(token)
            for _ in range(matches):
                tokens_linea.append((num_linea, token, "Paréntesis izquierdo"))

        # Buscar paréntesis derechos
        for token in parentesis_cierra:
            matches = linea.count(token)
            for _ in range(matches):
                tokens_linea.append((num_linea, token, "Paréntesis derecho"))

        # Buscar llaves izquierdas
        for token in llaves_abre:
            matches = linea.count(token)
            for _ in range(matches):
                tokens_linea.append((num_linea, token, "Llave izquierda"))

        # Buscar llaves derechas
        for token in llaves_cierra:
            matches = linea.count(token)
            for _ in range(matches):
                tokens_linea.append((num_linea, token, "Llave derecha"))

        # Buscar punto y coma
        for token in punto_coma:
            matches = linea.count(token)
            for _ in range(matches):
                tokens_linea.append((num_linea, token, "Punto y coma"))

        # Buscar coma
        matches = linea.count(coma)
        for _ in range(matches):
            tokens_linea.append((num_linea, coma, "Coma"))

        # Buscar identificadores y clasificarlos correctamente
        identificadores = re.findall(r"\b[a-zA-Z][a-zA-Z0-9_]*\b", linea)
        for identificador in identificadores:
            if identificador.lower() in reservadas:
                tokens_linea.append((num_linea, identificador, "Palabra reservada"))
            else:
                tokens_linea.append((num_linea, identificador, "Variable"))

        # Verificar si hay errores
        if len(identificadores) == 0:
            # Si no se encontraron identificadores en la línea, marcarla como un error
            tokens_linea.append((num_linea, "Error", "Error"))

        tokens_totales.extend(tokens_linea)
    
    return tokens_totales
