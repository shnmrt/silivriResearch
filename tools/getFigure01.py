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

# loading the data files
locmap = Image.open('../thumbnail.png')

with open('../data/relocatedHypocentres.json','r') as file:
    df_EQ = pd.read_json(json.load(file), orient='split')

with open('../data/faults.json','r') as file:
    faults = json.load(file)

# pivot table and trait function for 
# animation of the earthquakes 
def pivotTable(dataFrame):
    df = dataFrame
    dates, legendG = [], []
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
        elif 2 <= df.iloc[dd]['MAG'] < 3:
            legendG.append('2 < M < 3')
        elif 3 <= df.iloc[dd]['MAG'] < 4:
            legendG.append('3 < M < 4')
        else:
            lg ='4 < M'
            legendG.append('4 < M')


    df['name'] = legendG # name and legendgroup
    df['DATE'] = dates
    df['DEPTH'] *= -1
    df['DATE'] = pd.to_datetime(df['DATE'], infer_datetime_format=True)
    df = df.sort_values(['DATE'])
    df['DATE']=df['DATE'].astype(str)

    df = pd.pivot(df, index='DATE', columns='name', values=['LAT', 'LON','DEPTH','MAG','CC'])
    return df

df = pivotTable(df_EQ)


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
