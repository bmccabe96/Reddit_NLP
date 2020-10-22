# Reddit_NLP

## Introduction

The goal of this project is to pull comment data from political subreddits that are either biased to the 'Left' or the 'Right', and from those comments train a model to understand the linquistic differences between comments made on subreddits on opposite ends of the political spectrum.

**Model Use Case**
Sites like Reddit often times employ censorship (usually for filtering out heinous posts), but specific subreddits may have rules for allowable comments. If a forum-based company, like Reddit, wanted to censor opposing opinions from a political forum, the company could employ a model such as the one worked on in this project. A model like this one may also suit an authoritarian government, but hopefully that doesn't happen...I do enjoy speaking freely.

*Items of Note*
  * **Scripts**: Scripts for pulling data from reddit and storing in sql
  * **Analysis**: EDA and modeling
  * **Pics**: Various visualizations
  
## EDA and Visualization

### Class Imbalance

The following chart shows the class imabalance of our dataset after preprocessing. We see slightly more comments from left leaning subreddits. This is addressed by upsampling in the modeling notebook. We did not want to use SMOTE because we want our comments to be real, human-created comments, not artificially created by an algorithm.

![Image](Pics/Class_Imbalance.png?raw=true)

### Profanity

Here we can see that right leaning subreddits use slightly more profanity than left leaning subreddits, in terms of both count of total profane words in a comment, as well as number of profane words relative to the size of the comment (percentage).

We performed a two sample t test to test the hypothesis that we see in the graphs and found the difference to be significant. Additionally, we found an increase in model performance when we added this as a feature to our model (percent profane).

![Image](Pics/Profanity_Violinplot.png?raw=true) 
![Image](Pics/Profanity.png?raw=true)

### Word Clouds

For interest alone, we wanted to generate word clouds of the most frequent words. Our model uses TF IDF vectorization, though, so it is important to note that these "most frequent" words do not have a large impact on our models. 
#### Left Leaning
![Image](Pics/left_wc_final.png?raw=true)

#### Right Leaning
![Image](Pics/right_wc_final.png?raw=true)


## Modeling

### Baseline Model

Our baseline model for comparison was a simple dummy classifier. As expected, running this on our preprocessed data results in 50% accuracy (common for binary classification problems).

### Iteratibve Process and Improvement Through More Data

Throughout the week, we grabbed data from our data pulling script every morning. This resulted in better model performance every day, signifying the importance in more data for an NLP project such as this one.

#### The Feature Engineering
 * We tried using Word2Vec to create a model based off word vectorizations. This resulted in a decent score, but we did not tune it, as explained below
 * We then tried a simple TF IDF vectorization model
 * Lastly, we improved our TF IDF matric by appending custom features, such as lexical diversity and the use of profanity in a comment.
 
#### The Models
 * In the beginning, out of curiosity, we wanted to see how our dataset would react to an unsupervised learning algorithm. We implemented KMeans, and got an accuracy 61% -- we did not explore this further, but it was interesting to see that the algorithm picked up on some differences between the two groups. One possible reason it performed worse than the models we'll explain soon is that, for our supervised learning, we explicitly created two political groups, left and right. However, in reality, there are likely centrists and many other subgroups, representing more true classes then just simply 'left' and 'right'. So, KMeans may want to classify more than 2 groups. The plot below shows a clear first elbow for 3 classes.
 
 ![Image](Pics/sil_score.png?raw=true)

 * Random Forest Classification: This was the model we primarily used. It provided good scoring, is resistant to overfitting, handles outliers well, and allows us some insight into feature importance. We saw that our engineered features were important, and we also saw some of the words that were important in TFIDF vectorization, such as "underpaying" and "catastrophe".
 * Support Vector Machine Classification: This can be good for NLP, but for our project and the size of our dataset, it took too long to run the model each time (and we wanted to run lots and lots of models). This was performing about as well as Random Forest, but took a much longer amount of time so we went with Random Forest.



## Analysis and Conclusion

### Why We Chose our Model

Our best model was a random forest classification using TF IDF features merged with all of our custom features (we were happy about this, our feature engineering paid off!). See model for actual implementation. The model predicted on our test set (roughly 9,000 observations) with an accuracy of 94.49%. This is a pretty great accuracy for the scope of our business problem. Also to note, we chose accuracy as a metric because there is no big harm in false positives and false negatives in the same way that there is for medical diagnosis or credit fraud. Thus, a simple accuracy score makes sense when predicting classes that have equal "importance". 

We believe TF IDF performed better than word embeddings because the two ends of the political spectrum likely have some important buzzwords, which would empower a TF IDF model.

Of our custom features, "profanity" and "lexical diversity" provided the most importance in our random forest model. This insinuates that, in some way, there is some detectable difference regarding the use of profanity and the complexity of comments in these different subreddits. See EDA notebook for implementation. 

### Misclassification Analysis

TBD


## Next Steps

* Expand to new subreddits
* Expand from a simple binary classification. See if we can capture "centrists", "libertarians", etc.
* Test on a user level -- instead of classifying a comment, aggregate all comments for an active user
* Get hired by an authoritarian regime and squelch all hopes of free speech
