NLTK-Natural Language Toolkit

1. Core Concepts 

* Tokenization: Splitting text into smaller units like words or sentences.  
Python

        from nltk.tokenize import word_tokenize, sent_tokenize

        text = "This is a sentence. Here is another."
        words = word_tokenize(text)
        sentences = sent_tokenize(text)
* Stop Words: Common words (e.g., "the," "is") often removed for analysis.  
Python

        from nltk.corpus import stopwords

        stop_words = set(stopwords.words('english'))
        filtered_words = [word for word in words if word.lower() not in stop_words]
* Stemming: Reducing words to their root form (e.g., "running" to "run").  
Python

        from nltk.stem import PorterStemmer

        stemmer = PorterStemmer()
        stemmed_words = [stemmer.stem(word) for word in filtered_words]
* Lemmatization: Reducing words to their dictionary form using WordNet.  
Python

        from nltk.stem import WordNetLemmatizer

        lemmatizer = WordNetLemmatizer()
        lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
* Part-of-Speech (POS) Tagging: Identifying the grammatical role of words.  
Python

        from nltk import pos_tag

        tagged_words = pos_tag(lemmatized_words)
* Named Entity Recognition (NER): Identifying entities like names, locations, and organizations.  
Python

        from nltk import ne_chunk

        ner_tree = ne_chunk(tagged_words)
2. Working with Corpora 

NLTK includes various text datasets (corpora). 

Python
```python
        from nltk.corpus import movie_reviews

        documents = [(list(movie_reviews.words(fileid)), category)
                     for category in movie_reviews.categories()
                     for fileid in movie_reviews.fileids(category)]
```
3. Additional Functionality 

* Frequency Distributions: Analyzing word frequencies.  
Python

        from nltk import FreqDist

        fdist = FreqDist(words)
        most_common = fdist.most_common(10)
* Chunking: Grouping words into phrases.  
* Sentiment Analysis: Determining the emotional tone of text.  
* WordNet: A lexical database of English.  
4. Usage Steps 

* Import necessary NLTK modules.
* Download required data (if not already done).
* Load and preprocess text data.
* Apply NLP techniques like tokenization, stemming, or POS tagging.
* Analyze the results.  
5. Example 

Python


```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')

text = "NLTK is a powerful tool for natural language processing."
words = word_tokenize(text)
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in words if word.lower() not in stop_words]
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in filtered_words]

print(stemmed_words)
```
This is a basic overview. NLTK offers many more advanced features for various NLP tasks.