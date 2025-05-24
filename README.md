# 📊 Churn Predictor Web App

Esta aplicación web, desarrollada con **Streamlit**, permite a los usuarios cargar datos de clientes y obtener predicciones personalizadas sobre el riesgo de abandono (churn). La app se conecta a una **API creada con FastAPI**, que expone un modelo de machine learning previamente entrenado para ofrecer respuestas rápidas y precisas.

Ofrece una interfaz interactiva y amigable para facilitar el análisis visual de los datos, así como la interpretación de las predicciones generadas por el modelo.

## 🎯 Objetivo

El objetivo principal de esta herramienta es apoyar a las empresas en sus estrategias de **retención de clientes**, proporcionando una solución práctica y accesible para identificar clientes en riesgo de churn. 

La aplicación permite:
- **Visualizar los datos** de forma clara y ordenada.
- **Realizar predicciones automáticas**, mostrando la probabilidad de abandono para cada cliente.
- **Interpretar resultados** de forma intuitiva para apoyar la toma de decisiones basada en datos.

Está pensada para equipos de negocio, marketing o analítica que buscan integrar modelos predictivos sin necesidad de conocimientos técnicos avanzados.

## 🌐 Tecnologías utilizadas

- Python 3.10+
- Streamlit
- requests (para consumir la API)
- Pandas / NumPy
- FastAPI (API externa que se conecta con esta app)

## ⚙️ Ejecución local

### 1. Clona el repositorio

```bash
git clone https://github.com/Lacruz0599/churn-predictor-web-app.git
cd churn-predictor-web-app
```

### 2. (Opcional) Crea y activa un entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecuta la aplicación

```bash
streamlit run app.py
```

## 📡 Requisitos

- Tener corriendo la [API de churn](https://github.com/Lacruz0599/churn-prediction-api) localmente o desplegada en la nube.
- Modificar la URL de conexión en el archivo `datasource/api_churn_datasource.py` si la API está desplegada remotamente.

```python
API_URL = "http://127.0.0.1:8000/churn-api/v1/predict/list"  # Cambia esta URL si usas una API externa
```

## 🧪 Cómo funciona

1. El usuario llena un formulario con los datos de un cliente.
2. La aplicación envía la información a la API de predicción.
3. Se muestra la respuesta con la predicción (`Sí` / `No`) y la probabilidad asociada.


## 🔗 Enlaces Relacionados

-  **API del modelo**: [Repositorio de la API](https://github.com/Lacruz0599/churn-prediction-api)
-  **Modelo de Ml usado en la api**: [Predicción De Abandono De Clientes Telecom](https://github.com/Lacruz0599/prediccion-de-abandono-de-clientes-Telecom)


## 📬 Contacto

César Eduardo Cruz Cabrera  
📧 cesareduardocruzcabrera@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/cesar-eduardo-cruz-cabrera)

---

Este proyecto forma parte de mi portafolio como científico de datos en formación.  
¡Gracias por visitarlo!
```
