#   Spatiotemporal evolution of the 2019 Silivri earthquakes
#   with 3D fault model that gathered from seismic profiles
#   and 1D crustal structure models of the Sea of Marmara
#   for the PhD study
#   author: murat sahin
#   email: sahinmurat2@itu.edu.tr


# importing the libraries   
import json
import pandas as pd
import numpy as np
from PIL import Image
import plotly.graph_objects as go
import sys
sys.path.append('../tools')
from layoutMaker import Lgenerator

def getFigure():
    # loading the data files
    #locmap = Image.open('../tools/thumbnail.png')

    with open('../data/relocatedHypocenters.json','r') as file:
        df_EQ = pd.read_json(json.load(file), orient='split')

    with open('../data/faults.json','r') as file:
        faults = json.load(file)

    # pivot table and trait function for 
    # animation of the earthquakes 
    def pivotTable(dataFrame):
        df = dataFrame
        dates, legendG, CC = [], [], []
        for dd in range(df.shape[0]):
            date = str(int(df.iloc[dd]['YR']))+'-'+\
                str(int(df.iloc[dd]['MO']))+'-'+\
                str(int(df.iloc[dd]['DY']))+' T'+\
                str(int(df.iloc[dd]['HR']))+':'+\
                str(int(df.iloc[dd]['MI']))+':'+\
                str((df.iloc[dd]['SC']))
            dates.append(date)
            if df.iloc[dd]['MAG'] < 2:
                legendG.append('M < 2')
                CC.append('lightblue')
            elif 2 <= df.iloc[dd]['MAG'] < 3:
                legendG.append('2 < M < 3')
                CC.append('green')
            elif 3 <= df.iloc[dd]['MAG'] < 4:
                legendG.append('3 < M < 4')
                CC.append('chocolate')
            else:
                lg ='4 < M'
                legendG.append('4 < M')
                CC.append('red')


        df['name'] = legendG # name and legendgroup
        df['DATE'] = dates
        df['CC'] = CC
        df['DEPTH'] *= -1
        df['DATE'] = pd.to_datetime(df['DATE'], infer_datetime_format=True)
        df = df.sort_values(['DATE'])
        df['DATE']=df['DATE'].astype(str)

        df = pd.pivot(df, index='DATE', columns='name', values=['LAT', 'LON','DEPTH','MAG','CC'])
        return df

    df = pivotTable(df_EQ)
    #print(df.head())


    # container for data in form of list
    plotData = []

    # loading the fault meshes by iterating 
    for fault in faults.keys():
        faultMesh = go.Mesh3d(
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
        plotData.append(faultMesh)

    # loading empty scatters for legends
    # it is an ugly work around 
    plotData.append(
        go.Scatter3d(
            x=[np.nan], y=[np.nan], z=[np.nan],
            name='M < 2', legendgroup=0,
            mode='markers', marker=dict(color='lightblue', size=6)
        )
    )
    plotData.append(
        go.Scatter3d(
            x=[np.nan], y=[np.nan], z=[np.nan],
            name='2 < M < 3', legendgroup=1,
            mode='markers', marker=dict(color='green', size=8)
        )
    )
    plotData.append(
        go.Scatter3d(
            x=[np.nan], y=[np.nan], z=[np.nan],
            name='3 < M < 4', legendgroup=2,
            mode='markers', marker=dict(color='chocolate', size=10)
        )
    )
    plotData.append(
        go.Scatter3d(
            x=[np.nan], y=[np.nan], z=[np.nan],
            name='4 < M', legendgroup=3,
            mode='markers', marker=dict(color='red', size=12)
        )
    )

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


    # initializing the Layout Props.
    Layout = Lgenerator('figure1')
    # slider trait of the animation
    Layout['sliders'] = [
        dict(
            steps = [
                dict(
                    method='animate',
                    args=[[f'{k+1}'],
                    dict(
                        mode='immediate',
                        frame=dict(
                           duration=3,
                           redraw=True
                        ),
                        transition = dict(duration=0)
                    )
                    ],
                    label = str(df_EQ.iloc[k]['DATE'])
                ) for k in range(1, df_EQ.shape[0])
            ],
            active=1,
            transition = dict(duration=0),
            x=0.1,
            y=0.1,
            xanchor="left",
            yanchor="top",
            len=0.9,
            currentvalue = dict(
                font=dict(size=16, color='white'),
                prefix='Date: ',
                visible=True,
                xanchor='right'
            ),
            font = dict(color='white', size=7)
        )
    ]
    # Building the Frames 
    frames = [
        dict(
            name=f'{k}',
            data = [
                dict(
                    type='scatter3d',
                    x = df.iloc[:k]['LON','M < 2'],
                    y = df.iloc[:k]['LAT','M < 2'],
                    z = df.iloc[:k]['DEPTH', 'M < 2'],
                    mode='markers',
                    marker = dict(
                        color='lightblue',
                        size=6
                    ),
                    hoverinfo='text',
                    text=['Date: %s<br>M: %s<br>' %(d,m) for d,m in (zip(df['MAG','M < 2'][:k].index,df['MAG','M < 2'][:k]))]
                ),
                dict(
                    type='scatter3d',
                    x = df.iloc[:k]['LON','2 < M < 3'],
                    y = df.iloc[:k]['LAT','2 < M < 3'],
                    z = df.iloc[:k]['DEPTH', '2 < M < 3'],
                    mode='markers',
                    marker = dict(
                        color='green',
                        size=8
                    ),
                    hoverinfo='text',
                    text=['Date: %s<br>M: %s<br>' %(d,m) for d,m in (zip(df['MAG','2 < M < 3'][:k].index,df['MAG','2 < M < 3'][:k]))]
                ),
                dict(
                    type='scatter3d',
                    x = df.iloc[:k]['LON','3 < M < 4'],
                    y = df.iloc[:k]['LAT','3 < M < 4'],
                    z = df.iloc[:k]['DEPTH', '3 < M < 4'],
                    mode='markers',
                    marker = dict(
                        color='chocolate',
                        size=10
                    ),
                    hoverinfo='text',
                    text=['Date: %s<br>M: %s<br>' %(d,m) for d,m in (zip(df['MAG','3 < M < 4'][:k].index,df['MAG','3 < M < 4'][:k]))]
                ),
                dict(
                    type='scatter3d',
                    x = df.iloc[:k]['LON','4 < M'],
                    y = df.iloc[:k]['LAT','4 < M'],
                    z = df.iloc[:k]['DEPTH', '4 < M'],
                    mode='markers',
                    marker = dict(
                        color='red',
                        size=12
                    ),
                    hoverinfo='text',
                    text=['Date: %s<br>M: %s<br>' %(d,m) for d,m in (zip(df['MAG','4 < M'][:k].index,df['MAG','4 < M'][:k]))]
                )
            ],
            traces=[28,29,30,31]
        )for k in range(df.shape[0])
    ]

    return go.Figure(
        data=plotData,
        layout=Layout, 
        frames=frames
    )

