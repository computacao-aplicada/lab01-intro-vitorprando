import streamlit as st
import numpy as np
from PIL import Image

def converter_tons_de_cinza(imagem, metodo):
    imagem_np = np.array(imagem).astype(float)
    if metodo == "Média":
        cinza = np.mean(imagem_np, axis=2)
    elif metodo == "Percepção de Luminância":
        cinza = 0.299 * imagem_np[:, :, 0] + 0.587 * imagem_np[:, :, 1] + 0.114 * imagem_np[:, :, 2]
    elif metodo == "Aproximação Linear":
        cinza = 0.2126 * imagem_np[:, :, 0] + 0.7152 * imagem_np[:, :, 1] + 0.0722 * imagem_np[:, :, 2]
    else:
        cinza = np.mean(imagem_np, axis=2)
    return Image.fromarray(np.uint8(cinza))

st.sidebar.title("Cores Top")

imagem = st.sidebar.file_uploader("Escolha um arquivo", type=["jpg", "jpeg", "png"], accept_multiple_files=False)

view = st.sidebar.radio(
    "Selecione a visualização",
    ["Tons de cinza", "Quantização"]
)

if imagem is not None:
    imagem = Image.open(imagem)
    st.image(imagem, caption="Imagem Original")

    if view == "Tons de cinza":
        metodo = st.radio("Método de Conversão", ["Média", "Percepção de Luminância", "Aproximação Linear"])
        imagem_convertida = converter_tons_de_cinza(imagem, metodo)
        st.image(imagem_convertida, caption=f"Imagem em tons de cinza - {metodo}")
else:
    st.write("Aguardando imagem!")
