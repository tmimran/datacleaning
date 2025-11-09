import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 EDA Application")

# -----------------------------
# CSV Upload Section
# -----------------------------
uploaded_file = st.file_uploader("Upload any CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("✅ Dataset Preview")
    st.dataframe(df)

    st.subheader("📌 Basic Information")
    st.write("Shape:", df.shape)
    st.write("Columns:", list(df.columns))

    # -----------------------------
    # Visualization Section
    # -----------------------------
    st.subheader("📈 Data Visualization")

    numeric_columns = df.select_dtypes(include=["float64", "int64"]).columns.tolist()

    # Dropdowns
    x_axis = st.selectbox("Select X-axis column", options=df.columns)
    y_axis = st.selectbox("Select Y-axis column", options=numeric_columns)

    # Line Chart
    if st.button("Click Here For Line Graph"):
        fig, ax = plt.subplots()
        ax.plot(df[x_axis], df[y_axis])
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        ax.set_title(f"Line Graph of {y_axis} vs {x_axis}")
        st.pyplot(fig)

    # Bar Chart
    if st.button("Click Here For Bar Chart"):
        fig, ax = plt.subplots()
        ax.bar(df[x_axis], df[y_axis])
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        ax.set_title(f"Bar Chart of {y_axis} vs {x_axis}")
        st.pyplot(fig)

else:
    st.info("👆 Please upload a CSV file to begin.")
