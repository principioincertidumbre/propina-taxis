# propina-taxis

Proyecto para la asignatura Desarrollo de Proyectos y Productos de Datos Magíster en Data Science Universidad del Desarrollo

# Organización del Proyecto

├── LICENSE<br>
├── README.md          <- Descripción del proyecto y cómo ejecutarlo.<br>
├── data/<br>
│   ├── raw/            <- Datos originales descargados.<br>
│   └── processed/      <- Datos transformados para entrenamientos y pruebas.<br>
│
├── models/             <- Modelos entrenados y serializados.<br>
│
├── notebooks/          <- Notebooks para exploración y validación.<br>
│
│
├── reports/            <- Análisis relacionados con el proyecto.<br>
│   └── figures/        <- Gráficos y figuras para reportes.<br>
│
│
├── scripts/           <- Scripts de prueba del proyecto.<br>
│   ├── entrenamiento.py<br>   
|   ├── evaluacion.py   <br>  
│   ├── evaluacion_mensual.py<br>  
│   ├── predicción.py<br>                                                                     
│   │  
├── src/                <- Código fuente del proyecto definido como módulos.<br>
│   ├── __init__.py 
|   ├── config.py      <- Parámetros y rutas de configuración.<br>
│   │
│   ├── data/<br>                                                                       
│   │   └── dataset.py <- Descarga, carga y preprocesamiento de datos.<br>
│   │
│   ├── features/  <br>     
│   │   └── build_features.py <- Creación de variables a partir de los datos.<br>
│   |
│   ├── modeling/<br>         
│   │   ├── predict_model.py  <- Entrenamiento del modelo.<br>
│   │   └── train_model.py    <- Predicción y evaluación.<br>
│   │
│   └── visualization/<br>
│       └── plots.py   <- Visualización de resultados.<br>
├── requirements.txt   <- Lista de dependencias necesarias.
