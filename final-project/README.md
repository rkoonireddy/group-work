# Final Project

### Final project for Digital Tools for Finance 2022

## App

Flask is a web framework, more precisely a Python module that lets you develop web applications easily. We've used it for the development of an interactive [App](app).

## Research Project

The [Final Code](final-code) folder contains the necessary code for running the research project. The code is provided in both .py and .pynb formats to accommodate different user preferences. In addition to the code, the folder includes stored parquet datasets, which were accessed via an API and used for calculations in the research project. These datasets are an essential component of the code and will be required for the successful execution of the project. 

## LaTeX and visualization

The [Project repport](project-report) folder contains the [Paper](project-report/paper) and [Presentation](project-report/presentation) files. The former includes all files associated with the LaTeX part of the documentation, which was completed using Overleaf. The latter includes a beamer presentation.

## Reproducibility

We have implemented two methods for reproducing our project. The first method involves using [Dockerfile](reproducibility-docker/Dockerfile).The second method involves using [Binder](https://mybinder.org/v2/gh/ncanto/group-work.git/main?labpath=final-project%2Ffinal-code%2FResearch_Final.ipynb). Both of these methods allow users to easily reproduce the project and its results.

The [Test code](test-code) folder contains code that we experimented with during development but did not include in the final version of the application. As a result, this folder has been added to the .gitignore file to prevent its contents from being committed to the repository.
    
<p><small>Project documentation based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
