import streamlit as st


def br(how_much:int = 1):
    return st.markdown("<br>"*how_much, unsafe_allow_html=True)

def tplotly_chart(fig):
    return st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})


def shrag():
    return "¯\\\\_(ツ)\_/¯"

def summury(header: str, points: list):
    text = f""" ##### {header}
    {'- '.join([bulet + '<br>' for bulet in points])}
    """
    return st.markdown(text, unsafe_allow_html=True)

def hide_ui_and_padding():
    remove_space_style = """
    <style>
        /* Полностью скрываем header */
        [data-testid="stHeader"] {
            display: none;
        }
        /* Скрываем кнопку сайдбара */
        [data-testid="stBaseButton-headerNoPadding"] {
            display: none;
        }
        /* Скрываем footer */
        footer {
            visibility: hidden;
        }
        /* Убираем отступы у основного контейнера */
        .stAppViewBlockContainer {
            padding-top: 0;
            margin-top: 0;
        }
        /* Убираем отступы у контентного контейнера */
        .stVerticalBlockBorderWrapper {
            padding-top: 0;
            margin-top: 0;
        }
    </style>
    """
    st.markdown(remove_space_style, unsafe_allow_html=True)
    pass


def pritty_st():
    st.markdown(
    """
    <style>
    [data-testid="stDecoration"] {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
    )
    pass