# Planificador de Viajes: Freddy Sierra Silva

Aplicación web interactiva que recomienda destinos de viaje de manera personalizada mediante conversación en lenguaje natural.  
El sistema combina datos estructurados (dataset de destinos) con un modelo de lenguaje (LLM) para generar sugerencias claras, útiles y contextualizadas según las preferencias del usuario.

Desarrollado en **Python + Streamlit** y desplegado en **Streamlit Cloud** para acceso vía enlace.

---

##  Características Principales

- Interfaz tipo **chat conversacional**.
- Recomendaciones basadas en:
  - Presupuesto estimado
  - Preferencias climáticas
  - Actividades de interés
- Uso de **modelos de lenguaje (IA)** para generar respuestas en tono cálido y natural.
- Dataset editable para agregar nuevos destinos.
- Despliegue en la nube accesible por URL.

---

##  Estructura del Proyecto
- planificador_viajes/
- │
- ├── app.py # Aplicación principal en Streamlit          
- ├── destinos.csv # Dataset base de destinos y atributos 
- ├── requirements.txt # Dependencias del entorno         
- ├── .gitignore # Exclusiones del repositorio            
- └── README.md # Documentación del proyecto              


---

##  Uso de IA en el Proyecto

### 1) Prompt Engineering
Los prompts se diseñan para guiar el comportamiento del modelo, especificando:
- Contexto (rol de experto en turismo)
- Estilo de comunicación (amable, cálido, claro)
- Parámetros del usuario (presupuesto, clima, actividades)
  
Esto permite que las respuestas sean **coherentes y útiles**, no solo texto generado al azar.

### 2) RAG (Retrieval-Augmented Generation)
La aplicación no se basa únicamente en el modelo de lenguaje.  
Antes de generar una recomendación, **filtra el dataset `destinos.csv`** para obtener destinos que cumplan con las preferencias del usuario.

Los resultados filtrados se pasan al modelo para que la respuesta esté sustentada en **datos reales**.

Este enfoque es RAG en nivel básico.

### 3) Posibilidad de Integrar Herramientas Externas
Aunque la versión actual trabaja offline, su arquitectura permite añadir:
| API / Herramienta | Uso Potencial |
|-------------------|--------------|
| OpenWeather        | Clima real por destino |
| Skyscanner / Amadeus | Cotización de vuelos |
| Booking / Airbnb   | Recomendaciones de alojamiento |
| Bing Search API    | Eventos y actividades en tiempo real |

Esto facilita evolucionar el sistema hacia un **Agente Inteligente Autónomo**.

---

##  Ejecución en la Web:

1. copie la siguiente URL y péguela en su navegador: https://planificadorviajes-8ywnarbe6zfsb3sjktygjl.streamlit.app/
2. Espero que este planificador no solo cumpla con lo requerido técnicamente sino que le permita planear su próximo viaje a Colombia. Éxitos.
   Atentamente: Freddy Sierra Silva. CC6478800
   


