# How to solve TSP with Python

**NOTE:** This can be done after following the steps on the documentation for Atom and Python.

### 1.	Open the following link https://developers.google.com/optimization/routing/tsp#program1 It will give you instructions on how to solve the Traveling Salesmen Problem (TSP).


### 2.	Copy the following code and paste it on a new file inside Atom.

![Pic1](https://user-images.githubusercontent.com/47669890/58341743-907bf800-7e14-11e9-9fac-eb8f20a2f0be.png)
![Pic2](https://user-images.githubusercontent.com/47669890/58341755-983b9c80-7e14-11e9-8895-3ca030e1c42b.png)


### 3.	Save the file as TSPExample.py If you save any file with .py your coding will be with python language, it should appear as the image below.

![Pic3](https://user-images.githubusercontent.com/47669890/58341757-9b368d00-7e14-11e9-86be-69e7b1513142.png)
![Pic4](https://user-images.githubusercontent.com/47669890/58341758-9d005080-7e14-11e9-8ace-73869548f694.png)


### 4.	To run the code click Alt+R, on the bottom right side of the screen the result should appear.

![Pic5](https://user-images.githubusercontent.com/47669890/58341761-9f62aa80-7e14-11e9-970c-9ef6506c482b.png)


### 5.	To solve the SyntaxError with the print commands add a parenthesis like the example below to all the print commands.
![Pic6](https://user-images.githubusercontent.com/47669890/58341764-a1c50480-7e14-11e9-891e-0e42e81d2b1b.png)


Incorrect:  print "Total distance: " + str(assignment.ObjectiveValue()) + " miles\n"

Correct:  print ("Total distance: " + str(assignment.ObjectiveValue()) + " miles\n")
![Pic7](https://user-images.githubusercontent.com/47669890/58341773-a4275e80-7e14-11e9-841e-243e1530177e.png)


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

![Pic8](https://user-images.githubusercontent.com/47669890/58341781-a8ec1280-7e14-11e9-8d17-f890f31b3be9.png)
![Pic9](https://user-images.githubusercontent.com/47669890/58341788-ac7f9980-7e14-11e9-82af-532bc26b15f8.png)


C)	Download OR-Tools, copy- paste the link below inside the command prompt, like the image below. Click enter and it should appear successful download.

**`python -m pip install --user ortools`**

![Pic10](https://user-images.githubusercontent.com/47669890/58341791-aee1f380-7e14-11e9-844f-d630254ccb87.png)

### 7.	Open the atom TSP¬_Example.py and run it (Click Alt+R), the following result should appear.

![Pic11](https://user-images.githubusercontent.com/47669890/58341809-b6090180-7e14-11e9-9366-e1a500229d43.png)
