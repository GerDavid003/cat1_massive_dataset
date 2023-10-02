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