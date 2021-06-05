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
    if figureCode is 'figure6':
        #layout['title'] = dict(
        #    text='Figure S6: Pre-Coulomb, cummulative stress change and rate of stress change with precise earthquake locations.',
        #    xanchor='center',
        #    x=0.5,
        #    font=dict(
        #        size=12,
        #    )
        #)
        #layout['annotations'] = [
        #    dict(
        #        x=0.5,
        #        y=-0.1,
        #        text="<b>CBEEF: </b>Central Basin Eastern Edge Fault, <b>CBIF: </b>Central Basin Inner Faults, <b>CBNBF: </b>Central Basin Northern Border Faults, <b>KBIF: </b>Kumburgaz Basin Inner Faults,<br>\
        #            <b>KBNBF: </b>Kumburgaz Basin Northern Boundary Fault, <b>NAFZ-C</b> and <b>NAFZ-D: </b>North Anatolian Fault Zone C and D segments, <br>\
        #            <b>SF: </b>Silivri Fault, <b>SRF: </b>Silivri Ridge Fault, <b>SRSBF: </b>Silivri Ridge Southern Border Fault<br>",
        #        align='center',
        #        font=dict(size=12),
        #        xref='paper',
        #        yref='paper',
        #        showarrow=False
        #    )
        #]
        return layout
    #elif figureCode is 'figure5':
    #    layout['scene'] = None
    #    layout['plot_bgcolor'] = 'black'
    #    layout['title'] = dict(
    #        text = "<b>Figure 5: </b>Pre-Coulomb stress, cummulative Coulomb stress \
    #        change and rate of Coulomb stress change on the faults. First pane indicates \
    #        the pre-Coulomb stress by slip deficit,<br>second pane represents the cummulative \
    #        Coulomb stress change and third pane indicates the rate of stress change. \
    #        Stress calculation based on the selected slip distribution geometry and friction coefficient.",
    #        font=dict(size=12),
    #        x=0.5,
    #        #y=1,
    #        xref='paper',
    #        yref='paper',
#
    #    )
    #    layout['annotations'] = [
    #        dict(
    #            x=0.5,
    #            y=-0.14,
    #            text="<b>CBEEF: </b>Central Basin Eastern Edge Fault, <b>CBIF: </b>Central Basin Inner Faults, <b>CBNBF: </b>Central Basin Northern Border Faults, <b>KBIF: </b>Kumburgaz Basin Inner Faults,<br>\
    #                <b>KBNBF: </b>Kumburgaz Basin Northern Boundary Fault, <b>NAFZ-C</b> and <b>NAFZ-D: </b>North Anatolian Fault Zone C and D segments, <br>\
    #                <b>SF: </b>Silivri Fault, <b>SRF: </b>Silivri Ridge Fault, <b>SRSBF: </b>Silivri Ridge Southern Border Fault<br>",
    #            align='center',
    #            font=dict(size=12),
    #            xref='paper',
    #            yref='paper',
    #            showarrow=False
    #        )
    #    ]
    #    layout['scene']['xaxis'] = dict(gridcolor='black')
    #    layout['scene']['yaxis'] = dict(gridcolor='black', zerolinecolor='black', showticklabels=False)
    #    return layout
    #elif figureCode is 'figure4':
    #    layout['title'] = dict(
    #        text='Figure S4: Coulomb stress change on the receiver faults and the source fault with various slip distribution.',
    #        xanchor='center',
    #        x=0.5,
    #        font=dict(
    #            size=12,
    #        )
    #    )
    #    layout['annotations'] = [
    #        dict(
    #            x=0.5,
    #            y=-0.1,
    #            text="<b>CBEEF: </b>Central Basin Eastern Edge Fault, <b>CBIF: </b>Central Basin Inner Faults, <b>CBNBF: </b>Central Basin Northern Border Faults, <b>KBIF: </b>Kumburgaz Basin Inner Faults,<br>\
    #                <b>KBNBF: </b>Kumburgaz Basin Northern Boundary Fault, <b>NAFZ-C</b> and <b>NAFZ-D: </b>North Anatolian Fault Zone C and D segments, <br>\
    #                <b>SF: </b>Silivri Fault, <b>SRF: </b>Silivri Ridge Fault, <b>SRSBF: </b>Silivri Ridge Southern Border Fault<br>",
    #            align='center',
    #            font=dict(size=12),
    #            xref='paper',
    #            yref='paper',
    #            showarrow=False
    #        )
    #    ]
    #    return layout
    else:
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
            sizex=0.25,
            sizey=0.25,
            )]
        #layout['annotations']= [
        #    dict(
        #        xanchor='right',
        #        yanchor='top',
        #        x=1.26,
        #        y=0.45,
        #        showarrow=False,
        #        align='left',
        #        font = dict(size=10),
        #        text='\
        #            <b>Instructions for Figure<br>\
        #            <br>\
        #            Play and Pause buttons for the animation of earthquakes, that<br>\
        #            is based on the occurence date of the tremor with a range slider.<br>\
        #            You can hide/show the events or fault geometries by using the<br>\
        #            legend. Click on any square or circle to hide/show the element<br>\
        #            again or double click on the element to isolate.<br>\
        #            <br>\
        #            <b>For Main Marmara Fault model show the following and hide the<br>\
        #            others. <b>CBNBF, CBIF, NAFZ-D, and CBEEF. <br>\
        #            <br>\
        #            <br>\
        #            <br>'
        #    )
        #]
        if figureCode is 'figure3':
            layout['title'] = dict(
            text="<b>Figure S3:</b> Distribution of relocated Silivri earthquakes by Bentz et al. (2020) <br>",
            xanchor='center',
            x=0.5,
            font=dict(
                size=14,
                color='white'
            )
        )
            return layout
        elif figureCode is 'figure2':
            layout['title'] = dict(
                text="<b>Figure S2:</b> Source mechanism solutions of Silivri earthquakes<br>",
                xanchor='center',
                x=0.5,
                font=dict(
                    size=14,
                    color='white'
                )
            )
            return layout
        elif figureCode is 'figure1':
            layout['title'] = dict(
                text="<b>Figure S1:</b> Spatio-temporal distribution of relocated Silivri earthquakes<br>",
                xanchor='center',
                x=0.5,
                font=dict(
                    size=14,
                    color='white'
                ),
            )
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
