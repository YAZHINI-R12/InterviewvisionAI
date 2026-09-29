import streamlit as st
from google import genai

from prompts import SYSTEM_PROMPT


# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="InterviewVision AI",
    page_icon="🎯",
    layout="centered"
)


# --------------------------------------------------
# GEMINI CLIENT
# --------------------------------------------------

GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]


@st.cache_resource
def get_gemini_client():
    return genai.Client(api_key=GEMINI_API_KEY)


gemini_client = get_gemini_client()


# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🎯 InterviewVision AI")

st.write(
    "AI-powered technical interview coach that turns your "
    "study material into an interactive interview."
)


# --------------------------------------------------
# DISPLAY PREVIOUS MESSAGES
# --------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# --------------------------------------------------
# CHAT INPUT
# --------------------------------------------------

user_input = st.chat_input(
    "Ask something or start your interview..."
)


# --------------------------------------------------
# PROCESS USER MESSAGE
# --------------------------------------------------

if user_input:

    # Display user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    # Create conversation history
    conversation = SYSTEM_PROMPT + "\n\n"

    for message in st.session_state.messages:

        conversation += (
            f"{message['role'].upper()}: "
            f"{message['content']}\n"
        )

    # Generate Gemini response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = gemini_client.models.generate_content(
                model="gemini-3.5-flash",
                contents=conversation
            )

            assistant_response = response.text

            st.markdown(assistant_response)

    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": assistant_response
        }
    )