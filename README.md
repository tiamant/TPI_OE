# Chatbot de RRHH - Gestión de Vacaciones

Este proyecto es un Trabajo Práctico Integrador para la cátedra de Organización Empresarial (UTN - TUP). Consiste en un Asistente Virtual desarrollado en Python con Streamlit que automatiza el proceso administrativo de solicitud de vacaciones.

## Características
- Modelo BPMN 2.0 integrado en la lógica de programación.
- Máquina de estados para gestionar la sesión del usuario.
- Persistencia de datos mediante lectura y actualización de archivos CSV (Pandas).
- Manejo de excepciones y validación de reglas de negocio (Camino Infeliz).

## Requisitos Previos
- Python 3.x
- Instalar dependencias: `pip install streamlit pandas`

## Cómo ejecutar el proyecto
1. Clonar el repositorio.
2. Ejecutar el siguiente comando en la terminal:
   `python -m streamlit run app.py` (o `py -m streamlit run app.py`).
3. Interactuar con la interfaz en `http://localhost:8501`.