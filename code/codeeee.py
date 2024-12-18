import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def plot_feasible_region(exercise):
    fig, ax = plt.subplots(figsize=(8, 5))

    if exercise == "Ejercicio 1":
        # Define constraints for Exercise 1
        x_vals = np.linspace(0, 5, 400)
        y_vals1 = (10 - 4 * x_vals) / 2
        y_vals2 = (14 - 3 * x_vals) / 4
        y_vals3 = (7 - 2 * x_vals) / 1

        # Plot constraints
        ax.plot(x_vals, y_vals1, label="4x1 + 2x2 + x3 <= 10")
        ax.plot(x_vals, y_vals2, label="3x1 + 4x2 + 2x3 <= 14")
        ax.plot(x_vals, y_vals3, label="2x1 + x2 + 3x3 <= 7")

        # Fill feasible region
        y_combined = np.minimum.reduce([y_vals1, y_vals2, y_vals3])
        ax.fill_between(x_vals, 0, y_combined, where=(y_combined >= 0), alpha=0.3)

        ax.set_xlim(0, 5)
        ax.set_ylim(0, 5)
        ax.set_xlabel("x1")
        ax.set_ylabel("x2")
        ax.set_title("Región Factible - Ejercicio 1")
        ax.legend()

    elif exercise == "Ejercicio 2":
        # Define constraints for Exercise 2
        x_vals = np.linspace(0, 3, 400)
        y_vals1 = (6 - 3 * x_vals) / 4
        y_vals2 = x_vals - 1

        # Plot constraints
        ax.plot(x_vals, y_vals1, label="3x + 4y <= 6")
        ax.plot(x_vals, y_vals2, label="x - y <= 1")

        # Fill feasible region
        y_combined = np.minimum(y_vals1, y_vals2)
        ax.fill_between(x_vals, 0, y_combined, where=(y_combined >= 0), alpha=0.3)

        ax.set_xlim(0, 3)
        ax.set_ylim(0, 3)
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_title("Región Factible - Ejercicio 2")
        ax.legend()

    st.pyplot(fig)

# Streamlit app
st.title("Visualización de Restricciones")
st.sidebar.title("Opciones")

exercise = st.sidebar.selectbox("Selecciona el ejercicio", ["Ejercicio 1", "Ejercicio 2"])

if st.sidebar.button("Visualizar Gráfico"):
    plot_feasible_region(exercise)
