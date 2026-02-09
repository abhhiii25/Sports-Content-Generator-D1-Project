from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key="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")

def generate_content(prompt: str):
    try:
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
