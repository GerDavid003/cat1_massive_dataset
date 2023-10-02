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

        for jsonl_file in self.jsonl_files:
            language = None
            for lang in languages:
                if lang in jsonl_file:
                    language = lang
                    break

            if language:
                with open(jsonl_file, 'r', encoding='utf-8') as file:
                    data = [json.loads(line) for line in file]

                partitioned_data = {'train': [], 'dev': [], 'test': []}
                for item in data:
                    partition = item['partition']
                    partitioned_data[partition].append(item)

                for partition, partition_data in partitioned_data.items():
                    output_file = os.path.join(self.output_folder, language, partition, os.path.basename(jsonl_file))
                    with open(output_file, 'w', encoding='utf-8') as output:
                        for item in partition_data:
                            json.dump(item, output, ensure_ascii=False)
                            output.write('\n')

        print("Data categorization and saving completed.")

    def translate_data(self):
        print("Processing data...")
        input_folder = os.path.join(self.parent_folder, 'Cat1', 'data')
        pivot_file = os.path.join(self.jsonl_folder, 'en-US.jsonl')
        partition_to_extract = 'train'

        en_us_translations = {}
        with jsonlines.open(pivot_file, 'r') as reader:
            for item in reader:
                if item['partition'] == partition_to_extract:
                    en_us_translations[item['id']] = item['utt']

        translations = {}

        for jsonl_file in self.jsonl_files:
            lang = os.path.splitext(os.path.basename(jsonl_file))[0]
            translations[lang] = []

            with jsonlines.open(os.path.join(self.jsonl_folder, jsonl_file), 'r') as reader:
                for item in reader:
                    if item['partition'] == partition_to_extract:
                        translation_item = {
                            'id': item['id'],
                            f'{lang}_utt': item['utt'],
                            'English-Translation': en_us_translations.get(item['id'], 'Translation not found in English'),
                        }
                        translations[lang].append(translation_item)

        output_file = os.path.join(self.output_folder, 'en-xx.json')
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, 'w', encoding='utf-8') as json_file:
         json.dump(translations, json_file, indent=4, sort_keys=True, separators=(',', ': '))

    
        print(f"Translations saved to '{output_file}'.")