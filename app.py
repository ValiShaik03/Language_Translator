import streamlit as st
import google.generativeai as genai
import os
#api set
#Set Up The Google API Key
os.environ["GOOGLE_API_KEY"] = "YOUR API KEY"
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
#initialize the Gemini Model
model=genai.GenerativeModel("models/gemini-1.5-pro")
#app or ui design

#custom function
def language_translate(text,target_lang):
    prompt = f"""
    Translate the following text to {target_lang}:
    {text}

    please don't add any extra information or explanation, just give me the translated text.
    """
    response = model.generate_content(prompt)
    return response.text if response else "Translation failed."

st.title("Language Translation With Gemini AI 🚀")
st.markdown(
    """
    <style>
    /* Hand cursor for the select box */
    div[data-baseweb="select"] {
        cursor: pointer;
    }
    /* Hand cursor for each dropdown option */
    div[role="option"] {
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True
)

user_text=st.text_area("Enter Text To Translate:")
#Language Option
languages = ['English','Urdu','Hindi','Telugu','Hindi','French','German','Portuguese','Spanish','Italian','Chinese','Japanese','Korean','Arabic','Tamil','Malayalam','Kannada']
target_lang = st.selectbox("Select Target Langugae:", languages)

if st.button("Translate"):
    if user_text.strip():
        translation=language_translate(user_text,target_lang)
        st.subheader("Translated Text:")
        st.write(translation)
    else:
        st.warning("⚠️ Please enter text to translate")
