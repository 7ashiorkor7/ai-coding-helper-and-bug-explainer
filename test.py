from bug_whisperer import explain_bug
from hint_generator import generate_hint

code_sample = "x = 1 + 1"

print("Bug explanation:")
print(explain_bug(code_sample))

print("Generated hint:")
print(generate_hint(code_sample))
