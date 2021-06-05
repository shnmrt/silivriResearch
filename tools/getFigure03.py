#   Spatial distribution of the 2019 Silivri earthquakes 
#   dataset from Bentz et al. (2020) used in Durand et al (2020)
#   with a 3D fault model
#   for the PhD study
#   author: murat sahin
#   email: sahinmurat2@itu.edu.tr

import json
import pandas as pd 
import numpy as np
from PIL import Image
import plotly.graph_objects as go
import sys
sys.path.append('./tools')
from layoutMaker import Lgenerator


def getFigure():
    plotData = []
    
    # load data
    #locmap = Image.open('../tools/thumbnail.png')
    with open('../data/faults.json','r') as file:
        faults = json.load(file)
    
    df_EQ = pd.read_csv('../data/Bentz(2020)_reloc.txt', sep='\t')


    for fault in faults.keys():
        faults[fault].keys()
        mesh = go.Mesh3d(
            x=faults[fault]['x'],
            y=faults[fault]['y'],
            z=faults[fault]['z'],
            i=faults[fault]['i'],
            j=faults[fault]['j'],
            k=faults[fault]['k'],
            color=faults[fault]['color'],
            name=faults[fault]['name'],
            hovertext=faults[fault]['hovertext'],
            opacity=faults[fault]['opacity'],
            hoverinfo=faults[fault]['hoverinfo'],
            showlegend=faults[fault]['showlegend'],
            legendgroup=faults[fault]['legendgroup']
        )
        plotData.append(mesh)

    df_EQ = df_EQ.sort_values(by=['MAG'])
    tremorLegend = list() # same fucntion with the nameTAG variable
    dates = list()
    for dd in range(df_EQ.shape[0]):
        date = str(int(df_EQ.iloc[dd]['YR']))+'-'+\
                str(int(df_EQ.iloc[dd]['MO']))+'-'+\
                str(int(df_EQ.iloc[dd]['DY']))+' T'+\
                str(int(df_EQ.iloc[dd]['HR']))+':'+\
                str(int(df_EQ.iloc[dd]['MI']))+':'+\
                str((df_EQ.iloc[dd]['SC']))
        dates.append(date)

        if df_EQ.iloc[dd]['MAG'] < 2:
            lg = 'M < 2'
            cc = 'lightblue'
            if lg not in tremorLegend:
                tremorLegend.append(lg)
                legend_option = True
            else:
                legend_option = False
        elif 2 <= df_EQ.iloc[dd]['MAG'] < 3:
            lg = '2 < M < 3'
            cc = 'green'
            if lg not in tremorLegend:
                tremorLegend.append(lg)
                legend_option = True
            else:
                legend_option = False
        elif 3 <= df_EQ.iloc[dd]['MAG'] < 4:
            lg = '3 < M < 4'
            cc = 'chocolate'
            if lg not in tremorLegend:
                tremorLegend.append(lg)
                legend_option=True
            else:
                legend_option=False
        else:
            lg = '4 < M'
            cc = 'red'
            if lg not in tremorLegend:
                tremorLegend.append(lg)
                legend_option=True
            else:
                legend_option=False

        ff = go.Scatter3d(
            x = [df_EQ.iloc[dd]['LON']],
            y = [df_EQ.iloc[dd]['LAT']],
            z = [df_EQ.iloc[dd]['DEPTH']*-1],
            name=lg,
            legendgroup=lg,
            showlegend=legend_option,
            mode='markers',
            hoverinfo='text',
            text=['Date: %s<br>M: %s' %(date,df_EQ.iloc[dd]['MAG'])],
            marker=dict(
                size=df_EQ.iloc[dd]['MAG']*2,
                color=cc
            )

        )
        plotData.append(ff)
    # Adding the North Arrow
    #HEAD
    plotData.append(
        go.Cone(
            x=[28.39],
            y=[40.9],
            z=[-21],
            u=[0],
            v=[0.02],
            w=[0],
            colorscale=['white','white'],
            showlegend=False,
            showscale=False,
            hoverinfo='text',
            hovertext='North Arrow'
        )
    )
    #TAIL
    plotData.append(
        go.Scatter3d(
            x=[28.39, 28.39],
            y=[40.87,40.9],
            z=[-21,-21],
            mode='lines',
            hoverinfo='text',
            hovertext='North Arrow',
            showlegend=False,
            line=dict(
                color='white',
                width=10
            )
        )
    )

    return go.Figure(
        data=plotData,
        layout=Lgenerator('figure3')
    )