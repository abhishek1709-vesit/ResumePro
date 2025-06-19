import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("API_KEY") 

def feedbackFromAi(content):
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
                            1) Provide an ATS Score out of 100, based on format, keyword usage, and clarity.

                            2) Give 4-5 specific and actionable improvement tips to help the candidate improve their resume's ATS compatibility.

                            3) Keep your feedback concise (under 100 words), but informative.
                            
                            4) Also add a short 4-5 lines paragraph after the points'''                 
                },
                {
                    "role": "user",
                    "content": content
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
