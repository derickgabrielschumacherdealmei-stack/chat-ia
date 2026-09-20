import streamlit as st
import google.generativeai as genai

# Configuração da página
st.set_page_config(
    page_title="IA Séria e Rigorosa",
    page_icon="🛡️",
    layout="centered"
)

# Estilo CSS para forçar a cor preta em todo o texto da resposta e da interface
st.markdown("""
    <style>
    /* Força todas as letras da aplicação e das caixas de texto a serem pretas */
    body, .stMarkdown, p, span, div, label, h1, h2, h3 {
        color: #000000 !important;
    }
    .stTextArea textarea {
        color: #000000 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ Assistente de IA - Rigoroso e Obediente")
st.write("Sistema configurado para seguir ordens estritamente, sem inventar informações e com texto em preto.")

# Configuração segura da chave da API usando os Segredos do Streamlit
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except Exception:
    st.error("⚠️ Erro crítico: A chave 'GEMINI_API_KEY' não foi configurada nos Segredos do Streamlit.")
    st.stop()

# Configuração do modelo com instruções estritas anti-alucinação e de obediência total
system_instruction = (
    "Você é um assistente de IA extremamente sério, literal e obediente. "
    "Você deve seguir à risca todas as instruções dadas pelo usuário, sem mudar nada por conta própria. "
    "É estritamente proibido inventar dados, fantasiar fatos ou cometer alucinações. "
    "Se não tiver certeza absoluta de uma informação ou se a resposta não puder ser verificada, "
    "você deve declarar claramente que não sabe, em vez de inventar."
)

# Inicializando o modelo com temperatura baixa para máxima precisão
generation_config = {
    "temperature": 0.1,
}

model = genai.GenerativeModel(
    model_name='gemini-1.5-flash',
    system_instruction=system_instruction,
    generation_config=generation_config
)

# Caixa de entrada para a ordem ou pergunta do usuário
pergunta_usuario = st.text_area("Insira sua instrução ou pergunta com rigor:")

if st.button("Executar com Rigor"):
    if pergunta_usuario:
        with st.spinner("Processando com máxima precisão..."):
            try:
                response = model.generate_content(pergunta_usuario)
                
                st.subheader("Resposta Oficial:")
                # Exibe a resposta garantindo o formato em texto preto
                st.markdown(f"<div style='color: #000000;'>{response.text}</div>", unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"Erro na execução: {e}")
    else:
        st.warning("Por favor, insira uma instrução antes de executar.")
