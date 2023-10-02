import argparse
import os
from functions import DataProcessor

def parse_arguments():
    print("Processing data...")
    parser = argparse.ArgumentParser(description="Data Processing Pipeline")
    parser.add_argument('--parent_folder', type=str, required=True, help="Path to the parent folder")
    parser.add_argument('--process', action='store_true', help="Process data")
    parser.add_argument('--categorize', action='store_true', help="Categorize data")
    parser.add_argument('--translate', action='store_true', help="Translate data")
    return parser.parse_args()

def main():
    args = parse_arguments()
    parent_folder = args.parent_folder

    # Create an instance of the DataProcessor class with the parent_folder variable
    data_processor = DataProcessor(parent_folder)

    if args.process:
        data_processor.process_data()
    if args.categorize:
        data_processor.categorize_data()
    if args.translate:
        data_processor.translate_data()

if __name__ == "__main__":
    main()
