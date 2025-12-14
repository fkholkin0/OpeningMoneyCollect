import dataclasses as dc
import typing as t

import plotly.io as pio




@dc.dataclass
class PlotlyOptions:
    display_mode_bar: bool = False
    colorway: tuple[str, ...] = (
        '#8AC7E5',
        '#716AD1',
        '#E5ACAC',
        '#82BEBE',
        '#C799DF',
    )

    @property
    def hide(self) -> dict[str, t.Any]:
        return {'displayModeBar': False}

default = PlotlyOptions(
    display_mode_bar=False,
    colorway=(
        '#D796C1',
        '#716AD1',
        '#E5ACAC',
        '#82BEBE',
        '#FC6667',
        '#D796C1',
        '#A8A3F1',
        '#FDE2A2',
        '#96DDB9',
        '#95ADE2',
        '#D481B9',
        '#FAD370',
        '#66C797',
        '#95ADE2',
        '#AF5692',
        '#1D6B77',
        '#B79FE9',
        '#D481B9',
        '#7AC6B2'
    ),
)

rd = PlotlyOptions(
    display_mode_bar=False,
    colorway=(
        '#716AD1',
        '#7BD3EA',
        '#C9F4AA',
        '#FFADAD',
        '#CDF0EA',
        '#A1EEBD',
        '#D796C1',
        '#96DDB9',
        '#95ADE2',
        '#D481B9',
        '#FAD370',
        '#66C797',
        '#95ADE2',
        '#AF5692',
        '#1D6B77',
        '#B79FE9',
        '#D481B9',
        '#7AC6B2'
    ),
)

r2 = PlotlyOptions(
    display_mode_bar=False,
    colorway=(
        '#96DDB9',
        '#D481B9',
        '#716AD1',
        '#FDE2A2',
        '#1D6B77',
        '#82BEBE',
        '#AF5692',
        '#A8A3F1',
        '#FDE2A2',
        '#FC6667',
        '#D796C1',
        '#96DDB9',
        '#95ADE2',
        '#D481B9',
        '#FAD370',
        '#66C797',
        '#95ADE2',
        '#B79FE9',
        '#D481B9',
        '#7AC6B2'
    ),
)

r3 = PlotlyOptions(
    display_mode_bar=False,
    colorway=(
        '#96DDB9',
        '#D481B9',
        '#716AD1',
        '#FDE2A2',
        '#1D6B77',
        '#82BEBE',
        '#AF5692',
        '#A8A3F1',
        '#FDE2A2',
        '#FC6667',
        '#D796C1',
        '#96DDB9',
        '#95ADE2',
        '#D481B9',
        '#FAD370',
        '#66C797',
        '#95ADE2',
        '#B79FE9',
        '#D481B9',
        '#7AC6B2'
    ),
)


shift = PlotlyOptions(
    display_mode_bar=False,
    colorway=(
        '#8AC7E5',
        '#716AD1',
        '#E5ACAC',
        '#82BEBE',
        '#C799DF',
        '#D796C1',
        '#A8A3F1',
        '#FDE2A2',
        '#96DDB9',
        '#95ADE2'
    ),
)
s2 = PlotlyOptions(
    display_mode_bar=False,
    colorway=(
        '#716AD1',
        '#8AC7E5',
        '#C799DF',
        '#D796C1',
        '#82BEBE',
        '#96DDB9',
        '#E5ACAC',
        '#FDE2A2',
        '#A8A3F1',
        '#95ADE2'
    ),
)



formating = PlotlyOptions(
    display_mode_bar=False,
    colorway=(
        '#5C79B6',
        '#95ADE2',
        '#895ECE',
        '#B79FE9',
        '#5C8C52',
        '#91C089',
        '#AF5692',
        '#D796C1'
    ),
)


fun = PlotlyOptions(
    display_mode_bar=False,
    colorway=(
        '#D481B9',
        '#7AC6B2',
        '#A8A3F1',
        '#FAD370',
        '#FC6667',
        '#66C797',
        '#C460A5',
        '#1D6B77',
        '#716AD1',
        '#91C089',
    ),
)
f2 = PlotlyOptions(
    display_mode_bar=False,
    colorway=(
        '#66C797',
        '#FAD370',
        '#7AC6B2',
        '#FC6667',
        '#716AD1',
        '#D481B9',
        '#1D6B77',
        '#91C089',
        '#C460A5',
        '#A8A3F1',
    ),
)
f3 = PlotlyOptions(
    display_mode_bar=False,
    colorway=(
        '#CC0B28',
        '#0077FF',
        '#FAD370',
        '#7AC6B2',
        '#716AD1',
        '#D481B9',
        '#1D6B77',
        '#91C089',
        '#C460A5',
        '#A8A3F1',
    ),
)
g1 = PlotlyOptions(
    display_mode_bar=False,
    colorway=(
        '#A3D8F4', '#005377', '#0477BF', '#FFD1DC', '#BF4D73', '#DB7093',
        '#D0E1F9', '#4B0082', '#8A2BE2', '#FFE4B2'
    ),
)

g2 = PlotlyOptions(
    display_mode_bar=False,
    colorway=(
        '#FFE4C4', '#A52A2A', '#8B4513', '#B0E0E6', '#4682B4', '#5F9EA0',
        '#FFF8DC', '#556B2F', '#6B8E23', '#F0E68C'
    ),
)

g3 = PlotlyOptions(
    display_mode_bar=False,
    colorway=(
        '#E6E6FA', '#8A2BE2', '#4B0082', '#FFFACD', '#DAA520', '#B8860B',
        '#F5F5DC', '#228B22', '#006400', '#E0FFFF'
    ),
)

g4 = PlotlyOptions(
    display_mode_bar=False,
    colorway=(
        '#FFB3BA', '#FFDFBA', '#FFFFBA', '#BAFFC9', '#BAE1FF',
        '#E6B3FF', '#FFBAFF', '#B0E0E6', '#FFD1DC', '#D3FFCE'
    ),
)

g5 = PlotlyOptions(
    display_mode_bar=False,
    colorway=(
        '#FFCCCC', '#FFCC99', '#FFFF99', '#CCFFCC', '#CCCCFF',
        '#FF99CC', '#FF6666', '#99CCFF', '#FFCC66', '#99FFCC'
    ),
)

g6 = PlotlyOptions(
    display_mode_bar=False,
    colorway=(
        '#FF6961', '#77DD77', '#84B6F4', '#F49AC2', '#FFB347',
        '#D3B6FF', '#FFB3BA', '#FFDAC1', '#FFFFBA', '#BAFFC9'
    ),
)




def set_colors(options: PlotlyOptions) -> None:
    pio.templates[pio.templates.default].layout.colorway = options.colorway

