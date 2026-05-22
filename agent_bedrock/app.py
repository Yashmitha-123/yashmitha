import streamlit as st
from agent import agent_response, get_groq_client
import html

st.set_page_config(
    page_title="AI Support Agent",
    page_icon="🤖",
    layout="centered"
)


st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #0e0e10;
    color: white;
}

/* Title */
h1 {
    color: white;
    text-align: center;
    font-size: 36px;
    margin-bottom: 20px;
}

/* Chat input box */
.stTextInput > div > div > input {
    background-color: #1a1a1d;
    color: white;
    border: 1px solid #333;
    padding: 10px;
    border-radius: 10px;
}

/* Button */
.stButton > button {
    background-color: #6c5ce7;
    color: white;
    border-radius: 10px;
    padding: 8px 20px;
    border: none;
    transition: 0.3s;
}

.stButton > button:hover {
    background-color: #a29bfe;
    transform: scale(1.02);
}

/* Chat container */
.chat-box {
    background-color: #161618;
    padding: 12px;
    border-radius: 12px;
    margin-bottom: 10px;
    border: 1px solid #2a2a2a;
}

/* User message */
.user {
    color: #00d2ff;
    font-weight: bold;
}

/* Bot message */
.bot {
    color: #00ff9f;
    font-weight: bold;
}

/* Sidebar */
.css-1d391kg {
    background-color: #111111;
}
            /* Make all labels white */
label, .stTextInput label {
    color: white !important;
    font-weight: 500;
}

</style>
""", unsafe_allow_html=True)




st.title("🤖 AI Support Agent")

api_key = st.text_input("Enter Groq API Key", type="password")


if "messages" not in st.session_state:
    st.session_state.messages = []

if api_key:

    client = get_groq_client(api_key)

    user_input = st.text_input("Ask your question:")

    if st.button("Send") and user_input:


        response = agent_response(client, user_input)
        st.session_state.messages.append({
            "user": user_input,
            "bot": response
        })

    
    for chat in st.session_state.messages:

        st.markdown(f"""
        <div class="chat-box">
            <div class="user"> You:</div>
            <div>{html.escape(chat['user'])}</div>

            <div>{html.escape(chat['bot'])}</div>
        </div>
        """, unsafe_allow_html=True)

    if st.button("Clear Chat"):
        st.session_state.messages = []