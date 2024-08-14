# API REST PARA UN SISTEMA RAG - CHATBOT
## Pasos para levantar servidor S.O. WINDOWS

1. **Crear entorno virtual y activar:**
    ```bash
    python -m venv env
    .\env\Scripts\activate
    ```
    
2. **Instalar librerias:**
    ```bash
    pip install -r .\requirements.txt
    ```
    
3. **Ejecutar comando:**
    ```bash
    fastapi dev .\app.py
    ```

## Características

- Guardar diferentes tipos de archivos (.txt, .docs, .pdf, .csv, .xlxs, etc)
- Brindar respuestas con contexto y con NPL (Natural Procesing Language)
- Convertir de texto a voz (devuelve audio)

## Endpoints

### Guardar datos 

- **Método:** POST
- **URL:** `/save-data`
- **Body (JSON):**
    ```json
    {
        "files": ["document/doc.txt", "document/doc.pdf"],
    }
    ```

### Petición retrieval al model LLM

- **Método:** POST
- **URL:** `/retrieval`
- **Body (JSON):**
    ```json
    {
        "query": "Dónde esta mi padre?",
    }
    ```

### Petición retrieval al model LLM

- **Método:** POST
- **URL:** `/text-to-speech`
- **Body (JSON):**
    ```json
    {
        "text": "Traduceme esta bitch!",
    }
    ```