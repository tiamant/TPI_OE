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
            empleado = df[df["dni_empleado"] == dni]
            if not empleado.empty:
                st.session_state["dni_empleado"] = dni
                st.session_state["saldo"] = int(empleado.iloc[0]["saldo_vacaciones"])
                st.session_state["nombre"] = empleado.iloc[0]["nombre_empleado"]
                st.session_state["estado"] = "esperando_dias"
                st.success(
                    f"Bienvenido/a {st.session_state['nombre']}. Su saldo de vacaciones es de {st.session_state['saldo']} días."
                )
                st.rerun()
            else:
                st.error("Legajo no encontrado. Verifique el DNI ingresado.")

if st.session_state["estado"] == "esperando_dias":
    dias_solicitados = st.number_input(
        "Ingrese la cantidad de días a solicitar:", min_value=0, step=1
    )
    if st.button("Solicitar Vacaciones"):
        if dias_solicitados <= 0:
            st.error("La cantidad de días debe ser mayor a 0.")
        else:
            if dias_solicitados <= st.session_state["saldo"]:
                nuevo_saldo = st.session_state["saldo"] - dias_solicitados
                df.loc[
                    df["dni_empleado"] == st.session_state["dni_empleado"],
                    "saldo_vacaciones",
                ] = nuevo_saldo
                df.to_csv("data/empleados.csv", index=False)
                st.session_state["saldo"] = nuevo_saldo
                st.session_state["estado"] = "finalizado"
                st.success(
                    f"Solicitud aprobada. Se descontaron {dias_solicitados} días. Nuevo saldo: {nuevo_saldo} días."
                )
            else:
                st.error(
                    "Saldo insuficiente. No puede solicitar más días de los disponibles."
                )
