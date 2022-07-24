
import os
import pandas as pd
import sys
import tkinter.filedialog as tkfd


def generate_index(path=None):
    path = path if path else tkfd.askdirectory() # Request path if not provided

    df = pd.DataFrame(columns=['File'])
    for root, _ , files in os.walk(path):
        files = [f for f in files if not f.startswith('~') and f!='Thumbs.db']
        df1 = pd.DataFrame({'File': files, 'Value': 0})
        df = df.append(df1)
    df = df.reset_index(drop=True)
    return df
  
if __name__ == '__main__':
    df = generate_index("/home/kshitiz/Downloads/research/Data/Valid/benign")
    df.to_excel('Valid_benign.xlsx')