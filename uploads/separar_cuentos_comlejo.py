import re
import os

def separar_cuentos(archivo_entrada, directorio_salida):
    """
    Lee un archivo Markdown con cuentos separados por '---' y crea un archivo .md para cada cuento.
    
    Args:
        archivo_entrada (str): Ruta al archivo que contiene todos los cuentos
        directorio_salida (str): Directorio donde se guardarán los cuentos individuales
    """
    
    # Crear directorio de salida si no existe
    if not os.path.exists(directorio_salida):
        os.makedirs(directorio_salida)
    
    # Leer el contenido completo del archivo
    with open(archivo_entrada, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    # Dividir el contenido usando el separador '---'
    # Usamos re.split para manejar posibles variaciones en el separador
    cuentos = re.split(r'\n---\n', contenido)
    
    # Contador para nombres de archivo secuenciales
    contador = 1
    
    for cuento in cuentos:
        # Limpiar espacios en blanco al inicio y final
        cuento = cuento.strip()
        
        # Saltar cuentos vacíos
        if not cuento:
            continue
        
        # Extraer el título del cuento (primera línea que empiece con ###)
        lineas = cuento.split('\n')
        titulo_archivo = f"cuento_{contador:02d}"
        
        for linea in lineas:
            if linea.startswith('### **'):
                # Extraer el texto entre ** **
                titulo_match = re.search(r'\*\*(.*?)\*\*', linea)
                if titulo_match:
                    titulo = titulo_match.group(1)
                    # Crear nombre de archivo seguro
                    titulo_archivo = re.sub(r'[^\w\s-]', '', titulo)
                    titulo_archivo = re.sub(r'[-\s]+', '_', titulo_archivo)
                    titulo_archivo = titulo_archivo.lower()
                break
        
        # Crear el nombre del archivo
        nombre_archivo = f"{titulo_archivo}.md"
        ruta_completa = os.path.join(directorio_salida, nombre_archivo)
        
        # Escribir el cuento en su propio archivo
        with open(ruta_completa, 'w', encoding='utf-8') as f:
            f.write(cuento)
        
        print(f"✓ Creado: {nombre_archivo}")
        contador += 1
    
    print(f"\nSe crearon {contador-1} cuentos individuales en '{directorio_salida}'")

def separar_cuentos_por_titulo(archivo_entrada, directorio_salida):
    """
    Versión alternativa que separa por títulos ### en lugar del separador '---'
    """
    
    if not os.path.exists(directorio_salida):
        os.makedirs(directorio_salida)
    
    with open(archivo_entrada, 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    # Buscar todos los cuentos que empiezan con ###
    patron = r'(### \*\*.*?\*\*.*?)(?=\n### |\Z)'
    cuentos = re.findall(patron, contenido, re.DOTALL)
    
    for i, cuento in enumerate(cuentos, 1):
        cuento = cuento.strip()
        if not cuento:
            continue
        
        # Extraer título para el nombre del archivo
        lineas = cuento.split('\n')
        titulo_archivo = f"cuento_{i:02d}"
        
        for linea in lineas:
            if linea.startswith('### **'):
                titulo_match = re.search(r'\*\*(.*?)\*\*', linea)
                if titulo_match:
                    titulo = titulo_match.group(1)
                    titulo_archivo = re.sub(r'[^\w\s-]', '', titulo)
                    titulo_archivo = re.sub(r'[-\s]+', '_', titulo_archivo)
                    titulo_archivo = titulo_archivo.lower()
                break
        
        nombre_archivo = f"{titulo_archivo}.md"
        ruta_completa = os.path.join(directorio_salida, nombre_archivo)
        
        with open(ruta_completa, 'w', encoding='utf-8') as f:
            f.write(cuento)
        
        print(f"✓ Creado: {nombre_archivo}")
    
    print(f"\nSe crearon {len(cuentos)} cuentos individuales en '{directorio_salida}'")

# Uso del script
if __name__ == "__main__":
    archivo_entrada = "cuentos.md"
    directorio_salida = "cuentos_individuales"
    
    # Intentar con el método del separador '---' primero
    try:
        separar_cuentos(archivo_entrada, directorio_salida)
    except Exception as e:
        print(f"Error con el primer método: {e}")
        print("Intentando con el método alternativo...")
        separar_cuentos_por_titulo(archivo_entrada, directorio_salida)
