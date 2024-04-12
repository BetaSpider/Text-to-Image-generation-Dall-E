#!/usr/bin/env python
# coding: utf-8

# In[3]:


import openai 
import streamlit as st 
import urllib.request
from PIL import Image



# In[4]:


openai.api_key="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"


# In[5]:


def gen_img(img_des):
    img_res=openai.image.create(prompt=img_des,n=1, size="512x512")
    img_url=img_res['data'][0]['url']
    urllib.request.urlretrieve(img_url,'image.png"')
    img=Image.open('image.png')
    return img

st.title('Image Generation based on the given text-MY 1st GenerativeAI project')
img_text=st.text_input('Type the Text')
if st.button("Generate Image"):
    final_img=gen_img(img_des)
    st.image(final_img)


# In[ ]:




