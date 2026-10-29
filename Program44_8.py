#Q8 : Plot a line chart of marks for 'Amit' across all subjects

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

    X = df.columns[1:4]
    Y = df.loc[df['Name'] == 'Amit', ['Math','Science','English']].values[0]

    plt.plot(X, Y, marker='o', markersize=8, linestyle='--')

    plt.title("Amit Progress Report")
    plt.xlabel("Subjects")
    plt.ylabel("Marks across all subjects")
   
    plt.show()

if __name__ == "__main__":
    main()