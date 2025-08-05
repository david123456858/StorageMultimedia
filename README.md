# 🎬 StorageMultimedia API

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org)
[![Cloudinary](https://img.shields.io/badge/Cloudinary-3448C5?style=for-the-badge&logo=cloudinary&logoColor=white)](https://cloudinary.com/)
[![Turso](https://img.shields.io/badge/Turso-4F46E5?style=for-the-badge&logo=sqlite&logoColor=white)](https://turso.tech/)

> **Backend moderno para gestión de usuarios y almacenamiento de archivos multimedia**

Un proyecto backend desarrollado con **FastAPI** que implementa principios de **Clean Architecture**, **SOLID** y patrones de diseño para la gestión eficiente de usuarios y archivos multimedia.

## 🚀 Demo en Vivo

- **API Base:** [https://storagemultimedia.onrender.com](https://storagemultimedia.onrender.com)
- **Documentación Swagger:** [https://storagemultimedia.onrender.com/docs](https://storagemultimedia.onrender.com/docs)
- **Redoc:** [https://storagemultimedia.onrender.com/redoc](https://storagemultimedia.onrender.com/redoc)

## ✨ Características Principales

- 🔐 **Gestión de usuarios** con autenticación segura
- 📁 **Almacenamiento multimedia** en la nube (Cloudinary)
- 📊 **Consultas paginadas** para optimizar rendimiento
- 🏗️ **Arquitectura limpia** y modular
- 📚 **Documentación automática** con Swagger/OpenAPI
- 🧪 **Estructura escalable** y mantenible
- ⚡ **Base de datos SQLite** en la nube con Turso

## 🛠️ Stack Tecnológico

| Tecnología | Propósito | Versión |
|------------|-----------|---------|
| **FastAPI** | Framework web asíncrono | 0.110.0+ |
| **Python** | Lenguaje principal | 3.11+ |
| **Uvicorn** | Servidor ASGI | 0.29.0+ |
| **Cloudinary** | Almacenamiento multimedia | - |
| **Turso** | Base de datos SQLite en la nube | - |

## 🏗️ Arquitectura del Proyecto

El proyecto sigue principios de **Clean Architecture** con separación clara de responsabilidades:

```
StorageMultimedia/
├── src/
│   ├── frameworks/
│   │   └── fastApi/           # 🌐 Infraestructura web (FastAPI)
│   │       ├── main.py        # Punto de entrada de la aplicación
│   │       └── config/        # Configuraciones
│   └── feature/
│       └── User/              # 👥 Módulo de usuarios
│           ├── controller/    # 🎮 Controladores HTTP
│           ├── routes/        # 🛣️ Definición de endpoints
│           ├── caseUse/       # 💼 Casos de uso (lógica de negocio)
│           ├── entities/      # 🏛️ Entidades del dominio
│           ├── repository/    # 🗄️ Acceso a datos
│           └── services/      # 🔧 Servicios auxiliares
├── requirements.txt           # 📦 Dependencias
├── .env.example              # 🔐 Variables de entorno ejemplo
└── README.md                 # 📖 Documentación
```

## 🚀 Instalación y Configuración

### Prerrequisitos

- Python 3.11 o superior
- Git
- Cuenta en [Cloudinary](https://cloudinary.com/) (opcional para desarrollo)
- Cuenta en [Turso](https://turso.tech/) (opcional para desarrollo)

### Instalación Local

1. **Clona el repositorio**
   ```bash
   git clone https://github.com/david123456858/StorageMultimedia.git
   cd StorageMultimedia
   ```

2. **Crea el entorno virtual**
   ```bash
   python -m venv env
   ```

3. **Activa el entorno virtual**
   ```bash
   # Windows
   env\Scripts\activate
   
   # macOS/Linux
   source env/bin/activate
   ```

4. **Instala las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configura las variables de entorno**
   ```bash
   cp .env.example .env
   # Edita .env con tus credenciales
   ```

6. **Ejecuta la aplicación**
   ```bash
   uvicorn src.frameworks.fastApi.main:app --reload
   ```

### ✅ Verificación de Instalación

Una vez iniciado el servidor, verifica que todo funcione correctamente:

- **Servidor local:** [http://localhost:8000](http://localhost:8000)
- **Documentación:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **Health check:** `GET http://localhost:8000/health`

## 📚 Uso de la API

### Endpoints Principales

#### 👥 Gestión de Usuarios

```http
POST /api/v1/users/register
Content-Type: application/json

{
  "username": "usuario_ejemplo",
  "email": "user@example.com",
  "password": "password123"
}
```

#### 📁 Gestión de Archivos

```http
POST /api/v1/multimedia/upload
Content-Type: multipart/form-data

file: [archivo_multimedia]
user_id: 123
title: "Mi archivo"
description: "Descripción del archivo"
```

#### 📄 Consulta Paginada

```http
GET /api/v1/multimedia?page=1&limit=10&user_id=123
```

**Respuesta:**
```json
{
  "data": [
    {
      "id": 1,
			"public_id": "adasfasfasfasf",
			"resource_type": "image",
			"created_at": "2025-08-01T20:34:50.835752",
			"url": "https://res.cloudinary.com",
			"thumbnail_url": "https://res.cloudinary.com"
		}
    }
  ]
}
```

### Códigos de Respuesta HTTP

| Código | Descripción |
|--------|-------------|
| `200` | Operación exitosa |
| `201` | Recurso creado |
| `400` | Solicitud inválida |
| `401` | No autorizado |
| `404` | Recurso no encontrado |
| `422` | Error de validación |
| `500` | Error interno del servidor |

## 🧪 Testing (Próximamente)

```bash
# Ejecutar tests unitarios
pytest tests/unit/

# Ejecutar tests de integración
pytest tests/integration/

# Coverage report
pytest --cov=src tests/
```

## 🚀 Deployment

### Render (Recomendado)

1. Conecta tu repositorio de GitHub
2. Configura las variables de entorno
3. El servicio se despliega automáticamente

### Variables de Entorno Requeridas

```env
CLOUDINARY_CLOUD_NAME=tu_cloud_name
CLOUDINARY_API_KEY=tu_api_key
CLOUDINARY_API_SECRET=tu_api_secret
TURSO_DATABASE_URL=tu_database_url
TURSO_AUTH_TOKEN=tu_auth_token
```

## 🔧 Desarrollo

### Agregar Nueva Funcionalidad

1. Crea un nuevo módulo en `src/feature/NuevoModulo/`
2. Implementa los casos de uso en `caseUse/`
3. Crea los controladores en `controller/`
4. Define las rutas en `routes/`
5. Actualiza `requirements.txt` si es necesario

### Estándares de Código

- Seguir principios **SOLID**
- Usar **Type Hints** en Python
- Documentar funciones complejas
- Mantener separación de responsabilidades

## 🤝 Contribución

1. Fork del proyecto
2. Crea una rama feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit de cambios (`git commit -m 'Añadir nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📝 Roadmap

- [ ] Sistema de autenticación JWT
- [ ] Tests unitarios y de integración
- [ ] Documentación de API más detallada
- [ ] Soporte para videos
- [ ] Sistema de notificaciones
- [ ] Cache con Redis
- [ ] Métricas y monitoreo

## 🐛 Problemas Conocidos

- **Límite de tamaño de archivos:** Cloudinary tiene límites en plan gratuito
- **Conexiones concurrentes:** Turso tiene límites en plan gratuito

## 📧 Contacto

- **GitHub:** [@david123456858](https://github.com/david123456858)
- **LinkedIn:** [@JuanPeralta](www.linkedin.com/in/juan-david-peralta-fuentes-a7a944268)
- **Email:** juandavidperaltafuentes@gmail.com 

