import streamlit as st
import pandas as pd
from hit_api import trigger_jobs
from get_result import get_result

st.logo("mars_logo.png",size='large')
st.write("## MARKET INTELLIGENCE INPUT FORM")


st.write('### Setup Data')

df_mat_num = pd.DataFrame({
    'Material Number': [1461833,1499604,1511948,1499605,1461278,1493837],
    })

df_ven_1461833 = pd.DataFrame({
    'Vendor Name' : ['BERRY GLOBAL INC']
})

df_ven_1461833 = pd.DataFrame({
    'Vendor Name' : ['BERRY GLOBAL INC']
})

df_ven_1493837 = pd.DataFrame({
    'Vendor Name' : ['BERRY GLOBAL INC','TECHNIMARK LLC','PLASTEK INDUSTRIES INC']
})

df_ven_1499604 = pd.DataFrame({
    'Vendor Name' : ['BERRY GLOBAL INC']
})

df_ven_1499605 = pd.DataFrame({
    'Vendor Name' : ['SILGAN PLASTICS CORPORATION']
})

df_ven_1511948 = pd.DataFrame({
    'Vendor Name' : ['TECHNIMARK LLC']
})
df_ven_None = pd.DataFrame({
        'Vendor Name': ['BERRY GLOBAL INC','SILGAN PLASTICS CORPORATION','TECHNIMARK LLC','PLASTEK INDUSTRIES INC']
})

df_units = pd.DataFrame({
    'Unit': [
        'Grams','Kilograms','Liters','Milliliters','Meters','Centimeters','Pieces']
})

df_countries = pd.DataFrame({'Country': ['Northern America', 'China', 'Mexico', 'UK', 'Germany']})

df_raw_materials = pd.DataFrame({
    'Raw Material': ['GP-Homopolymer', 'Copolymer']
})

df_pkg_material = pd.DataFrame({
    'Packaging Material': ['Corrugated Box','Layer Sheets','Pallet']
})

df_pkg_dimension = pd.DataFrame({
    'Packaging Dimension': ['Small','Medium','Large']
})

df_labor_type = pd.DataFrame({'Labor Type': ['First-Line Supervisors of Production and Operating Workers']
})


##########################################################################################
### SETUP DATA ###
matnr = st.selectbox(
    'Select the Material Number',
     df_mat_num['Material Number'],
     index=0,
     placeholder='MATNR')
# st.write("You selected:",matnr)

if matnr == None:
    vendr = st.selectbox(
    'Select the Vendor Name',
     eval(f"df_ven_None['Vendor Name']"),
     index=0)
    # st.write("You selected:",vendr)
else:
    vendr = st.selectbox(
    'Select the Vendor Name',
        eval(f"df_ven_{matnr}['Vendor Name']"),
        index=0)
    # st.write("You selected:",vendr)

unit_count = st.text_input("Enter #units for should cost calculation",placeholder='Enter your input')
# st.write(unit_count)

estimated_units = st.text_input("Enter estimated units produced per month",placeholder='Enter your input')
# st.write(estimated_units)

country = st.selectbox('Select Country',
                     df_countries['Country'],
                     index=0)
# st.write("You selected:",country)

run_rate_per_hour = st.text_input("Enter production run rate per hour",placeholder="Enter your input")

###RAW MATERIAL###
st.write('### Raw Material Cost')

raw_material = st.selectbox('Select Raw Material',['Polypropylene (PP)'],index=0)

raw_material_grade = st.selectbox('Select Raw Material Grade',
                     df_raw_materials['Raw Material'],
                     index=1)
# st.write("You selected:",rm_grade)

uom_raw_material = st.selectbox('Unit of measure for Raw Material',
                     df_units['Unit'],
                     index=0)
# st.write("You selected:",uom_raw_material)

rm_quantity = st.text_input("Quantity required per unit of finished product",placeholder='Enter your input(Eg. 50g)')
# st.write(rm_quantity)

rm_waste_factor = st.text_input("Waste/Scrap factor (in percentage)",placeholder='Enter your input(Eg. 5%)')
# st.write(rm_waste_factor)

#################### Packaging & Material Handling #######################

st.write('### Packaging & Material Handling')
pkg_input_count = st.slider("How many packaging material you want to input?", 0, 3, 3)

pkg_list_1 = []
pkg_list_2 = []
pkg_list_3 = []
pkg_list = []
pkg_dict = {
    1 : pkg_list_1,
    2 : pkg_list_2,
    3 : pkg_list_3
}
pkg_quantity_list = []

for i in range(pkg_input_count):
    st.write(f"Input for {i+1} Packaging Material")
    pkg_name = st.selectbox('Select Packaging Material Name',
                        df_pkg_material['Packaging Material'],
                        index=i,key=f"pkg_name_key_{i}")
    pkg_dict[i+1].append(pkg_name)
    # st.write("You selected:",pkg_name)
    if pkg_name == 'Pallet':
        pkg_dim = st.selectbox('Select Packaging Material type',
                        ['Presswood','Standard Wood','Recycled Wood','Plastic','Paper'],
                        index=0,key=f"pkg_dim_key_{i}")
        pkg_dict[i+1].append(pkg_dim)
    else:
        pkg_dim = st.selectbox('Select Packaging Material Dimension',
                        df_pkg_dimension['Packaging Dimension'],
                        index=i,key=f"pkg_dim_key_{i}")
        pkg_dict[i+1].append(pkg_dim)
    
    pkg_quantity = st.text_input("Quantity required for selected #Units",placeholder='Enter your input(Eg. 5)',key=f"pkg_quant_key_{i}")
    pkg_dict[i+1].append(pkg_quantity)
    pkg_list.append(pkg_dict[i+1])

# pkg_list.append(pkg_list_2)
# pkg_list.append(pkg_list_3)
pkg_str = str(pkg_list)
################# RENTAL COST ##################################
st.write('### Rental Cost')
facility_size = st.text_input("Enter the facility size(in SQF)",placeholder='Enter your input(Eg. 20000)')
maintenance_cost = st.text_input("Enter Operating cost (% of rent)",placeholder='Enter your input')

################# ELECTRICITY COST ##################################
st.write('### Electricity Cost')
avg_unit_consume_per_month = st.text_input("Input the average units consumed per month",placeholder='Enter your input(Eg 20000)')

################# Labor COST ##################################
st.write('### Labor Cost')
labor_type = st.selectbox('Select the labor type',
                     df_labor_type['Labor Type'],
                     index=0)

man_hours = st.text_input("Input man-hours to produce selected units",placeholder='Enter your input(Eg. 4)')

st.write('### SG&A')
sga_percentage = st.text_input("Input SG&A (%)",placeholder='Enter your input(Eg. 6)')

margin_percentage = st.text_input("Input margin (%)",placeholder='Enter your input(Eg. 10)')


if st.button("Submit", key='submit', help=None, on_click=None, args=None, kwargs=None, type="secondary", icon=None, disabled=False, use_container_width=False):
    run_id = trigger_jobs(matnr,vendr,unit_count,estimated_units,country,run_rate_per_hour,raw_material,raw_material_grade,uom_raw_material,rm_quantity,rm_waste_factor,pkg_str,maintenance_cost,facility_size,avg_unit_consume_per_month,man_hours,sga_percentage,margin_percentage)
    st.write('Response Submitted')
    if run_id != None:
     result = get_result(run_id)
     st.json(result)
    





