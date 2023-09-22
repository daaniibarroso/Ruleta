# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 10:20:16 2023

@author: alcba
"""

import random
import streamlit as st

#import numpy as np
#import pandas as pd

st.set_page_config(page_title="Ruleta", layout="wide")

#----------FUNCIONES--------------

def generar_numero():
    #Generacion de número en cada ronda
    numero = random.randint(0,36)


    if numero == 0:
        color = "Verde"
    if numero > 0:
        if numero < 11:
            if numero % 2 == 0:
                color = "Negro"
            else:
                    color = "Rojo"
        if numero > 10:
            if numero < 19:
                if numero % 2 == 0:
                    color = "Rojo"
                else:
                        color = 'Negro'
            if numero > 18:
                if numero < 29:
                    if numero % 2 == 0:
                        color = "Negro"
                    else:
                            color = 'Rojo'
                if numero > 28:
                    if numero % 2 == 0:
                        color = "Rojo"
                    else:
                            color = 'Negro'
    st.write("El número que ha salido en esta tirada es:", numero, color)  
        
    return(numero, color)
"""------------------------------------------------"""


x = st.slider("A qué número quieres apostar", min_value=0, max_value=36)
st.write("Número apostado:", x)

color_opciones = ["Rojo", "Negro", "Nada"]
color = st.selectbox("A qué color quieres apostar", options = color_opciones)

paridad_opciones = ["Par", "Impar", "No quiero apostar"]
paridad = st.selectbox("¿Quieres apostar a paridad?", paridad_opciones)

mitades_opciones = ["1-18", "19-36", "No quiero apostar"]
mitad = st.selectbox("¿Quieres apostar a mitades?", mitades_opciones)

tercios_opciones = ["1-12", "13-24", "25-36", "No quiero apostar"]
tercios = st.selectbox("¿Quieres apostar a tercios?", tercios_opciones)

girar = st.button("Girar ruleta")


if girar == True:
    resultado_numero, resultado_color = generar_numero()
    
    if resultado_numero == x:
        st.write("Has acertado el numero")
     
        
    if resultado_color == color:
        st.write("Has acertado el color")
      
        
    if paridad == "Par":
        if resultado_numero % 2 == 0:
            st.write("Has acertado la paridad")

    if paridad == "Impar":
        if resultado_numero % 2 != 0:
            st.write("Has acertado la paridad")


    if mitad == "1-18":
        if resultado_numero > 0 and resultado_numero < 19:
            st.write("Has acertado la mitad")

    if mitad == "19-36":
        if resultado_numero > 18 and resultado_numero < 37:
            st.write("Has acertado la mitad")
            

    if tercios == "1-12":
        if resultado_numero > 0 and resultado_numero < 13:
            st.write("Has acertado el tercio")

    if tercios == "13-24":
        if resultado_numero > 12 and resultado_numero < 25:
            st.write("Has acertado el tercio")
        
    if tercios == "25-36":
        if resultado_numero > 24 and resultado_numero < 37:
            st.write("Has acertado el tercio")