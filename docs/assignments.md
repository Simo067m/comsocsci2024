---
layout: page
title: assignments
tagline: DTU 02467 Computational Social Science Course Spring 2024
description: A course led by Laura Alessandretti on Computational Social Science
---

 <div class="navbar">
     <div class="navbar-inner">
         <ul class="nav">
             <li><a href="#timeline">timeline</a></li>
             <li><a href="#groups">groups</a></li>
             <li><a href="#assignments12">assignments 1 and 2</a></li>
             <li><a href="#project-assignment">project assignment</a></li>
         </ul>
     </div>
 </div>



### <a name="timeline"></a>Timeline

[Assignment 1](https://nbviewer.org/github/lalessan/comsocsci2024/blob/main/assignments/Assignment1.ipynb?flash_cache=True)
Posted: During Lecture 4  
Due: Tuesday, Feb 27th, 23:59

Assignment 2
Posted: During Lecture 8  
Due: Tuesday, Apr 2nd, 23:59  


_Project Assignment A_  
Slides Due: Tuesday, Apr 16th, 23:59
Presentation: Wednesday, Apr 19th (in class)

_Project Assignment B_  
Due: Friday, May 10th, 23:59  


### <a name="groups"></a>Groups
* Assignments should be handed in in groups.
* You shall register in a group on DTU Learn. 
* Groups should have 3 members.
* You shall work in the same groups throughout the course.
* All group members should be familiar with every aspect of the assignment. Everyone in the group should be able to solve every exercise.
* It is possible to have fewer than 3 group members, but we judge all reports the same. 


### <a name="assignments12"></a>Assignments 1 and 2
The lectures in this class run over 8 weeks. Each week, I will post a number of exercises. After 4 lectures, I will post an assignment. 
The assignment is a subset of the exercises you have solved in the previous 4 weeks (including the ongoing week). 
This means that, if you solve the exercises each week, the assignments will be easy.
Follow carefully the instructions below to ensure your work is correctly submitted and assessed:

#### Repository Setup

- **Create a Private Repository**: Create a repository on GitHub or GitLab. This will allow me to review the commit history of each group member. Keep the repository private until the assignment deadline.
- **Collaboration**: Work collaboratively on the assignment within your group. It's important that each member is familiar with all exercises.
- **Jupyter Notebook**: Include a Jupyter notebook in your repository, named `Assignment1.ipynb` or `Assignment2.ipynb`, containing solutions to all exercises.
- **First Cell Requirements**: The initial cell must contain a link to your GitHub repository and a contribution statement, explaining how you have divided work among members of the group. If you have worked together, but all commits to the Github repository were made by one (or two) specific member(s) of the group, explain why. 
  
#### Submission Instructions

- **Ensure the code runs**: Make sure that your notebook runs and all outputs are visible. I recommend selecting `Kernel -> Restart and run all cells` before submission.
- **Verify Output**: Double-check that all outputs are correctly rendered. You'll be annoyed to get bad evaluations because no-one could see your plots or there were errors in the output.
- **Upload the Jupyter Notebook to DTU Learn**: Submit the Jupyter notebook on DTU Learn.
- **Make Repository Public**: Change your repository's visibility to public on the submission date.


#### Compliance 

- **Understand the Assignment**: Read questions carefully and ensure you understand exactly what I ask before answering.
- **Complete All Parts**: Make sure you address all sub-questions.  
- **Follow Instructions**: Follow any additional guidelines (specified in the assignment) regarding answer length, formatting, etc.

#### Notebook Formatting

You shall follow these formatting rules:

- **Divide Your Answers**: Do not solve all exercises in a single code cell. Organize your code according to the questions.
- **Question Repetition**: For clarity, repeat the question above its corresponding answer.
- **Conciseness**: Provide clear and concise answers, respecting any word limits set.
- **Code Documentation and Output formatting**: Include all necessary code and ensure it is well-documented and tidy. Avoid lengthy outputs and ensure there are no errors displayed.
- **Plot Formatting**: Format your plots properly. Label axes on plots and include explanatory text. 
- **Use of References**: Cite references appropriately following academic standards.
- **Objective Language**: Be precise, write in objective language (avoid: "I think ...", "In my opinion...", etc) - if you make an observation, support it with data.

**Important**: Non-compliance with the above instructions may negatively impact your evaluation (more on that below). 
    
   
#### Evaluation 

Your assignment will be assessed based on the following:

- **Individual Assignment Parts**:
    - Completeness (all questions/exercises have been answered/solved)
    - You have taken appropriate decisions to ensure the integrity/accuracy of your solution you have justified your choices
    - Code is implemented correctly
    - Your answers to the reflection and open questions demonstrate that you have understood the exercise and the course material. 
   
- **Notebook Formatting**:
  - Adherence to the provided formatting guidelines.
  - Quality and clarity of plots and figures.

**Scoring**: Scores are assigned on a scale from 0 (insufficient), 1 (sufficient), 2 (good) to 3 (excellent), with the possibility of half-point increments (e.g., 0.5, 1.5, 2.5). The overall evaluation is the average of these scores, including all individual parts and the notebook formatting evaluation. These scores are intended for feedback purposes and do not directly map to a grade in the standard Danish grading scale.

### <a name="project-assignment"></a>Project Assignment

The point of the Project Assignments is to try out the skills you've learned in the course on your own dataset. We've been working on understanding networks and natural language processing, so the idea is to find a dataset to analyze that will let you show off what you can do.


* [Standford Large Networks Dataset Collection](https://snap.stanford.edu/data/) is a collection of large network datasets.
* [Twitter API](https://developer.twitter.com/en/docs/twitter-api). You can use the Twitter API to collect data about Twitter users and their tweets.
* [Wikipedia API](https://www.mediawiki.org/wiki/API:Main_page) You can collect Wikipedia data for whatever you are into.
* You can also use data from specialized wikis (examples include [Wookiepedia](https://starwars.fandom.com/wiki/Main_Page), [Game of Thrones Wiki](https://gameofthrones.fandom.com/wiki/Game_of_Thrones_Wiki), [Simpson's Wiki](https://simpsons.fandom.com/wiki/Simpsons_Wiki), etc)
* [Netzschleuder](https://networks.skewed.de/). Another collection of Network Datasets.
* [Social Networks Awesome datasets](https://github.com/awesomedata/awesome-public-datasets#socialnetworks). Another collection of public social network datasets.

And new ideas for datasets are very welcome. You should work with something that interests you - that way the project will be much more fun to work on. You will be working together in groups just as for the first two assignments.


#### Project Assignment A

The first part of the final project is a 5 minute presentation, which should explain the central idea/concept that you will investigate in your final project. You're making the presentation so that I can give you feedback, and you can get ideas from other groups. The presentation must contain the following:

* An explanation of the central idea behind your project (what is the idea?, why is it interesting? which datasets did you need to explore the idea?, how did you download them)
* An outline on the elements you'll need to get to your goal & the implementation plan.
* A walk-through of your preliminary data-analysis, addressing
    * What is the total size of your data? (MB, number of rows, number of variables, etc)
    * What is the network you will be analyzing? (number of nodes? number of links?, degree distributions, what are node attributes?, etc.)
    * What is the text you will be analyzing?
    * How will you tie the two together?

But other than that, there are no constraints on the format. Note that you will present to the entire class.

Handing in the assignment: Simply upload your slides on DTU Learn.
Note that since Project Assignment A now requires significant data-work, you have 2 weeks to create the video presentation.

#### Project Assignment B

The deliverables for the Final project will be

__A website__. The website should contain your analysis, it should tell the story about the data that you're interested in getting across. The website should not be technical, but rather aim at using visualization and explanation to get your insights across to a non-scientific reader.

__An explainer Notebook__. The Notebook should contain all the behind the scenes stuff, details on the dataset, why you've selected this particular dataset, explanations of your choices regarding network analysis, etc. You should link to the notebook from the site.
The idea is that you can create much more complex, fun and interactive analysis (and visualizations) on line. So the website is a way for you to present your work in a way that everyone can understand it ... including dynamic visualizations, interactive analysis, etc, etc ... that would not work on a piece of paper.

#### More about the website

This part of the assignment is quite free. The main point of the website is to present your idea/analyses to the world in a way that showcases your use of what you've learned in class. It can be as simple as an old fashioned static web-page, and as complicated as you want it to be. Let your creativity run wild (but keep in mind that this is not a coding class - we care mostly about content and analysis).

The website should be self-contained and tell the story of your dataset without the need for the Explainer Notebook (the purpose of the notebook is to provide additional details for interested readers). Here are some requirements

* The page should say clearly what the dataset is and give the reader some idea of its most important properties (kind of Project Assignment A-style).
* The page should contain your network and text analysis (that's the main part).
* There should be download options for data sets (so the user can play around).
* You must link to the Explainer Notebook (more details below) that explains the details of your analysis (including all of the machine learning, the model selection, etc). You can achieve this with a link to a notebook displaying on the nbviewer.
* For hosting, I recommend using your DTU website or Github pages.


#### More on the explainer notebook

The notebook should contain your analysis and code. Please structure it into the following 4 sections

1. Motivation
    * What is your dataset?
    * Why did you choose this/these particular dataset(s)?
    * What was your goal for the end user's experience?
2. Basic stats. Let's understand the dataset better
    * Write about your choices in data cleaning and preprocessing
    * Write a short section that discusses the dataset stats (here you can recycle the work you did for Project Assignment A)
3. Tools, theory and analysis. Describe the process of theory to insight
    * Talk about how you've worked with text, including regular expressions, unicode, etc.
    * Describe which network science tools and data analysis strategies you've used, how those network science measures work, and why the tools you've chosen are right for the problem you're solving.
    * How did you use the tools to understand your dataset?
4. Discussion. Think critically about your creation
    * What went well?
    * What is still missing? What could be improved? Why?
