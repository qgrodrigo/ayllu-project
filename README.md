# ayllu-project
Es una plataforma web para la gestión administrativa de comunidades campesinas del Perú. Permite gestionar el padrón de comuneros, asambleas, actas, documentos, faenas y procesos comunales, centralizando la información en un entorno seguro y accesible. Desarrollado con FastAPI, PostgreSQL y React. Licencia: por definir.

## Pasos para levantar el backend
### requerimientos
* instalar python
* instalar uv (gestor de dependencias de python)
* abrir la terminal en la carpeta backend y ejecutar el comando: uv sync
* para ejecutar el backend(levantar las apis) ejecutar el comando: uv run uvicorn backend.main:app --reload
* Una vez que levante en la terminal buscar: INFO: Uvicorn running on http://127.0.0.1:{puerto} y copiarlo en el navegador
* Para revisar la documentación con swagger, en el navegador agregar docs a la url. Es decir: http://127.0.0.1:{puerto}/docs
 
