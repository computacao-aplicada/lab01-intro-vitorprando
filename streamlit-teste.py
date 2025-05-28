import streamlit as st
import pandas as pd
import numpy as np
from io import StringIO
from PIL import Image
import requests

st.sidebar.title("Cores Tops")

imagem = st.sidebar.file_uploader("Escolha um arquivo", type=["jpg", "jpeg", "png"], accept_multiple_files=False)

view = st.sidebar.radio(
    "Selecione a visualização",
    ["Tons de cinza", "Quantização"]
)

if imagem is not None:
    st.image(imagem)
    imagem_cinza = imagem.convert("L")
    imagem_np = np.array(imagem)
    valores = st.slider("Valores", 1, 256, 256)

else:
    st.write("Aguardando imagem!")