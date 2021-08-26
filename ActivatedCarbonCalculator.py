from google.protobuf.symbol_database import Default
import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title('Activated Carbon Calculator')
st.write("\n")

st.markdown(
    """<div style='display: block; font-style:italic;'> \
       Mustafa A. Al Ibrahim, Layla A. Al Ibrahim, and Zahra A. Al Ibrahim 
       </div>
    """,
    unsafe_allow_html=True,
)

st.write("\n")


st.markdown(
    """<div style='display: block; text-align: justify;'> \
          Welcome to the emission Activated Carbon Calculator. \
          This calculator will allow you to estimate the emmissions \
          reserved and removed from the atmosphere by converting farm waste, \
          specifically palm tree waste, to activated carbon and using it for \
          removal of emisson. The calculator will take you through the steps and \
          assumptions made to reach the final estimates Lets get going!</div>
    """,
    unsafe_allow_html=True,
)

st.write("\n")

st.image('images/intro2.png', use_column_width=True)

# Slider
st.header("Biomass Weight (tons)")
st.markdown(
    """<div style='display: block; text-align: justify;'> \
       The biomass is the raw material for the activated carbon in this initiative, \
        specifically, we will use plant waste (mainly palm tree waste). It is estimated \
        that Saudi Arabia produces about 200,000 tons of palm waste per year.
       </div>
    """,
    unsafe_allow_html=True,
)
biomass_weight = st.slider(
    label="", min_value=0,
    max_value=1000000, value=200000, step=10000, key='my_slider')

#st.write(biomass_weight)

st.header("Activated Carbon Weight Percentage in Biomass")
st.markdown(
    """<div style='display: block; text-align: justify;'> \
       When the biomass undergoes pyrolysis (heating), it produces petrochemical. These petrochemicals \
       can be sold and utilized in industrial applications. As we heat the remaining material, it is \
       converted into activated carbon. Activated carbon. Activated Carbon is a special type of coal \
       with high specific area. It can absorb and adsorb high amount of emmissions easily. The ratio of \
       activated carbon to biomass by weight is generally between 6% and 9% depending on the material used.
       </div>
    """,
    unsafe_allow_html=True,
)
activated_carbon = st.number_input("", key="activated_carbon", min_value=0, max_value=100, value=7)

st.header("Emission Adsorption Percentage")
st.markdown(
    """<div style='display: block; text-align: justify;'> \
       When the biomass undergoes pyrolysis (heating), it produces petrochemical. These petrochemicals \
       can be sold and utilized in industrial applications. As we heat the remaining material, it is \
       converted into activated carbon. Activated carbon. Activated Carbon is a special type of coal \
       with high specific area. It can absorb and adsorb high amount of emmissions easily. The ratio of \
       activated carbon to biomass by weight is generally between 6% and 9% depending on the material used.
       </div>
    """,
    unsafe_allow_html=True,
)
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


