import subprocess

dangerous = ["format", "shutdown", "del", "rm", "rd", "rmdir", "erase"]

def is_safe(cmd):
    return not any(word in cmd.lower() for word in dangerous)

def run_command(cmd):
    if not is_safe(cmd):
        return "Blocked: Command may be dangerous."

    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout.strip() or result.stderr.strip()
    except Exception as e:
        return f"Error: {str(e)}"
