# propina-taxis

Proyecto para la asignatura Desarrollo de Proyectos y Productos de Datos Magíster en Data Science Universidad del Desarrollo

# Organización del Proyecto

├── LICENSE
├── README.md          <- Descripción del proyecto y cómo ejecutarlo.
├── data/
│   ├── raw/            <- Datos originales descargados.
│   └── processed/      <- Datos transformados para entrenamientos y pruebas.
│
├── models/             <- Modelos entrenados y serializados.
│
├── notebooks/          <- Notebooks para exploración y validación.
│
│
├── reports/            <- Análisis relacionados con el proyecto.
│   └── figures/        <- Gráficos y figuras para reportes.
│
│
├── scripts/           <- Scripts de prueba del proyecto.
│   ├── entrenamiento.py   
|   ├── evaluacion.py     
│   ├── evaluacion_mensual.py  
│   ├── predicción.py                                                                     
│   │  
├── src/                <- Código fuente del proyecto definido como módulos.
│   ├── __init__.py 
|   ├── config.py      <- Parámetros y rutas de configuración.
│   │
│   ├── data/                                                                       
│   │   └── dataset.py <- Descarga, carga y preprocesamiento de datos.
│   │
│   ├── features/       
│   │   └── build_features.py <- Creación de variables a partir de los datos.
│   │
│   ├── modeling/         
│   │   ├── predict_model.py  <- Entrenamiento del modelo.
│   │   └── train_model.py    <- Predicción y evaluación.
│   │
│   └── visualization/
│       └── plots.py   <- Visualización de resultados.
├── requirements.txt   <- Lista de dependencias necesarias.
