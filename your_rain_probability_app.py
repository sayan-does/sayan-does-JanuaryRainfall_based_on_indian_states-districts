import joblib
model = joblib.load('Rain_model.pkl')
import streamlit as st
st.title("January Rain, Are you there?")


st.write("Hello! Sayan does another cool(literaly) project yet again.\n in this window you can predict how much there is going to be in the month of January \n\n yes with data of previous months")

# Input features
st.write("ALL THE UNITS OF RAIN IN 'CM' ")
feb = st.slider("Rain in FEBRUARY ",max_value=200)
mar = st.slider("Rain in MARCH ",max_value=200)
apr = st.slider("Rain in APRIL ",max_value=200)
may = st.slider("Rain in MAY ",max_value=200)
nov = st.slider("Rain in NOVEMBER ",max_value=200)
dec = st.slider("Rain in DECEMBER ",max_value=200)
mar2may = mar+apr+may
year = st.slider("TOTAL Rain last year  ",min_value=1000,max_value=3000)



# Make predictions
if st.button("predict rainfalls in January"):
    features = [[feb,mar,apr,may,nov,dec,mar2may,year]]
    prediction = model.predict(features)
    st.write(f"Rain fall: {prediction[0]:.2f}CM")
    if prediction>100:
        st.write("Your start of the year is gonna be wettt! \n pro tip: carry umbrellas") 
    elif prediction<100 and prediction>50:
        st.write("Janaury gonna be pretty regular")
    elif prediction<50:
        st.write("January as dry as your wife")
    
