# 🏗️ Estructura del Proyecto

## Arquitectura General

faro_cuantico_familiar/
├── 📄 index.html # Aplicación principal
├── 📁 data/
│ └── cuentos_reales_COMPLETOS.json # Base de datos de cuentos
├── 📁 docs/ # Documentación
└── 📁 assets/ # Recursos estáticos


## Flujo de Datos

### Carga de Cuentos
```javascript
cargarCuentosReales() 
    → fetch('cuentos_reales_COMPLETOS.json')
    → procesarDatos()
    → actualizarInterfaz()

Sistema de Favoritos

marcarComoFavorito()
    → localStorage.setItem()
    → actualizarContadores()
    → actualizarInterfaz()

Navegación entre Módulos

cambiarModulo()
    → ocultarModulos()
    → mostrarModulo()
    → cargarContenidoEspecifico()

Componentes Principales
1. Sistema de Navegación
Responsive: Menú desktop/móvil

Estado: Mantiene módulo activo

Historial: Manejo de navegación

2. Gestor de Cuentos
Carga: Desde JSON estático

Búsqueda: Tiempo real con múltiples estrategias

Filtrado: Por categorías y temas

3. Sistema de UI/UX
Modales: Para lectura de cuentos

Notificaciones: Feedback al usuario

Animaciones: Transiciones suaves

4. Tutor Evolutivo
Logros: Sistema de desbloqueo

Recomendaciones: Algoritmo inteligente

Progreso: Seguimiento de actividad

Estructura de Datos
Cuento Individual

{
  titulo_real: "**El Faro**",
  categoria: "🌊 Elementos Acuáticos",
  palabras: 462,
  contenido: "Texto completo del cuento...",
  es_real: true,
  temas: ["autodescubrimiento", "luz interior"],
  personajes: ["FARO", "LUCIÉRNAGA"]
}

Perfil de Usuario

{
  nivel: 1,
  experiencia: 4404,
  cuentosLeidos: ["**El Faro**", "**La Casa...**"],
  logros: ["Iniciador de Sueños", "Lector Ávido"]
}

Responsive Design
Breakpoints
> 1024px: Desktop completo

769px - 1024px: Tablet

< 768px: Móvil con menú hamburguesa

Estrategias Mobile-First
CSS Grid y Flexbox

Unidades relativas (rem, %)

Media queries progresivas

**📄 .gitignore**
```gitignore
# Dependencias
node_modules/
npm-debug.log*

# Entornos de desarrollo
.env
.env.local

# Archivos del sistema
.DS_Store
Thumbs.db

# Logs
*.log

# Archivos temporales
*.tmp
*.temp

# Backup files
*.backup


