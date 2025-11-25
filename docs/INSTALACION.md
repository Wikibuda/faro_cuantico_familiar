# 🚀 Guía de Instalación

## Opción 1: Servidor Local (Recomendado)

### Con Python
```bash
# Python 3
python3 -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000

### Con Node.js

# Usando serve
npx serve .

# O usando http-server
npx http-server

### Con PHP

php -S localhost:8000

## Opción 2: Abrir Directamente
Puedes abrir index.html directamente en tu navegador, pero algunas funciones como la carga de JSON pueden no funcionar correctamente debido a políticas CORS.

Opción 3: Servidor Web Real
Apache/Nginx
Sube todos los archivos a tu servidor web

Asegúrate de que el archivo JSON esté accesible

El sistema funcionará inmediatamente

🔧 Solución de Problemas
Error de CORS al cargar JSON
Síntoma: Los cuentos no se cargan, consola muestra error CORS

Solución: Usar un servidor local en lugar de abrir el archivo directamente

El menú móvil no funciona
Solución: Verificar que el JavaScript esté cargado correctamente

Los cuentos no se abren
Solución: Verificar la consola del navegador para errores


**📄 docs/USO.md**
```markdown
# 📖 Guía de Uso

## Primeros Pasos

### 1. Explorar el Dashboard
- Mira las estadísticas generales
- Revisa los cuentos destacados
- Lee el mensaje mágico del niño

### 2. Navegar por la Biblioteca
- Usa los filtros por categoría
- Busca cuentos específicos
- Lee las vistas previas

### 3. Leer un Cuento Completo
- Haz clic en "Leer Completo"
- El cuento se abre en un modal
- Puedes compartirlo o agregarlo a favoritos

## Características Avanzadas

### Sistema de Favoritos
1. Haz clic en ⭐ en cualquier cuento
2. Los favoritos se guardan automáticamente
3. Accede a ellos en "Mi Aprendizaje"

### Aventuras Interactivas
1. Ve al módulo "Interactivo"
2. Elige una aventura
3. Toma decisiones que cambian la historia
4. Gana experiencia y logros

### Analizador Profundo
- Descubre patrones en los cuentos
- Ve análisis de emociones y arquetipos
- Entende la estructura narrativa

## Tips y Trucos

### 📱 En Móviles
- Usa el menú hamburguesa (☰)
- Desliza para navegar
- Toca para seleccionar opciones

### 🎯 Para Maximizar el Aprendizaje
- Sigue las recomendaciones del tutor
- Completa los logros
- Explora diferentes categorías de cuentos

### 🔍 Búsqueda Avanzada
Puedes buscar por:
- Títulos
- Contenido
- Categorías  
- Temas específicos


