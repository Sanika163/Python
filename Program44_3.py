# Q3: Add a new column 'Total' to the DataFrame as the sum of all subject marks. 

import pandas as pd 

def main():
    Data = {
        'Name': ['Amit', 'Sagar', 'Pooja'], 
        'Math': [85, 90, 78], 
        'Science': [92, 88, 80], 
        'English': [75, 85, 82]
    }

    df = pd.DataFrame(Data)

    # 1. df = df.assign(Total = df['Math'] + df['Science'] + df['English'])
    # 2. df['Total'] = df['Math'] + df['Science'] + df['English']
    # 3. Total = df['Math'] + df['Science'] + df['English']
    #    df['Total'] = Total
    # 4
    df['Total'] = df[['Math','Science','English']].sum(axis=1)

    print("Updated DataFrame is :\n", df)

if __name__ == "__main__":
    main()