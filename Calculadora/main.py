import streamlit as st

st.set_page_config(page_title="Uma simples Calculadora feita por mim❤ utilizando python", page_icon="❤")

st.title("Vamos Calcular!")
st.write("Uma Calculadora simples, feita para teste pelo L E O N A R D O!")

num1 = st.number_input("Escolha um número:", value=None, step=1)
num2 = st.number_input("Escolha outro número:", value=None, step=1)

op = st.selectbox(
    "Escolha uma Operação:",
    ["Soma (+)", "Subtração (-)", "Multiplicação (*)", "Divisão (/)", "Potência (!)"])

resultado = 0
erro = False


if num1 is not None and num2 is not None:

    if op == "Soma (+)":
        resultado = num1 + num2
    elif op == "Subtração (-)":
        resultado = num1 - num2
    elif op == "Multiplicação (*)":
        resultado = num1 * num2
    elif op == "Divisão (/)":
        if num2 != 0:
            resultado = num1 / num2
        else:
            erro = True
            st.error("Não é possível dividir por zero! ❌")
    elif op == "Potência (!)":
        resultado = num1 ** num2

    if not erro:
        st.success(f"### 🎉 Resultado: {resultado}")

else:
    st.info("Digite os números nos campos acima para ver o cálculo. 🔢")
