#   slip deficit derived Pre-Coulomb stress,
#   cummulative stress change, and
#   rate of stress change
#   of the faults in vicinity of Silivri earthquakes, 
#   for the PhD study
#   author: murat sahin
#   email: sahinmurat2@itu.edu.tr

import json
import numpy as np
from plotly.subplots import make_subplots
from plotly import graph_objects as go

def getFigure(slipType, friction):

    #load data
    with open('../data/silivri_total.json','r') as file:
        panelData = json.load(file)
    
    # figure definition
    figMain = make_subplots(
        cols=1, rows=18,
        shared_xaxes='columns',
        vertical_spacing=0.002
    )
    # names of the faults
    names = ['CBNBF-II','SF-M','CBNBF-I','SRF','SF-S','SRSBF','CBEEF','KBNBF','NAFZ-D','NAFZ-C']
    # row IDs of faults
    rowID = [1,1,2,2,3,3,4,4,5,6]
    """
        structure of the subplot
    row1    'CBNBF-II', 'SF-M'
    row2    'CBNBF-I','SRF'
    row3    'SF-S','SRSBF'
    row4    'CBEEF','KBNBF'
    row5    'NAFZ-D'
    row6    'NAFZ-C'

    """
    # Plotting the pre-Coulomb pane with 6 sub-panes
    for indis, faultName in enumerate(names):
        figMain.add_trace(
            go.Heatmap(
                z = np.flipud(np.array(panelData['heatmap'][faultName]['coulomb']['pre-Coulomb'][friction])),
                x = np.array(panelData['heatmap'][faultName]['geometry']['x']),
                zmin=-5,
                zmax=5,
                colorscale='RdBu_r',
                name=faultName,
                hovertemplate='%{z:.2f} MPa',
                showscale=True if rowID[indis]==6 else False,
                colorbar=dict(
                    title = 'Pre-Coulomb<br>stress<br>(MPa)',
                    len = 0.35,
                    x = 1,
                    y = 0.85
                )
            ),
            col=1,
            row=rowID[indis]
        )
    # Cummulative stress change pane with 6 sub-panes
    rowID = np.array(rowID)+6
    for indis, faultName in enumerate(names):
        figMain.add_trace(
            go.Heatmap(
                z=np.flipud(np.array(panelData['heatmap'][faultName]['coulomb']['total change'][slipType][friction])*10),
                x=np.array(panelData['heatmap'][faultName]['geometry']['x']),
                zmin = -1,
                zmax = 1,
                name = faultName,
                colorscale = 'portland',
                hovertemplate='%{z:.2f} bars',
                showscale=True if rowID[indis]==12 else False,
                colorbar = dict(
                    title = 'Event based<br>cummulative<br>stress change<br>(bars)',
                    len = 0.35,
                    x = 1,
                    y = 0.5
                )
            ),
            col = 1,
            row=rowID[indis]
        )
    # rate of change
    rowID = np.array(rowID)+6
    for indis, faultName in enumerate(names):
        figMain.add_trace(
            go.Heatmap(
                z=np.flipud((panelData['heatmap'][faultName]['coulomb']['total change'][slipType][friction]/np.abs(panelData['heatmap'][faultName]['coulomb']['pre-Coulomb'][friction]))*100),
                x=panelData['heatmap'][faultName]['geometry']['x'],
                zmin = -10,
                zmax = 10,
                name = faultName,
                colorscale = 'spectral_r',
                hovertemplate='%{z:.2f} %',
                showscale=True if rowID[indis]==18 else False,
                colorbar = dict(
                    title = 'Rate of<br>stress<br>change<br>(%)',
                    len = 0.35,
                    x = 1,
                    y = 0.15
                )
            ),
            col = 1,
            row=rowID[indis]
        )
    figMain.update_layout(
        margin=dict(l=5,r=5,t=5,b=5),
        height = 800,
        plot_bgcolor='black',
        paper_bgcolor='black',
        font_color='white',
    )
    figMain.update_xaxes(gridcolor='black')
    figMain.update_yaxes(gridcolor='black',zerolinecolor='black')
    figMain.update_yaxes(showticklabels=False)
    return figMain