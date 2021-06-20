import os
import pandas as pd

UPLOAD_FOLDER = 'files'
INPUT_FILENAME = 'ab.xlsx'
OUTPUT_FILENAME = 'c.xlsx'
input_file_path = os.path.join(UPLOAD_FOLDER, INPUT_FILENAME)
output_file_path = os.path.join(UPLOAD_FOLDER, OUTPUT_FILENAME)

def test():
    # read values from input file
    df_ab = pd.read_excel(input_file_path)
    a = df_ab['a'].iloc[0]
    b = df_ab['b'].iloc[0]
    # perform summation
    c = a + b
    # save value to output file
    df_c = pd.DataFrame({'c':[c]})
    df_c.to_excel(output_file_path, index=False)
    return a, b, c