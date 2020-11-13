![Header Image](https://github.com/lanapalmer/Reddit_Bot_Classifier/blob/master/Figures/RedditBotClassifierHeader.png)

# Bot or Not? Bot Classification on Reddit #

## Introduction ##

While the word ‘bot’ may evoke images of artificially intelligent robots run amok, most bots found on online message boards are simple software programs written to execute commands and automate mundane tasks. Bots on Reddit range from the innocuous, such as ![u/JImmyButler](https://www.reddit.com/user/JlmmyButler), a bot that replies to users with compliments, the administrative, like the many moderator bots used to help subreddit ‘mods’, and the simply annoying, such as bots that spam URLS. 

Social media platforms are currently setting new precedents for free speech vs misinformation, and the proliferation of bots and 'inauthentic' accounts only exacerbate these concerns. Left unchecked, bots can pose a threat to public health during a pandemic, the democratic process during an election, and the stock market in the midst of a global recession. 

With this project, I will develop a classifier that can predict whether a comment on the Reddit platform was made by a bot or a human user. 

## Data Collection & Cleaning ## 
![Data Collection Notebook](https://github.com/lanapalmer/Reddit_Bot_Classifier/blob/master/RBC_1_DataCollection.ipynb)

I used the [Pushshift API](https://pushshift.io/) to collect Reddit comments from both bots and non-bots. In order to ensure the authenticity of my non-bot data set, I verified that the accounts were human users by reading several of their posts and comments. My non-bot data set includes a mix of users, from celebrities [u/janellemonae](https://www.reddit.com/user/janellemonae), popular Redditors [u/dickfromaccounting](https://www.reddit.com/user/dickfromaccounting), and a selection of regular users.

To gather bots, I used Beautiful Soup to scrape a list of ![known bots on Reddit](https://www.reddit.com/r/autowikibot/wiki/redditbots). 

For both bots and non-bots, I collected the following features:

* Author: The Redditor username, i.e. [PresidentObama](https://www.reddit.com/user/presidentobama)
* Comment: The raw comment, which may contain emojis and links.
* Subreddit: The subdirectory the comment was posted on.
* Score: The total upvotes/downvotes, which may be a negative number
* Time: The epoch time of the comment.
* Flair: A special designation that can be awarded by moderators in each subreddit.

The data did not require extensive cleaning, as null values were excluded from the API call. I converted Epoch time to datetime, and added 'Class' feature to specify the comments as from Bots or Non-Bots, and merged the two data frames.

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

