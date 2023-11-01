import streamlit as st
import pandas as pd

csv_github_url = 'https://raw.githubusercontent.com/medp4/sdata/main/pv_simulation_data.csv'

# Load the CSV data from the GitHub URL using st.cache_resource
@st.cache_resource
def load_data(github_url):
    data = pd.read_csv(github_url)
    return data

# Main function
def main():
    st.title("Projet avec M. Tahani Abdelouahad")

    try:
        data = load_data(csv_github_url)

        st.subheader("graphs relatifs aux séries temporelles")
        for column in data.columns[1:]:
            st.subheader(column)
            st.line_chart(data.set_index("Time")[column])

    except Exception as e:
        st.error(f"Erreur de chargement de la base de données: {str(e)}")

if __name__ == "__main__":
    main()
