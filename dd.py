# input csv
from matplotlib.pyplot import xlabel
from numpy import integer
import pandas as pd
import streamlit as st
import altair as alt
df = pd.read_csv("symptom_table.csv")# 僅需更換
# print(df.head)
# print(df.columns)

# 設計UI

st.header("Differential Diagnosis:")
st.sidebar.header("Symptom")
st.sidebar.text("Jen Ping Lee")



selected_ls = []
for col in df.columns:
    x = st.sidebar.checkbox(label=str(col))
    if x == True:
        selected_ls.append(str(col))

# st.dataframe(df[selected_ls])
dfs = df[selected_ls]
# st.write(dfs.iloc[0,1])
pool_ls = []
for i in range(0,dfs.shape[0]):
    for j in range(0,dfs.shape[1]):   
        # st.write(dfs.iloc[i,j])
        pool_ls.append(dfs.iloc[i,j])

# for j in range(0,dfs.shape[1]):
#     pool_ls.append(dfs[:,j].unique())



pool_sr = pd.Series(pool_ls)
# st.write(pool_sr.value_counts())


dfsd = pd.DataFrame(pool_sr.value_counts())
dfsd.columns = ["frequency"]
dfsd = dfsd.sort_values(by="frequency",ascending=False).copy()
# dfsd = dfsd.transpose()
# st.write(dfsd)


dfsd['Diagnosis'] = dfsd.index

chart = alt.Chart(dfsd).mark_bar().encode(
    x = 'frequency',
    y = alt.Y('Diagnosis', sort='-x'),
    tooltip = ['frequency']
)



st.altair_chart(chart,use_container_width=True)

dfsd.drop('Diagnosis',axis = 1)
st.write(dfsd)


# st.bar_chart(dfsd,height=0)

# streamlit run C:/vscode_workplace/gyn_dd_gyn

## 查看library:
### 1)pip freeze > requirements.txt
### 2)cat requirements.txt