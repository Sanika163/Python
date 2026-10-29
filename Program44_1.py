# Q1: Create a DataFrame for student marks and print basic information like shape, columns, and data types. 
# data = { 
#  'Name': ['Amit', 'Sagar', 'Pooja'], 
#  'Math': [85, 90, 78], 
#  'Science': [92, 88, 80], 
#  'English': [75, 85, 82] 
# } 

import pandas as pd 

def main():
    Data = {
        'Name': ['Amit', 'Sagar', 'Pooja'], 
        'Math': [85, 90, 78], 
        'Science': [92, 88, 80], 
        'English': [75, 85, 82]
    }

    df = pd.DataFrame(Data)

    print("Shape of data is : ", df.shape)

    print("Columns from Dataset are : ", df.columns)

    print("Data types of columns are : ", df.dtypes)

if __name__ == "__main__":
    main()