from RestrictedPython import compile_restricted, safe_globals, limited_builtins

def run_user_code(user_code):
    try:
        byte_code = compile_restricted(user_code, "<string>", "exec")
        env = {"__builtins__": limited_builtins}
        exec(byte_code, safe_globals, env)
        return "No error. Code executed successfully."
    except Exception as e:
        return str(e)
