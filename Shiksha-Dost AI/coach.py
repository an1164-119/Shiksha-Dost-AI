import google.generativeai as genai

genai.configure(api_key="YOUR_GOOGLE_API_KEY")
model = genai.GenerativeModel('gemini-1.5-flash')

def get_advice(teacher_query, grade):
    mentor_persona = f"You are a supportive mentor for a {grade} teacher in a rural school. Give a simple, low-cost activity."
    response = model.generate_content(f"{mentor_persona}\nQuery: {teacher_query}")
    return response.text