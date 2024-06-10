# Importing all the relevant packages.

## WARNING: After pressing run, the script will take around 1-2 minutes to run.
## untill it computes the final results.

import spacy #This statement should work if you have spaCy installed 
import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report


from spacytextblob.spacytextblob import SpacyTextBlob
!python -m textblob.download_corpora

# Loading the english language small model
nlp = spacy.load('en_core_web_sm')

# Loading the spacytextblob to do the polarity analysis
nlp.add_pipe('spacytextblob')


#1)====================IMPORTING THE AMAZON REVIEWS===================

data = pd.read_csv("amazon_product_reviews.csv", index_col=0)

reviews_data=data[['reviews.text']]

# cleaning the data:
clean_data=reviews_data.dropna()
clean_data=reviews_data.dropna(subset=['reviews.text'])

#Dropping the index column with the id. We will now only have 5000 numerical rows.
clean_data.reset_index(drop=True, inplace=True)


#2)====================FUNCTION TO PREPROCESS THE TEXT USING SPACY======
def preprocess(text):
    doc = nlp(text)
    cleaned_tokens = [token.lemma_.lower() for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(cleaned_tokens)


#3)====================CREATING THE REVIEWS DATAFRAME==================

# Creating 3 empty lists to store the sentiment and reviews.
sent_score_list=[]      #Sentiment Score list, float
sent_type=[]            #Sentiment type, string -> Positive, Neutral , Negative
rev_list=[]             #Reviews list, string

# Looping through the reviews and placing them into a list.
for i in range(0,len(clean_data)):
    
    clean_data['reviews.text'][i]

    # Extracting the reviews and appending them to rev_list
    reviews=preprocess(clean_data['reviews.text'][i])
    rev_list.append(reviews)

    # Extracting the reviews and working out its polarity and appending it to the sent_score_list
    sentiment=nlp(preprocess(clean_data['reviews.text'][i]))
    sent_score_list.append(sentiment._.blob.polarity)

    # Adding the classification of the sentiment: positive, neutral and negative depending on the polarity score
    if sentiment._.blob.polarity==0:
        sent_type.append("Neutral")
    elif sentiment._.blob.polarity<0:
        sent_type.append("Negative")
    else:
        sent_type.append("Positive")

# converting the lists into numpy arrays
sent_score_arr = np.array(sent_score_list)
sent_type_arr = np.array(sent_type)
rev_arr = np.array(rev_list)

#creating 3 dataframes: Reviews , Sentiment_Score and Sentiment_Type
rev_df=pd.DataFrame(rev_arr)
sent_score_df=pd.DataFrame(sent_score_arr)
sent_type_df=pd.DataFrame(sent_type_arr)

# Concatenating the separate data frames into a single data frame
sent_analysis_df=pd.concat([rev_df,sent_score_df,sent_type_df],axis=1)
sent_analysis_df.columns=['Reviews','Sentiment_Score','Sentiment_Type']

#4)==============SPLITTING THE DATA INTO TRAINING AN TEST SETS=========

X_train, X_test, y_train, y_test = train_test_split(sent_analysis_df['Reviews'], sent_analysis_df['Sentiment_Type'], test_size=0.2, random_state=42)

# Create a CountVectorizer with and without preprocessing
vectorizer_unprocessed = CountVectorizer()
X_train_unprocessed = vectorizer_unprocessed.fit_transform(X_train)
X_test_unprocessed = vectorizer_unprocessed.transform(X_test)

# Train a Naive Bayes classifier on the unprocessed data
clf_unprocessed = MultinomialNB()
clf_unprocessed.fit(X_train_unprocessed, y_train)
y_pred_unprocessed = clf_unprocessed.predict(X_test_unprocessed)

print("Results without preprocessing:")
print(f"Accuracy: {accuracy_score(y_test, y_pred_unprocessed)}")
print(classification_report(y_test, y_pred_unprocessed))