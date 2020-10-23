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

We performed a two sample t test to test the hypothesis that we see in the graphs and found the difference to be significant (p value 2.007e-139). Additionally, we found an increase in model performance when we added this as a feature to our model (percent profane).

![Image](Pics/Profanity_Violinplot.png?raw=true) 

### Lexical Diversity

Here we analyzed the lexical diversity of comments in the two subreddits -- for us this meant (# unique words) / (# total words). The chart below does not show a clear difference, but after running a two sample t test, we got a p value (.0002) that did indeed show significance. Spoiler, later on in the modeling, adding in lexical diversity as a feature added to model performance.

![Image](Pics/Lexical_Div_Violinplot.png?raw=true)

### Word Clouds

For interest alone, we wanted to generate word clouds of the most frequent words. Our model uses TF IDF vectorization, though, so it is important to note that these "most frequent" words do not have a large impact on our models. 
#### Left Leaning
![Image](Pics/left_wc_final.png?raw=true)

#### Right Leaning
![Image](Pics/right_wc_final.png?raw=true)


## Modeling

### Baseline Model

Our baseline model for comparison was a simple dummy classifier. As expected, running this on our preprocessed data results in 50% accuracy (common for binary classification problems).

### Iterative Process and Improvement Through More Data

Throughout the week, we grabbed data from our data pulling script every morning. This resulted in better model performance every day, signifying the importance in more data for an NLP project such as this one.

#### The Feature Engineering
 * We tried using Word2Vec to create a model based off word vectorizations. This resulted in a decent score, but we did not tune it, as explained below
 * We then tried a simple TF IDF vectorization model
 * Lastly, we improved our TF IDF matric by appending custom features, such as lexical diversity and the use of profanity in a comment.
 
#### The Models
 * In the beginning, out of curiosity, we wanted to see how our dataset would react to an unsupervised learning algorithm. We implemented KMeans, and got an accuracy 61% -- we did not explore this further, but it was interesting to see that the algorithm picked up on some differences between the two groups. One possible reason it performed worse than the models we'll explain soon is that, for our supervised learning, we explicitly created two political groups, left and right. However, in reality, there are likely centrists and many other subgroups, representing more true classes then just simply 'left' and 'right'. So, KMeans may want to classify more than 2 groups. The plot below shows a clear first elbow for 3 classes.
 
 ![Image](Pics/sil_score.png?raw=true)

 * Random Forest Classification: This was the model we primarily used. It provided good scoring, is resistant to overfitting, handles outliers well, and allows us some insight into feature importance. We saw that our engineered features were important, and we also saw some of the words that were important in TFIDF vectorization, such as "fizzled" and "catalyst".
 * Support Vector Machine Classification: This can be good for NLP, but for our project and the size of our dataset, it took too long to run the model each time (and we wanted to run lots and lots of models). This was performing about as well as Random Forest, but took a much longer amount of time so we went with Random Forest.
 * MN Bayes: Decent results, but again not as good as RFC, so we didn't explore to much here.



## Analysis and Conclusion

### Why We Chose our Model

Our best model was a random forest classification using TF IDF features merged with all of our custom features (we were happy about this, our feature engineering paid off!). See model for actual implementation. The model predicted on our test set (roughly 9,000 observations) with an accuracy of 94.49%. This is a pretty great accuracy for the scope of our business problem. Also to note, we chose accuracy as a metric because there is no big harm in false positives and false negatives in the same way that there is for medical diagnosis or credit fraud. Thus, a simple accuracy score makes sense when predicting classes that have equal "importance". 

We believe TF IDF performed better than word embeddings because the two ends of the political spectrum likely have some important buzzwords, which would empower a TF IDF model.

Of our custom features, "profanity" and "lexical diversity" provided the most importance in our random forest model. This insinuates that, in some way, there is some detectable difference regarding the use of profanity and the complexity of comments in these different subreddits. See EDA notebook for implementation. 

**The following wordcloud is off the feature importance from our best model -- includes most important words, as well as our custom features, indicated with a leading X** 

![Image](Pics/top_100.png?raw=true)


### Misclassification Analysis

Reading through some of the misclassified comments, we noticed the following:
* This is a comment from a left-leaning sub that was guessed incorrectly. Our model likely associates affinity for guns with right-leaning subreddits, when in reality there are certainly comments in left-leaning subreddits that are okay with guns. 
```
In my 8th grade class there was a class you could choose to take and part of it they taught us about guns. At the end of the firearm segment we got to go to a range and shoot .22s It was a very fun class.
```
* The following comment comes from a right-leaning subreddit and proves that not all right-leaning subreddit comments necessarily indicate a preference towards a republican potus. Our model guessed 'Left', due to the nature that this comment represents disatisfaction for Trump...and, it does. However, this comment actually comes from a right-leaning sub. This means that simply labeling all comments from a right or left leaning sub will always have some noise. Thankfully, from the results of our models, the noise is small enough that, for the most part, our accuracy is still good.
```
I live in a complete red zone. I'm the only one I know that doesn't worship Trump. It can be a bit much to process at times....so I feel your pain.
```

## Next Steps

* Expand to new subreddits
* Expand from a simple binary classification. The elbow plot from our KMeans analysis points us this way. See if we can capture "centrists", "libertarians", etc.
* Test on a user level -- instead of classifying a comment, aggregate all comments for an active user
* Get hired by an authoritarian regime and squelch all hopes of free speech
