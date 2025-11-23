BUG_EXPLANATION_PROMPT = """
You are a tutor helping a beginner Python programmer.

The student wrote the following code:
{code}

It produced this error:
{error}

1. Explain the error in very simple language.
2. Mention the common beginner misconception.
3. Ask ONE guiding Socratic question instead of giving the full fix.
"""

HINT_PROMPT = """
You are a Python tutor generating hints for a beginner.

Exercise:
{exercise}

Hint level: {level}

Generate a hint at this level:
1 = tiny nudge
2 = conceptual explanation
3 = step-by-step plan
4 = full solution

Respond with only the hint.
"""
