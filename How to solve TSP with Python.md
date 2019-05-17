# How to solve TSP with Python

**NOTE:** This can be done after following the steps on the documentation for Atom and Python.

### 1.	Open the following link https://developers.google.com/optimization/routing/tsp#program1 It will give you instructions on how to solve the Traveling Salesmen Problem (TSP).


### 2.	Copy the following code and paste it on a new file inside Atom.

![1](/Pic1.png)

![2](/Pic2.png)


### 3.	Save the file as TSPExample.py If you save any file with .py your coding will be with python language, it should appear as the image below.

![3](/Pic3.png)

![4](/Pic4.png)

### 4.	To run the code click Alt+R, on the bottom right side of the screen the result should appear.

![5](/Pic5.png)

### 5.	To solve the SyntaxError with the print commands add a parenthesis like the example below to all the print commands.

![6](/Pic6.png)

Incorrect:  print "Total distance: " + str(assignment.ObjectiveValue()) + " miles\n"

Correct:  print ("Total distance: " + str(assignment.ObjectiveValue()) + " miles\n")

![7](/Pic7.png)

### 6.	To solve the OR-Tools Error you must follow the instructions below:
https://developers.google.com/optimization/install/python/windows (Link with same instructions as below)


A)	 You must have one of the following Python versions
    - Python 3.7x 64-bit from python.org
    - Python 3.6x 64-bit from python.org
    - Python 3.5x 64-bit from python.org
    - Python 2.7x 64-bit from python.org
    
B)	Verify that you have pip 9.01 or higher (If you have one of the Python versions above you must have this pip version), to do that open the command prompt (Like the image below), copy-paste the following link and click enter. The results from the last image must 

**`python --version
python -c "import platform; print(platform.architecture()[0])"
python -m pip --version
`**

![8](/Pic8.png)
![9](/Pic9.png)

C)	Download OR-Tools, copy- paste the link below inside the command prompt, like the image below. Click enter and it should appear successful download.

**`python -m pip install --user ortools`**


![10](/Pic10.png)
### 7.	Open the atom TSP¬_Example.py and run it (Click Alt+R), the following result should appear.

![11](/Pic11.png)
