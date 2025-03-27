import streamlit as st
import openai
from dotenv import load_dotenv
import os

load_dotenv()

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Use your real key

st.title("AI Travel Planner")

# 🔹 Structured Input Fields
destination = st.text_input("Destination")
starting_point = st.text_input("Starting Location")
budget = st.selectbox("Budget", ["Low", "Moderate", "High"])
duration = st.slider("Trip Duration (days)", 1, 14, 5)
purpose = st.selectbox("Purpose", ["Leisure", "Adventure", "Family", "Romantic", "Business"])
preferences = st.text_input("Any specific preferences? (food, culture, etc.)")

# 🔹 Button to trigger response
if st.button("Generate Travel Plan"):
    if destination and budget and duration:
        prompt = f"""
        Plan a {duration}-day {purpose.lower()} trip from {starting_point} to {destination}.
        The budget is {budget.lower()}.
        Preferences include: {preferences if preferences else "not specified"}.
        Please provide a personalized day-by-day itinerary.
        """
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful travel planner."},
                {"role": "user", "content": prompt}
            ]
        )
        st.write(response.choices[0].message.content)
    else:
        st.warning("Please fill all the required fields.")
