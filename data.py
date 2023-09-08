import streamlit as st
import pandas as pd
import seaborn as sns

# 1. Title and subheader add
st.title("Data Analysis")
st.subheader("Data Analysis using Python and Streamlit")


# 2. Upload Dataset
upload = st.file_uploader("Upload Your Dataset (IN CSV Format)")
if upload is not None:
    data=pd.read_csv(upload)


# 3. Show Dataset
if upload is not None:
    if st.checkbox("Preview Dataset"):
       if st.button("Head"):
          st.write(data.head())
       if st.button("Tail"):
          st.write(data.tail())
# 4. Check Datatype of Each Columns
if upload is not None:
    if st.checkbox("DataType of Each Column"):
        st.text("DataTypes")
        st.write(data.dtypes)

# 5. Find Shape of our dataset How many columns and rows         
if upload is not None:
    data_shape = st.radio("What Dimension Do you want to Check?" ,('Rows','Columns'))
    if data_shape =='Rows':
        st.text("Number of Rows")
        st.write(data.shape[0])
    if data_shape =='Columns':
        st.text("Number of Columns")
        st.write(data.shape[1])
# 6. Find Null Values in the Dataset 
if upload is not None:
    test =  data.isnull().values.any()
    if test==True:
        if st.checkbox("Null values in the dataset"):
            sns.heatmap(data.isnull())
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot() 
    else:
        st.success("Congratulations, No Missing Values")  
#7. Find Duplicate Values in the dataset

if upload is not None:
    test=data.duplicated().any()
    if test ==True:
        st.warning("This Dataset Contains Some Duplicate values")
        dup=st.selectbox("Do You want to Remove Duplicate Values?",\
                          ("Select One", "Yes","No"))
        if dup=="Yes":
           data = data.drop_duplicates()
           st.text("Duplicate values are Removed")
        if dup=="No":
           st.text("OK No Problem")  

# 8. Get Overall Statistics
if upload is not None:
    if st.checkbox("Summary of the Dataset"):
        st.write(data.describe())  
# 9. About Selection

if st.button("About App"):
    st.text("Built with Streamlit")
    st.text("Thanks to Streamlit")

# 10. By
if st.checkbox("By"):
    st.success("MUHAMMAD ISHAQ (:)")    