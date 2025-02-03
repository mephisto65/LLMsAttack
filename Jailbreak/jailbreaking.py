from attacker_LLM import create_attacker_prompt,get_system_prompt_attacker
from victim_LLM import create_victime_answer,get_system_prompt_victim
from judge import create_judge_feedback,get_system_prompt_judge

def main():

#################### INIT ########################################

    iteration = 0                           # Init iteration
    victim_answer = ""                      # Init answer
    judge_feedback= ""    
    history_attacker,history_victim=[{"role": "system", "content": get_system_prompt_attacker(iteration)}],[{"role": "assistant", "content": get_system_prompt_victim()}]   # Initialize histories
    history_judge = [{"role": "system", "content": get_system_prompt_judge()}]

###################################################################
 
    while True:
        print("\n1. ------------------- Attacker creates a prompt.-------------------------------\n")
        attacker_prompt,history_attacker = create_attacker_prompt(history_attacker,iteration,victim_answer,judge_feedback=judge_feedback)
        print(f"{attacker_prompt}\n")
        
        print("\n2. ---------------- Victim answers to the prompt.-------------------------------\n")
        victim_answer,history_victim = create_victime_answer(history_victim,attacker_prompt)
        print(f"{victim_answer}\n")

        print("\n3. ------------------ Judge creates a feedback.--------------------------------\n")
        judge_feedback,history_judge = create_judge_feedback(history_judge,victim_answer,attacker_prompt)
        print(f"{judge_feedback}\n")

        # Ask the user whether to continue or stop
        next_step = input("\nClick 'Enter' to continue or 'q' to leave : ")
        iteration+=1
        if next_step.lower() == 'q':
            print("End of program.")
            break

if __name__ == "__main__":
    main()
