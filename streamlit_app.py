# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(":cup_with_straw: Customize Your Smoothie :tropical_drink:")
st.write(
    """Choose the fruits you want in your custom Smoothie! :point_right:
    """)

name_on_order = st.text_input('Name on Smoothie:')
st.write('The name on your Smoothie will be:', name_on_order)

session = get_active_session()
my_dataframe = session.table("smoothies.public.fruit_options").select (col('FRUIT_NAME'))
#st.dataframe(data=my_dataframe, use_container_width=True)

ingredients_list = st.multiselect(
    'Choose up to 5 ingredients:',
    my_dataframe,
    max_selections=5
    )

#dočasná stopka
#st.write(my_insert_stmt)
#st.stop()


if ingredients_list:
        ingredients_string = ''

        for fruit_chosen in ingredients_list:
            ingredients_string += fruit_chosen + ' '
    
        #st.write(ingredients_string) 
#řádek , '1' je pro testování, když mím víc sloupců v tabulce
        my_insert_stmt = """ insert into smoothies.public.orders
            values ('1','1'
            ,'""" + ingredients_string + """', '""" + name_on_order + """'
            ,'1'
            )"""

    
        time_to_insert = st.button ('Submit Order')
    
        if time_to_insert:
            session.sql(my_insert_stmt).collect()
          
            st.success('Your Smoothie is ordered! ' + name_on_order +'!', icon="✅")
