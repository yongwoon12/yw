#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import pandas as pd


# In[3]:


st.write('# dt_FBC Preview')
st.write('## raw')
view = [100,150,30]
view

st.write('## bar chart')
st.bar_chart(view)

sview = pd.Series(view)
sview


# In[ ]:




