### 🧩 Descripción del proyecto

Este proyecto corresponde a un Sistema de Gestión de Clientes desarrollado en Python, aplicando principios de Programación Orientada a Objetos (POO).

La aplicación funciona a través de una interfaz de línea de comandos (CLI) y permite administrar distintos tipos de clientes, validando datos de entrada, persistiendo información en archivos y generando reportes.

### 🎯 Funcionalidades principales

- ✅ Agregar clientes (Regular, Premium y Corporativo)

- ✅ Validaciones inmediatas de:

  - Nombre (solo letras)

  - Email (formato válido)

  - Teléfono (solo números, 8 a 12 dígitos)

  - ID único

- ✅ Listar clientes

- ✅ Buscar clientes por ID o email

- ✅ Actualizar información de clientes

- ✅ Eliminar clientes

- ✅ Persistencia de datos en archivo CSV

- ✅ Generación de reporte en archivo TXT

- ✅ Registro de eventos y errores mediante logs

- ✅ Manejo de excepciones personalizadas

### Estructura

![estructura_proyecto](https://drive.google.com/file/d/1XDmy-SyQp4MNyTb0gHPX2kg6TMv6RwY0/view?usp=sharing)

### 🧠 Principios de POO aplicados

- Encapsulamiento
 Uso de propiedades (@property) para proteger atributos internos.

- Herencia
 RegularClient, PremiumClient y CorporateClient heredan de Client.

- Polimorfismo
 Métodos como get_type() y to_dict() se comportan según el tipo de cliente.

- Abstracción
 Separación clara entre lógica de negocio, validaciones y persistencia.

### 🗂️ Persistencia de datos


# 📄 CSV (data/clients.csv)

 - Almacena la información estructurada de los clientes.

 - Puede abrirse directamente en Excel u otras herramientas.

# 📄 TXT (reports/report.txt)

 - Reporte legible para humanos.

 - Ideal para impresión o revisión rápida.

# 📄 LOG (logs/app.log)

 - Registro técnico de eventos, errores y acciones del sistema.

 - Pensado para depuración y auditoría.


### 📊 Diagramas UML

- Version Inglés:


![uml_ingles](https://drive.google.com/file/d/1SdbAVAZYMq7AwhLkPamNvVuvhMvtrWDy/view?usp=sharing)




- Versión Español:

![uml_español](https://drive.google.com/file/d/1SsBLlPs7fiRbDgV6LGh4f7_kzhZKen5v/view?usp=sharing)





### ▶️ Video demostración









Adjunto un vídeo de ejecución y prueba:

![video_ejecucion_POO](https://drive.google.com/file/d/1icOuyCgHiJt8kseOfbX__wXeBmw25LBj/view?usp=sharing)



### 👩‍💻 Autora

Montserrat Espinoza Flores
Proyecto académico – Programación Orientada a Objetos en Python
