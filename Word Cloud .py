#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Here are all the installs and imports you will need for your word cloud script and uploader widget

get_ipython().system('pip install wordcloud')
get_ipython().system('pip install fileupload')
get_ipython().system('pip install ipywidgets')
get_ipython().system('jupyter nbextension install --py --user fileupload')
get_ipython().system('jupyter nbextension enable --py fileupload')

import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys


# In[2]:


# This is the uploader widget

def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()


# In[3]:


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "in","it", "of", "and", "or", "an", "as", "i", "me", "my", \
                       "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its",
                       "they", "them", "C"\
                       "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be",
                       "been", "being", \
                       "have", "has", "had", "do", "does", "did", "but","other" , "their","on" , "for","The", "at", "by", "with", "from", "here", "when",
                       "where", "how","c" \
                       "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can",
                       "will", "just", "now " , "so" ,"over", "while" "up"]
    #uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or","be", "been", "being", \
    #"have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    #"all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE
    word_list = file_contents.split()
    word_dict = {}
    for order in range(0 , len(word_list)):
        if word_list[order] not in uninteresting_words :
            word_list[order] = ''.join(e for e in word_list[order] if e.isalnum())
            if word_list[order] not in word_dict:
                count = 0
                for ord in range (order , len(word_list)) :
                    word_list[ord] = ''.join(e for e in word_list[ord] if e.isalnum())
                    if word_list[order] in word_list[ord]:
                        count += 1
                word_dict[word_list[order].lower()] = count
    #generate_from_frequencies(word_dict)
        
             
                    
    
    
    
    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(word_dict)
    return cloud.to_array()


# In[4]:


# Display your wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()


# In[ ]:




