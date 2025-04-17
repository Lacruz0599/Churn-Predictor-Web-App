# 📊 Churn Predictor Web App

Una aplicación web desarrollada en Streamlit que permite cargar datos de clientes y obtener predicciones sobre el riesgo de abandono (churn), consumiendo un modelo de machine learning a través de una API creada con FastAPI.

## 🎯 Objetivo

Esta herramienta tiene como propósito facilitar la toma de decisiones en empresas que buscan reducir la pérdida de clientes. Permite visualizar de forma clara los datos ingresados, predecir el churn de forma automática y mostrar probabilidades asociadas a cada predicción.

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

- Tener corriendo la API de churn localmente o desplegada en la nube.
- Modificar la URL de conexión en el archivo `datasource/api_churn_datasource.py` si la API está desplegada remotamente.

```python
API_URL = "http://127.0.0.1:8000/churn-api/v1/predict/list"  # Cambia esta URL si usas una API externa
```

## 🧪 Cómo funciona

1. El usuario llena un formulario con los datos de un cliente.
2. La aplicación envía la información a la API de predicción.
3. Se muestra la respuesta con la predicción (`Sí` / `No`) y la probabilidad asociada.


## 📬 Contacto

César Eduardo Cruz Cabrera  
📧 cesareduardocruzcabrera@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/cesar-eduardo-cruz-cabrera)

---

Este proyecto forma parte de mi portafolio como científico de datos en formación.  
¡Gracias por visitarlo!
```
