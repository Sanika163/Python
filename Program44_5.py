# Q5: Replace 'Pooja' with 'Puja' in the 'Name' column. 

import pandas as pd 

def main():
    Data = {
        'Name': ['Amit', 'Sagar', 'Pooja'], 
        'Math': [85, 90, 78], 
        'Science': [92, 88, 80], 
        'English': [75, 85, 82]
    }

    df = pd.DataFrame(Data)

    # df = df.replace(to_replace="Pooja", value="Puja")
    
    df['Name'] = df['Name'].replace("Pooja", "Puja")

    print("Updated Column values are : ", df['Name'])

if __name__ == "__main__":
    main()