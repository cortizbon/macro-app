import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import econpizza as ep

from utils import read_model, test_shock, plot_results

st.set_page_config(layout='wide')

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
    fig = plot_results(50, model, x)
    st.pyplot(fig)


with tab2:
    st.header("Modelo RBC")
    model = read_model("./yamls/RBC.yaml")
    # ecuaciones de equilibrio

    var_shock = st.selectbox("Seleccione el shock a evaluar: ", model.shocks, key=1)

    _ = model.solve_stst()
    # schock

    x = test_shock(var_shock, model)

    # ingreso de parámetros para análisis de estabilidad
    # obtener resultados
    fig = plot_results(50, model, x)
    st.pyplot(fig)    
with tab3:
    st.header("MIU")
    model = read_model("./yamls/miu.yaml")
    # ecuaciones de equilibrio

    var_shock = st.selectbox("Seleccione el shock a evaluar: ", model.shocks, key=2)

    _ = model.solve_stst()
    # schock

    x = test_shock(var_shock, model)

    # ingreso de parámetros para análisis de estabilidad
    # obtener resultados
    fig = plot_results(50, model, x)
    st.pyplot(fig)
with tab4:
    st.header("NeoKeynesian")
    st.subheader("Taylor")
    model = read_model("./yamls/taylor_.yaml")
    # ecuaciones de equilibrio

    var_shock = st.selectbox("Seleccione el shock a evaluar: ", model.shocks, key=3)

    _ = model.solve_stst()
    # schock

    x = test_shock(var_shock, model)

    # ingreso de parámetros para análisis de estabilidad
    # obtener resultados
    fig = plot_results(50, model, x)
    st.pyplot(fig) 
    st.subheader("Optimal")
    model = read_model("./yamls/optimal.yaml")
    # ecuaciones de equilibrio

    var_shock = st.selectbox("Seleccione el shock a evaluar: ", model.shocks, key=4)

    _ = model.solve_stst()
    # schock

    x = test_shock(var_shock, model)

    # ingreso de parámetros para análisis de estabilidad
    # obtener resultados
    fig = plot_results(50, model, x)
    st.pyplot(fig)