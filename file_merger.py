# Standard library imports
import os
from tkinter.filedialog import askopenfilenames
import tkinter as tk

# Third-party library imports
import openpyxl
import pandas as pd

def import_excel_data():
    print("Function started")
    filepaths = askopenfilenames() # show an "Open" dialog box and return the path to the selected file
    print("Filepaths obtained:",filepaths)
    dataframes = {"report1.csv": "Level1",
                  "report2.csv": "Level2",
                  "report3.csv": "Level3" }
    
    #Updating global variables by generating a dict looping over filepaths and adding entries to new dict
    #key for new dict is resulting value obtained when using filename from dataframes dict as a key. 
    globals().update({dataframes[filepath.split("/")[-1]]: pd.read_csv(filepath) for filepath in filepaths if filepath.split("/")[-1] in dataframes})

    print("DataFrames created")
    textbox.insert(tk.INSERT,"Upload complete.\n")
      
def interact_with_data():
    df = pd.concat([Level1,Level2,Level3])
    
    list(df.columns.values)

    # rename columns
    global codes
    codes = df[["Name","Level Code"]].rename(columns={
        "Name": "NAME","Level Code": "LEVELCODE"
    })

    codes = (
        codes.groupby(["NAME","LEVELCODE"],
            dropna=False,).size().reset_index(name="counts")
        .sort_values(by=["NAME"])
        )

    print(codes.head())

    # chain pivot_table and fillna operations
    codes = pd.pivot_table(
        codes,
        values="counts",
        index=["NAME"],
        columns="LEVELCODE",
    ).reset_index().fillna(0)

    print(codes.head())

    for col in ["Level1", "Level2", "Level3"]:
        codes[col].mask(codes[col] > 1, 1, inplace=True)

      
    codes = codes.reindex(
        columns=["NAME","Level1","Level2","Level3"])

    textbox.insert(tk.INSERT,"File merge complete.\n")

def logic_tests():
    textbox.insert(tk.INSERT,"Checking for dropped rows during the file merge.\n")
    print(codes.head())
    
    #Helper function
    def check_codes(df_orig, orig_col, codes_col, message):
        a = df_orig[orig_col].nunique()
        df1 = df_orig[[orig_col]].copy()
        df1.drop_duplicates(subset=orig_col, inplace=True, keep="first")
        df1["SOURCE"] = "_test"
    
        df2 = codes[[codes_col]].copy()
        df2["SOURCE"] = "codes"
        df2 = df2[(df2[codes_col] == 1)]
        b = len(df2)
    
        if a == b:
            textbox.insert(tk.INSERT, message + " okay\n")
        else:
            textbox.insert(tk.INSERT, f"Original number of names in {message} report not the same as final {message} count\n")

    check_codes(Level1, "Name", "Level1", "Level1")
    check_codes(Level2, "Name", "Level2", "Level2")
    check_codes(Level3, "Name", "Level3", "Level3")
   

def format_to_csv():
    # Renaming columns using a dictionary of names
    codes.rename(
        columns={
            
            "NAME": "Student Name",
            "Level1": "Level 1: Cadet",
            "Level2": "Level 2: Journeyman",
            "Level3": "Level 3: Practioner",
           }, inplace=True
    )

    # Insert "Classification" column in case results are sensitive
    codes["Classification"] = "Confidential"

    # Sorting dataframe
    codes.sort_values(by=list(codes.columns), inplace=True, ascending=True)

    # Exporting dataframe to csv
    path = os.getcwd()
    export_path = os.path.join(path, 'results.csv')
    codes.to_csv(export_path, index=False, header=True)
    textbox.insert(tk.INSERT, "File exported.")

#############################################################################
root = tk.Tk()  # setting up the root window
root.geometry('800x600')  # set window size
root.title('Report Merger')
frame = tk.Frame(root)  # container widget
frame.pack()

textbox = tk.Text(root)
textbox.pack()

# Define the button properties in a list of dictionaries
buttons = [
    {"text": "Upload Files", "command": import_excel_data},
    {"text": "Merge Files", "command": interact_with_data},
    {"text": "Check for Errors", "command": logic_tests},
    {"text": "Save to CSV", "command": format_to_csv},
]

# Use a loop to create the buttons
for button in buttons:
    tk.Button(frame, text=button["text"], fg="blue", command=button["command"]).pack(side=tk.LEFT)

# Create a label to display messages
message_label = tk.Label(frame, text="")
message_label.pack()

root.mainloop()


    
  
    
    
    
    
    
    
