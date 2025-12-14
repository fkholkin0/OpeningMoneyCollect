import pandas as pd

import requests


import streamlit as st
from tadash.helpers import  pritty_st, br
from tadash.gsauth import gs_oauth
import webbrowser


@st.cache_data
def getPeople():
    auth = gs_oauth()
    gs_data = (
        auth
        .open_by_key("18Wf1wWZIMNCXyzAxlKtfCKfB3T9S1c2ItiBHTSOZLUI")
        .worksheet('main')
        .get_values('A:E')
    )
    return pd.DataFrame(gs_data[1:], columns=gs_data[0])


st.set_page_config(
    page_title='Сбор на шары',
    layout="centered",
    page_icon='static/favicon.png',
    initial_sidebar_state='collapsed',
)

pritty_st()
# hide_ui_and_padding()


data = getPeople()
people_list = data.query('`status` != "complete"')['FIO'].to_list()
  
val = st.multiselect( label="Выбери участника", options= people_list,
   default=[], 
)



if "data" not in st.session_state:
    st.session_state["data"] = pd.DataFrame({
        "FIO": val,
        "complect": pd.NA
    })

complect_price_map = {
    "Прокатный типман 500": 500,
    "Механика и тубы 1000": 1000,
    "Электроника и тубы 1500": 1500,
}



edited_data = st.data_editor(
   (
      pd.DataFrame({"FIO":val})
      .merge(st.session_state['data'], how='left', left_on='FIO', right_on='FIO')
   )
    ,column_config={
        "complect": st.column_config.SelectboxColumn(
            "Комплект",
            options=list(complect_price_map.keys()),
            required=False,
        )
    },
    disabled=["FIO"],
    hide_index=True,
    key="data_editor",
)


if not edited_data['complect'].isna().any() and edited_data.size > 0:
    total_price = edited_data.assign(price = lambda d: d['complect'].apply( lambda x: complect_price_map.get(x)))['price'].sum()
    col1, col2, col3 = st.columns([0.2, 0.3,  0.35])

    with col1:
        st.caption("Комментарий платежа")
        st.code(f"""{','.join(edited_data['FIO'].apply(lambda x: x.replace(" ", "")).tolist())}""")

    with col3:
        # br(1)
        st.markdown(
       f"""
       <div style="font-size: 30px; font-weight: bold; color: #4CAF50; text-align: left;">
           Всего к оплате: {total_price}
       </div>
       """,
       unsafe_allow_html=True
        )
        data_to_send = edited_data.assign(
            price=lambda d: d["complect"].apply(lambda x: complect_price_map.get(x))
            ).to_dict("records")

        post_url = "https://script.google.com/macros/s/AKfycbysTYvVhdNdu3C36psqIjQUnAdBpMM82ggamlWXSxBx70hqRhgoAT0mi4PmixVX-_xZ/exec"
        redirect_url = "https://www.tbank.ru/collectmoney/crowd/r_WJeJcbTXZg.FzRTyxtcnP/KIf8i73700/?short_link=6Lly6zmCwnV&httpMethod=GET"

            
        lb_value = st.button(label= "🚀 Ок, давайте скорее оплачивать!")
        if lb_value:
            webbrowser.open(redirect_url)
            response = requests.post(post_url, json={"data": data_to_send, "data_source": "streamlit_form"})
            
        
        















































        




















