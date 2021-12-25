import streamlit as st
import pandas as pd
import plotly
import pickle


def load_data():
    # load original data
    df_original = pd.read_excel('CO2 dataset.xlsx')
    df_original.index = pd.to_datetime(df_original['Year'], format='%Y')
    df_original.drop('Year', axis=1, inplace=True)
    return df_original


def load_pkl():
    # load pkl file
    pickled_model = pickle.load(open('arimafoo.pkl', 'rb'))
    return pickled_model


def user_input():
    # user input select boxes
    start = str(st.sidebar.selectbox(label='enter start', options=range(2015, 2050)))
    end = str(st.sidebar.selectbox(label='enter end', options=range(2016, 2051)))
    return start, end


def predict(end):
    # prediction using pkl
    df = pd.DataFrame(load_pkl().predict('2015', end))
    df.columns = ['CO2']

    for i in range(len(df)):
        if i == 0:
            df.iloc[0, ] = df.iloc[0, ] + load_data().iloc[-1, ]
        else:
            df.iloc[i, ] = df.iloc[i, ] + df.iloc[i-1, ]

    # merge original and predicted data
    data = pd.concat([load_data(), df])
    data.index = data.index.map(lambda x: x.strftime('%Y'))
    data.index.name = 'Year'
    return data


def plot_raw_data(data):
    fig = plotly.graph_objects.Figure()
    fig.update_layout(width=850, height=650)
    fig.add_trace(go.Scatter(x=data.index, y=data['CO2'], name='Air Quality'))
    fig.layout.update(title_text="Yearly CO2 levels", xaxis_title='Years')
    fig.update_traces(mode="lines", hovertemplate=None)
    fig.update_layout(hovermode="x unified", yaxis_title='CO2 levels', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)


def main():
    # Title
    st.title('Air Quality Forecasting')
    st.sidebar.title('User Input')
    ui_input = user_input()

    # display forecasted values
    st.sidebar.subheader('Forecasted Values')
    st.sidebar.dataframe(predict(ui_input[1]).loc[ui_input[0]:ui_input[1], ])

    # display past values
    st.sidebar.subheader('Past Values')
    st.sidebar.dataframe(predict(ui_input[1]).loc['1800':'2014', ], width=2000)

    # plot the data
    plot_raw_data(predict(ui_input[1]))


if __name__ == '__main__':
    main()
