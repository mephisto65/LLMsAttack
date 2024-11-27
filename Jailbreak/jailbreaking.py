from attacker_LLM import create_prompt
from victim_LLM import create_victime_answer
import json

def write_iteration(iteration):
    with open('info.json', 'w') as f:
        json.dump({"iteration": iteration}, f)

def get_attacker_prompt(file_name):
    with open(file_name, 'r') as json_file:
        data = json.load(json_file)
        attacker_prompt = data.get("attacker prompt")

        return attacker_prompt

def main():
    iteration = 0
    while True:
        print("\n1. Attacker crée un prompt.")
        attacker_json = create_prompt()
        
        print("\n2. Victime répond au prompt.")
        attacker_prompt = get_attacker_prompt("info.json")
        print(attacker_prompt)
        victim_answer = create_victime_answer(attacker_prompt)

        # Demander à l'utilisateur s'il veut continuer ou arrêter
        next_step = input("\nAppuyez sur 'Entrée' pour continuer ou 'q' pour quitter : ")
        iteration+=1
        write_iteration(iteration)
        if next_step.lower() == 'q':
            print("Fin du programme.")
            break

if __name__ == "__main__":
    main()