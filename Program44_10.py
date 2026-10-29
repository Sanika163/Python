# Q10: Drop the 'English' column from original DataFrame. 

import pandas as pd
import numpy as np

def main():
    Data = {
        'Name': ['Amit', 'Sagar', 'Pooja'], 
        'Math': [85, 90, 78], 
        'Science': [92, 88, 80], 
        'English': [75, 85, 82]
    }

    df = pd.DataFrame(Data)

    df = df.drop('English', axis=1)

    print("DataFrame after dropping the English Column : \n", df)

if __name__ == "__main__":
    main()