# 🚀 AI Travel Planner – Internship Assignment

## 🔗 Live Demo  
👉 ("https://mananbagadi100-travel-itinerary-app-xbqxsm.streamlit.app")
    Please open this link in your browser.
---

## 🧠 Objective  
To build an AI-powered travel planner that interacts with users, understands their travel preferences, and generates a personalized day-by-day itinerary.

---

## 💡 Scenario  
The system acts as a travel assistant that asks for key travel details like budget, trip duration, destination, purpose, and preferences. Based on this, it generates curated activity suggestions and a travel itinerary.

---

## 📥 User Inputs Handled
- Destination  
- Starting Location  
- Budget (Low, Medium, High)  
- Trip Duration (1 to 14 days)  
- Purpose (Family, Leisure, Adventure, etc.)  
- Preferences (e.g., food, culture, specific requests like "good seafood")

---

## 🔄 Prompt System

### 🟨 System Prompt
> You are an AI travel planner. Based on user input, generate curated suggestions and an itinerary with grouped activities for each day.

### 🟩 User Prompt
> “I want to go to Goa with my family for 6 days. I have a low budget and love good seafood.”

### 🟦 Model Response (Sample)
**Day 2: North Goa Exploration**
- Visit Aguada Fort
- Beaches of Baga, Calangute
- Seafood lunch at a beach shack
- Night market at Arpora

*(...and so on for the entire trip)*

---

## 🔒 Security  
- Used Streamlit Secrets to store API key  
- `.env` and virtual environment folders are excluded via `.gitignore`  
- No secrets are pushed to GitHub

---

## 🧪 Tech Stack  
- Python  
- Streamlit  
- OpenAI API  
- GitHub for version control  
- Streamlit Cloud for deployment  

---

## 🧾 Run Locally  
```bash
git clone https://github.com/MananBagadi100/travel_itinerary.git
cd travel_itinerary
pip install -r requirements.txt
streamlit run app.py

---

## ⚠️ Limitations

- **No Real-Time Web Search**: The application does not fetch live data from the internet. All travel suggestions are based on prior training data of the language model.
- **Knowledge Cutoff**: The AI's responses are based on information available up to **September 2023** and may not include the latest travel advisories, hotel prices, or events.
- **Static Recommendations**: Recommendations like restaurant or hotel suggestions are generalized and not guaranteed to be up-to-date or available.
- **Not a Booking Tool**: The planner does not integrate with booking engines or provide reservation capabilities.

---


