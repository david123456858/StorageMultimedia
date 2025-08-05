# 📦 StorageMultimedia Backend

Este es un proyecto backend desarrollado con **FastAPI** para la gestión de usuarios y almacenamiento de archivos multimedia. Una iniciativa que refleja buenas prácticas, casos de uso reales y una experiencia de usuario excelente.
En este protecto se quiso implementar base de lo que son las api Rest, con una screaming architecture pero siguiendo las bases e intenciones de la arquitectura limpia, principios solid, algunos patrones de diseño y patrones creacionales.

---

## 🚀 Tecnologías utilizadas

- 🐍 Python 3.11+
- ⚡ FastAPI
- 🚀 Uvicorn
- ☁️ Cloudinary (almacenamiento de archivos)
- 🧠 Turso (base de datos SQLite en la nube)

>[!NOTE]  
Este backend está diseñado pensando en escalabilidad, modularidad y separación de responsabilidades.

---

## 🧱 Arquitectura del Proyecto

El proyecto sigue una estructura modular y limpia inspirada en principios de **Clean Architecture** y **DDD básico**.

```plaintext
StorageMultimedia/
│
├── src/
│   ├── frameworks/
│   │   └── fastApi/        # Infraestructura: Servidor FastAPI
│   └── feacture/
│       └── User/           # Módulo del usuario
│           ├── controller/ # Controladores HTTP
│           ├── routes/     # Definición de endpoints
│           ├── caseUse/    # Casos de uso (negocio)
│           └── ...         # Otros adaptadores/lógica
├── requirements.txt
└── README.md
```

## 📥 Instalación paso a paso

### 1. Clonar el repositorio

```bash
git clone <URL_DE_TU_REPOSITORIO>
cd StorageMultimedia
```

### 2. Crear un entorno virtual (opcional pero recomendado)

```bash
python -m venv env
```

### 3. Activar el entorno virtual

- En **Windows**:
```bash
env\Scripts\activate
```

- En **macOS/Linux**:
```bash
source env/bin/activate
```

### 4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

---

## 🚦 Cómo ejecutar el servidor

Ubícate en la carpeta raíz del proyecto y ejecuta:

```bash
uvicorn src.frameworks.fastApi.main:app --reload
```
>[!IMPORTANT]
El parámetro --reload es ideal para desarrollo ya que recarga el servidor automáticamente ante cambios.

✅ El servidor quedará disponible en:  
[http://localhost:8000](http://localhost:8000)

✅ Documentación automática (Swagger):  
[http://localhost:8000/docs](http://localhost:8000/docs)

✅ Demo disponible en:  
[https://storagemultimedia.onrender.com](https://storagemultimedia.onrender.com)

☁️ Base de datos y almacenamiento
🧠 Turso es usado como base de datos relacional SQLite en la nube, ideal para proyectos ligeros.

📦 Cloudinary gestiona el almacenamiento de imágenes/videos de manera eficiente y escalable.

>[!NOTE]
Ambos servicios son fácilmente reemplazables si decides migrar a PostgreSQL o AWS S3.

## 📝 Archivo `requirements.txt`

Este archivo contiene las dependencias necesarias para ejecutar el proyecto:

```plaintext
fastapi==0.110.0
uvicorn==0.29.0
```

Si agregas nuevas librerías, no olvides actualizar este archivo con:

```bash
pip freeze > requirements.txt
```


✅ ¡Listo! Con estos pasos cualquier persona podrá descargar tu proyecto, instalarlo y ejecutarlo sin complicaciones.


