

def Lgenerator(figureCode):


    from PIL import Image
    import plotly.graph_objects as go

    locmap = Image.open('../tools/thumbnail.png','r')
    layout = go.Layout(
        height = 800,
        paper_bgcolor = 'black',
        font_color = 'white',
        scene = dict(
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
    )
    layout['showlegend'] = True
    layout['legend'] = dict(
        title='                        <b>Explanations</b><br>',
        xanchor='right',
        yanchor='top',
        bordercolor='white',
        borderwidth=1,
        itemsizing='trace',
        x=1.26,
        y=1.0,
        font = dict(
            size = 10,
            color = 'white',
            )
    )
    layout['images'] = [dict(
        xanchor='right',
        yanchor='top',
        layer='above',
        source=locmap,
        xref='paper',
        yref='paper',
        x=1.26,
        y=0.2,
        sizex=0.3,
        sizey=0.3,
        )]
    
    if figureCode in ['figure2', 'figure3']:
        return layout
    elif figureCode is 'figure1':
        layout['updatemenus'] = [
                dict(
                    type='buttons',
                    showactive=True,
                    font = dict(color='blue'),
                    direction='left',
                    y=0.1,
                    x=0.1,
                    xanchor='right',
                    yanchor='top',
                    pad=dict(t=40, r=8),
                    buttons=[
                        dict(
                            label='Play',
                            method='animate',
                            args=[
                                None,
                                dict(
                                    frame = dict(
                                        duration=300,
                                        redraw=True
                                    ),
                                    transition=dict(duration=300),
                                    fromcurrent=True,
                                    mode='immediate'
                                )
                            ]
                        ),
                        dict(
                            label='Pause',
                            method='animate',
                            args=[
                                [None],
                                dict(
                                    frame = dict(
                                        duration=0,
                                        redraw=True
                                    ),
                                    mode='immediate',
                                    transition=dict(duration=0)
                                )
                            ]
                        )
                    ]
                )
            ]
        return layout
    else:
        print('figure code is not available!!')
