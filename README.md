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
![Image](Pics/left_leaning.png?raw=true)
![Image](Pics/right_leaning.png?raw=true)


## Modeling

### Baseline Model

### Iteratibve Process and Improvement Through More Data

### Best Model


## Analysis and Conclusion

### Why We Chose our Model

(note, talk about tfidf being better than word embeddings, probably because there are buzz words for left leaning vs right leaning)

### Misclassification Analysis



## Next Steps
