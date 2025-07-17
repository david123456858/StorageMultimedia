# 📦 StorageMultimedia Backend

Este es un proyecto backend desarrollado con **FastAPI** para la gestión de usuarios y almacenamiento de archivos multimedia.

---

## 🚀 Tecnologías utilizadas

- Python 3.11+
- FastAPI
- Uvicorn

---

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

✅ El servidor quedará disponible en:  
[http://localhost:8000](http://localhost:8000)

✅ Documentación automática (Swagger):  
[http://localhost:8000/docs](http://localhost:8000/docs)

---

## 📁 Estructura básica del proyecto

```
StorageMultimedia/
│
├── src/
│   ├── frameworks/
│   │   └── fastApi/
│   │       └── main.py
│   └── users/
│       └── routes.py
│
├── requirements.txt
└── README.md
```

---

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

---

## ❗ Notas adicionales

- El entorno virtual te ayuda a mantener tus dependencias organizadas, pero es opcional.
- El comando `--reload` permite que el servidor se reinicie automáticamente cada vez que haces cambios en el código.
- Todas las rutas están organizadas en routers para facilitar la escalabilidad del proyecto.

---

✅ ¡Listo! Con estos pasos cualquier persona podrá descargar tu proyecto, instalarlo y ejecutarlo sin complicaciones.
