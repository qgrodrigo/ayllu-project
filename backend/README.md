# Backend

## Tecnologías usadas:
* Python
* uv
* fastapi 
* pidantic
* SQLAlchemy

No es necesario configurar alguna versión específica de python y las librerías porque todo ello lo manejamos con uv.

## User stories
### HU-01: Registro de comuneros
* Como secretario comunal
* Quiero registrar nuevos comuneros en el padrón
* Para mantener actualizado el registro oficial de la comunidad.

#### Criterios de aceptación
Registrar datos personales del comunero.
Registrar estado (activo, inactivo, fallecido, suspendido).
Evitar registros duplicados por DNI.

### class: commoner
Es la clase que identifica a la entidad comunero, por buenas prácticas todo lo manejamos en inglés