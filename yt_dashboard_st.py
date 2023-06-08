import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# functions related to styling dashboard


def style_negative(v, props=''):  # style negative values
    try:
        return props if v < 0 else None
    except:
        pass


def style_positive(v, props=''):  # style positive values
    try:
        return props if v > 0 else None
    except:
        pass

# load data


df = pd.read_csv('yt_data.csv')
df['upload_date'] = pd.to_datetime(df['upload_date'])
df['Engagement'] = df['view_count'] + df['like_count'] + df['comment_count']

# data engineering

df_co = df.copy()
metric_data_12mo = df_co['upload_date'].max() - pd.DateOffset(months=12)
median_agg = df_co[df_co['upload_date'] >= metric_data_12mo].median()
numric_cols = np.array((df_co.dtypes == 'int64') | (df_co.dtypes == 'float64'))

df_co.iloc[:, numric_cols] = (
    df_co.iloc[:, numric_cols] - median_agg).div(median_agg)

# build dashboard
add_sidebar = st.sidebar.selectbox('Aggregate or Individual video  ', [
                                   'Aggregate Metrics ', 'Individual Video Anlysis'])


# Total picture
if add_sidebar == 'Aggregate Metrics ':
    df_agg_metrics = df[['view_count', 'like_count',
                         'comment_count', 'Engagement', 'upload_date']]
    metric_data_6mo = df_agg_metrics['upload_date'].max(
    ) - pd.DateOffset(months=6)
    metric_data_12mo = df_agg_metrics['upload_date'].max(
    ) - pd.DateOffset(months=12)
    metric_median_6mo = df_agg_metrics[df_agg_metrics['upload_date']
                                       >= metric_data_6mo].median()
    metric_median_12mo = df_agg_metrics[df_agg_metrics['upload_date']
                                        >= metric_data_12mo].median()

    col1, col2, col3, col4, col5 = st.columns(5)
    columns = [col1, col2, col3, col4, col5]
    count = 0

    for i in metric_median_6mo.index:
        with columns[count]:
            delta = (
                metric_median_6mo[i] - metric_median_12mo[i]) / metric_median_12mo[i]
            st.metric(label=i, value=round(
                metric_median_6mo[i], ), delta="{:.2%}".format(delta))
            count += 1
            if count == 5:
                break

    df_co['upload_date'] = df_co['upload_date'].dt.strftime('%Y-%m-%d')
    df_co_final = df_co.loc[:, ['video_title', 'upload_date', 'view_count',
                                'like_count', 'comment_count', 'Engagement']]

    df_agg_numric_lst = df_co_final.median().index.tolist()
    df_to_pct = {}
    for i in df_agg_numric_lst:
        df_to_pct[i] = '{:.2%}'

    st.dataframe(df_co_final.style.applymap(
        style_negative, props='color:red:;').applymap(style_positive, props='color:green:;').format(df_to_pct))


if add_sidebar == 'Individual Video Anlysis':
    # show all videos by views
    df_view = df.sort_values(by='view_count', ascending=False)
    df_view = df_view[['video_title', 'view_count', 'like_count',
                       'comment_count', 'Engagement', 'upload_date']]
    df_view['upload_date'] = df_view['upload_date'].dt.strftime('%Y-%m-%d')
    df_view = df_view.reset_index(drop=True)
    st.dataframe(df_view.style.applymap(
        style_negative, props='color:red:;').applymap(style_positive, props='color:green:;'))

    # line chart for views over time
    df_view_time = df[['upload_date', 'view_count']]
    df_view_time = df_view_time.groupby('upload_date').sum()
    df_view_time = df_view_time.reset_index()
    fig = px.line(df_view_time, x='upload_date', y='view_count',
                  title='The Chanel Views Over Time', labels={'upload_date': 'Date', 'view_count': 'Views'}, hover_data=['view_count'], template='plotly_dark')
    fig.update_traces(line_color='purple')
    st.plotly_chart(fig)

    # bar chart for top 5 videos by views
    df_view_top5 = df_view.head(5)
    fig = px.bar(df_view_top5, x='video_title', y='view_count',
                 color='Engagement', title='Top 5 Videos by Engagement', labels={'video_title': 'Video Title', 'view_count': 'Views', 'Engagement': 'Engagement'}, hover_data=['Engagement'], template='plotly_dark')
    st.plotly_chart(fig)
