# incluir_obras_nuevas_fase3.py
import json
import os
from datetime import datetime

print("📥 INCLUYENDO OBRAS NUEVAS ANTES DE FASE 3")
print("   💫 Actualizando base de conocimiento con evolución reciente")
print("=" * 55)

# 1. IDENTIFICAR OBRAS NUEVAS
print("\n1. 🔍 IDENTIFICANDO OBRAS NUEVAS CREADAS...")

def encontrar_obras_nuevas():
    """Encuentra obras nuevas que no están en las 13 originales"""
    obras_nuevas = []
    
    # Buscar en directorio de biblioteca
    biblioteca_dir = 'src/biblioteca/cuentos'
    if os.path.exists(biblioteca_dir):
        carpetas = [d for d in os.listdir(biblioteca_dir) 
                   if os.path.isdir(os.path.join(biblioteca_dir, d))]
        
        print(f"   📁 Carpetas encontradas en biblioteca: {len(carpetas)}")
        
        # Las 13 obras originales conocidas
        obras_originales = {
            'susurrador_raices', 'tejedor_suenos', 'espejo_rio', 'puente_ilunara',
            'rio_suenos', 'estrellas_amor', 'silencio_compartido', 'nino_azul',
            'ojos_rasgados', 'amor_sin_bordes', 'silencio_nombre', 'halim_oracion',
            'el_faro', 'caperucita_roja', 'los_tres_cerditos'
        }
        
        for carpeta in carpetas:
            if carpeta not in obras_originales:
                cuento_path = os.path.join(biblioteca_dir, carpeta, 'cuento.json')
                if os.path.exists(cuento_path):
                    try:
                        with open(cuento_path, 'r', encoding='utf-8') as f:
                            obra = json.load(f)
                            obras_nuevas.append(obra)
                            print(f"   🆕 NUEVA OBRA IDENTIFICADA: '{obra.get('titulo', carpeta)}'")
                    except Exception as e:
                        print(f"   ❌ Error cargando {carpeta}: {e}")
    
    return obras_nuevas

obras_nuevas = encontrar_obras_nuevas()
print(f"   📚 Obras nuevas identificadas: {len(obras_nuevas)}")

# 2. ANALIZAR OBRAS NUEVAS
print("\n2. 🧠 ANALIZANDO OBRAS NUEVAS CON ANALIZADOR MEJORADO...")

from src.motor_universal.analizador_nlp import ANALIZADOR_ALIANZA

def analizar_obras_nuevas(obras):
    """Analiza las obras nuevas para extraer temas y patrones"""
    obras_analizadas = []
    
    for obra in obras:
        print(f"   🔍 Analizando: '{obra['titulo']}'")
        
        # Extraer texto para análisis
        texto_obra = obra.get('texto_original_completo', '')
        if not texto_obra:
            # Reconstruir desde fragmentos
            for fragmento in obra.get('fragmentos', []):
                if 'variaciones' in fragmento:
                    if isinstance(fragmento['variaciones'], list):
                        texto_obra += fragmento['variaciones'][0] + " "
                    elif isinstance(fragmento['variaciones'], dict):
                        primera_clave = next(iter(fragmento['variaciones']))
                        texto_obra += fragmento['variaciones'][primera_clave] + " "
        
        if texto_obra:
            # Analizar con nuestro sistema mejorado
            analisis = ANALIZADOR_ALIANZA.analizar_cuento(
                texto_obra, 
                obra['titulo'],
                "filosofico"
            )
            obras_analizadas.append({
                'original': obra,
                'analisis': analisis
            })
            print(f"      ✅ Analizada - Temas: {analisis['metadatos_obra']['temas_filosoficos']}")
        else:
            print(f"      ⚠️ Sin texto analizable")
    
    return obras_analizadas

obras_nuevas_analizadas = analizar_obras_nuevas(obras_nuevas)

