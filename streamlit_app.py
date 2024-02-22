import streamlit as st
from streamlit_modal import Modal
from codify import generate_response
from gradio_client import Client
import uuid
from retieve_student_chat import evaluate_student



def meta_insight(thread_id=""):
    st.title(f"MetaInsight")

    if prompt := st.chat_input("How can I help you"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)

        response = generate_response(prompt, thread_id)

        st.session_state.messages.append({"role": "assistant", "content": response})
        st.chat_message("assistant").write(response)

def main():

    thread_id = st.sidebar.text_input("Enter Thread ID:", placeholder="abc123").lower()

    st.sidebar.markdown("### Examples of Prompts:")
    examples = [
        "Can you provide an overview of recent advancements in topological photonics?", 
        "Can you summarize the main themes and methodologies in recent topological photonics literature?", 
        "What are the most prominent research directions in topological photonics?",
        "What are the potential benefits and challenges of applying topological photonics principles to quantum computing interconnects?"
    ]

    # If not set by user set it randomly
    if not thread_id:
        task_id = str(uuid.uuid4()).split("-")[0]

    codify(thread_id)
    

    for example in examples:
       st.sidebar.markdown(example)


if __name__ == "__main__":
    main()
