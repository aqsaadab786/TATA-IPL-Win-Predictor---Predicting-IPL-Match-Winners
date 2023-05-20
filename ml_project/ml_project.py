import pickle
import pandas as pd
import streamlit as st
from PIL import Image
from streamlit.elements.arrow import ArrowMixin
from pandas.io.formats.style import Styler


teams=['Sunrisers Hyderabad',
       'Mumbai Indians',
       'Royal Challengers Bangalore',
       'Kolkata Knight Riders',
       'Kings XI Punjab',
       'Chennai Super Kings',
       'Rajasthan Royals',
       'Delhi Capitals',
       'Gujrat Titans',
       'Lucknow Super Giants']
cities=['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah','Mohali', 'Bengaluru']

teams_dict={'Sunrisers Hyderabad':0,
       'Mumbai Indians':1,
       'Royal Challengers Bangalore':2,
       'Kolkata Knight Riders':3,
       'Kings XI Punjab':4,
       'Chennai Super Kings':5,
       'Rajasthan Royals':6,
       'Delhi Capitals':7,
            "Pune Warriors":11,
       'Gujrat Titans':8,
       'Lucknow Super Giants':9,
           "Delhi Daredevils":10,
           "Deccan Chargers":12}
city_dict = {'Hyderabad':1, 'Bangalore':2, 'Mumbai':3, 'Indore':4, 'Kolkata':5, 'Delhi':6,
       'Chandigarh':7, 'Jaipur':8, 'Chennai':9, 'Cape Town':10, 'Port Elizabeth':11,
       'Durban':12, 'Centurion':13, 'East London':14, 'Johannesburg':15, 'Kimberley':16,
       'Bloemfontein':17, 'Ahmedabad':18, 'Cuttack':19, 'Nagpur':20, 'Dharamsala':21,
       'Visakhapatnam':22, 'Pune':23, 'Raipur':24, 'Ranchi':25, 'Abu Dhabi':26,
       'Sharjah':27,'Mohali':28, 'Bengaluru':29}
pipe = pickle.load(open('pipe.pkl','rb'))
st.title("TATA IPL WIN PREDICTOR POWERED BY DREAM 11")
img=Image.open("C:/Users/Aqsa/Downloads/IPL20201597936129432.jpg")
st.image(img,width=200,use_column_width=True)

col1, col2 = st.columns(2)
with col1:
       batting_team = st.selectbox('Select the batting team',sorted(teams))
with col2:
       bowling_team = st.selectbox('Select the bowling team',sorted(teams))

selected_city = st.selectbox('Select host city',sorted(cities))

target = st.number_input('Target')

col3,col4,col5 = st.columns(3)

with col3:
       score = st.number_input('Score')
with col4:
       overs = st.number_input('Overs completed')
with col5:
       wickets = st.number_input('Wicket out')

if st.button('Predict Probability'):
       runs_left =target- score
       balls_left = 120-(overs*6)
       wickets = 10-wickets
       crr =score/overs
       rrr = (runs_left*6)/balls_left
      # df = pd.read_csv()
       input_df = pd.DataFrame({'batting_team':[teams_dict[batting_team]],'bowling_team':[teams_dict[bowling_team]],'city':[city_dict[selected_city]],'runs_left':[runs_left],'balls_left':[balls_left],'wickets':[wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})
       result = pipe.predict_proba(input_df)
       loss = result[0][0]
       win= result[0][1]
       st.header(batting_team + "_ " + str(round(win*100)) + "%")
       st.header(bowling_team + "_ " + str(round(loss * 100)) + "%")

