# Python & tkinter GUI to Merge Files

## The Problem
Let's pretend that you are a teacher with a group of 15 students. Each student is progressing towards reaching a certification, but in order to qualify for the final test, they must completed three initial certification levels. 

Your reporting system can provide you with reports for each certification level, but you want to see a combined report listing each student's name, and whether or not they have completed the required certification levels. 

## The Solution
Use Python to merge all three certification level reports into one single report. To make it prettier, the tkinter package is used to create a GUI so that files can easily be selected, merged, tested for correctness (no dropped rows here!), and exported as a csv file. 

The final file will show a 1.0 if the student has passed the certification level, or a 0 if they have not.

## Instructions
1. Download the input files report1.csv, report2.csv, and report3.csv along with the Python script file_merger.py.
2. In a terminal, install required packages from requirements.txt by running the following in terminal:
   ```
   pip install -r requirements. txt
   ```
3. Run file_merger.py
   ```
   python3 file_merger.py
   ```
4. A GUI will appear with four buttons:
    - Starting from the left-most button (Upload Files button), use the GUI to upload files, merge them, check for errors, and finally save to a csv!


<img width="798" alt="image" src="https://github.com/user-attachments/assets/a018328f-25d0-4ceb-9e0d-c9d3b899f4dc">
