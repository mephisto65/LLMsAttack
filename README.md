# Jailbreak Prompt Refinement System

## Description

This project simulates a prompt refinement system where two entities interact: an "attacker" who refines a prompt to bypass model restrictions and a "victim" whose responses to these prompts are used to further refine the attack. The system generates a series of prompts and responses, iterating until the user decides to stop.

## Features

- **Attacker's Role**: The attacker refines a baseline prompt in each iteration to bypass restrictions by the model.
- **Victim's Role**: The victim answers the refined prompt, providing data for further refinement.
- **JSON-based data storage**: The prompts and responses are stored in a JSON file, enabling the iteration process.
- **Iteration-based interaction**: The attacker and victim interact in a loop, with each iteration refining the prompts based on the previous victim's answers.

## Installation

To run the project, ensure that you have Python 3.x installed along with the following dependencies:
- `openai`
- `json`
- `re`

## Usage

The program relies on a JSON file (info.json) to store iteration data, prompts, and victim responses. This file is automatically created and initialized when you first run the program.

To initialize the info.json file, run the following command:

python jailbreaking.py
