import math
import streamlit as st

# 1. Configuração da página (DEVE ser o primeiro comando do Streamlit no código)
st.set_page_config(page_title="Calculadora Programada em Python", page_icon="🔢")

# 2. Link direto da imagem do quadro de matemática
url_da_imagem = "https://www.shutterstock.com/shutterstock/photos/360399383/display_1500/stock-vector-math-theory-and-mathematical-formula-equation-doodle-handwriting-icon-in-blackboard-background-with-360399383.jpg"

# 3. Injeção do fundo de tela e estilização dos textos para máxima visibilidade
st.markdown(
    f"""
    <style>
    /* Aplica a imagem de fundo de forma fixa */
    .stApp {{
        background-image: url("{url_da_imagem}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    
    /* Força os títulos, textos e labels das caixas a ficarem brancos e com contorno de sombra preta */
    h1, h2, h3, p, label, .stWidgetLabel p {{
        color: #FFFFFF !important;
        text-shadow: 2px 2px 6px #000000, -2px -2px 6px #000000, 2px -2px 6px #000000, -2px 2px 6px #000000 !important;
        font-weight: bold !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# 4. Títulos e Textos na tela
st.title("Vamos Calcular!")
st.write("Uma Calculadora simples, feita por teste pelo L E O N A R D O!")

# 5. Caixas de entrada (Começam vazias e pulam de 1 em 1)
num1 = st.number_input("Escolha o primeiro número (ou o Radicando da raiz):", value=None, step=1)
num2 = st.number_input("Escolha o segundo número (ou o Índice da raiz):", value=None, step=1)

# 6. Menu de seleção de operações
op = st.selectbox(
    "Escolha uma Operação:",
    ["Soma (+)", "Subtração (-)", "Multiplicação (*)", "Divisão (/)", "Potência (**)", "Raiz (√)"]
)

resultado = 0
erro = False

# 7. Estrutura lógica de cálculos (Textos dos blocos batem 100% com o menu acima)
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
    elif op == "Potência (**)":
        resultado = num1 ** num2
    elif op == "Raiz (√)":
        if num2 != 0:
            resultado = num1 ** (1 / num2)
        else:
            erro = True
            st.error("O índice da raiz (Número 2) não pode ser zero! ❌")
            
    # Exibe a barra verde apenas se não houver erro matemático
    if not erro:
        st.success(f"### 🎉 Resultado: {resultado}")

else:
    # Mensagem azul que aparece enquanto as caixas estiverem em branco
    st.info("Digite os números nos campos acima para ver o cálculo. 🔢")
