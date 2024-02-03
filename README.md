# Dice-Simulator
## About the Project
### Aim
To create a dice roller simulator which randomly displays different numbers on the  sides of a dice when clicked on the roll dice button.

### Tech Stack
#### Used following technologies for the project:
- Python
- Pillow
- Tkinter
- VsCode

### File Structure
```python
Volume serial number is C270-B8A2
C:.
\---Dice-Simulator
    |   main.py
    |   README.md
    |   
    \---DiceImg
            d1.png
            d2.png
            d3.png
            d4.png
            d5.png
            d6.png
```

## Getting Started
### Prerequisites
#### Importing necessary libraries 

```python
pip install tkinter
```

```python
pip install pillow
```
### Execution
- Navigate to the 'DiceImg' folder in the main branch to download the required images.
- Execute the main.py file and ensure that correct file paths of images are included.

## Theory
### Tkinter LIBRARY IN PYTHON :
Python offers multiple options for developing GUI (Graphical User Interface). Out of all the GUI methods, tkinter is the most commonly used method. It is a standard Python interface to the Tk GUI toolkit shipped with Python. Python tkinter is the fastest and easiest way to create GUI applications. Creating a GUI using tkinter is an easy task.

To create a tkinter Python app:
- Importing the module – tkinter
- Create the main window (container)
- Add any number of widgets to the main window
- Apply the event Trigger on the widgets.


Importing a tkinter is the same as importing any other module in the Python code. Note that the name of the module in Python 2.x is ‘Tkinter’ and in Python 3.x it is ‘tkinter’.

```python
   import tkinter
```

There are two main methods used which the user needs to remember while creating the Python application with GUI.

Tk(screenName=None,  baseName=None,  className=’Tk’,  useTk=1): To create a main window, tkinter offers a method ‘Tk(screenName=None,  baseName=None,  className=’Tk’,  useTk=1)’. To change the name of the window, you can change the className to the desired one. The basic code used to create the main window of the application is:
```python
	m=tkinter.Tk() where m is the name of the main window object
```


- mainloop(): There is a method known by the name mainloop() that is used when your application is ready to run. mainloop() is an infinite loop used to run the application, wait for an event to occur and process the event as long as the window is not closed.

```python
	m.mainloop()
```



### Pillow LIBRARY IN PYTHON :
Python Imaging Library (expansion of PIL) is the de facto image processing package for Python language. It incorporates lightweight image processing tools that aids in editing, creating and saving images. Support for Python Imaging Library got discontinued in 2011, but a project named pillow forked the original PIL project and added Python3.x support to it. Pillow was announced as a replacement for PIL for future usage. Pillow supports a large number of image file formats including BMP, PNG, JPEG, and TIFF. The library encourages adding support for newer formats in the library by creating new file decoders.
If the IDE does not contain the Pillow library, we need to install it in the terminal.


### Random MODULE IN PYTHON :
Python has a built-in module that you can use to make random numbers.
In the code, random module has been used to select an image of dice having a number, randomly, so that it is randomly displayed when the button is clicked.

## Results
#### Every time the “Roll Dice” button is clicked, different numbers on the sides of the dice are displayed.
![Screenshot (245)](https://github.com/2412anushka/Dice-Simulator/assets/135850373/0e562ee8-de15-4c2f-b50e-7501a5fffabf)

![Screenshot (247)](https://github.com/2412anushka/Dice-Simulator/assets/135850373/eabca742-2eb1-423b-a5c8-b3de40f6e22f)

![Screenshot (249)](https://github.com/2412anushka/Dice-Simulator/assets/135850373/96f45d5f-3862-4578-b7c8-6b4ee9f5b23f)

![Screenshot (250)](https://github.com/2412anushka/Dice-Simulator/assets/135850373/c25d9bab-1fef-4816-a7a0-17e8bc690b72)

## Contributor
- [Anushka Yadav](https://github.com/2412anushka "SORRY")

## References
- [Create a Dice Roll Simulation Using Python](https://www.youtube.com/watch?v=CIm5vfsfgO0)