import streamlit as st
import cv2
from PIL import Image
import numpy as np
import copy


st.markdown("<h1 style='text-align: center; color: white;'>Color Image</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white; letter-spacing: 2px'>Praktikum 1 Pengolahan Citra Digital</p>", unsafe_allow_html=True)


image = cv2.imread("./Tugas/Meeting 4/Images/gambar.jpeg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
r, g, b = cv2.split(image)
r_dup = copy.deepcopy(r)
g_dup = copy.deepcopy(g)
b_dup = copy.deepcopy(b)
r_dup[:] = 0
g_dup[:] = 0
b_dup[:] = 0


tab1, tab2, tab3, tab4, tab5= st.tabs(["RGB", "BGR", "Red", "Green", "Blue"])

with tab1:
  st.markdown("<p style='text-align: center; color: white; letter-spacing: 2px'>RGB</p>", unsafe_allow_html=True)
  st.image(image)

with tab2:
  st.markdown("<p style='text-align: center; color: white; letter-spacing: 2px'>BGR</p>", unsafe_allow_html=True)
  st.image(cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

with tab3:
  st.markdown("<p style='text-align: center; color: white; letter-spacing: 2px'>Red</p>", unsafe_allow_html=True)
  merged = cv2.merge([r, g_dup, b_dup])
  pil_032 = Image.fromarray(merged)
  st.image(pil_032)

with tab4:
  st.markdown("<p style='text-align: center; color: white; letter-spacing: 2px'>Green</p>", unsafe_allow_html=True)
  merged = cv2.merge([r_dup, g, b_dup])
  pil_032 = Image.fromarray(merged)
  st.image(pil_032)

with tab5:
  st.markdown("<p style='text-align: center; color: white; letter-spacing: 2px'>Blue</p>", unsafe_allow_html=True)
  merged = cv2.merge([r_dup, g_dup, b])
  pil_032 = Image.fromarray(merged)
  st.image(pil_032)