import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from pulp import LpMaximize, LpMinimize, LpProblem, LpVariable, value

# Configuración inicial de la aplicación
st.set_page_config(page_title="Programación Entera", layout="wide")
st.title("Visualización de Ejercicios de Programación Entera")

# Sidebar para seleccionar el ejercicio
st.sidebar.title("Selecciona un Ejercicio")
opcion = st.sidebar.selectbox("Elige el ejercicio:", ["Ejercicio 1", "Ejercicio 2"])

# Mostrar el problema según la selección
if opcion == "Ejercicio 1":
    st.header("Ejercicio 1: Método de Ramificación y Acotamiento (Dakin)")
    st.markdown("""
    **Maximizar:**  
    \\[
    P(x_1, x_2, x_3) = 4x_1 + 3x_2 + 3x_3
    \\]
    **Sujeto a:**  
    \\[
    \\begin{aligned}
    4x_1 + 2x_2 + x_3 & \\leq 10 \\\\
    3x_1 + 4x_2 + 2x_3 & \\leq 14 \\\\
    2x_1 + x_2 + 3x_3 & \\leq 7 \\\\
    \\end{aligned}
    \\]
    donde \\(x_1, x_2, x_3\\) son enteros no negativos.
    """)

    # Gráfico de la región factible
    st.subheader("Región Factible")
    x_vals = np.linspace(0, 5, 400)
    y1 = (10 - 4 * x_vals) / 2
    y2 = (14 - 3 * x_vals) / 4
    y3 = (7 - 2 * x_vals)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x_vals, y1, label="4x₁ + 2x₂ + x₃ ≤ 10")
    ax.plot(x_vals, y2, label="3x₁ + 4x₂ + 2x₃ ≤ 14")
    ax.plot(x_vals, y3, label="2x₁ + x₂ + 3x₃ ≤ 7")
    ax.fill_between(x_vals, np.minimum(np.minimum(y1, y2), y3), 0, where=(y1 >= 0) & (y2 >= 0) & (y3 >= 0), alpha=0.3)
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 5)
    ax.set_xlabel("x₁")
    ax.set_ylabel("x₂")
    ax.legend()
    ax.set_title("Región Factible")
    st.pyplot(fig)

elif opcion == "Ejercicio 2":
    st.header("Ejercicio 2: Método de Planos de Corte (Cut-Planes)")
    st.markdown("""
    **Minimizar:**  
    \\[
    C(x, y) = x - y
    \\]
    **Sujeto a:**  
    \\[
    \\begin{aligned}
    3x + 4y & \\leq 6 \\\\
    x - y & \\leq 1 \\\\
    \\end{aligned}
    \\]
    donde \\(x, y\\) son enteros no negativos.
    """)

    # Gráfico de la región factible
    st.subheader("Región Factible")
    x_vals = np.linspace(0, 3, 400)
    y1 = (6 - 3 * x_vals) / 4
    y2 = x_vals - 1

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x_vals, y1, label="3x + 4y ≤ 6")
    ax.plot(x_vals, y2, label="x - y ≤ 1")
    ax.fill_between(x_vals, np.minimum(y1, y2), 0, where=(y1 >= 0) & (y2 >= 0), alpha=0.3)
    ax.set_xlim(0, 3)
    ax.set_ylim(0, 3)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    ax.set_title("Región Factible")
    st.pyplot(fig)

# Pie de página
st.sidebar.info("Creado por: Andree Alessandro")
