import os
import json
import glob
from datetime import datetime

class PobladorCompleto:
    def __init__(self):
        self.directorio_cuentos = "uploads/ya-en-faro-cuantico"
        
    def cargar_todos_los_contenidos(self):
        print("🔮 CARGANDO CONTENIDOS COMPLETOS DE 32 CUENTOS...")
        
        if not os.path.exists(self.directorio_cuentos):
            print(f"❌ No existe: {self.directorio_cuentos}")
            return []
        
        os.chdir(self.directorio_cuentos)
        archivos_md = glob.glob("*.md")
        print(f"📁 Encontrados {len(archivos_md)} archivos .md")
        
        cuentos_completos = []
        
        for archivo in archivos_md:
            try:
                with open(archivo, 'r', encoding='utf-8') as f:
                    contenido_completo = f.read().strip()
                
                if not contenido_completo:
                    print(f"⚠️  {archivo} está vacío")
                    continue
                
                lineas = contenido_completo.split('\n')
                titulo_real = lineas[0].replace('#', '').strip() if lineas and lineas[0].startswith('#') else archivo.replace('.md', '').replace('_', ' ').title()
                
                cuento = {
                    "titulo_archivo": archivo,
                    "titulo_real": titulo_real,
                    "contenido": contenido_completo,  # ✅ CONTENIDO COMPLETO
                    "palabras": len(contenido_completo.split()),
                    "lineas": len(lineas),
                    "categoria": self.detectar_categoria(archivo, contenido_completo),
                    "temas": self.detectar_temas(contenido_completo),
                    "personajes": self.detectar_personajes(contenido_completo),
                    "fecha_carga": datetime.now().isoformat(),
                    "es_real": True
                }
                
                cuentos_completos.append(cuento)
                print(f"✅ {titulo_real} - {cuento['palabras']} palabras")
                
            except Exception as e:
                print(f"❌ Error en {archivo}: {e}")
        
        return cuentos_completos
    
    def detectar_categoria(self, archivo, contenido):
        contenido_min = contenido.lower()
        archivo_min = archivo.lower()
        
        categorias = {
            'barquero': '🌊 Navegante Espiritual',
            'cartero': '📬 Mensajero del Alma',
            'farero': '💡 Guía en la Oscuridad', 
            'herrero': '⚒️ Forjador de Destinos',
            'tejedor': '🧵 Tejedor de Realidades',
            'jardinero': '🌱 Cultivador de Sueños',
            'panadero': '🥖 Artesano de la Vida',
            'pastor': '☁️ Pastor de Ideas',
            'relojero': '⏰ Arquitecto del Tiempo',
            'sastre': '👗 Diseñador de Identidades',
            'alfarero': '🏺 Moldeador de Esencia',
            'hornero': '🍞 Alquimista Cotidiano',
            'guardián': '🛡️ Protector de Secretos'
        }
        
        for oficio, categoria in categorias.items():
            if oficio in archivo_min:
                return categoria
        
        if any(p in contenido_min for p in ['niña', 'mujer', 'señora', 'dama']):
            return "👩 Sabiduría Femenina"
        elif any(p in contenido_min for p in ['río', 'mar', 'agua', 'océano']):
            return "🌊 Elementos Acuáticos"
        elif any(p in contenido_min for p in ['sueño', 'soñar', 'dormir']):
            return "💤 Reino Onírico"
        else:
            return "📖 Cuento Mágico"
    
    def detectar_temas(self, contenido):
        contenido_min = contenido.lower()
        temas = []
        
        if any(p in contenido_min for p in ['tiempo', 'años', 'siempre', 'eterno']):
            temas.append("⏳ Temporalidad")
        if any(p in contenido_min for p in ['recordar', 'memoria', 'olvidar']):
            temas.append("🧠 Recuerdo")
        if any(p in contenido_min for p in ['buscar', 'encontrar', 'hallar']):
            temas.append("🔍 Búsqueda")
        if any(p in contenido_min for p in ['perder', 'adiós', 'despedida']):
            temas.append("💔 Pérdida")
        if any(p in contenido_min for p in ['amor', 'querer', 'corazón']):
            temas.append("💞 Emociones")
            
        return temas[:3]
    
    def detectar_personajes(self, contenido):
        lineas = contenido.split('\n')
        personajes = []
        
        for linea in lineas:
            palabras = linea.split()
            for i, palabra in enumerate(palabras):
                if palabra.lower() in ['el', 'la'] and i + 1 < len(palabras):
                    siguiente = palabras[i + 1]
                    if siguiente[0].isupper() and len(siguiente) > 2:
                        personajes.append(siguiente)
        
        return list(set(personajes))[:5]
    
    def crear_json_completo(self, cuentos):
        estructura = {
            "metadata": {
                "fecha_creacion": datetime.now().isoformat(),
                "total_cuentos": len(cuentos),
                "total_palabras": sum(c['palabras'] for c in cuentos),
                "version": "COMPLETA_2.0"
            },
            "cuentos": cuentos
        }
        
        # Guardar en el directorio principal
        os.chdir("..")  # Volver al directorio principal
        with open('cuentos_reales_COMPLETOS.json', 'w', encoding='utf-8') as f:
            json.dump(estructura, f, indent=2, ensure_ascii=False)
        
        return estructura

if __name__ == "__main__":
    print("🌌 POBLADOR COMPLETO - CARGANDO TODOS LOS CONTENIDOS")
    print("=" * 60)
    
    poblador = PobladorCompleto()
    cuentos = poblador.cargar_todos_los_contenidos()
    
    if cuentos:
        print(f"\n🎉 PROCESADOS {len(cuentos)} CUENTOS COMPLETOS")
        
        # Crear JSON mejorado
        datos = poblador.crear_json_completo(cuentos)
        
        print(f"💾 Guardado: cuentos_reales_COMPLETOS.json")
        print(f"📊 Resumen:")
        print(f"   • 📚 Cuentos: {datos['metadata']['total_cuentos']}")
        print(f"   • 📝 Palabras totales: {datos['metadata']['total_palabras']}")
        print(f"   • ✅ Todos con contenido completo: SÍ")
        
    else:
        print("❌ No se pudieron cargar los cuentos")
