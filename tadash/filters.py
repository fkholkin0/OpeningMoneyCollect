import dataclasses as dc
import datetime as dt
import os

import pandas as pd
import streamlit as st

@dc.dataclass
class DateFilters:
    date_from: str
    date_to: str
    days: int
    develop_mode: bool


dev_mode_allowed = os.environ.get('DEV_MODE_ALLOWED') == 'true'


def get_date_filters(
    start_date: dt.datetime.date = dt.datetime.now(tz=dt.UTC).date() - dt.timedelta(days=90),
    days_selected: int = 89,
    allways_actual: bool = False
                     ) -> DateFilters:
    if allways_actual:
        days_selected = (start_date - (dt.datetime.now(tz=dt.UTC).date())).days - 1
    filter_date_range = pd.date_range(
        start=start_date,
        end=dt.datetime.now(tz=dt.UTC).date(),
        freq='D',
    )

    with st.sidebar:
        date_from, date_to = st.date_input(
            label='Date filter',
            value=(
                filter_date_range.max() - dt.timedelta(days=days_selected),
                filter_date_range.max() - dt.timedelta(days=1),
            ),
            min_value=filter_date_range.min(),
            max_value=filter_date_range.max(),
            format='YYYY-MM-DD',
        )

        if dev_mode_allowed:
            develop_mode = st.toggle('Dev mode')

        date_from, date_to = pd.to_datetime(date_from), pd.to_datetime(date_to)
        dates_difference = (date_to- date_from).days

        return DateFilters(
            date_from=date_from.strftime('%Y-%m-%d'),
            date_to=date_to.strftime('%Y-%m-%d'),
            days=dates_difference,
            develop_mode=develop_mode if dev_mode_allowed else False,
        )
