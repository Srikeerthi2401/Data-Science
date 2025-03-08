import streamlit as st
from transformers import pipeline
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Load a pre-trained Hugging Face model
chatbot = pipeline("text-generation", model="distilgpt2")

# Define healthcare-specific response logic
def healthcare_chatbot(user_input):
    user_input = user_input.lower()  # Convert input to lowercase for better matching
    
    # Rule-based responses for common healthcare queries
    if "symptom" in user_input or "feeling sick" in user_input:
        return "It seems like you're experiencing symptoms. Please consult a doctor for accurate advice."
    elif "appointment" in user_input or "schedule doctor" in user_input:
        return "Would you like me to schedule an appointment with a doctor?"
    elif "medication" in user_input or "prescription" in user_input:
        return "It's important to take your prescribed medications regularly. If you have concerns, consult your doctor."
    elif "side effect" in user_input or "reaction to medicine" in user_input:
        return "If you're experiencing side effects, it's best to consult your doctor immediately."
    elif "emergency" in user_input or "urgent help" in user_input:
        return "If this is an emergency, please call emergency services or visit the nearest hospital."
    elif "diet" in user_input or "nutrition" in user_input:
        return "Maintaining a balanced diet is important for good health. Consider consulting a nutritionist for personalized advice."
    elif "exercise" in user_input or "fitness" in user_input:
        return "Regular exercise is beneficial for both physical and mental health. Would you like some workout recommendations?"
    elif "mental health" in user_input or "feeling stressed" in user_input:
        return "Mental health is crucial. If you're feeling stressed, consider speaking to a professional or practicing relaxation techniques."
    elif "vaccination" in user_input or "vaccine" in user_input:
        return "Vaccinations are important for disease prevention. Would you like information on recommended vaccines?"
    elif "blood pressure" in user_input:
        return "Maintaining a healthy blood pressure is important. Regular check-ups and a healthy lifestyle can help."
    elif "diabetes" in user_input:
        return "Managing diabetes involves diet, exercise, and sometimes medication. Would you like tips on diabetes management?"
    elif "pregnancy" in user_input:
        return "Pregnancy requires proper care and regular check-ups. Do you need guidance on prenatal health?"
    elif "allergy" in user_input:
        return "Allergies can be managed with avoidance, medication, and sometimes immunotherapy. Do you need advice on allergy management?"
    elif "sleep" in user_input or "insomnia" in user_input:
        return "Good sleep hygiene is essential for health. Avoid caffeine before bed, maintain a routine, and limit screen time."
    elif "flu" in user_input or "cold" in user_input:
        return "Rest, hydration, and over-the-counter medications can help with flu symptoms. If symptoms persist, see a doctor."
    elif "skin care" in user_input or "dermatology" in user_input:
        return "Healthy skin starts with hydration, a good diet, and proper skincare. Do you need specific skincare recommendations?"
    elif "headache" in user_input or "migraine" in user_input:
        return "Headaches can be caused by stress, dehydration, or medical conditions. Rest, hydration, and pain relievers may help."
    elif "back pain" in user_input or "joint pain" in user_input:
        return "Back and joint pain can be relieved with stretching, proper posture, and physical therapy."
    elif "hydration" in user_input or "water intake" in user_input:
        return "Drinking enough water is essential for overall health. Try to drink at least 8 glasses a day."
    
    # If no predefined responses match, use the Hugging Face model to generate a response
    else:
        response = chatbot(user_input, max_length=200, num_return_sequences=1)
        return response[0]['generated_text']


# Streamlit app interface
def main():
    st.title("AI- powered Healthcare Assistant Chatbot")
    user_input = st.text_input("How can I assist you today?", "")
    if st.button("Submit"):
        if user_input:
            st.write("User: ", user_input)
            response = healthcare_chatbot(user_input)
            st.write("Healthcare Assistant: ", response)
        else:
            st.write("Please enter a query.")

if __name__ == "__main__":
    main()