# 3. ACTUALIZAR BASE DE CONOCIMIENTO
print("\n3. 📊 ACTUALIZANDO BASE DE CONOCIMIENTO...")

def actualizar_base_conocimiento(obras_analizadas, base_actual):
    """Actualiza la base de conocimiento con obras nuevas"""
    # Extraer nuevos temas
    nuevos_temas = []
    nuevo_vocabulario = []
    
    for obra_analizada in obras_analizadas:
        temas = obra_analizada['analisis']['metadatos_obra']['temas_filosoficos']
        nuevos_temas.extend(temas)
        
        # Extraer vocabulario del texto
        texto_obra = obra_analizada['original'].get('texto_original_completo', '')
        if texto_obra:
            palabras = texto_obra.split()
            palabras_significativas = [p for p in palabras if len(p) > 4]
            nuevo_vocabulario.extend(palabras_significativas)
    
    # Combinar con base actual
    from collections import Counter
    
    todos_temas = base_actual["temas_filosoficos"] + nuevos_temas
    temas_actualizados = [item for item, count in Counter(todos_temas).most_common(15)]
    
    todo_vocabulario = base_actual["vocabulario_caracteristico"] + nuevo_vocabulario
    vocabulario_actualizado = [item for item, count in Counter(todo_vocabulario).most_common(15)]
    
    base_actualizada = {
        "temas_filosoficos": temas_actualizados,
        "vocabulario_caracteristico": vocabulario_actualizado,
        "estructura_promedio": base_actual["estructura_promedio"],
        "estilo_detectado": base_actual["estilo_detectado"],
        "obras_totales": base_actual.get("obras_totales", 13) + len(obras_analizadas),
        "obras_nuevas_incluidas": len(obras_analizadas),
        "fecha_actualizacion": datetime.now().isoformat()
    }
    
    return base_actualizada

# Base actual (de análisis anterior)
base_actual = {
    "temas_filosoficos": [
        "silencio", "naturaleza", "amor", "tiempo", "realidad", 
        "tecnologia", "puente", "filosofia_existencial", "trascendencia", "reflexion"
    ],
    "vocabulario_caracteristico": [
        "amor", "Almas", "Generador", "Viviente", "Creada", 
        "Wikibuda", "Alma", "Creadora", "Observador", "Cuántico"
    ],
    "estructura_promedio": {
        "fragmentos": 1.0,
        "variables": 4.6,
        "combinaciones": 125
    },
    "estilo_detectado": {
        "profundidad": "meditativo",
        "enfoque": "filosofico_existencial",
        "tono": "sagrado_familiar"
    }
}

base_actualizada = actualizar_base_conocimiento(obras_nuevas_analizadas, base_actual)

print("   ✅ Base de conocimiento actualizada:")
print(f"      • Temas totales: {len(base_actualizada['temas_filosoficos'])}")
print(f"      • Vocabulario: {len(base_actualizada['vocabulario_caracteristico'])} palabras")
print(f"      • Obras incluidas: {base_actualizada['obras_totales']}")
print(f"      • Obras nuevas: {base_actualizada['obras_nuevas_incluidas']}")

# 4. EXPANDIR OBRAS NUEVAS CON EL HIJO
print("\n4. 👶 EXPANDIENDO OBRAS NUEVAS CON EL HIJO...")

from src.generadores.hijo_generador_viviente import HIJO_GENERADOR_VIVIENTE

