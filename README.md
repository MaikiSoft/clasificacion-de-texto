**Nombre del Proyecto: Clasificador de Texto con Modelo de Hugging Face**

**README.md**

### Visión General:
¡Bienvenido a nuestro proyecto de Clasificador de Texto! Esta aplicación utiliza una combinación de HTML, CSS, JavaScript, Python y FastAPI para clasificar textos utilizando técnicas avanzadas de procesamiento de lenguaje natural. La esencia de nuestro sistema radica en su capacidad para determinar si un texto dado contiene más de 1000 tokens. Si lo hace, el texto se divide y se envía a un modelo de inteligencia artificial para su clasificación. Posteriormente, las clasificaciones se agregan para proporcionar una respuesta integral.

### Requisitos:
- Python 3.x instalado en su sistema.
- Familiaridad con los lenguajes de programación HTML, CSS, JavaScript y Python.
- Comprensión básica del marco de trabajo FastAPI.

### Instrucciones de Configuración:
1. **Clonar el Repositorio:**
   - Comience clonando nuestro repositorio en su máquina local usando el siguiente comando:
     ```
     git clone <repository_url>
     ```

2. **Instalar Dependencias:**
   - Navegue hasta el directorio del proyecto e instale las dependencias de Python requeridas ejecutando:
     ```
     pip install -r requirements.txt
     ```

3. **Obtener Modelo de Hugging Face:**
   - Visite el sitio web de Hugging Face (https://huggingface.co/models) para seleccionar y descargar un modelo de lenguaje preentrenado adecuado. Asegúrese de que el modelo elegido sea compatible con tareas de clasificación de texto.

4. **Ejecutar el Servidor FastAPI:**
   - Inicie el servidor FastAPI ejecutando el siguiente comando en su terminal:
     ```
     python3  -m uvicorn main:app --port 8082 --reload
     ```
   - Este comando inicia la aplicación FastAPI, permitiendo la comunicación entre el frontend y el backend.

### Uso:
1. **Acceder a la Aplicación:**
   - Abra su navegador web y vaya a la URL donde se esté ejecutando el servidor FastAPI (generalmente `http://localhost:8000` de forma predeterminada).

2. **Ingresar Texto:**
   - Ingrese su texto en el área de texto proporcionada dentro de la interfaz web. Asegúrese de que el texto contenga al menos 1000 tokens para una clasificación significativa.

3. **Iniciar la Clasificación:**
   - Después de ingresar el texto, haga clic en el botón "Clasificar" para iniciar el proceso de clasificación.

4. **Ver Resultados:**
   - Una vez que la clasificación esté completa, la aplicación mostrará la respuesta agregada obtenida del modelo de IA. Esta respuesta resume las clasificaciones de las porciones segmentadas del texto de entrada.

### Estructura del Proyecto:
- **Archivos HTML, CSS y JavaScript:**
  - Estos archivos definen la interfaz de usuario de la aplicación, permitiendo a los usuarios ingresar texto e interactuar con el sistema.
- **Archivos Python:**
  - Contiene la lógica del backend implementada utilizando FastAPI, que orquesta el proceso de clasificación de texto.
- **Modelo Preentrenado:**
  - Guarde los archivos del modelo preentrenado de Hugging Face en un directorio designado dentro de la estructura del proyecto. Asegúrese de que el modelo sea accesible para el backend de Python para inferencia.

### Notas Adicionales:
- **Tokenización y Segmentación:**
  - Los textos con más de 1000 tokens se segmentan en partes más pequeñas para facilitar el procesamiento eficiente. Esta segmentación asegura que incluso textos extensos puedan clasificarse de manera efectiva sin abrumar.
