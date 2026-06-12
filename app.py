import streamlit as st
import pandas as pd

df = pd.read_csv("data/empleados.csv")

if "estado" not in st.session_state:
    st.session_state["estado"] = "esperando_dni"

st.title("Chatbot de Recursos Humanos")

if st.session_state["estado"] == "esperando_dni":
    dni_input = st.text_input("Ingrese su DNI:")
    if st.button("Enviar"):
        if not dni_input.isdigit():
            st.error("El DNI ingresado no es válido. Debe contener solo números.")
        else:
            dni = int(dni_input)
            empleado = df[df["dni"] == dni]
            if not empleado.empty:
                st.session_state["saldo"] = empleado.iloc[0]["saldo_vacaciones"]
                st.session_state["nombre"] = empleado.iloc[0]["nombre"]
                st.session_state["estado"] = "esperando_dias"
                st.success(
                    f"Bienvenido/a {st.session_state['nombre']}. Su saldo de vacaciones es de {st.session_state['saldo']} días."
                )
            else:
                st.error("Legajo no encontrado. Verifique el DNI ingresado.")
