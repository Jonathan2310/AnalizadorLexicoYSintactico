import re

def analizar_sintaxis(codigo):
    lineas = codigo.split("\n")
    errores = []
    llaves_abiertas = 0

    for num_linea, linea in enumerate(lineas, start=1):
        stripped_linea = linea.strip()

        # Verificar comillas, paréntesis balanceados y caracteres especiales
        if stripped_linea.count('"') % 2 != 0:
            errores.append((num_linea, stripped_linea, "Error: comillas desbalanceadas"))
        if stripped_linea.count('(') != stripped_linea.count(')'):
            errores.append((num_linea, stripped_linea, "Error: paréntesis desbalanceados"))
        if re.search(r"[^a-zA-Z0-9\s;{}()+\-*/=,.\"\'<>:_()]", stripped_linea):
            errores.append((num_linea, stripped_linea, "Error: caracteres especiales inesperados"))

        # Verificar la estructura de system.out.print
        if 'system.out.print' in stripped_linea:
            if not re.match(r'.*System\.out\.print(l?n?)\s*\(.*\)\s*;', stripped_linea):
                errores.append((num_linea, stripped_linea, "Error sintáctico en la estructura de System.out.print"))

        # Verificar si falta ';'
        if not stripped_linea.endswith(';') and not stripped_linea.endswith('{') and not stripped_linea.endswith('}') and 'for' not in stripped_linea:
            errores.append((num_linea, stripped_linea, "Error sintáctico: falta ';'"))

        # Verificar la estructura del bucle 'for'
        if 'for' in stripped_linea:
            match = re.match(r'\s*for\s*\(\s*[^;]*;\s*[^;]*;\s*[^;]*\s*\)\s*\{?', stripped_linea)
            if not match:
                errores.append((num_linea, stripped_linea, "Error sintáctico en la estructura del bucle for"))

        # Contar llaves abiertas y cerradas
        llaves_abiertas += stripped_linea.count('{')
        llaves_abiertas -= stripped_linea.count('}')

    if llaves_abiertas > 0:
        errores.append((num_linea, "", "Error: falta llave de cierre"))
    elif llaves_abiertas < 0:
        errores.append((num_linea, "", "Error: falta llave de apertura"))

    if errores:
        return errores
    else:
        return "Estructura FOR correcta"
