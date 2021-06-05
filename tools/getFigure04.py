#   Event based coseimic stress change in vicinity of Silivri earthquakes
#   for the PhD study
#   author: murat sahin
#   email: sahinmurat2@itu.edu.tr

import json
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def getFigure(slipType, friction):

    #event based data load
    with open('../data/Silivri_Coulomb.json','r') as file:
        eventLoad = json.load(file)

    # building figure
    fig = make_subplots(
        rows=2, cols=2,
        vertical_spacing=0.05,
        specs=[
            [{'type':'scene'},{'type':'scene'}],
            [{'type':'scene'},{'type':'scene'}]
        ],
        subplot_titles=('2019-09-24 08:00:20 M 4.7 (1<sup>st</sup> Event)',\
                        '2019-09-26 10:59:02 M 5.8 (2<sup>nd</sup> Event)',\
                        '2019-09-26 11:26:36 M 4.1 (3<sup>rd</sup> Event)',\
                        '2019-09-26 20:20:18 M 4.1 (4<sup>th</sup> Event)')
    )

    # First Event M 4.7
    eventID='01'
    # plottin slip distribution on source fault
    fig.add_trace(
        go.Mesh3d(
            name='SRF',
            x=eventLoad['coseismic'][eventID]['x'],
            y=eventLoad['coseismic'][eventID]['y'],
            z=np.array(eventLoad['coseismic'][eventID]['z'])/1000, # m to km
            i=eventLoad['coseismic'][eventID]['i'],
            j=eventLoad['coseismic'][eventID]['j'],
            k=eventLoad['coseismic'][eventID]['k'],
            intensity=np.array(eventLoad['coseismic'][eventID]['slip'][slipType])*100000, # km to cm,
            intensitymode='cell',
            hovertemplate='%{intensity:.4f} cm',
            cmin=0,
            colorscale='viridis',
            colorbar={
                'bgcolor':'gray',
                'title': 'Slip (cm)',
                'len':0.35,
                'x':-0.045,
                'y':0.85
            }
        ),
        col=1,
        row=1
    )
    # plotting coulomb stress on receiver faults
    for f in eventLoad['coulomb'][eventID]:
        fig.add_trace(
            go.Mesh3d(
                name=eventLoad['coulomb']['faults'][f]['name'],
                x=eventLoad['coulomb']['faults'][f]['geom']['x'],
                y=eventLoad['coulomb']['faults'][f]['geom']['y'],
                z=np.array(eventLoad['coulomb']['faults'][f]['geom']['z'])/1000, # m to km
                i=eventLoad['coulomb']['faults'][f]['geom']['i'],
                j=eventLoad['coulomb']['faults'][f]['geom']['j'],
                k=eventLoad['coulomb']['faults'][f]['geom']['k'],
                intensity=np.array(eventLoad['coulomb']['faults'][f]['cou'][slipType][eventID][friction])*10, # MPa to bar
                cmin=-2,
                cmax=2,
                colorscale='RdBu_r',
                intensitymode='cell',
                hovertemplate='%{intensity:.4f} bar',
                colorbar={
                    'bgcolor':'grey',
                    'title':'Coulomb<br>Stress<br><br>(bar)',
                    'len':0.32,
                    'x':-0.045,
                    'y':0.51,
                }
            ),
            col=1,
            row=1
        )

    # Second Event
    eventID='02'
    fig.add_trace(
        go.Mesh3d(
            name='SF-M',
            x=eventLoad['coseismic'][eventID]['x'],
            y=eventLoad['coseismic'][eventID]['y'],
            z=np.array(eventLoad['coseismic'][eventID]['z'])/1000, # m to km
            i=eventLoad['coseismic'][eventID]['i'],
            j=eventLoad['coseismic'][eventID]['j'],
            k=eventLoad['coseismic'][eventID]['k'],
            intensity=np.array(eventLoad['coseismic'][eventID]['slip'][slipType])*100000, # km to cm,
            intensitymode='cell',
            hovertemplate='%{intensity:.4f} cm',
            cmin=0,
            colorscale='viridis',
            colorbar={
                'bgcolor':'gray',
                'title': 'Slip (cm)',
                'len':0.35,
                'x':1,
                'y':0.85
            }
        ),
        col=2,
        row=1
    )
    for f in eventLoad['coulomb'][eventID]:
        fig.add_trace(
            go.Mesh3d(
                name=eventLoad['coulomb']['faults'][f]['name'],
                x=eventLoad['coulomb']['faults'][f]['geom']['x'],
                y=eventLoad['coulomb']['faults'][f]['geom']['y'],
                z=np.array(eventLoad['coulomb']['faults'][f]['geom']['z'])/1000, # m to km
                i=eventLoad['coulomb']['faults'][f]['geom']['i'],
                j=eventLoad['coulomb']['faults'][f]['geom']['j'],
                k=eventLoad['coulomb']['faults'][f]['geom']['k'],
                intensity=np.array(eventLoad['coulomb']['faults'][f]['cou'][slipType][eventID][friction])*10, # MPa to bar
                cmin=-2,
                cmax=2,
                colorscale='RdBu_r',
                intensitymode='cell',
                hovertemplate='%{intensity:.4f} bar',
                showscale=False
            ),
            col=2,
            row=1
        )

    # Third Event
    eventID='03'
    fig.add_trace(
        go.Mesh3d(
            name='SRSBF',
            x=eventLoad['coseismic'][eventID]['x'],
            y=eventLoad['coseismic'][eventID]['y'],
            z=np.array(eventLoad['coseismic'][eventID]['z'])/1000, # m to km
            i=eventLoad['coseismic'][eventID]['i'],
            j=eventLoad['coseismic'][eventID]['j'],
            k=eventLoad['coseismic'][eventID]['k'],
            intensity=np.array(eventLoad['coseismic'][eventID]['slip'][slipType])*100000, # km to cm,
            intensitymode='cell',
            hovertemplate='%{intensity:.4f} cm',
            cmin=0,
            colorscale='viridis',
            colorbar={
                'bgcolor':'gray',
                'title': 'Slip (cm)',
                'len':0.35,
                'x':-0.045,
                'y':0.17
            }
        ),
        col=1,
        row=2
    )
    for f in eventLoad['coulomb'][eventID]:
        fig.add_trace(
            go.Mesh3d(
                name=eventLoad['coulomb']['faults'][f]['name'],
                x=eventLoad['coulomb']['faults'][f]['geom']['x'],
                y=eventLoad['coulomb']['faults'][f]['geom']['y'],
                z=np.array(eventLoad['coulomb']['faults'][f]['geom']['z'])/1000, # m to km
                i=eventLoad['coulomb']['faults'][f]['geom']['i'],
                j=eventLoad['coulomb']['faults'][f]['geom']['j'],
                k=eventLoad['coulomb']['faults'][f]['geom']['k'],
                intensity=np.array(eventLoad['coulomb']['faults'][f]['cou'][slipType][eventID][friction])*10, # MPa to bar
                cmin=-2,
                cmax=2,
                colorscale='RdBu_r',
                intensitymode='cell',
                hovertemplate='%{intensity:.4f} bar',
                showscale=False
            ),
            col=1,
            row=2
        )

    # Fourth Event
    eventID='04'
    fig.add_trace(
        go.Mesh3d(
            name='SRF',
            x=eventLoad['coseismic'][eventID]['x'],
            y=eventLoad['coseismic'][eventID]['y'],
            z=np.array(eventLoad['coseismic'][eventID]['z'])/1000, # m to km
            i=eventLoad['coseismic'][eventID]['i'],
            j=eventLoad['coseismic'][eventID]['j'],
            k=eventLoad['coseismic'][eventID]['k'],
            intensity=np.array(eventLoad['coseismic'][eventID]['slip'][slipType])*100000, # km to cm,
            intensitymode='cell',
            hovertemplate='%{intensity:.4f} cm',
            cmin=0,
            colorscale='viridis',
            colorbar={
                'bgcolor':'gray',
                'title': 'Slip (cm)',
                'len':0.35,
                'x':1,
                'y':0.17
            }
        ),
        col=2,
        row=2
    )
    for f in eventLoad['coulomb'][eventID]:
        fig.add_trace(
            go.Mesh3d(
                name=eventLoad['coulomb']['faults'][f]['name'],
                x=eventLoad['coulomb']['faults'][f]['geom']['x'],
                y=eventLoad['coulomb']['faults'][f]['geom']['y'],
                z=np.array(eventLoad['coulomb']['faults'][f]['geom']['z'])/1000, # m to km
                i=eventLoad['coulomb']['faults'][f]['geom']['i'],
                j=eventLoad['coulomb']['faults'][f]['geom']['j'],
                k=eventLoad['coulomb']['faults'][f]['geom']['k'],
                intensity=np.array(eventLoad['coulomb']['faults'][f]['cou'][slipType][eventID][friction])*10, # MPa to bar
                cmin=-2,
                cmax=2,
                colorscale='RdBu_r',
                intensitymode='cell',
                hovertemplate='%{intensity:.4f} bar',
                colorbar={
                    'bgcolor':'grey',
                    'title':'Coulomb<br>Stress<br><br>(bar)',
                    'len':0.32,
                    'x':1,
                    'y':0.51,
                }
            ),
            col=2,
            row=2
        )



    #NorthArrow
    for r in [1,2]:
        for c in [1,2]:
            fig.add_trace(
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
                ),
                row=r,
                col=c
            )
            fig.add_trace(
                go.Scatter3d(
                    x=[28.39,28.39],
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
                ),
                col=c,
                row=r
            )
    
    # Layout settings
    mainScene = dict(
        bgcolor='rgb(25,25,25)',
        camera=dict(
            eye = dict(x=1, y=.5,z=1),
            up  = dict(x=0, y=0, z=3)
        ),
        xaxis=dict(
            showbackground=False,
            color='white',
            title='Longitude',
            range=[28.0, 28.4]
        ),
        yaxis=dict(
            showbackground=False,
            color='white',
            title='Latitude',
            range=[40.775, 40.925]
        ),
        zaxis=dict(
            showbackground=False,
            color='white',
            title='Depth (km)',
            range=[-22, 0]
        ),
        aspectmode='manual',
        aspectratio=dict(x=2,y=1,z=0.3),
    )


    fig.update_layout(
        height=800,
        paper_bgcolor='black',
        font_color='white',
        hoverlabel=dict(
            bgcolor='black'
        ),
        scene=mainScene,
        scene2=mainScene,
        scene3=mainScene,
        scene4=mainScene,
        #title=dict(
        #    text="<b>            Structural complexity and Stress Change along the North Anatolian Fault Offshore Istanbul identified by the 2019 Silivri earthquakes</b><br>\
        #         Murat Şahin,<sup>1</sup> Cenk Yaltırak,<sup>1</sup> Fatih Bulut<sup>2</sup> and Aslı Doğru<sup>2</sup><br><br>\
        #         <sup>1</sup> <i> Istanbul Technical University, Faculty of Mines, Department of Geological Engineering, Istanbul, Turkey</i><br>\
        #         <sup>2</sup> <i> Boğaziçi University, Kandilli Observatory and Earthquake Research Institute, Department of Geodesy, Istanbul, Turkey</i>",
        #    x=0.5,
        #    y=0.98,
        #    font=dict(size=12)
        #),
        #margin=dict(b=100,t=150),
        #images=[
        #   dict(
        #       xanchor='right',
        #       yanchor='top',
        #       layer='above',
        #       source=locmap,
        #       xref='paper',
        #       yref='paper',
        #       x=1.05,
        #       y=1.2,
        #       sizex=0.18,
        #       sizey=0.18,
        #   )
        #],
    )
    return fig