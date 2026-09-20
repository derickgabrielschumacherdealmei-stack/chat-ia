import streamlit as st
import google.generativeai as genai

# Configuração da página
st.set_page_config(
    page_title="IA Séria e Rigorosa",
    page_icon="🛡️",
    layout="centered"
)

# Estilo CSS para forçar a cor preta em todo o texto e interface
st.markdown("""
    <style>
    body, .stMarkdown, p, span, div, label, h1, h2, h3 {
        color: #000000 !important;
    }
    .stChatInput input {
        color: #000000 !important;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ Assistente de IA - Rigoroso e Obediente")
st.write("Interface de chat contínuo configurada para máxima precisão, sem alucinações e com texto em preto.")

# Configuração segura da chave da API usando os Segredos do Streamlit
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except Exception:
    st.error("⚠️ Erro crítico: A chave 'GEMINI_API_KEY' não foi configurada nos Segredos do Streamlit.")
    st.stop()

# Configuração do modelo com instruções estritas anti-alucinação
system_instruction = (
    "Você é um assistente de IA extremamente sério, literal e obediente. "
    "Você deve seguir à risca todas as instruções dadas pelo usuário, sem mudar nada por conta própria. "
    "É estritamente proibido inventar dados, fantasiar fatos ou cometer alucinações. "
    "Se não tiver certeza absoluta de uma informação ou se a resposta não puder ser verificada, "
    "você deve declarar claramente que não sabe, em vez de inventar."
)

generation_config = {
    "temperature": 0.1,
}

model = genai.GenerativeModel(
    model_name='models/gemini-1.5-flash',
    system_instruction=system_instruction,
    generation_config=generation_config,
)

# Inicializa o histórico de mensagens do chat na sessão do Streamlit
if "chat_history" not in st.session_state:
    st.session_state.chat_history = model.start_chat(history=[])

# Exibe as mensagens anteriores do chat na tela
for message in st.session_state.chat_history.history:
    role = "user" if message.role == "user" else "assistant"
    with st.chat_message(role):
        st.markdown(f"<div style='color: #000000;'>{message.parts[0].text}</div>", unsafe_allow_html=True)

# Caixa de entrada do chat na parte inferior
if prompt_usuario := st.chat_input("Digite sua instrução ou pergunta aqui..."):
    # Mostra a mensagem do usuário imediatamente na interface
    with st.chat_message("user"):
        st.markdown(f"<div style='color: #000000;'>{prompt_usuario}</div>", unsafe_allow_html=True)
    
    # Envia para a IA e obtém a resposta mantendo o contexto
    with st.chat_message("assistant"):
        with st.spinner("Processando com rigor..."):
            try:
                response = st.session_state.chat_history.send_message(prompt_usuario)
                st.markdown(f"<div style='color: #000000;'>{response.text}</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Erro na execução: {e}")
