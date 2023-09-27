# %%%
import streamlit as st
import pandas as pd

st.markdown("## Job fair Unimi 2023 - All the job posts!")
st.image("https://cosp.careerserviceunimi.it/assets/img/logo/logo-job-fair-unimi-800.png")
st.write("Prepare to ace your interview at the Job fair by easily searching for the positions you would like to unveil.🚀", unsafe_allow_html=True)
st.write("Search among all the job posts and not only company-by-company as on the cosp platform (do you pretend us to be in love with only one company?)🔍", unsafe_allow_html=True)

# %%%
# jobs_posts = pd.read_excel("Job posts.xlsx")
jobs_posts = pd.read_excel("Job posts.xlsx")
# Function to create clickable link buttons
def make_clickable(link):
    # target _blank to open new window
    return f'<a target="_blank" href="{link}">{link}</a>'

jobs_posts['Firm page'] = jobs_posts['Firm page'].apply(make_clickable)
# %%

def filter_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds a UI on top of a dataframe to let viewers filter columns

    Args:
        df (pd.DataFrame): Original dataframe

    Returns:
        pd.DataFrame: Filtered dataframe
    """
    modify = st.checkbox("Apply filters")

    if not modify:
        return df

    df = df.copy()

    modification_container = st.container()

    with modification_container:
        to_filter_columns = st.multiselect("Filter:", df.columns)
        for column in to_filter_columns:
            left, right = st.columns((1, 20))
            left.write("↳")
            user_text_input = right.text_input(f"Search for a {column}",)
            if user_text_input:
                df = df[df[column].str.contains(user_text_input)]
    return df

st.markdown(filter_dataframe(jobs_posts).style.hide(axis="index").to_html(escape=False), unsafe_allow_html=True)