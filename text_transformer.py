import nltk
from nltk.tokenize import word_tokenize
# nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
import string

stopwords_list = stopwords.words("english")
# manualy created a list of stopwords
ls = ['ur',"&lt;#&gt;", "...", "ÌÏ", ":)", "&amp;", "å£", "£"] + list(string.punctuation) + list(string.ascii_letters) + list(string.digits)
stopwords_list += ls

def txt_transformer(text):
    # Lowercase the text
    msg = text.lower()

    # Tokenize the text
    msg = nltk.word_tokenize(msg)

    # Remove non-alphanumeric tokens, stopwords and punctuation
    sentance = []
    for i in msg:
        if i.isalnum() and i not in stopwords_list:
            # Stem the words and append to sentance list
            sentance.append(ps.stem(i))
    # join the sentance with an empty space and return
    return " ".join(sentance)
