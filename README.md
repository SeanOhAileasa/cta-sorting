< [GMIT Data Analytics](https://web.archive.org/web/20201029063153/https://www.gmit.ie/computer-science-and-applied-physics/higher-diploma-science-computing-data-analytics-ict) | [Home](https://github.com/SeanOhAileasa) | [README](https://github.com/SeanOhAileasa/cta-sorting/blob/main/README.md) >

[![GMIT](https://github.com/SeanOhAileasa/SeanOhAileasa/blob/master/rc/gmit.png?raw=true)](https://web.archive.org/web/20201029063153/https://www.gmit.ie/computer-science-and-applied-physics/higher-diploma-science-computing-data-analytics-ict)

## Computational Thinking with Algorithms - Course Material 2021
### Topic: [Sorting](https://nbviewer.jupyter.org/github/SeanOhAileasa/cta-sorting/blob/main/cta-sorting.ipynb)

Course material for the ``Computational Thinking with Algorithms`` module (5 Credits) of the ``Higher Diploma in Science in Computing (Data Analytics) (H.Dip)`` programme (75 Credits) at **Galway-Mayo Institute of Technology (GMIT)**.

## Learning Outcomes

The aim of the module is to provide a comprehensive grounding in solving computational problems and designing algorithms.

1. Apply structured methodology to problem solving and computing.

2. Designing algorithms to solve computational problems.

3. Critically evaluate and assess the performance of algorithms.

4. Translate real world problems into problems that can be solved through computation.

Keeping in mind the ambiguity or imprecision that in the real-world humans deal with quite well, however computers are very precise and are much less able to deal with flexibility. A key skill is translating real-world problems into computational problems (precisely communicate an intention to the computer).

## Topic Roadmap

- Define the concept of sorting/sorting problems [1].

- Define mathematically the conditions for sorting [1].

- Define the idea of a comparator function (sorting algorithms which work based on comparisons) [1].

- Define the concepts of sort keys and satellite data [1].

- Define the desirable properties for sorting algorithms: i) stability - preserving the relative ordering of elements which are equally valued; ii) efficiency - making sure that the algorithms chosen are appropriate for the specific class of input instances and also to make sure that they will run in an acceptable amount of time; iii) in-place sorting - relates to memory usage when sorting [1].

- Brief overview of some well-known sorting algorithms. Considering the criteria which might be used to choose an appropriate sorting algorithm from these well-known algorithms [1].

## Getting Started
- Keeping in mind: i) GMIT assignment/project submission marking scheme; and ii) impression given to someone who is looking at this repository, endeavour to provide direct evidence of each of the items listed in each category where applicable - ``Research`` - ``Development`` - ``Consistency`` - ``Documentation``:

1. Research:

	- GMIT: **"Evidence of research performed on topic; submission based on referenced literature, particularly academic literature; evidence of understanding of the documentation for any software or libraries used."**

	- Investigation of packages used as demonstrated by references, background information, and approach: References will be in the format:

		- [referenceNumber] authorNames, referenceTitle, locationWebsiteBookVideo, dateMonthYear.

	- Demonstrating work complete with appropriate references and not just for the problem but for level of understanding of the problem.

	- Code commentary will include details of package, module, object (if applicable) to demonstrate understanding of software documentation and libraries used. Enhancements to completed GMIT projects/assignments for self-examination and preparation for future modules of the H.Dip programme/self-education will not include this detail.

```python
# b_T_hird_P_arty-imports
from matplotlib.pyplot import plot
```
```python
# package matplotlib - module pyplot
plot(x,y)
```

2. Development:

	- GMIT: **"Environment can be set up as described; code works without tweaking and as described; code is efficient, clean, and clear; evidence of consideration of standards and conventions appropriate to code of this kind."**

	- Clear, well-written, and efficient code with appropriate comments - using Jupyter Notebook markdown cells to summarise concise workings. 

	- As much as possible use the ``Style Guide for Python Code`` [Guido van Rossum](https://web.archive.org/web/20201029095211/https://www.python.org/dev/peps/pep-0008/). User-defined [Coding Conventions](#coding-conventsions) to be given separate section within this README.

3. Consistency:

	- GMIT: **"Evidence of planning and project management; pragmatic attitude to work as evidenced by well-considered commit history; commits are of a reasonable size; consideration of how commit history will be perceived by others."**

	- Git commits blurb to include number of days outstanding before deadline (if applicable).

	- Commits to highlight changes made since the last commit so that reviews of the git history can demonstrate compartmentation of work into the different sections.   

4. Documentation:

	- GMIT: **"Clear documentation of how to create an environment in which any code will run, how to prepare the code for running, how to run the code including setting any options or flags, and what to expect upon running the code. Concise descriptions of code in comments and README."**

	- Include descriptions/plots of theoretical and practical aspects of the problem(s) - comments to be very concise for ease of readability. 

	- Descriptions of code requiring further explanation will be presented in Jupyter Notebook markdown cells prior to code execution.   

## Considerations

- Using the four listed categories - ``Research`` - ``Development`` - ``Consistency`` - ``Documentation`` - in an attempt to not only focus on programming but also look at the information - data - manipulating the data and coming up with techniques.

- Sometimes the most complex algorithms are counter-intuitive but do work and have been proven to work. Sometimes only a few lines of code is required to complete a topic/section - endeavour to explain the development of the algorithm and the reasoning behind why/how the code works.

- Jupyter Notebook text formatting/presentation to be tidied up closer to the deadline (if applicable).

## Coding Conventions

- user-defined function / name (variable) - start with letters as follows

| Example       | Signify 		          |
| :------------ |:------------------------|
|	f        	|	user-defined function |
|	n        	|	name - no variables   |

## Prerequisites

###### Anaconda

- Require Python to be loaded on your local machine. Recommend downloading and installing Anaconda.

https://www.anaconda.com/download/

###### IPyPlot

- ``IPyPlot`` is a small Python package offering fast and efficient plotting of images using ``IPython`` with HTML for displaying large numbers of images. [[Reference](http://web.archive.org/web/20201103205220/https://github.com/karolzak/ipyplot)]

- installed through ``PyPI``:

```
pip install ipyplot
```

- installed directly from repo using pip:

```
pip install git+https://github.com/karolzak/ipyplot
```

## Execute Jupyter Notebook

- The software must be downloaded and run on a machine as follows:

	- Clone the repository with the following command:

	``git clone https://github.com/SeanOhAileasa/cta-sorting.git``

    - Run Jupyter Notebooks from the command line with the following:

	``jupyter notebook``

    - Open notebook - ``cta-sorting.ipynb``

    - Once running within the Jupyter environment can navigate with ease - links are plentiful.

	- ***Notebook links will not work on github given that github renders as static HTML - also not able to view equation tag numbers. Please run on a local machine or use nbviewer (see below).***

- An alternative to downloading and running on a local machine with all features included (links/equation tag number etc) can view via [nbviewer](https://nbviewer.jupyter.org/github/SeanOhAileasa/cta-sorting/blob/main/cta-sorting.ipynb).

## END