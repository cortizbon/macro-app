import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import econpizza as ep

from utils import read_model, test_shock, plot_results


st.title("Modelos de macro avanzada")

tab1, tab2, tab3, tab4 = st.tabs(["Modelo básico",
                                  "RBC",
                                  "MIU",
                                  "NeoKeynesian"])

with tab1:
    st.header("Modelo básico")
    model = read_model("./yamls/model.yaml")
    # ecuaciones de equilibrio

    var_shock = st.selectbox("Seleccione el shock a evaluar: ", model.shocks)

    _ = model.solve_stst()
    # schock

    x = test_shock(var_shock, model)

    # ingreso de parámetros para análisis de estabilidad
    # obtener resultados
    plot_results(50, model, x)
    

with tab2:
    st.header("Modelo RBC")
    pass
with tab3:
    st.header("MIU")
    pass
with tab4:
    st.header("NeoKeynesian")
    pass