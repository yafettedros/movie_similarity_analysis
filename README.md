Movie Similarity Recommender

This project uses cosine similarity and the MovieLens 100k dataset to identify the top 10 most similar movies to a given query title. The goal is to demonstrate how data science techniques can be used to power personalized recommendations for streaming platforms.

---

#Project Overview

*Objective*
Given a movie that a user likes, return the 10 most similar movies based on genre and user rating patterns.

*Why it matters:*
Streaming platforms rely on smart recommendation systems to keep users engaged. This project showcases how similarity assessment can drive such features using lightweight, interpretable methods.

---

#Technologies Used

- Python 3.x  
- pandas  
- scikit-learn  
- matplotlib  
- MovieLens 100k Dataset

---

#Methods

1. **Data Collection:**  
   Downloaded from:https://grouplens.org/datasets/movielens/100k/

2. **Data Preprocessing:**  
   - Merged movie metadata and rating data
   - Created binary genre vectors
   - Calculated average user ratings per movie

3. **Feature Engineering:**  
   Combined genre vectors and average ratings into a feature matrix.

4. **Similarity Metric:**  
   Used **cosine similarity** to compare movies in feature space.

---

#Query Examples

We analyzed three classic films and generated their top 10 most similar movie recommendations:

- *Star Wars*
- *Toy Story*
- *Titanic*

---

Write a Medium post describing use of similarity assessment for a data-science problem. Using methods from module 3, identify at least 3 "query" entities of interest in a dataset you determine, develop a ranking of the most similar elements to these queries, and list the top 10 most similar entities for each query. You may use any distance/similarity metric that is most appropriate for your analysis.  

Your post should include the following:

Describe a question you think can be answered by measuring similarity between data points, what specific stakeholder is asking this question, and what decision(s) the answer to this question will inform.
Describe the data that could answer this question, what fields it contains, and why it is relevant to your question.
Explain how you collected some subset of this data (e.g., libraries like requests, BeautifulSoup, tweepy, praw, etc. or from data archive).
Define how you are measuring similarity between data points; include what features you are using for measuring similarity, and which similarity metric you are using.
For each of your chosen query items, identify the top 10 most similar items in your dataset and list them.
Provide an answer to your question, explaining your analysis of the data you collected, and how it answers that question.
Include figures or tables summarizing your findings. 
Describe how you cleaned up this data, common bugs you think others might encounter, and how you fixed them, etc.
Discuss the limitations of your analysis. What’s missing? How might it be biased?
Include a link to one of your GitHub repositories that contains the code you have developed for this assignment.
When you have written your post, publish it via Medium, add your post it to the class publication via Medium, and submit the URL to it via Canvas.
