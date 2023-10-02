#!/bin/bash

# Define the command you want to run on each file
COMMAND_TO_RUN="python main.py"  

# Define the parent folder (update with your actual parent folder)
PARENT_FOLDER="C:\Users\admin\Desktop\Python-Projects\CS"

# Process command-line arguments
while [[ $# -gt 0 ]]; do
    key="$1"
    case $key in
        -p|--process)
        PROCESS=true
        shift # past argument
        ;;
        -c|--categorize)
        CATEGORIZE=true
        shift # past argument
        ;;
        -t|--translate)
        TRANSLATE=true
        shift # past argument
        ;;
        *)
        # Unknown option
        echo "Unknown option: $1"
        exit 1
        ;;
    esac
done