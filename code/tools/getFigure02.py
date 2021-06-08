#   Source Mechanism solutions of the M3+ earthquakes of Silivri
#   with a 3D fault model
#   for the PhD study
#   author: murat sahin
#   email: sahinmurat2@itu.edu.tr

import json
from PIL import Image
import plotly.graph_objects as go
import sys
sys.path.append('../tools')
from layoutMaker import Lgenerator

def getFigure():

    # container for data in form of list
    plotData = []

    # loading the data files
    #locmap = Image.open('../tools/thumbnail.png')
    with open('../data/faults.json','r') as file:
        faults = json.load(file)
    with open('../data/focalMechs.json','r') as file:
        focalMech = json.load(file)

    # Adding the fault geometries
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

    #Adding the beachballs 
    for s in focalMech.keys():
        for e in focalMech[s].keys():
            spheres = go.Surface(
                x=focalMech[s][e]['x'],
                y=focalMech[s][e]['y'],
                z=focalMech[s][e]['z'],
                hoverinfo=focalMech[s][e]['hoverinfo'],
                text=focalMech[s][e]['text'],
                colorscale=focalMech[s][e]['colorscale'],
                surfacecolor=focalMech[s][e]['surfacecolor'],
                showlegend=focalMech[s][e]['showlegend'],
                showscale=focalMech[s][e]['showscale'],
                legendgroup=focalMech[s][e]['legendgroup'],
                name=focalMech[s][e]['name'],
            )
            plotData.append(spheres)
    
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
        layout=Lgenerator('figure2')
    )