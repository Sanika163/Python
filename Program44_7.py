# Q7: Create a bar plot of student names vs total marks. 

import pandas as pd
import matplotlib.pyplot as plt

def main():
    Data = {
        'Name': ['Amit', 'Sagar', 'Pooja'], 
        'Math': [85, 90, 78], 
        'Science': [92, 88, 80], 
        'English': [75, 85, 82]
    }

    df = pd.DataFrame(Data)

    df['Total'] = df[['Math','Science','English']].sum(axis=1)

    X = df['Name']
    Y = df['Total']

    plt.bar(X, Y, width=0.4, edgecolor='black', color='purple', alpha = 0.6)

    plt.title("Student Name Vs Total Marks")
    plt.xlabel("Student Names")
    plt.ylabel("Total Marks")
    
    plt.show()

if __name__ == "__main__":
    main()