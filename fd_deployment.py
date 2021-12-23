import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import pickle

# Title
st.title('Air Quality Forecasting')
st.sidebar.title('User Input')

# load original data
df_original = pd.read_excel(r'C:\Users\shiva\ExcelR\Project\CO2 dataset.xlsx')
df_original.index = pd.to_datetime(df_original['Year'], format='%Y')
df_original.drop('Year', axis=1, inplace=True)

# load pkl file
pickled_model = pickle.load(open('C:\\Users\\shiva\\ExcelR\\Project\\arimafoo.pkl', 'rb'))

# user input select boxes
start = str(st.sidebar.selectbox(label='enter start', options=range(2015, 2050)))
end = str(st.sidebar.selectbox(label='enter end', options=range(2016, 2051)))

# prediction using pkl
df = pd.DataFrame(pickled_model.predict('2015', end))
df.columns = ['CO2']


for i in range(len(df)):
    if i == 0:
        df.iloc[0, ] = df.iloc[0, ] + df_original.iloc[-1, ]
    else:

        df.iloc[i, ] = df.iloc[i, ] + df.iloc[i-1, ]


# merge original and predicted data
data = pd.concat([df_original, df])

data.index = data.index.map(lambda x: x.strftime('%Y'))
data.index.name = 'Year'


def plot_raw_data():
    fig = go.Figure()
    fig.update_layout(width=850, height=650)
    fig.add_trace(go.Scatter(x=data.index, y=data['CO2'], name='Air Quality'))
    fig.layout.update(title_text="Yearly CO2 levels", xaxis_title='Years')
    fig.update_traces(mode="lines", hovertemplate=None)
    fig.update_layout(hovermode="x unified", yaxis_title='CO2 levels', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)


plot_raw_data()     # plot the data

# display forecasted values
st.sidebar.subheader('Forecasted Values')
st.sidebar.dataframe(data.loc[start:end, ])

st.sidebar.subheader('Past Values')
st.sidebar.dataframe(data.loc['1800':'2014', ], width=2000)


# dftest = pd.DataFrame(pickle_preds.predict('2001', '2014'))
# dftest.columns = ['CO2']
# fitted = pd.DataFrame(pickle_preds.fittedvalues, columns = ['CO2'])
# fitted1 = pd.concat([fitted,dftest ,df])
# fitted1['cumsum'] = fitted1['CO2'].cumsum()
# fitted1['cumsum'] = fitted1['cumsum'] + df_original.iloc[1,1]
