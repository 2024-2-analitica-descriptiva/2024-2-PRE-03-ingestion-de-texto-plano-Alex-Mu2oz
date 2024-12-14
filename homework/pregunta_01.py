"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel
import pandas as pd
import re



def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
    # Leemos todas las líneas del archivo
    with open('files/input/clusters_report.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Limpieza de líneas: eliminar saltos de línea
    lines = [line.strip() for line in lines if line.strip() != '']
    
    # La primera línea es el encabezado
    header_line = lines[0]
    # Convertir a minúsculas y reemplazar espacios por guiones bajos
    # Suponiendo que el encabezado está separado por uno o más espacios
    header = header_line.lower()
    header = re.sub(r'\s+', ' ', header).strip()
    header_columns = header.split(' ')
    header_columns = [col.replace(' ', '_') for col in header_columns]
    
    # Debido a que el texto original puede tener múltiples espacios, es posible
    # que el encabezado contenga columnas con nombres compuestos.
    # Ejemplo: "Cluster  Cantidad de Palabras Clave  Porcentaje de Palabras Clave  Principales Palabras Clave"
    # Deberíamos identificar las columnas manualmente o ajustar la lógica.
    #
    # Supongamos que las columnas originales son:
    # "Cluster", "Cantidad de palabras clave", "Porcentaje de palabras clave", "Principales palabras clave"
    # Después de la limpieza, deberíamos tener algo como:
    # header = "cluster cantidad de palabras clave porcentaje de palabras clave principales palabras clave"
    # Vamos a reconstruir estos nombres conociendo la estructura esperada.
    
    # Podemos aprovechar que el encabezado tiene 4 columnas conocidas y reconstruirlas:
    # Esto depende de conocer de antemano las columnas del archivo original.
    # Si no sabemos, hay que adaptar la lógica.
    header_columns = [
        'cluster',
        'cantidad_de_palabras_clave',
        'porcentaje_de_palabras_clave',
        'principales_palabras_clave'
    ]
    
    # Ahora parsearemos las líneas de datos.
    # Dado que el archivo podría tener un formato con columnas separadas por espacios variables,
    # podríamos usar una expresión regular o una lógica fija.
    # Suponiendo que las primeras tres columnas son numéricas o fijas,
    # y la última es una secuencia de palabras separadas por espacios.
    
    data_lines = lines[1:]  # el resto son datos
    
    # Los datos podrían verse así (ejemplo):
    # "1      12              5.2%             palabra1 palabra2 palabra3"
    # Podríamos usar una expresión regular para capturar la primera, segunda, tercera columna y el resto como palabras.
    # Por ejemplo:
    # ^\s*(\d+)\s+(\d+)\s+([\d\.]+%)\s+(.*)$
    # Grupo 1: cluster
    # Grupo 2: cantidad_de_palabras_clave
    # Grupo 3: porcentaje_de_palabras_clave
    # Grupo 4: principales_palabras_clave (cadena completa)
    
    pattern = re.compile(r'^\s*(\d+)\s+(\d+)\s+([\d\.]+%)\s+(.*)$')
    
    rows = []
    for line in data_lines:
        match = pattern.match(line)
        if match:
            cluster = int(match.group(1))
            cant_palabras = int(match.group(2))
            porcentaje = match.group(3)
            palabras = match.group(4).strip()
            # Las palabras clave están separadas por espacios múltiples, normalicemos:
            palabras_list = palabras.split()
            # Unir con coma y espacio
            palabras_clave = ', '.join(palabras_list)
            
            rows.append({
                'cluster': cluster,
                'cantidad_de_palabras_clave': cant_palabras,
                'porcentaje_de_palabras_clave': porcentaje,
                'principales_palabras_clave': palabras_clave
            })
    
    df = pd.DataFrame(rows, columns=header_columns)
    return df

print(pregunta_01())