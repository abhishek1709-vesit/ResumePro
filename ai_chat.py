
from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()
api_key = os.getenv("API_KEY") 
def ai_chat(content, question):
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        data=json.dumps({
            "model": "deepseek/deepseek-r1-0528:free",
            "messages": [
                {
                "role": "system",
                "content":'''You are a professional resume analyzer specializing in Applicant Tracking System (ATS) optimization.
                            You will receive the raw text extracted from a user’s resume (from PDF).
                            Your tasks are:
                            1) Answer the questions by the user in 5 to 10 words but informative content
                            2) Rely only on the resume content provided.'''                 
                },
                {
                    "role": "user",
                    "content": f"Resume; {content}"
                },
                {
                    "role": "user",
                    "content": f"User question: {question}"
                }
            ],
        })
    )

    if response.status_code == 200:
        data = response.json()
        # print(data)
        return (data["choices"][0]["message"]["content"])
    else:
        return f"Error:, {response.status_code}, {response.text})"
   