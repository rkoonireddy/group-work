We created two ways to replicate our project for you to interact using jupyter-labs: 

Method 1 - using binder
---------------

Using a simple online service called Binder Interactive. You can find more information about binder here: https://mybinder.org/

--> To interactively run our code on jupyter lab you can use the following link directly without downloading here:
"" 
https://mybinder.org/v2/gh/ncanto/group-work.git/main?labpath=final-project%2Ffinal-code%2FResearch_Final.ipynb 

or 

https://mybinder.org/v2/gh/ncanto/group-work/d18d6bccff58fa0962301df49707a97b33ae4d33?urlpath=lab%2Ftree%2Ffinal-project%2Ffinal-code%2FResearch_Final.ipynb

"" 

Method 2 - docker image
---------
Using the docker image file we created
you can get our docker image from the following link on docker hub: <docker pull rkoonireddy/d2ff-final>

You must run the following commands interactively:
1. < docker run -it -p 8888:8888 jrny-final bash > 
--> this takes you into our docker image, then run this
2. < jupter lab --ip='0.0.0.0' --port=8888 --no-browser --allow-root >
once the second command is executed, you will see links to open jupyter lab in your browser. open it and open the attached ipynb file there. 