import streamlit as st
import pandas as pd
import umap
import plotly.express as px
import numpy as np


def page1():
    st.title("Page 1: Welcome!")
    st.write("This is the content of Page 1.")
    st.image("https://placekitten.com/200/200", caption="A Cute Kitten", width=200)


def page2():
    st.title("Page 2: UMAP Plot")
    st.write("Select elements to visualize:")

    # Dummy data for demonstration
    dummy_data = pd.DataFrame(
        np.random.rand(100, 10),
        columns=[f"feature_{i}" for i in range(10)],
        index=[f"element_{i}" for i in range(100)],
    )

    # Multiselect for elements
    selected_features = st.multiselect(
        "Select elements", dummy_data.columns.to_list(), key="umap_multi_select"
    )

    if selected_features:  # Only proceed if elements are selected
        # Filter data based on selected elements
        filtered_data = dummy_data[selected_features]

        # UMAP embedding
        reducer = umap.UMAP()
        umap_embedding = reducer.fit_transform(filtered_data)

        # Create plot with Plotly
        umap_df = pd.DataFrame(
            umap_embedding, columns=["UMAP_1", "UMAP_2"], index=filtered_data.index
        )
        umap_df.index.name = "element"

        fig = px.scatter(
            umap_df,
            x="UMAP_1",
            y="UMAP_2",
            text=umap_df.index,
            title="UMAP of selected elements",
        )
        fig.update_traces(textposition="bottom center")
        st.plotly_chart(fig)
    else:
        st.warning("Please select at least one element to display a UMAP plot.")


def page3():
    st.title("Page 3: Settings")
    st.write("Configure your settings here.")
    st.selectbox("Theme", ["Light", "Dark"])


def main():
    st.sidebar.title("Navigation")

    if st.sidebar.button("Page 1"):
        st.session_state.page = "Page 1"
    if st.sidebar.button("Page 2"):
        st.session_state.page = "Page 2"
    if st.sidebar.button("Page 3"):
        st.session_state.page = "Page 3"

    if "page" not in st.session_state:
        st.session_state.page = "Page 1"

    if st.session_state.page == "Page 1":
        page1()
    elif st.session_state.page == "Page 2":
        page2()
    elif st.session_state.page == "Page 3":
        page3()


if __name__ == "__main__":
    main()