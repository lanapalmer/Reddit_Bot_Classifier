![Header Image](https://github.com/lanapalmer/Reddit_Bot_Classifier/blob/master/Figures/RedditBotClassifierHeader.png)

# Bot or Not? Bot Classification on Reddit #

## Introduction ##

## Motivation ## 

## Data Collection & Cleaning ## 
![Data Collection Notebook](https://github.com/lanapalmer/Reddit_Bot_Classifier/blob/master/RBC_1_DataCollection.ipynb)

## Exploratory Data Analysis ## 
![EDA Notebook](https://github.com/lanapalmer/Reddit_Bot_Classifier/blob/master/RBC_2_EDA.ipynb)

## Feature Engineering ##
![Feature Engineering Notebook](https://github.com/lanapalmer/Reddit_Bot_Classifier/blob/master/RBC_3_FeatureEngineering_PreProcessing.ipynb)

## Algorithms and Machine Learning ## 

## Model Evaluation ## 
![Model Evaluation Notebook](https://github.com/lanapalmer/Reddit_Bot_Classifier/blob/master/RBC_4_Model_Eval_Analysis.ipynb)

## Model Deployment and Predictions ##
![Flask App Repository](https://github.com/lanapalmer/Reddit_Bot_Classifier/tree/master/app)
I built a Flask app which takes a user-submitted Reddit comment and score, processes the data, and provides a prediction with probabilities. 

![Deployed Model Screenshot](https://github.com/lanapalmer/Reddit_Bot_Classifier/blob/master/Figures/DeployedScreenshot.png)

You can view the app at https://reddit-bot-or-not.herokuapp.com/, or on my website: http://lanapalmer.io/reddit-bot-classifier/

## Conclusion and Caveats ## 

## Next Steps ##

I would love to build a second model which works on a user-basis, rather than on a comment basis. For this model, I would take a rolling average of all features for a user's most recent posts. I believe this model will have a higher accuracy rate, as the originality of Bot posts will be, on average, much lower than for human users.

## Credits ## 
Thank you to my Springboard mentor Blake Arensdorf for helping me to hone my skills, and guiding this process with patience and precision. Thank you to Scott Lundberg for the Shap library, Shivam Bansal and Chaitanya Aggarwal for their Textstat library, and to Reddit and Pushshift for providing public access to Reddit data.


## References ## 
