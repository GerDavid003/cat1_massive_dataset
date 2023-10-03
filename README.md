# Massive dataset manipulation
## Introduction
This project involves data manipulation with JSON files from amazon MASSIVE dataset in relation to the following tasks

## Project Tasks
## Question 1: python3 environment setup 
In this section, you will set up the python 3 environment and work with the MASSIVE dataset

Task 1 : Build a python3 project with the structure of projects installing the necessary dependencies in preffered IDE (pycharm, visual studio) then import the MASSIVE dataset https://github.com/alexa/massive

Task 2 : generate "en-xx.xlxs" files for all languages, using id, utt and annot_utt. Recursion is not used due to its heavy time complexity.

Task 3 : have the flags running the solution in the run_script.sh

## Question 2: Working with files 
In this question, you will be manipulating JSON files to produce required outputs:

Task 1: generate seperate JSONL files for English (en), Swahili (sw) and German (de) with test, train and dev.

Task 2: generate a single JSON file showing all the translations from en to xx with id and utt for all the train sets(pretty print your json file structure)

## Task pre-requisites 
The following are the prerequisites to complete these tasks:
* Python3 Development Environment
* Amazon Massive Dataset

## Installation 
1.  Clone the repository to your local device
   ```command line
git@github.com:GerDavid003/cat1_massive_dataset.git
```
2. Setup a virtual environment
   ```command line
   virtualenv venv
   ```
3. Import the MASSIVE dataset to the dataset folder the MASSIVE dataset can be found in https://github.com/alexa/massive.

4. Install all the required dependencies needed to run the project
   ```command line
   python -r pip install requirements.txt
   ```


