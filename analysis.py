import streamlit as st
import pandas as pd

tab1, tab2 = st.tabs(["Analysis", "Interactive Dashboard"])

data = pd.read_csv("all_players.csv")
data = data.dropna()
data = data.drop_duplicates()

with tab1:
    st.title("MLS Players Analysis")
    st.write("This is a simple analysis of MLS players")

    st.write("Dataset used for analysis:")
    st.write(data)

    # 2 columns for the 2 charts
    col1, col2 = st.columns(2)

    # Group by year
    per_year = data.groupby(["Year"]).mean(numeric_only=True)

    with col1:
        st.write("Line chart of average goals and assists per year:")
        st.line_chart(data=per_year, y=["G", "A"])

    # Group by position
    per_position = data.groupby(["POS"]).mean(numeric_only=True)

    with col2:
        st.write("Bar chart of average goals and assists per position:")
        st.bar_chart(data=per_position, y=["G", "A"])


    # Group by club
    per_club = data.groupby(["Club"]).mean(numeric_only=True)

    st.write("Bar chart of average goals and assists per club:")
    st.bar_chart(data=per_club, y=["G", "A"])

    # Scatter plot of goals and assists
    st.write("Scatter plot of goals and assists:")
    st.scatter_chart(data=data, x="G", y="A")

    # Scatter plot of shots and shot accuracy
    st.write("Scatter plot of shots and shot accuracy:")
    st.scatter_chart(data=data, x="SHTS", y="SOG%")


with tab2:
    st.title("Interactive Dashboard")
    with st.sidebar:
        year_list = data["Year"].unique()
        selected_year = st.selectbox("Select year", year_list)
        selected_color = st.color_picker("Select color")
        selected_year_data = data[data["Year"] == selected_year]
        per_position = selected_year_data.groupby(["POS"]).mean(numeric_only=True)

    col1, col2 = st.columns(2)

    with col1:
        st.scatter_chart(data=selected_year_data, x="G", y="A", color=selected_color)

    with col2:
        st.scatter_chart(data=selected_year_data, x="SHTS", y="SOG%", color=selected_color)
        
    st.bar_chart(data=per_position, y=["G", "A"])
      

    