import streamlit as st
from main import app  # Import the LangGraph compiled app
import pprint

st.set_page_config(page_title="Agentic AI Workflow", layout="wide")
st.markdown("<h1 style='text-align: center;'>🧠 Multi-Agent AI Assistant</h1>", unsafe_allow_html=True)

# Center layout using columns
col1, col2, col3 = st.columns([1, 2, 1])  # 1:2:1 width ratio

with col2:
    # Custom label with larger font
    st.markdown("<h2 style='font-size:20px; font-weight:bold;'>Ask your question:</h2>", unsafe_allow_html=True)
    
    # Then the actual input (without label)
    user_question = st.text_input( label="Ask your question (hidden for styling)", 
    placeholder="Ask Me Something...",
    label_visibility="collapsed" )


    if st.button("🚀 Run") or user_question:
        st.subheader("Agent Workflow Outputs")

        with st.spinner("Processing through agents..."):
            inputs = {
                "messages": [
                    ("user", user_question),
                ]
            }

            # Display results step-by-step
            for event in app.stream(inputs):
                for key, value in event.items():
                    if value is None:
                        continue
                    last_message = value.get("messages", [])[-1] if "messages" in value else None
                    if last_message:
                        with st.expander(f"🔹 Output from node '{key}'", expanded=True):
                            st.markdown(f"**Agent:** `{last_message.name}`")
                            st.markdown(f"**Response:**\n\n{last_message.content.strip()}")
