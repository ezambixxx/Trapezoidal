import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad  # Untuk menghitung exact integral

# Fungsi untuk metode Trapezoidal Rule
def trapezoidal_rule(x, y):
    n = len(x)
    integral = (x[-1] - x[0]) * (y[0] + 2 * np.sum(y[1:n-1]) + y[n-1]) / (2 * (n - 1))
    return integral

# Title of the application
st.title("Aplikasi Metode Numerik - Trapezoidal Rule")

# Layout dengan st.columns untuk menata input dan output di tengah
col1, col2, col3 = st.columns([1, 12, 1])  # Menyesuaikan lebar kolom

# Menempatkan form input di kolom tengah
with col2:
    # Input fungsi
    function_input = st.selectbox(
        "Pilih Fungsi:",
        ["sin(x)", "cos(x)", "x**2", "e**x", "1/x", "log(x)"]
    )
    
    # Input batas bawah dan batas atas untuk x
    x_min = st.number_input("Batas bawah x", min_value=-100.0, max_value=100.0, value=0.0)
    x_max = st.number_input("Batas atas x", min_value=-100.0, max_value=100.0, value=10.0)
    
    # Input jumlah titik pembagi
    n_points = st.slider("Jumlah Titik Pembagi", min_value=2, max_value=100, value=10)

# Menentukan titik pembagi (x) dan nilai fungsi (y)
x = np.linspace(x_min, x_max, n_points)
if function_input == "sin(x)":
    y = np.sin(x)
elif function_input == "cos(x)":
    y = np.cos(x)
elif function_input == "x**2":
    y = x**2
elif function_input == "e**x":
    y = np.exp(x)
elif function_input == "1/x":
    y = 1/x
elif function_input == "log(x)":
    y = np.log(x)

# Menghitung hasil integral menggunakan Trapezoidal Rule
result = trapezoidal_rule(x, y)

# Menampilkan hasil integral
st.subheader("Hasil Integral")
st.write(f"Integral menggunakan metode Trapezoidal Rule adalah: {result:.4f}")

# Menghitung Exact Integral menggunakan metode numerik (scipy.integrate.quad)
def exact_integral(function, x_min, x_max):
    if function == "sin(x)":
        return quad(np.sin, x_min, x_max)[0]
    elif function == "cos(x)":
        return quad(np.cos, x_min, x_max)[0]
    elif function == "x**2":
        return quad(lambda x: x**2, x_min, x_max)[0]
    elif function == "e**x":
        return quad(np.exp, x_min, x_max)[0]
    elif function == "1/x":
        return quad(lambda x: 1/x, x_min, x_max)[0]
    elif function == "log(x)":
        return quad(np.log, x_min, x_max)[0]

# Mendapatkan Exact Integral
exact_result = exact_integral(function_input, x_min, x_max)

# Menghitung error (selisih antara hasil metode Trapezoidal dan Exact Integral)
error = abs(result - exact_result)

# Menampilkan Exact Integral dan Error
st.subheader("Hasil Perbandingan dan Error")
st.write(f"Exact Integral adalah: {exact_result:.4f}")
st.write(f"Error (selisih antara Trapezoidal dan Exact Integral) adalah: {error:.4f}")

# Menampilkan grafik fungsi dan trapezoidal rule
st.subheader("Grafik Fungsi dan Trapezoidal Rule")

# Set warna grafik
color_function = 'purple'  # Warna grafik fungsi
color_trapezoid = 'blue'  # Warna trapezoidal rule

fig, ax = plt.subplots(figsize=(8, 6))

# Plot fungsi dengan warna yang ditentukan
ax.plot(x, y, label=f"Fungsi: {function_input}", marker="o", color=color_function)

# Menambahkan trapezoidal rule pada grafik dengan warna yang ditentukan
for i in range(len(x) - 1):
    ax.plot([x[i], x[i+1]], [y[i], y[i+1]], color=color_trapezoid, linestyle='-', linewidth=2)
    ax.fill_between([x[i], x[i+1]], [0, 0], [y[i], y[i+1]], color=color_trapezoid, alpha=0.3)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title(f"Grafik Fungsi dan Trapezoidal Rule ({function_input})")
ax.legend()

# Menampilkan grafik di Streamlit
st.pyplot(fig)
