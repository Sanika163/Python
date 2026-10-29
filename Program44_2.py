# Q2: Use the DataFrame from Q1 and print descriptive statistics using .describe(). 

import pandas as pd 

def main():
    Data = {
        'Name': ['Amit', 'Sagar', 'Pooja'], 
        'Math': [85, 90, 78], 
        'Science': [92, 88, 80], 
        'English': [75, 85, 82]
    }

    df = pd.DataFrame(Data)

    print("Dataframe description  : ", df.describe())

if __name__ == "__main__":
    main()