# Python Challenge
## Python Homework - Py Me Up, Charlie!

### Task
There are two challenges in this homework task - PyBank and PyPoll.

In the PyBank challenge we are required to analyse the financial records of a company using a Python script. 
We are provided with a budget_data.csv file which contains two columns: _Date_ and _Profit/Losses_

A Python script needs to be created that analyses the budget file and provides the below results:

* The total number of months included in the dataset.
* The net total amount of "Profit/Losses" over the entire period.
* Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes.
* The greatest increase in profits over the entire period - include the month and amount.
* The greatest decrease in losses over the entire period - include the month and amount.

The results need to be printed to the terminal and a text file with the results needs to be exported.

In the PyPoll challenge we are analysing the election data of a town.
We are provided with a election_data.csv file which contains three columns: _Voter ID_ , _County_ and _Candidate_

A Python script needs to be created that analyses the election file and provides the below results

* The total number of votes cast.
* A complete list of candidates who received votes.
* The percentage of votes each candidate won.
* The total number of votes each candidate won.
* The winner of the election based on popular vote.

The results need to be printed to the terminal and a text file with the results needs to be exported.

### Method

## PyBank
The Python script starts by importing the csv file and setting up the code so that we can analyse the data from the csv file. 

The first calculations in the script look at each row in the budget file and adds up the number of rows in the file and sums the profit. Two lists are then created – a list that stores all the totals from the file and list that stores the months in the dataset.

Next the profit/loss variance from month to month is calculated by using a for loop and comparing the current value to the previous value. Once the variance is identified, it is added to a new list (called change_list) and then the current value becomes the new previous value. 

The script then sums up the vales in the change list and determines the length of the list so the average variance can be calculated.
The script then determines the greatest positive and negative variance in the change list. The index of each variance is identified and then used to determine the corresponding month of each variance.

The results are then changed into currency format.

The final results are printed to the terminal and a text file displaying the results is exported.

Note: For further explanation on the method used, please refer to the comments in the code.

## PyPoll
The Python script starts by importing the csv file and setting up the code so that we can analyse the data from the csv file. 

The first calculations in the script determines the unique candidates in the data and creates a list to store these names. The script also creates a dictionary to that stores the candidates name and the number of votes each candidate gets.

The script then sums all the values in the dictionary to determine the total number of votes.

The dictionary is then split into 2 separate lists – one for the candidate names and one for their vote total. Using the values list, the percentages are then calculated and stored in a new list.

Therefore 3 lists are currently in use:
*	The list of candidate names
*	The list of candidate votes
*	The list of candidate percentages

Due to the way lists are created, we can be confident in knowing that the first entry in each list relates to each other.
The winner of the vote is then determined by finding the maximum value in the original candidate dictionary. 
The results are then printed to the terminal and a text file displaying the results is exported.

Note: For further explanation on the method used, please refer to the comments in the code.

### Results
The Python scripts will print the below to the terminal and to a text file.

## PyBank
### Terminal
![PyBank terminal print](https://user-images.githubusercontent.com/82348616/119446973-92b21d80-bd72-11eb-9438-de3d1fd4acb0.PNG)

### Text file
![PyBank text print](https://user-images.githubusercontent.com/82348616/119446993-9a71c200-bd72-11eb-98b4-5e2b37938a06.PNG)

## PyPoll
### Terminal
![PyPoll terminal print](https://user-images.githubusercontent.com/82348616/119447024-a3629380-bd72-11eb-93da-555ec11d45ac.PNG)

### Text file
![PyPoll text print](https://user-images.githubusercontent.com/82348616/119447037-a8bfde00-bd72-11eb-9018-a9681fef631f.PNG)

### Files
This repo consists of a PyBank folder and a PyPoll folder. Each folder contains a script titled _main.py_ which should be used to analyse the data.
Each folder also consists of an additional folder titled "Resources" which contains the csv file being analyse, and a folder titled "Analysis" which is where the text filed is exported to.
