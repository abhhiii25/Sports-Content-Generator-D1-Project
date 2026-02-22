from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)
def generate_content(prompt: str):
    try:
        print("API KEY LOADED:", OPENAI_API_KEY)
        response = client.chat.completions.create(
            model="gpt-4o-mini",   # Recommended
            messages=[
                {"role": "system", "content": "You are a professional sports journalist."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception as e:
        print("OpenAI Error:", str(e))
        raise e
