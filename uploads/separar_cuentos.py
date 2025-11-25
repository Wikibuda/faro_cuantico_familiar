import re
import os

def separar_cuentos_simple():
    """Versión simple para separar los cuentos"""
    
    # Leer el archivo original
    with open('cuentos.md', 'r', encoding='utf-8') as f:
        contenido = f.read()
    
    # Crear directorio para cuentos individuales
    os.makedirs('cuentos_individuales', exist_ok=True)
    
    # Separar por el patrón '---' entre cuentos
    cuentos = contenido.split('\n---\n')
    
    for i, cuento in enumerate(cuentos, 1):
        cuento = cuento.strip()
        if not cuento:
            continue
        
        # Buscar el título del cuento
        titulo_match = re.search(r'### \*\*(.*?)\*\*', cuento)
        if titulo_match:
            titulo = titulo_match.group(1)
            # Crear nombre de archivo amigable
            nombre_archivo = titulo.lower().replace(' ', '_').replace('¿', '').replace('?', '')
            nombre_archivo = re.sub(r'[^\w_]', '', nombre_archivo)
            nombre_archivo = f"{nombre_archivo}.md"
        else:
            nombre_archivo = f"cuento_{i:02d}.md"
        
        # Guardar cuento individual
        with open(f'cuentos_individuales/{nombre_archivo}', 'w', encoding='utf-8') as f:
            f.write(cuento)
        
        print(f'Creado: {nombre_archivo}')

# Ejecutar el script
if __name__ == "__main__":
    separar_cuentos_simple()
    print("\n¡Todos los cuentos han sido separados en archivos individuales!")
