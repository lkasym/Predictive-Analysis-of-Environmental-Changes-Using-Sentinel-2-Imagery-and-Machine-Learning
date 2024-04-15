import streamlit as st
import numpy as np
import pickle
import os

# Load models
model_directory = 'C:\\Users\\laksh\\Downloads\\sml project'
models = {}

for filename in os.listdir(model_directory):
    if filename.endswith('.pkl'):
        model_path = os.path.join(model_directory, filename)
        models[filename] = pickle.load(open(model_path, 'rb'))

# Hardcoded average densities for each month
monthly_avg_densities = {
    1: {'vegetation_density': 0.2756, 'water_density': 0.01454, 'urban_density': 0.57678},
    2: {'vegetation_density': 0.26108, 'water_density': 0.05166, 'urban_density': 0.56644},
    3: {'vegetation_density': 0.1622, 'water_density': 0.00606, 'urban_density': 0.67652},
    4: {'vegetation_density': 0.2195, 'water_density': 0.00538, 'urban_density': 0.65786},
    5: {'vegetation_density': 0.20626, 'water_density': 0.0094, 'urban_density': 0.67592},
    6: {'vegetation_density': 0.743525, 'water_density': 0.014846, 'urban_density': 0.239436},
    7: {'vegetation_density': 0.719823, 'water_density': 0.014847, 'urban_density': 0.198218},
    8: {'vegetation_density': 0.654542, 'water_density': 0.014441, 'urban_density': 0.201167},
    9: {'vegetation_density': 0.760818, 'water_density': 0.0147660, 'urban_density': 0.227956},
    10: {'vegetation_density': 0.732601, 'water_density': 0.0148583, 'urban_density': 0.21654},
    11: {'vegetation_density': 0.49782, 'water_density': 0.01556, 'urban_density': 0.40468},
    12: {'vegetation_density': 0.35042, 'water_density': 0.01076, 'urban_density': 0.51628}
}

def get_model_and_densities(month, model_type, area_type):
    model_filename = f"{model_type}_{area_type}_area.pkl"
    model = models.get(model_filename)
    avg_densities = monthly_avg_densities.get(month, {'vegetation_density': 0.5, 'water_density': 0.2, 'urban_density': 0.3})
    return model, avg_densities

# Navigation
st.sidebar.title("Navigation")
section = st.sidebar.radio("Go to", ('Home', 'Trend', 'Prediction', 'Data Analysis', 'Team Members'))

if section == 'Home':
    st.header("Change Analysis in Pune")
    st.write("""
        This project aims to provide insights into the environmental and urban changes in Pune over recent years. Through detailed analysis and predictive modeling, we explore trends, predict future changes, and understand the impact of human activities on urban areas.
        
        Understanding the dynamics of urban expansion and environmental impact requires robust data analysis and predictive tools to aid city planners and policy makers in making informed decisions.
    """)
    st.image("C:\Users\laksh\Downloads\Screenshot 2024-04-15 041025.png", caption="Data Labelling Illustration")

elif section == 'Trend':
    st.header("Trend Analysis Dashboard")
    trend_option = st.selectbox("Choose a trend to display", ('Vegetation', 'Water', 'Urban', 'Overall'))
    
    if trend_option == 'Vegetation':
        st.image("C:\Users\laksh\Downloads\Decomposition_Plots\Vegetation_Area_Trends.png", caption="Vegetation Trends")
        st.write("""
            Vegetation trends show high variability, with pronounced seasonality likely due to natural growth cycles. The general trend indicates a decline, suggesting potential deforestation or urban development impacts.
        """)
    elif trend_option == 'Water':
        st.image("C:\Users\laksh\Downloads\Decomposition_Plots\Water_Area_Trends.png", caption="Water Trends")
        st.write("""
            Water trends indicate variability with a slight overall decrease over time. This could reflect climate change impacts or changes in land use affecting water bodies.
        """)
    elif trend_option == 'Urban':
        st.image("C:\Users\laksh\Downloads\Decomposition_Plots\Urban_Area_Trends.png", caption="Urban Trends")
        st.write("""
            Urban trends show a steady increase, indicating ongoing urban expansion. The trend highlights the critical need for sustainable urban planning to accommodate growth without compromising environmental integrity.
        """)
    elif trend_option == 'Overall':
        st.image("path_to_overall_image.png", caption="Overall Trends")
        st.write("""
            The overall data indicates urban expansion at the expense of vegetation and possibly affecting water bodies. This comprehensive view underscores the importance of integrated environmental management strategies.
        """)

elif section == 'Prediction':
    st.header("Prediction Interface")
    month = st.selectbox("Select Month", list(range(1, 13)), format_func=lambda x: f"Month {x}")
    model_type = st.selectbox("Select Model Type", ['Linear_Regression', 'Random_Forest', 'Gradient_Boosting', 'SVM'])
    area_type = st.selectbox("Select Area Type", ['vegetation', 'water', 'urban'])
    
    predict_button = st.button("Predict")
    if predict_button:
        model, avg_densities = get_model_and_densities(month, model_type, area_type)
        if not model:
            st.error("Model not found.")
        else:
            year = 2024  # As per your fixed year setup
            inputs = np.array([[year, month, avg_densities['vegetation_density'], avg_densities['water_density'], avg_densities['urban_density']]])
            prediction = model.predict(inputs)[0]
            st.success(f"Prediction: {prediction}")


