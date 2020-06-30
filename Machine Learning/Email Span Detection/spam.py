import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import string
from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
data = pd.read_csv("spam.csv",encoding='latin-1')
data.head()
data=data.drop(["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], axis=1)
data=data.rename(columns={"v1":"class", "v2":"text"})
data.head()
data['length']=data['text'].apply(len)
data.head()
count_class=pd.value_counts(data['class'], sort=True)
count_class.plot(kind= 'bar', color= ["blue", "orange"])
plt.title('Bar chart')
plt.show()
count_class.plot(kind = 'pie',  autopct='%1.0f%%')
plt.title('Pie chart')
plt.ylabel('')
plt.show()
import seaborn as sns
ham =data[data['class'] == 'ham']['text'].str.len()
sns.distplot(ham, label='Ham')
spam = data[data['class'] == 'spam']['text'].str.len()
sns.distplot(spam, label='Spam')
plt.title('Distribution by Length')
plt.legend()
from collections import Counter
ount1 = Counter(" ".join(data[data['class']=='ham']["text"]).split()).most_common(30)
data1 = pd.DataFrame.from_dict(count1)
data1 = data1.rename(columns={0: "words of ham", 1 : "count"})
count2 = Counter(" ".join(data[data['class']=='spam']["text"]).split()).most_common(30)
data2 = pd.DataFrame.from_dict(count2)
data2 = data2.rename(columns={0: "words of spam", 1 : "count_"})

data1.plot.bar(legend = False, color = 'purple',figsize = (20,15))
y_pos = np.arange(len(data1["words of ham"]))
plt.xticks(y_pos, data1["words of ham"])
plt.title('Top 30 words of ham')
plt.xlabel('words')
plt.ylabel('number')
plt.show()

data2.plot.bar(legend = False, color = 'green', figsize = (20,17))
y_pos = np.arange(len(data2["words of spam"]))
plt.xticks(y_pos, data2["words of spam"])
plt.title('Top 30 words of spam')
plt.xlabel('words')
plt.ylabel('number')
plt.show()
import matplotlib as mpl
mpl.rcParams['patch.force_edgecolor'] = True
plt.style.use('seaborn-bright')
data.hist(column='length', by='text', bins=50,figsize=(11,5))
def pre_process(text):
    
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = [word for word in text.split() if word.lower() not in stopwords.words('english')]
    words = ""
    for i in text:
            stemmer = SnowballStemmer("english")
            words += (stemmer.stem(i))+" "
    return words

import nltk

nltk.download('stopwords')

textFeatures = data['text'].copy()
textFeatures = textFeatures.apply(pre_process)
vectorizer = TfidfVectorizer("english")
features = vectorizer.fit_transform(textFeatures)
features_train, features_test, labels_train, labels_test = train_test_split(features, data['class'], test_size=0.3, random_state=111)
from sklearn.metrics import accuracy_score
from sklearn.svm import SVC


for x in range (1, 7):
    svc = SVC(kernel='sigmoid', gamma=x)
    svc.fit(features_train, labels_train)
    prediction = svc.predict(features_test)
    print("Accuracy Test", accuracy_score(labels_test,prediction))
    print("Accuracy Traning", svc.score(features_train, labels_train))
    




























