#Load packages
from flask import Flask, render_template, redirect, request
import pandas as pd
import pickle
import emoji
import textstat
from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.ensemble import GradientBoostingClassifier
from func import *


# load model and dependencies
cv = pickle.load(open('models/cv.pkl','rb'))
tf = pickle.load(open('models/tf.pkl','rb'))
scaler = pickle.load(open('models/scaler.pkl','rb'))
model = pickle.load(open('models/Gradient_Boosting_Model.pkl','rb'))


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def main():
	return redirect('/index')

@app.route('/index', methods=['GET'])
def index():
	return render_template('index.html')


@app.route('/prediction', methods=['POST'])
def prediction():
	df3 = process_inputs()

	scaled = scaler.transform(df3)

	prediction = model.predict(scaled)
	probability = model.predict_proba(scaled)

	nb_prob = (probability[0][0] * 100).round(2)

	b_prob = (probability[0][1] * 100).round(2)

	if prediction == 1:
		result = "A Bot"
	else:
		result = "Not a Bot"

	#Create Chart
	labels = ["Bot", "Not a Bot"]
	values = [b_prob, nb_prob]

	column_labels = df3.columns.tolist()
	features = model.feature_importances_.tolist()

	# Zip together
	labels_features = list(zip(column_labels, features))

	#Create Dataframe
	results = pd.DataFrame(labels_features)
	results = results.rename(columns={0: "Feature", 1: "Importance"})
	results = results.sort_values(by=['Importance'], ascending=False).reset_index(drop=True)
	results = results.head(10)

	cLabels = results['Feature']
	cValues = results['Importance']

	return render_template('prediction.html', res_var=result, nb_prob_var= nb_prob, b_prob_var=b_prob, values=cValues, labels=cLabels)
   

def process_inputs():
	text_keys = ['Comment']
	int_keys = ['Score']
	inputs = {}

	for key, val in request.form.items():
		if key in int_keys:
			inputs[key] = int(val)
		else:
			inputs[key] = val

	df = pd.DataFrame(inputs, index=[0])

	#Feature Engineering
	#Emoji Count
	df["EmojiCount"] = df["Comment"].apply(split_count)

    #Replace Special Characters
	df['CommentClean'] = df['Comment'].str.replace('[^a-zA-Z]', ' ')
	df['CommentClean'] = df['CommentClean'].str.lower()
	
	#Get Comment Length
	df['CommentLength'] = df['CommentClean'].str.split().str.len()

	#Average Word Length
	df['CommentCharacters'] = df['CommentClean'].str.len()
	df['AvgWordLength'] = df['CommentCharacters'] / df['CommentLength']
	
	#Lexicon Count
	df["LexCount"] = df['CommentClean'].apply(textstat.lexicon_count)

	#Sentence Count
	df["SentenceCount"] = df['Comment'].apply(textstat.sentence_count)

	df["ReadEase"] = df['CommentClean'].apply(textstat.flesch_reading_ease)

	df["SyllableCount"] = df['CommentClean'].apply(textstat.syllable_count)


	#Count Vectorizer
	count_vector = cv.transform(df['CommentClean'])

	#TFIDF
	TFIDF = tf.transform(count_vector)

	#Create dataframe of features
	cv_df = pd.DataFrame(TFIDF.toarray(), columns=cv.get_feature_names()).add_prefix('Counts_')

	#Join dataframes
	df2 = df.join(cv_df)

	#Drop Columns
	df2 = df2.drop(['Comment', 'CommentClean'], axis=1)

	#Scale
	return df2

if __name__ == '__main__':
    app.run(debug=True)
