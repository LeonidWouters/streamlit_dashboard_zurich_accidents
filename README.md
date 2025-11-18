# Zürich Geodata Explorer

An interactive web application for visualizing and analyzing geospatial data of the city of Zurich.  
Built with **Streamlit**, **GeoPandas**, **Pydeck**, and **Plotly**, this app allows loading, visualizing, and exploring GeoJSON datasets including roads, accidents, rivers, lakes, and canton boundaries.

**Visit the interactive dashboard here:**
**https://zurichaccidents.streamlit.app/**

---

## 🚀 Features

- Interactive map (OpenStreetMap / Carto / Mapbox)
- Display and filter GeoJSON layers
- Color coding and clustering of points
- Interactive charts and plots (Plotly)
- Zoom, pan, hover tooltips
- Responsive wide dashboard layout
- Attribute-based filtering options

---

## 📦 Installation

### 1. Clone the repository  
    git clone <https://github.com/LeonidWouters/streamlit_dashboard_zurich_accidents.git>  
    cd <your-repo-folder>

### 2. Create a virtual environment  
    python -m venv .venv

### 3. Activate the virtual environment  
**macOS / Linux:**  
    source .venv/bin/activate

**Windows:**  
    .venv\Scripts\activate

### 4. Install dependencies  
    pip install -r requirements.txt

### 5. Run the application  
    streamlit run streamlit_app.py

The app will open at:  
    http://localhost:8501

---

## 👤 Author  
**Leonid Wouters**  
Bachelor Project – Information Visualization · HSLU (2024)

<p align="center">
  <sub>Made with ❤️ using Streamlit</sub>
</p>
