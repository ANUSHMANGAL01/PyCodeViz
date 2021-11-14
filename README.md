# PyCodeVis

This is an extension of the popular online tool Python Tutor. It alters the visualization by separating functional components like Functions and Class declarations. It also adds to the original by rendering separate details like For-Loops, If-conditions and code frequency.

Python Tutor -- http://pythontutor.com/ -- helps people overcome a fundamental barrier to learning programming: understanding what happens as the computer executes each line of a program's source code. Using this tool, you can write Python, Java, JavaScript, TypeScript, Ruby, C, and C++ programs in your Web browser and visualize what the computer is doing step-by-step as it executes those programs.

This tool was created by [Philip Guo](http://pgbovine.net/) in January 2010. [See project history](history.txt).

All documentation is viewable online at: https://github.com/pgbovine/OnlinePythonTutor/tree/master/v3/docs

### The New Version

The bcode ase has been borrowed from [this](https://github.com/ajesse11x/OnlinePythonTutor) repository.


### How To Run

All the code is in the v5-unity directory.
To run locally on your own computer, to run Python visualizations try:

```
pip install bottle # make sure the bottle webserver (http://bottlepy.org/) is installed
cd OnlinePythonTutor/v5-unity/
python bottle_server.py
```

You should see the visualizer at: http://localhost:8003/visualize.html

- Type the python code in the code box in the page that opens up
- Click the 'Visualize Code' button
- Move through the code by using the Next or Prev button. You can set-up intermediate stop points to directly jump between too
- The color of the code line number specifies the frequency of usage of that corresponding code line: grey, if unvisited and darkening shades of yellow to red to indicate increasing frequency
- There are four sections in the execution visualization: Functions & classes, Frames, Objects and For & If structures
- The Functions and Classes section shows all the global functions and class definitions
- The Frames section shows all the frame-wise variables both local and global
- The Objects section shows the complex objects connected to their declaration instance in the frames section
- The For and If section visualizes all the current open loops and iterations and shows various details such as the current iteration number and the truth value of the condition in the If

Traverse through the code and have a fun experience learning!



### The Code Alterations

All the code alterations are within the v5-unity/build/visualize.bundle.js file
Any change to this file will be directly reflected in the local pytutor when reloading


### Acknowledgments

For code or security contributions
- The original Python Tutor repository at: https://github.com/pgbovine/OnlinePythonTutor
- The forked repository: https://github.com/ajesse11x/OnlinePythonTutor

