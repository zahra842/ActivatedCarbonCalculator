from google.protobuf.symbol_database import Default
import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title('Activated Carbon Calculator')
st.write("\n")

# Slider
st.subheader("Biomass Weight (tons)")
biomass_weight = st.slider(
    label="", min_value=0,
    max_value=1000000, value=200000, step=10000, key='my_slider')

#st.write(biomass_weight)

st.subheader("Activated Carbon Weight Percentage in Biomass")
activated_carbon = st.number_input("", key="activated_carbon", min_value=0, max_value=100, value=7)

st.subheader("Emission Adsorption Percentage")
emission_adsorption = st.number_input("", key="emission_adsorption", min_value=0, max_value=100, value=10)

st.subheader("Emission Percentage Generated Per Ton of Wood Burnt")
emission_generated = st.number_input("", key="emission_generated", min_value=0, max_value=1000, value=200)


emission_mass_absorbed = biomass_weight * activated_carbon/100 * emission_adsorption/100
st.write(emission_mass_absorbed) 
emission_mass_generated = biomass_weight * emission_generated/100
st.write(emission_mass_generated)

year = np.array(range(1,11))
st.write(year)
yearly_adsorption = year * emission_mass_absorbed
cum_adsorption = np.cumsum(yearly_adsorption)
yearly_total = cum_adsorption + 400000
cum_total = np.cumsum(yearly_total)
st.write(cum_adsorption)
st.write(yearly_total)
st.write(cum_total)


#data = np.vstack([cum_adsorption, cum_total]).transpose()
data = pd.DataFrame(cum_total, index=year, columns=["cumulative"])
st.write(data)
st.line_chart(data)


#data=[[slider], [slider*0.1]]
#st.line_chart(data)


# Team
with st.container():
    st.subheader('Made by:')
    st.text('Mustafa A. Al Ibrahim, Layla A. Al Ibrahim, and Zahra A. Al Ibrahim')


