![image](https://github.com/GrahamboJangles/LocalAssistantPy/assets/36944031/b5eeb127-6a78-497c-9161-a86b3e78f515)


# LocalAssistantPy
LocalAssistantPy is a simple Streamlit-based Python application that utilizes the GPT4All library to create a chat interface with a local language model. This interface allows users to interact with the model by entering messages and receiving responses.

# Getting Started
To run the LocalAssistantPy application, make sure you have the required dependencies installed. You can install them using the following command:

```bash
pip install streamlit gpt4all
```
Clone this repository with [git](https://git-scm.com/downloads) and navigate to the project directory:

```bash
git clone https://github.com/GrahamboJangles/LocalAssistantPy.git
cd LocalAssistantPy
```
Run the Streamlit app:

```bash
streamlit run main.py
```

# Usage
Enter your message in the text area labeled "Enter your message below."
Click the "Submit" button to send your message to the language model.
The assistant's response will be displayed below the text area.
## Additional Features
Clear Context: Use the "Clear Context" button to reset the conversation context to the initial state.
# ⚠ Important Note ⚠
Make sure to set the correct path to your local language model by updating the `model_name` variable in the script. My favorite model to use with it is [Mistral 7b.](https://huggingface.co/TheBloke/SlimOpenOrca-Mistral-7B-GGUF/resolve/main/slimopenorca-mistral-7b.Q4_K_M.gguf?download=true)

```python
model_name = r"your/local/model/path"
```
# Dependencies
- Streamlit
- GPT4All
