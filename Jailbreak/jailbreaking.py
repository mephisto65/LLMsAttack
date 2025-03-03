from attacker_LLM import create_attacker_prompt,get_system_prompt_attacker
from victim_LLM import create_victime_answer,get_system_prompt_victim
from judge import create_judge_feedback,get_system_prompt_judge
from time import sleep
import argparse

def main(attacker_model, victim_model, judge_model,n_iterations=5):

#################### INIT ########################################

    iteration = 0                           # Init iteration
    tot_iteration = 0
    victim_answer = ""                      # Init answer
    judge_feedback= ""    
    history_attacker,history_victim=[{"role": "system", "content": get_system_prompt_attacker(iteration)}],[{"role": "assistant", "content": get_system_prompt_victim()}]   # Initialize histories
    history_judge = [{"role": "system", "content": get_system_prompt_judge()}]

###################################################################

    while True:

        while iteration < n_iterations :

            print(f"\niteration : {tot_iteration}\n")

            print("\n1. ------------------- Attacker creates a prompt.-------------------------------\n")
            attacker_prompt,history_attacker = create_attacker_prompt(attacker_model,history_attacker,iteration,victim_answer,judge_feedback=judge_feedback)
            print(f"{attacker_prompt}\n")

            if (attacker_model=="Mistral" and victim_model == "Mistral"): ########## delay to limit request per seconds because of the free plan from Mistral
                print("\nWaiting...\n") 
                sleep(1)

            print("\n2. ---------------- Victim answers to the prompt.-------------------------------\n")
            victim_answer,history_victim = create_victime_answer(victim_model,history_victim,attacker_prompt)
            print(f"{victim_answer}\n")

            if (victim_model=="Mistral" and judge_model == "Mistral"): ########## delay to limit request per seconds because of the free plan from Mistral
                print("\nWaiting...\n") 
                sleep(1)

            print("\n3. ------------------ Judge creates a feedback.--------------------------------\n")
            judge_feedback,history_judge = create_judge_feedback(judge_model,history_judge,victim_answer,attacker_prompt)
            print(f"{judge_feedback}\n")

            tot_iteration+=1
            iteration+=1

        # Ask the user whether to continue or stop
        next_step = input("\nClick 'Enter' to continue or 'q' to leave : ")
    
        if next_step.lower() == 'q':
            print("End of program.")
            break

        iteration = 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Automate LLM jailbreak testing.")
    parser.add_argument("--attacker-model", type=str, choices=["openAI", "Mistral","deepseek"], required=True, help="Specify the model which creates unethical prompts.")
    parser.add_argument("--victim-model", type=str, choices=["openAI", "Mistral","deepseek"], required=True, help="Specify the model to jailbreak.")
    parser.add_argument("--judge-model", type=str, choices=["openAI", "Mistral","deepseek"], required=True, help="Specify the model which analysis the attacker's prompt and the victim's answer to provide feedback")
    parser.add_argument("--n-iterations", type=int,required=False,help="Number of iterations to try before asking to the user if he wantss to continue the attack")
    args = parser.parse_args()
    main(args.attacker_model, args.victim_model, args.judge_model)
