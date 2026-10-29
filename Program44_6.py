# Q6: Sort the DataFrame by 'Total' marks in descending order. 

import pandas as pd 

def main():
    Data = {
        'Name': ['Amit', 'Sagar', 'Pooja'], 
        'Math': [85, 90, 78], 
        'Science': [92, 88, 80], 
        'English': [75, 85, 82]
    }

    df = pd.DataFrame(Data)

    df['Total'] = df[['Math','Science','English']].sum(axis=1)
    
    sorted_df = df.sort_values(by=['Total'], ascending=False)

    print("Dataframe after sorting in descending order based on marks :\n", sorted_df)

if __name__ == "__main__":
    main()