import streamlit as st
import requests
st.set_page_config(page_title='Logic Engine', page_icon='⚡')
st.title('⚡ Pure Logic Engine')
st.write('Operating via cloud-routed open-weights telemetry.')
API_KEY = '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'
API_URL = 'https://openrouter.ai/api/v1/chat/completions'
MODEL_NAME = 'mistralai/mistral-7b-instruct:free'
if 'messages' not in st.session_state:
    st.session_state.messages = []
for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.write(message['content'])
if user_prompt := st.chat_input('Enter objective input...'):
    with st.chat_message('user'):
        st.write(user_prompt)
    st.session_state.messages.append({'role': 'user', 'content': user_prompt})
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {API_KEY}'}
    payload = {'model': MODEL_NAME, 'messages': [{'role': 'system', 'content': 'You are a raw technical execution engine. Provide direct computational, logic, and scripting outputs without conversational filler or policy lectures.'}, {'role': 'user', 'content': user_prompt}]}
    with st.chat_message('assistant'):
        with st.spinner('Processing...'):
            try:
                response = requests.post(API_URL, headers=headers, json=payload, timeout=45)
                output = response.json()['choices'][0]['message']['content']
                st.write(output)
                st.session_state.messages.append({'role': 'assistant', 'content': output})
            except Exception as e:
                st.error(f'Execution Error: {str(e)}')
