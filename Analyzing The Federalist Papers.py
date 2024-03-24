#!/usr/bin/env python
# coding: utf-8

# In[7]:


file_path = "E:\\UGrad\\Advance Python\\assignment\\federalist.txt"

with open(file_path, "r", encoding="utf-8") as file:
    file_contents = file.read()


print(file_contents)



# In[10]:


import nltk
from nltk.tokenize import word_tokenize

tokens = word_tokenize(file_contents)

print(tokens[:20])


# In[11]:


from nltk.sentiment import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

polarity_scores_unprocessed = sid.polarity_scores(file_contents)


# In[15]:


from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
processed_tokens = [word.lower() for word in tokens if (word.lower() not in stop_words and word.lower() not in string.punctuation)]

print(processed_tokens[:20])


# In[23]:


exclude_words = ["would", "may", "must", "upon", "every"] 
filtered_tokens = [word for word in processed_tokens if word not in exclude_words]

freq_dist = nltk.FreqDist(filtered_tokens)
freq_dist


# In[24]:


import matplotlib.pyplot as plt
plt.figure(figsize=(10, 5))
freq_dist.plot(10, title="Top 10 Most Common Words")
plt.show()


# In[29]:


from nltk.stem import PorterStemmer, WordNetLemmatizer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

# stemming 
stemmed_tokens = [stemmer.stem(word) for word in filtered_tokens]

#  lemmatization
lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]

freq_dist_stemmed = nltk.FreqDist(stemmed_tokens)
freq_dist_lemmatized = nltk.FreqDist(lemmatized_tokens)

# stemmed tokens
plt.figure(figsize=(10, 5))
freq_dist_stemmed.plot(10, title="Top 10 Most Common Stemmed Words")
plt.show()

#lemmatized tokens
plt.figure(figsize=(10, 5))
freq_dist_lemmatized.plot(10, title="Top 10 Most Common Lemmatized Words")
plt.show()


# In[31]:


sid.polarity_scores(' '.join(stemmed_tokens))


# In[32]:


sid.polarity_scores(' '.join(lemmatized_tokens))


# In[33]:


from nltk.text import Text

# Convert Text 
text_object = Text(processed_tokens)

# concordance
concordance_result = text_object.concordance("king")

# Plot
plt.figure(figsize=(10, 5))
text_object.dispersion_plot(["king"])
plt.title("Dispersion Plot of the Word 'king'")
plt.show()


# In[ ]:




