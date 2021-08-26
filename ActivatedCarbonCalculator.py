from google.protobuf.symbol_database import Default
import streamlit as st
import altair as alt
import pandas as pd
import numpy as np

# Title
st.title('Sustainable palm tree activated carbon for emissions capture')
st.write("\n")

st.markdown(
    """<div style='display: block; font-style:italic;'> \
       Zahra A. Al Ibrahim, Mustafa A. Al Ibrahim, and Layla A. Al Ibrahim
       </div>
    """,
    unsafe_allow_html=True,
)

st.write("\n")


st.markdown(
    """<div style='display: block; text-align: justify;'> \
          Welcome to the emission activated carbon calculator. \
          This calculator will allow you to estimate the emmissions \
          reserved and removed from the atmosphere by converting farm waste, \
          specifically palm tree waste, to activated carbon and using it for \
          removal of emisson. The calculator will take you through the steps and \
          assumptions made to reach the final estimates Lets get going!</div>
    """,
    unsafe_allow_html=True,
)

st.write("\n")

st.image('images/intro.png', use_column_width=True)

# Slider
st.header("Biomass weight (tons)")
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

st.header("Activated carbon weight percentage in biomass")
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

st.header("Emission adsorption percentage")
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

st.image('images/adsorbtion.png', use_column_width=True)

st.header("Activated carbon usage per year")
st.markdown(
    """<div style='display: block; text-align: justify;'> \
       The produced activated carbon can be reused. Spent activated carbon can be reactivated using a number \
       number of chemical methods. The collected emissions can be utilized in chemical processes. For example, \
       carbon dioxide can be used for producing Polyols.
       </div>
    """,
    unsafe_allow_html=True,
)
n_usage = st.number_input("", key="n_usage", min_value=1, max_value=100, value=40)

st.header("Emission percentage generated per ton of wood burnt")
st.markdown(
    """<div style='display: block; text-align: justify;'> \
       Backyard burning is the common practice of burning biomass material. It generates large amount of \
       of carbon dioxide. An estimated 190% by weight is generated. For example, 1.9 kg of carbon \
       dioxide is generated per 1 kg of biomass burned.
       </div>
    """,
    unsafe_allow_html=True,
)
emission_generated = st.number_input("", key="emission_generated", min_value=0, max_value=1000, value=190)

st.header("Results")

emission_mass_adsorbed = biomass_weight * activated_carbon/100 * emission_adsorption/100 * n_usage
emission_mass_reserved = biomass_weight * emission_generated/100

year = np.array(range(1,11))
yearly_adsorption = year * emission_mass_adsorbed
cum_adsorption = np.cumsum(yearly_adsorption)

cum_reserved = year * emission_mass_reserved

ten_year_total = cum_reserved[-1] + cum_adsorption[-1] 

st.markdown(
    """<div style='display: block; text-align: justify;'> \
       The following graph shows the cumulative amount of emissions that will be captured by the \
        activated carbon produced from the biomass over ten years. 
       </div>
    """,
    unsafe_allow_html=True,
)

st.write("\n")

source = pd.DataFrame({
  'Year': year,
  'Cumulative emissions adsorbed (tons)': cum_adsorption
})

c = alt.Chart(source).mark_line().encode(
    x='Year',
    y='Cumulative emissions adsorbed (tons)'
)

st.altair_chart(c,  use_container_width=True)


# ===================================================


st.markdown(
    """<div style='display: block; text-align: justify;'> \
       The following graph shows the cumulative amount of emissions that will be reserved by \
        preventing backyard burning. 
       </div>
    """,
    unsafe_allow_html=True,
)

st.write("\n")

source = pd.DataFrame({
  'Year': year,
  'Cumulative emissions reserved (tons)': cum_reserved
})

c = alt.Chart(source).mark_line().encode(
    x='Year',
    y='Cumulative emissions reserved (tons)'
)

st.altair_chart(c,  use_container_width=True)


# ====================================================
st.header("Final remarks")
st.markdown(
    f"""<div style='display: block; text-align: justify;'> \
       A approximate total of {int(ten_year_total)} tons can be reserved over the first ten years by maximizing \
       the utilization of biomass. At the same time, petrochemicals can be extracted during \
       during the pyrolysis processes. Overall, biomass in Saudi Arabia is an untabbed resource \
       that can help us toward sustainable future.
       </div>
    """,
    unsafe_allow_html=True,
)