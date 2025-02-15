# -*- coding: utf-8 -*-
"""Tugas2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Q5nCVejDvsiiWAx0LtGdaM5ic5QrRoCq
"""



"""Tugas 2"""

import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menghitung suhu berdasarkan persamaan
def calculate_temperature(T0, Ta, k, t):
    return np.exp(-k * t) * (T0 - Ta) + Ta

# Parameter awal
T0 = 80  # Suhu awal (derajat Celsius)
Ta = 25   # Suhu lingkungan (derajat Celsius)
k = 0.1   # Konstanta laju pendinginan
time = np.linspace(0, 50, 500)  # Waktu dalam detik

# Hitung suhu
temperature = calculate_temperature(T0, Ta, k, time)

# Plot grafik
plt.figure(figsize=(8, 6))
plt.plot(time, temperature, label="Suhu $T(t)$", color="blue")
plt.axhline(y=Ta, color="red", linestyle="--", label="Suhu Lingkungan $T_a$")
plt.title("Grafik Suhu terhadap Waktu (Newton's Law of Cooling)")
plt.xlabel("Waktu (detik)")
plt.ylabel("Suhu (°C)")
plt.legend()
plt.grid()
plt.show()