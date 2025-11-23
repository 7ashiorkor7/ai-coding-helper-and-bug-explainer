from openai import OpenAI
from prompts import BUG_EXPLANATION_PROMPT
from sandbox import run_user_code

client = OpenAI()

def explain_bug(user_code):
    error_output = run_user_code(user_code)

    # If no error, return simple message
    if "No error" in error_output:
        return "Your code ran without errors!"

    prompt = BUG_EXPLANATION_PROMPT.format(code=user_code, error=error_output)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message["content"]
