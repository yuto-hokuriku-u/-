#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import streamlit as st
import plotly.express as px


# In[2]:


merged_df = pd.read_csv("merged.csv")


# In[5]:


st.title("加賀のサロン調査")

price_limit = st.slider("最低カット価格の上限",min_value=2000,max_value=8000,step=200,value=5000)
score_limit = score_limit = st.slider("人気スコアの下限", min_value=0.0, max_value=5.0, step=0.5, value=2.5)


# In[11]:


filtered_df = merged_df[
    (merged_df['価格3'] <= price_limit) &
    (merged_df['pop_score'] >= score_limit)
    ]


# In[12]:


fig = px.scatter(
    filtered_df,
    x='pop_score',
    y='価格3',
    hover_data=['タイトル','access','テキスト','テキスト1'],
    title='人気スコアと最低カット価格の散布図'
)

st.plotly_chart(fig)


# In[13]:


selected_salon = st.selectbox('気になるサロンを選んで詳細をかくにん',filtered_df['タイトル'])

if selected_salon:
    url = filtered_df[filtered_df['タイトル'] == selected_salon]['_リンク'].values[0]
    st.markdown(f"[{selected_salon}のページへ移動]({url})",unsafe_allow_html=True)


# In[14]:


sort_key = st.selectbox(
    "ランキング基準を選んでください",
    ("テキスト","pop_score","テキスト1","価格3","seat4")
)

ascending = True if sort_key == "価格3" else False


# In[18]:


st.subheader(f"{sort_key}によるサロン人気ランキング（上位10件)")

ranking_df = filtered_df.sort_values(by=sort_key,ascending=ascending).head(10)

st.dataframe(ranking_df[["タイトル","価格3","pop_score","テキスト","テキスト1","seat4","access"]])


# In[ ]:




