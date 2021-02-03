import streamlit as st
import pandas as pd
import numpy as np



st.set_page_config(page_title="Euler Eneström",
            layout="wide")

st.sidebar.title('Euler Enestroem')

DATE_COLUMN = 'published_date'
DATA_URL = ("./data/euler_works_1.xls")

@st.cache
def load_data():
    data = pd.read_excel(DATA_URL)
#    lowercase = lambda x: str(x).lower()
#    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN],errors='coerce')
    sdata=data[["title","published_date","list_view_id_tag"]]
    return sdata

#data_load_state = st.text('Loading data...')
data = load_data()
#data_load_state.text("Done! (using st.cache)")

#st.subheader('Number of pickups by hour')
#hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
#st.bar_chart(hist_values)

# Some number in the range 0-23
danfang = st.sidebar.slider('begin year', 1720, 1790, 1720)
dende = st.sidebar.slider('ende year', danfang, 1790, danfang+1)

filtered_data = data[data[DATE_COLUMN].dt.year > danfang]


if st.sidebar.checkbox('Show table'):
    #st.subheader('Table')
    st.write(filtered_data)



#st.subheader('Map of all pickups at %s:00' % hour_to_filter)
#st.map(filtered_data)