import streamlit as st
import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import copy

st.set_option('deprecation.showPyplotGlobalUse', False)


st.markdown("<h1 style='text-align: center; color: white;'>Histogram</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white; letter-spacing: 2px'>Praktikum 3 Pengolahan Citra Digital</p>", unsafe_allow_html=True)

def histogram_equalization(image):
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    hist, bins = np.histogram(img.flatten(), 256, [0, 256])

    # Menghitung jumlah kumulatif dari histogram
    cdf = hist.cumsum()

    # Menghitung menggunakan rumus equalization
    cdf_normalized = cdf * hist.max() / cdf.max()

    cdf_m = np.ma.masked_equal(cdf, 0)
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')

    equ = cdf[img]

    return equ

image_original = cv2.imread("./Tugas/Meeting 4/Images/gambar.jpeg")
image_original = cv2.cvtColor(image_original, cv2.COLOR_BGR2GRAY)
image_equalization = cv2.imread("./Tugas/Meeting 4/Images/gambar.jpeg")
hist = histogram_equalization(image_equalization)

col1, col2 = st.columns(2)

with col1:
  st.image(image_original)
  st.markdown("<p style='text-align: center; color: white; letter-spacing: 2px'>Original</p>", unsafe_allow_html=True)

with col2:
  st.image(hist)
  st.markdown("<p style='text-align: center; color: white; letter-spacing: 2px'>Equalization</p>", unsafe_allow_html=True)

# menghitung histogram gambar asli dan histogram equalization
hist_orig, bins_orig = np.histogram(image_original.ravel(), 256, [0, 256])
hist_eq, bins_eq = np.histogram(image_equalization.ravel(), 256, [0, 256])


# histogram plot
plt.subplot(121), 
plt.bar(bins_orig[:-1], hist_orig, width=1)
plt.xlim([0, 256])
plt.title('Histogram Gambar Asli')
plt.xlabel('Intensitas')
plt.ylabel('Jumlah Pixel')

plt.subplot(122), 
plt.bar(bins_eq[:-1], hist_eq, width=1)
plt.xlim([0, 256])
plt.title('Histogram Histogram Equalization')
plt.xlabel('Intensitas')
plt.ylabel('Jumlah Pixel')

st.pyplot()

# hist_original, bins_original = np.histogram(img.ravel(), 256, [0, 256])
# hist_equalization, bins_equalization = np.histogram(img.ravel(), 256, [0, 256])



