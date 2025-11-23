from openai import OpenAI
from prompts import HINT_PROMPT

client = OpenAI()

def generate_hint(exercise_text, level):
    prompt = HINT_PROMPT.format(exercise=exercise_text, level=level)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message["content"]
