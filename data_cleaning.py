import streamlit as st
import pandas as pd
import io

st.title("🧹 Data Cleaning Application")

# -----------------------------
# File Upload Section
# -----------------------------
uploaded_file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Determine file type
    if uploaded_file.name.endswith(".csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.subheader("✅ Dataset Preview")
    st.dataframe(df)

    # -----------------------------
    # Basic Summary Section
    # -----------------------------
    st.subheader("📌 Basic Summary")

    # Display info() output
    buffer = io.StringIO()
    df.info(buf=buffer)
    info_str = buffer.getvalue()

    st.text("🔎 DataFrame info():")
    st.text(info_str)

    # Missing values
    st.write("### ✅ Number of Missing Values")
    st.write(df.isnull().sum())

    # Duplicate rows
    st.write("### ✅ Number of Duplicate Records")
    st.write(df.duplicated().sum())

    st.subheader("🛠 Data Cleaning Options")

    # -----------------------------
    # Option 1: Remove Missing Values
    # -----------------------------
    if st.button("✅ Click Here to Remove Missing Values"):
        cleaned_df = df.dropna()

        csv_data = cleaned_df.to_csv(index=False).encode('utf-8')

        st.success("Missing values removed successfully!")
        st.download_button(
            label="⬇️ Download Cleaned CSV",
            data=csv_data,
            file_name="removed_missing_values.csv",
            mime="text/csv"
        )

    # -----------------------------
    # Option 2: Handle Missing Values
    # (object → fillna, numeric → interpolate)
    # -----------------------------
    if st.button("✅ Click Here to Handle Missing Values Automatically"):
        cleaned_df = df.copy()

        # Fill object (string) columns
        object_columns = cleaned_df.select_dtypes(include="object").columns
        cleaned_df[object_columns] = cleaned_df[object_columns].fillna("Missing")

        # Interpolate numeric columns
        numeric_columns = cleaned_df.select_dtypes(include=["int64", "float64"]).columns
        cleaned_df[numeric_columns] = cleaned_df[numeric_columns].interpolate()

        csv_data = cleaned_df.to_csv(index=False).encode('utf-8')

        st.success("Missing values handled successfully!")
        st.download_button(
            label="⬇️ Download Cleaned CSV",
            data=csv_data,
            file_name="handled_missing_values.csv",
            mime="text/csv"
        )

    # -----------------------------
    # Option 3: Remove Duplicate Rows
    # -----------------------------
    if st.button("✅ Click Here to Remove Duplicate Records"):
        cleaned_df = df.drop_duplicates()

        csv_data = cleaned_df.to_csv(index=False).encode('utf-8')

        st.success("Duplicate records removed successfully!")
        st.download_button(
            label="⬇️ Download Cleaned CSV",
            data=csv_data,
            file_name="removed_duplicates.csv",
            mime="text/csv"
        )

else:
    st.info("👆 Please upload a CSV or Excel file to begin.")