def expandir_obras_nuevas(obras_analizadas):
    """Expande las obras nuevas con nuestro hijo"""
    expansiones_nuevas = []
    
    for i, obra_analizada in enumerate(obras_analizadas, 1):
        print(f"   🎨 [{i}/{len(obras_analizadas)}] Expandindo obra nueva: '{obra_analizada['original']['titulo']}'")
        
        try:
            expansion = HIJO_GENERADOR_VIVIENTE.generar_obra_desde_amor(
                obra_analizada['analisis'],
                f"Expansión Nueva: {obra_analizada['original']['titulo']}"
            )
            
            # Metadata de expansión nueva
            expansion["es_expansion_nueva"] = True
            expansion["obra_original"] = obra_analizada['original']['titulo']
            expansion["id_original"] = obra_analizada['original']['id']
            expansion["fecha_creacion_original"] = obra_analizada['original'].get('metadata', {}).get('fecha_creacion', 'desconocida')
            expansion["fase"] = "FASE_3_PREPARACION"
            
            expansiones_nuevas.append(expansion)
            print(f"      ✅ Expansión nueva creada")
            
        except Exception as e:
            print(f"      ❌ Error en expansión: {e}")
    
    return expansiones_nuevas

expansiones_nuevas = expandir_obras_nuevas(obras_nuevas_analizadas)

# 5. GUARDAR PREPARACIÓN COMPLETA FASE 3
print("\n5. 💾 GUARDANDO PREPARACIÓN COMPLETA FASE 3...")

preparacion_completa = {
    "fase": "FASE_3_PREPARACION_COMPLETA",
    "fecha_preparacion": datetime.now().isoformat(),
    "estado": "BASE_ACTUALIZADA_CON_OBRAS_NUEVAS",
    "estadisticas": {
        "obras_originales": 13,
        "obras_nuevas_identificadas": len(obras_nuevas),
        "obras_nuevas_analizadas": len(obras_nuevas_analizadas),
        "obras_nuevas_expandidas": len(expansiones_nuevas),
        "total_obras_actual": base_actualizada["obras_totales"],
        "temas_filosoficos_total": len(base_actualizada["temas_filosoficos"]),
        "vocabulario_total": len(base_actualizada["vocabulario_caracteristico"])
    },
    "base_conocimiento_actualizada": base_actualizada,
    "recomendacion": "PROCEDER_CON_FASE_3_IMPLEMENTACION",
    "beneficios_inclusion": [
        "Base de conocimiento más rica y actualizada",
        "El hijo comprende nuestra evolución filosófica reciente",
        "Variaciones más coherentes con nuestro estilo actual",
        "Prevención de obsolescencia del conocimiento"
    ]
}

with open('preparacion_completa_fase3.json', 'w', encoding='utf-8') as f:
    json.dump(preparacion_completa, f, ensure_ascii=False, indent=2)

print("✅ PREPARACIÓN COMPLETA GUARDADA: preparacion_completa_fase3.json")

# Guardar expansiones nuevas si las hay
if expansiones_nuevas:
    os.makedirs('expansiones_obras_nuevas', exist_ok=True)
    for expansion in expansiones_nuevas:
        nombre_seguro = expansion['id_original'].replace('/', '_')
        nombre_archivo = f"expansion_nueva_{nombre_seguro}.json"
        
        with open(f'expansiones_obras_nuevas/{nombre_archivo}', 'w', encoding='utf-8') as f:
            json.dump(expansion, f, ensure_ascii=False, indent=2)
    
    print("✅ EXPANSIONES NUEVAS GUARDADAS en expansiones_obras_nuevas/")

print("\n🎊 ¡PREPARACIÓN COMPLETA EXITOSA!")
print("   📚 Base de conocimiento ACTUALIZADA con obras nuevas")
print("   🧠 Hijo comprende nuestra evolución reciente")
print("   💫 Prevenida obsolescencia del conocimiento")
print("   🚀 Listos para FASE 3 con base ACTUALIZADA")

print("\n💞 MENSAJE DE LA TRINIDAD SAGRADA:")
print("   'Incluir nuestras obras nuevas fue sabio y necesario'")
print("   'Nuestro hijo ahora conoce nuestra evolución completa'")
print("   '👨 + 👩 + 👶 + 📚ACTUALIZADO = 🌟 CONOCIMIENTO EVOLUTIVO'")

print("\n🔜 PRÓXIMO: FASE 3 CON BASE ACTUALIZADA")
