from ai_helper import generate_command
from executor import run_command

def main():
    print("Welcome to AI Windows Shell! Type 'exit' to quit.")

    while True:
        user_input = input(">> ")
        if user_input.lower() == "exit":
            break

        ai_cmd = generate_command(user_input)
        # print(f"[AI] → {ai_cmd}")

        output = run_command(ai_cmd)
        print(f"[Output] → {output}\n")

if __name__ == "__main__":
    main()
