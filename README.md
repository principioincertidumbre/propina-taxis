# propina-taxis

Proyecto para la asignatura Desarrollo de Proyectos y Productos de Datos Magíster en Data Science Universidad del Desarrollo. 

## Objetivo

El objetivo de este proyecto es la construcción de un modelo de machine learning, usando datos de viajes de los taxis amarillos de Nueva York para el año 2020, proporcionados por la [NYC Taxi and Limousine Commission (TLC)](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page). El propósito del modelo de machine learning es encontrar aquellos viajes donde la propina dejada por el pasajero fue mayor al 20% del costo del viaje.
Para ello ajustaremos un modelo de classificación binaria Random Forest usando los datos de los viajes de enero de 2020, comprobando si el rendimiento del modelo se mantiene constante entre enero y junio de 2020. La métrica utilizada para este propósito es F1-score.

## Instalación
1. Clone este repositorio:
```
git clone https://github.com/principioincertidumbre/propina-taxis
```
2. Navegue hasta el directorio del proyecto:
```
cd propinas-taxi
```
3. Cree un entorno virtual de Python:
```
python3 -m venv venv
```
4. Active el entorno virtual:
* Para Linux/MacOS:
 
```
source venv/bin/activate
```
* Para Windows:
```
venv\Scripts\activate.bat
```
5. Instale las librerías requeridas:
```
pip install -r requirements.txt
```
## Licencia
Este proyecto está bajo la licencia MIT. Consulte el archivo [LICENSE](https://github.com/principioincertidumbre/propina-taxis/blob/main/LICENSE) para obtener más información.
