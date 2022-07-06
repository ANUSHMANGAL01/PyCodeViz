# PyCodeViz - An Interactive Visualization Tool to Facilitate Program Comprehension

This is an improved version of the popular online tool Python Tutor. It alters the visualization by separating functional components like Functions and Class declarations. It also adds to the original by rendering separate details like Loops, If-conditions and code frequency. It is only made for Python.

Python Tutor -- http://pythontutor.com/ -- helps people overcome a fundamental barrier to learning programming: understanding what happens as the computer executes each line of a program's source code. Using this tool, you can write Python, Java, JavaScript, TypeScript, Ruby, C, and C++ programs in your Web browser and visualize what the computer is doing step-by-step as it executes those programs.

This tool was created by Philip Guo in January 2010. [See project history](history.txt).


### The New Version

The basecode has been borrowed from [this](https://github.com/ajesse11x/OnlinePythonTutor) repository.

This work is then further borrowed from [this](https://github.com/saidattatiruvuru/PythonCodeVisualizer) repository.

I was asked to add some more features to the above repository. I, being a beginner, made some visual changes and added some more features such as detection of recursive functions, adding the feature to show and hide the output, color coding of lines, and some more similar minor changes.
This was my first work and I was introduced to JavaScript, HTML and CSS because of this. It took some time to understand and do everything. 
The work was done in around 15 or so days because of time constraints. However, this work is important to me as I learned a lot doing this.  

I also made a github page for this repository. It is [here](https://anushmangal01.github.io/PyCodeVizDoc/).

### Papers
I, along with my senior Eashaan A. Rao, and my mentor, Dr. Sridhar Chimalakonda, wrote the research paper for this work to submit in ICPC Demo 22 and ICSE Demo 22 tracks. The works, although were not accepted, taught me a lot in terms of paper writing and the effort it takes to do everything. 

The files are Mangal_Rao_Chimalakonda_PyCodeViz_ICPCDemo22.pdf and Mangal_Rao_Chimalakonda_PyCodeViz_ICSEDemo22.pdf



### How To Run

All the code is in the v5-unity directory.
To run locally on your own computer, to run Python visualizations try:

```
pip install bottle # make sure the bottle webserver (http://bottlepy.org/) is installed
cd PyCodeViz/v5-unity/
python bottle_server.py
```

You should see the visualizer at: http://localhost:8003/visualize.html

- Type the python code in the code box in the page that opens up
- Click the 'Visualize Code' button
- Move through the code by using the Next or Prev button. You can set-up intermediate stop points to directly jump between too
- The color of the code line number specifies the frequency of usage of that corresponding code line: grey, if unvisited and darkening shades of yellow to red to indicate increasing frequency
- There are four sections in the execution visualization: Classes and functions, Frames, Objects and Loop & If structures
- The Functions and Classes section shows all the global functions and class definitions
- The Frames section shows all the frame-wise variables both local and global
- The Objects section shows the complex objects connected to their declaration instance in the frames section
- The Loop and If section visualizes all the current open loops and iterations and shows various details such as the current iteration number and the truth value of the condition in the If

Traverse through the code and have a fun experience learning!



### The Code Alterations

All the code alterations are within the v5-unity/build/visualize.bundle.js file
Any change to this file will be directly reflected in the local pytutor when reloading


### Acknowledgments

For code or security contributions
- The forked repository: https://github.com/ajesse11x/OnlinePythonTutor

