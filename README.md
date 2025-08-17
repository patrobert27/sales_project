# Sales Project: Mini proyecto para empezar, en análisis de ventas

Este proyecto es un mini proyecto de ciencia de datos que analiza ventas de productos por clientes y ciudades, usando Python y librerías de análisis y visualización de datos.

## Estructura del proyecto

sales_project/
    data/                 # Archivos CSV de entrada
        sales.csv
        clients.csv
        products.csv
    notebooks/            # Notebooks de análisis
        analysis.ipynb
    src/                  # Código fuente
        cleaning.py       # Funciones para cargar y limpiar datos
        analysis.py       # Funciones de análisis de ventas
        visualizations.py # Funciones para gráficos
    README.md             # Este archivo


## Objetivos

- Limpiar los datos de ventas eliminando valores nulos o duplicados
- Analizar ingresos totales y por ciudad
- Visualizar los resultados con gráficos de barras

## Tecnologías y librerías usadas

- Python 3.x
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

## Cómo ejecutar el proyecto

1. Clona el repositorio:

```bash
git clone https://github.com/patrobert27/sales_project.git
cd sales_project
```
2. Instalar las librerías necesarias:
```pip install pandas matplotlib seaborn jupyte```

3. Abrir el notebook:
```jupyter notebook notebooks/analysis.ipynb```



