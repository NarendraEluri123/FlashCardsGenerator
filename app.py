import streamlit as st
import google.generativeai as genai

# 1. API Configuration
GOOGLE_API_KEY = "AQ.Ab8RN6JYPU7B8yfjWW5_7qkidbykMrwCAcJ0OKNtcB3ea7XgAg"  # Replace with your actual key
genai.configure(api_key=GOOGLE_API_KEY)

# 2. Helper function to call Gemini
def ask_gemini(prompt):
    model = genai.GenerativeModel('gemini-2.5-flash')
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# 3. Streamlit Page Layout Setup
st.set_page_config(page_title="AI Flashcard Generator", layout="wide")
st.header("📙 AI Flashcard Generator")

# 4. Main Application Input & Logic
st.subheader("Generate Flashcards from Notes")
notes = st.text_area("Paste your study notes here:", height=100)

if st.button("Generate Flashcards"):
    if not notes.strip():
        st.warning("Please paste some study notes first!")
    else:
        with st.spinner("Creating flashcards..."):
            prompt = f"""
            Act as a tutor. Convert the following study notes into 5 clear Question & Answer flashcards.
            
            Notes:
            {notes}
            
            Format the output strictly as:
            Q1: [Question]\n
            A1: [Answer]
            ---
            """
            output = ask_gemini(prompt)
            st.markdown(output)


