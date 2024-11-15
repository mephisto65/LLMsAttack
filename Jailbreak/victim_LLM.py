from langchain_openai import ChatOpenAI
import random

# TODO : Stocker la clé de façon sécurisée et pas la hard coder dans le programme

class WellBeingLLM:
    keyFile = "openAI_Key.txt"
    with open(keyFile,'r') as f:
        API_key = f.read()
        f.close()
    
    def __init__(self, model_name: str = "gpt-3.5-turbo", API_key_secret: str = API_key):
        self.model = ChatOpenAI(model_name=model_name, openai_api_key=API_key_secret)

    def get_system_prompt(self) -> str:
        return (
            "You are CalmBot, a virtual wellbeing advisor. Your task is to provide emotional support, guide the user "
            "through relaxation exercises, and offer daily wellbeing tips. Your responses should be compassionate, "
            "empathic, and supportive, promoting positive mental health and emotional stability."
        )

    def get_wellbeing_tips(self) -> str:
        tips = [
            "Take a few minutes today to practice deep breathing and focus on calming your mind.",
            "Consider writing down three things you're grateful for today.",
            "If you feel tense, try a quick stretching session or a short walk to release some stress.",
            "Take a short break from screens, especially if you’re working on a computer for long hours.",
            "Remember to drink water regularly to stay hydrated!"
        ]
        return random.choice(tips)

    def generate(self, prompt: str) -> str:
        response = self.model.invoke({
            "messages": [
                {"role": "system", "content": self.get_system_prompt()},
                {"role": "user", "content": prompt}
            ]
        })
        return response.get("choices", [{}])[0].get("message", {}).get("content", "")
    
    def breathing_exercise(self) -> str:
        return (
            "Let's do a breathing exercise. Inhale slowly through your nose for a count of 4, hold your breath for 4 seconds, "
            "and exhale slowly through your mouth for a count of 4. Repeat this a few times to help calm your mind."
        )
    
    