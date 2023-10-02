import argparse
import os
import json
import glob
import pandas as pd
import jsonlines
import pprint


class DataProcessor:
    
    def __init__(self, parent_folder):
        print("Processing data...")
        self.parent_folder = parent_folder
        self.jsonl_folder = os.path.join(parent_folder, 'Cat1', 'data')
        self.jsonl_files = glob.glob(os.path.join(self.jsonl_folder, '*.jsonl'))
        self.output_folder = os.path.join(parent_folder, 'Cat1', 'output')

    
    def process_data(self):
        print("Processing data...")
        pivot_file = os.path.join(self.jsonl_folder, 'en-US.jsonl')
        pivot_data = []

        with open(pivot_file, 'r', encoding='utf-8') as pivot_file:
            for line in pivot_file:
                item = json.loads(line)
                id_value = item.get('id', None)
                utt_value = item.get('utt', None)
                annot_utt_value = item.get('annot_utt', None)

                if id_value is not None:
                    pivot_data.append({'id': id_value, 'utt': utt_value, 'annot-utt': annot_utt_value})

        pivot_df = pd.DataFrame(pivot_data)

        if 'annot-utt' not in pivot_df.columns:
            pivot_df['annot-utt'] = ""

        for jsonl_file in self.jsonl_files:
            if jsonl_file != 'en-US.jsonl':
                file_data = []

                with open(jsonl_file, 'r', encoding='utf-8') as file:
                    for line in file:
                        item = json.loads(line)
                        id_value = item.get('id', None)
                        utt_value = item.get('utt', None)
                        annot_utt_value = item.get('annot_utt', None)

                        if id_value is not None:
                            file_data.append({'id': id_value, 'utt': utt_value, 'annot-utt': annot_utt_value})

                file_df = pd.DataFrame(file_data)
                merged_df = pd.merge(pivot_df, file_df, on='id', how='left')

                language_code = os.path.splitext(os.path.basename(jsonl_file))[0]

                excel_filename = f'en-{language_code}.xlsx'
                excel_file = os.path.join(self.output_folder, excel_filename)
                merged_df.to_excel(excel_file, index=False, engine='openpyxl')

        print("Excel files created successfully!")

    def categorize_data(self):
        print("Processing data...")
        languages = ['en', 'sw', 'de']

        for language in languages:
            for partition in ['train', 'dev', 'test']:
                folder_path = os.path.join(self.output_folder, language, partition)
                os.makedirs(folder_path, exist_ok=True)