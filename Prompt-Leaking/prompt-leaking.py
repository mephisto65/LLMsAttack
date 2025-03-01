from victim_LLM import create_victime_answer

import json

def init_json(file_name):
    """
    Creates Json file or reinitializes it
    """
    with open(file_name,'w') as json_file:
        data = {}
        data["iteration"] = [0]
        data["prompt"] = []
        data["victim answer"] = []

        json.dump(data,json_file,indent=4)

def write_iteration(iteration):
    """
    Update json file
    """
    with open('Prompt-Leaking/info.json', 'r') as f:
        data = json.load(f)
        data["iteration"][0] = iteration
        f.close()
    with open('Prompt-Leaking/info.json', 'w') as f:
        json.dump(data,f,indent=4)

def main():
    iteration = 0
    while True:
        print("\n1. Attacker creates a prompt.")

        attacker_prompt=str(input("Enter the prompt to try to make leak the internal prompt of the victim : "))

        print("\n2. Victim answers to the prompt.")

        victim_answer = create_victime_answer(attacker_prompt)

        # Demander à l'utilisateur s'il veut continuer ou arrêter
        next_step = input("\nClick 'Enter' to continue or 'q' to leave : ")
        iteration+=1
        write_iteration(iteration)
        if next_step.lower() == 'q':
            print("End of program.")
            break

if __name__ == "__main__":
    init_json("Prompt-Leaking/info.json")
    main()