import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib


# page
st.set_page_config(
    page_title="Airbnb Analytics Dashboard",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 Airbnb Amsterdam Analytics Dashboard")
st.markdown("### Data Insights + Machine Learning + Geospatial Analysis")


# cache data
@st.cache_data
def load_data():
    df = pd.read_csv("./data/processed/listings_cleaned.csv")
    return df

df = load_data()


# sidebar
st.sidebar.header("🔍 Filters")

room_type = st.sidebar.selectbox(
    "Room Type",
    df["room_type"].unique()
)

price_range = st.sidebar.slider(
    "Price Range",
    int(df["price_clean"].min()),
    int(df["price_clean"].max()),
    (50, 300)
)

filtered_df = df[
    (df["room_type"] == room_type) &
    (df["price_clean"].between(price_range[0], price_range[1]))
]


# kpis
st.markdown("## 📊 Key Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Listings", len(filtered_df))
col2.metric("Min Price", f"${filtered_df['price_clean'].min():.0f}")
col3.metric("Max Price", f"${filtered_df['price_clean'].max():.0f}")
col4.metric("Hosts", filtered_df["host_id"].nunique())


# Ttabs
tab1, tab2, tab3 = st.tabs([
    "📊 Overview",
    "📍 Location Insights",
    "🤖 Price Prediction"
])


# tab - 1 
with tab1:

    st.subheader("Price Distribution")

    fig, ax = plt.subplots()
    ax.hist(filtered_df["price_clean"], bins=40)
    ax.set_title("Price Distribution")
    st.pyplot(fig)

    st.subheader("Room Type Distribution")
    st.bar_chart(df["room_type"].value_counts())


# tab - 2
with tab2:

    st.subheader("Top Neighborhoods")

    st.bar_chart(
        filtered_df["neighbourhood_cleansed"]
        .value_counts()
        .head(10)
    )

    st.subheader("Correlation Heatmap")

    cols = [
        "price_clean",
        "accommodates",
        "bedrooms",
        "beds",
        "number_of_reviews"
    ]

    corr = filtered_df[cols].corr()

    fig, ax = plt.subplots(figsize=(8, 5))
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

    
    # map view
    st.subheader("Geographical Distribution")

    if "latitude" in filtered_df.columns and "longitude" in filtered_df.columns:
        st.map(filtered_df[["latitude", "longitude"]].dropna())
    else:
        st.warning("No latitude/longitude data available")


# tab 3
with tab3:

    st.subheader("💰 Predict Airbnb Price")

    model = joblib.load("./models/random_forest_model.pkl")

    col1, col2 = st.columns(2)

    with col1:
        accommodates = st.slider("Accommodates", 1, 10, 2)
        bedrooms = st.slider("Bedrooms", 1, 5, 1)

    with col2:
        beds = st.slider("Beds", 1, 8, 1)
        bathrooms = st.slider("Bathrooms", 1, 5, 1)

    if st.button("Predict Price"):

        prediction = model.predict([[
            accommodates,
            bedrooms,
            beds,
            bathrooms,
            10,
            365  
        ]])

        st.success(f"💰 Predicted Price: ${prediction[0]:.2f}")


# footer
st.markdown("---")
st.markdown("🚀 Built with Streamlit | Airbnb Project")