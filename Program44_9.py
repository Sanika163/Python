# Q9: Create a DataFrame with missing values and fill them with column mean. 

import pandas as pd
import numpy as np

def main():
    Data = {
        'Name': ['Amit', 'Sagar', 'Pooja'], 
        'Math': [85, 90, 78], 
        'Science': [92, 88, 80], 
        'English': [75, 85, 82]
    }

    df1 = pd.DataFrame(Data)

    Data2 = { 
        'Name': ['Amit', 'Sagar', 'Pooja'], 
        'Math': [np.nan, 76, 88], 
        'Science': [91, np.nan, 85] 
    }

    df = pd.DataFrame(Data2)
    print("DataFrame with missing values :\n", Data2)

    df = df.fillna(df.mean(numeric_only=True))
    print("Updated DataFrame values :\n", df)

if __name__ == "__main__":
    main()