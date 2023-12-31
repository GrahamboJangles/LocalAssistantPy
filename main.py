import streamlit as st
from gpt4all import GPT4All

# Define a function to start the Streamlit chat
def start_chat(model_name):
    st.title('Coding Assistant')

    # Initialize the model and context
    if 'model' not in st.session_state:
        st.session_state.model = GPT4All(model_name)

    if 'context' not in st.session_state:
        st.session_state.context = "Context: You are a coding assistant."

    # The text area for the user input
    user_input = st.text_area("Enter your message below:")

    # Button to submit the message
    if st.button('Submit'):
        st.session_state.context += f"\n ### User: {user_input}\n"
        generate_and_stream_response()

    # Button to clear the context
    if st.button('Clear Context'):
        st.session_state.context = "Context: You are a coding assistant."

    # Use st.markdown to display the current context on the webpage
    st.markdown(f"Current Context:\n {st.session_state.context}")

def generate_and_stream_response():
    # Use st.empty to create a container for dynamic updates
    response_container = st.empty()
    # Prefix ### Assistant to context
    st.session_state.context += f"\n ### Assistant: "

    with st.session_state.model.chat_session():  # Use the model to get a response
        gen_output = ""
        for token in st.session_state.model.generate(prompt=st.session_state.context, max_tokens=2048, temp=0.7, streaming=True):
            gen_output += token
            with response_container:
                st.write(gen_output, unsafe_allow_html=True)
            if "User:" in gen_output:
                break

    # Update context with user input and assistant response
    st.session_state.context += f"{gen_output}\n"

if __name__ == "__main__":
    model_name = "G:\llama-b1407-bin-win-avx2-x64\models\slimopenorca-mistral-7b.Q4_K_M.gguf"
    start_chat(model_name)  # Start the chat interface
