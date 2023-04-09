import streamlit as st
import cv2

st.markdown("<h1 style='text-align: center; color: white;'>Proses Operasi Citra</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white; letter-spacing: 2px'>Praktikum 2 Pengolahan Citra Digital</p>", unsafe_allow_html=True)

def loadImage032(path):
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img

def showImage032(img, text=""):
    display(Image.fromarray(img), text)

def addImage032(img1, img2):
    img = cv2.add(img1, img2)
    return img

def subImage032(img1, img2):
    img = cv2.subtract(img1, img2)
    return img

def maxImage032(img1, img2):
    img = cv2.max(img1, img2)
    return img

def minImage032(img1, img2):
    img = cv2.min(img1, img2)
    return img
  
def numpyInverseImage032(img):
    img = 255 - img
    return img

def cvInverseImage032(img):
    img = cv2.bitwise_not(img)
    return img

def cvResizeImage032(img1, img2):
    height, width, channel = img1.shape
    img2 = cv2.resize(img2, (width, height))
    return img2

image1 = loadImage032("./Tugas/Meeting 4/Images/foto.jpg")
label = loadImage032("./Tugas/Meeting 4/Images/label.png")
label = cvResizeImage032(image1, label)
labelInverse = cvInverseImage032(label)

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["Penambahan", "Pengurangan", "Maximum", "Minimum", "Bitwise_Not", "Bitwise_And", "Bitwise_Or", "Bitwise_Xor"])

with tab1:
  st.markdown("<p style='text-align: center; color: white; letter-spacing: 2px'>Penambahan</p>", unsafe_allow_html=True)
  st.image(addImage032(image1, label))

with tab2:
  st.markdown("<p style='text-align: center; color: white; letter-spacing: 2px'>Pengurangan</p>", unsafe_allow_html=True)
  st.image(subImage032(image1, labelInverse))

with tab3:
  st.markdown("<p style='text-align: center; color: white; letter-spacing: 2px'>Maximum</p>", unsafe_allow_html=True)
  st.image(maxImage032(image1, labelInverse))

with tab4:
  st.markdown("<p style='text-align: center; color: white; letter-spacing: 2px'>Minimum</p>", unsafe_allow_html=True)
  st.image(minImage032(image1, label))

with tab5:
  st.markdown("<p style='text-align: center; color: white; letter-spacing: 2px'>Bitwise_Not</p>", unsafe_allow_html=True)
  st.image(cvInverseImage032(image1))

with tab6:
  st.markdown("<p style='text-align: center; color: white; letter-spacing: 2px'>Bitwise_And</p>", unsafe_allow_html=True)
  st.image(cv2.bitwise_and(image1, label))

with tab7:
  st.markdown("<p style='text-align: center; color: white; letter-spacing: 2px'>Bitwise_Or</p>", unsafe_allow_html=True)
  st.image(cv2.bitwise_or(image1, label))

with tab8:
  st.markdown("<p style='text-align: center; color: white; letter-spacing: 2px'>Bitwise_Xor</p>", unsafe_allow_html=True)
  st.image(cv2.bitwise_xor(image1, label))

