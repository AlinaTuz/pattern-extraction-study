# Scientific Conference Data Analysis

This Jupyter Notebook (Assigment3.ipynb) is designed to analyze data related to scientific conference papers. The analysis includes several stages aimed at identifying trends, thematic areas, and evaluating various aspects of the submitted papers and their review process.

Key stages of the analysis:

* **Paper Filtering:** Dividing papers into "accepted" and "rejected" based on reviewer scores.
* **Keyword Clustering:** Using TF-IDF and K-Means to identify the main research themes in the submitted papers. Results are visualized using PCA and t-SNE.
* **Thematic Area Analysis:** Comparing the number of accepted and rejected papers within each cluster to identify preferred research topics.
* **Identification of Popular Keywords:** Determining the most frequently occurring keywords to understand dominant research directions.
* **Sentiment Analysis:** Assessing the sentiment of paper abstracts.
* **Investigating the Influence of Reviewer Experience:** Analyzing the relationship between a reviewer's experience level and their decision on a paper using statistical methods (chi-squared, logistic regression).
* **Correlation Analysis:** Studying the interrelationships between paper ratings, review text length, and reviewer experience.

## Available Files:

1.  `Assigment3.ipynb` – The Jupyter Notebook containing all the analysis code and its description.
2.  `tp_2020conference.xlsx` – The Excel data file used for the analysis. (Ensure this file is in the same directory as the notebook, or provide the correct path to it in the code). Link to Excel data file: https://github.com/Seafoodair/Openreview/blob/master/data/ICLR%20data/tp_2020conference.xlsx

## Prerequisites/Dependencies:

To run the notebook correctly, you need to install the following Python libraries:

* pandas
* scikit-learn (sklearn: TfidfVectorizer, KMeans, PCA, TSNE, LogisticRegression, OneHotEncoder, train\_test\_split, classification\_report, confusion\_matrix, LabelEncoder)
* matplotlib
* textblob
* scipy
* seaborn
* openpyxl (for reading .xlsx files)

You can install them using pip:
```bash
pip install pandas scikit-learn matplotlib textblob scipy seaborn openpyxl
```

## Execute Cells:

Run the notebook cells sequentially, one after another (e.g., using Run All).