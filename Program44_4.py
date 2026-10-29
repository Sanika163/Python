# Q4: Display students who scored more than 85 in Science. 

import pandas as pd 

def main():
    Data = {
        'Name': ['Amit', 'Sagar', 'Pooja'], 
        'Math': [85, 90, 78], 
        'Science': [92, 88, 80], 
        'English': [75, 85, 82]
    }

    df = pd.DataFrame(Data)

    # StudentList = (df[df['Science']>85]['Name'])
    # print("List of students who scored more than 85 in Science : ", StudentList)

    StudentList = df.loc[df['Science']>85, 'Name']
    print("List of students who scored more than 85 in Science : ", StudentList)

if __name__ == "__main__":
    main()