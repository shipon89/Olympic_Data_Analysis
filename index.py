import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')
# remove the row which has at least one NA or Nan value in any column of that row
region_df = region_df.dropna()

# Merge
df2 = df.merge(region_df, on='NOC', how='left')
# remove the row which has at least one NA or Nan value in any column of that row
df2 = df2.dropna()
df2['Medal'].value_counts()
df2.drop_duplicates(inplace=True)
df3 = pd.concat([df2, pd.get_dummies(df2['Medal'])], axis=1)
df4 = pd.concat([df2, pd.get_dummies(df2['Season'])], axis=1)
df3.drop_duplicates(inplace=True)
df3.dropna()

df8=df['Sex'].value_counts()
df9 = pd.concat([df,pd.get_dummies(df['Sex'])],axis=1)






app = dash.Dash(__name__, meta_tags=[{"name=": "viewport", "content": "width=device-width"}])

app.layout = html.Div([
    html.Div([
        html.Div([
            html.Img(src=app.get_asset_url('Olympics-logo.jpg'),
                     id='olympic-image',
                     style={'height': '60px',
                            'width': 'auto',
                            'margin-bottom': '25px'})

        ], className='one-third column'),

        html.Div([
            html.Div([
                html.H3('Olympic Data Analysis', style={'margin-bottom': '0px', 'color': 'white'}),
                html.H5('1896-2016', style={'margin-top': '0px', 'color': 'white'})
            ])

        ], className='one-third column', id='title')


    ], id='header', className='row flex-display', style={'margin-bottom': '25px'}),




    html.Div([
        html.Div([

            html.P('Select Country', className='fix_label', style={'color': 'white'}),
            dcc.Dropdown(id='w_countries',
                         multi=False,
                         clearable=True,
                         searchable=True,
                         disabled=False,
                         style={'display': True},
                         value='United States',
                         placeholder='Select Country',
                         options=[{'label': c, 'value': c}
                                  for c in df3['Team'].unique()],
                         className='dcc_component'),






            html.P('Select Gender', className='fix_label', style={'color': 'white'}),
            dcc.RadioItems(id='w_gender',
                           labelStyle={'display': 'inline-block'},
                           value='M',
                           options=[{'label': i, 'value': i} for i in df9['Sex'].unique()],
                           style={'color': 'white'},

                           className='dcc_component'),





            html.P('Select Year', className='fix_label', style={'color': 'white'}),
            dcc.RangeSlider(id='select_year',
                            min=1896,
                            max=2016,
                            dots=False,
                            marks={
                                1896: '1896',
                                2016: '2016',
                            },
                            value=[1970, 2005],
                            tooltip={"placement": "bottom", "always_visible": True}),



        ], className='create_container three columns'),

        html.Div([
            dcc.Graph(id='bar_chart1', config={'displayModeBar': 'hover'})

        ], className='create_container six columns'),
        html.Div([
            dcc.Graph(id='pie_chart1', config={'displayModeBar': 'hover'})

        ], className='create_container three columns')

    ], className='row flex-display'),

    html.Div([
        html.Div([
            html.P('Select Year', className='fix_label', style={'color': 'white'}),
            dcc.Dropdown(id='select_year2',
                         multi=False,
                         clearable=True,
                         disabled=False,
                         style={'display': True},
                         value=2016,
                         placeholder='Select Year',
                         options=[{'label': c, 'value': c}
                                  for c in df3['Year'].unique()],
                         className='dcc_component'),




            dcc.RadioItems(id='radio_items1',
                           labelStyle={'display': 'inline-white'},

                           options=[{'label': 'Top 10 countries by medals', 'value': 'top1'},
                                    ],
                           value='top1',
                           style={'text-align': 'center', 'color': 'white'},

                           className='dcc_component'),





        ], className='create_container three columns'),
        html.Div([
            dcc.Graph(id='multi_chart1', config={'displayModeBar': 'hover'}),

        ], className='create_container nine columns'),



    ], className='row flex-display'),




html.Div([
        html.Div([

            html.P('Select Year', className='fix_label', style={'color': 'white'}),
            dcc.Dropdown(id='select_year3',
                         multi=False,
                         clearable=True,
                         disabled=False,
                         style={'display': True},
                         value=1992,
                         placeholder='Select Year',
                         options=[{'label': c, 'value': c}
                                  for c in df3['Year'].unique()],
                         className='dcc_component'),

            dcc.RadioItems(id='radio_items2',
                           labelStyle={'display': 'inline-white'},

                           options=[{'label': 'Top 10 Athletes by Gold medals', 'value': 'top1'},
                                    {'label': 'Top 10 Athletes by Silver medals', 'value': 'top2'},
                                    {'label': 'Top 10 Athletes by Bronze medals', 'value': 'top3'},
                                    ],
                           value='top1',
                           style={'text-align': 'center', 'color': 'white'},

                           className='dcc_component'),




        ], className='create_container three columns'),
    html.Div([

        dcc.Graph(id='multi_chart2', config={'displayModeBar': 'hover'}),

    ], className='create_container nine columns')



    ], className='row flex-display'),


html.Div([
        html.Div([
            html.P('Select Year', className='fix_label', style={'color': 'white'}),
            dcc.Dropdown(id='select_year4',
                         multi=False,
                         clearable=True,
                         disabled=False,
                         style={'display': True},
                         value=2016,
                         placeholder='Select Year',
                         options=[{'label': c, 'value': c}
                                  for c in df3['Year'].unique()],
                         className='dcc_component'),



            dcc.RadioItems(id='radio_items3',
                           labelStyle={'display': 'inline-white'},

                           options=[{'label': 'Top 10 Sports by  medal', 'value': 'top1'},
                                    {'label': 'Gold Medal', 'value': 'top2'},
                                    {'label': 'Silver Medal', 'value': 'top3'},
                                    {'label': 'Bronze Medal', 'value': 'top4'},
                                    ],
                           value='top1',
                           style={'text-align': 'center', 'color': 'white'},

                           className='dcc_component'),




        ], className='create_container three columns'),
        html.Div([
            dcc.Graph(id='multi_chart3', config={'displayModeBar': 'hover'}),

        ], className='create_container nine columns'),



    ], className='row flex-display'),





html.Div([
        html.Div([

            html.P('Select Year', className='fix_label', style={'color': 'white'}),
            dcc.RangeSlider(id='select_year5',
                            min=1896,
                            max=2016,
                            dots=False,
                            marks={
                                1896: '1896',
                                2016: '2016',
                            },
                            value=[1970, 2005],
                            tooltip={"placement": "bottom", "always_visible": True}),

            html.P('Select Country', className='fix_label', style={'color': 'white'}),
            dcc.Dropdown(id='w_countries2',
                         multi=False,
                         clearable=True,
                         disabled=False,
                         style={'display': True},
                         value='United States',
                         placeholder='Select Country',
                         options=[{'label': c, 'value': c}
                                  for c in df3['Team'].unique()],
                         className='dcc_component'),
            html.P('Select Season', className='fix_label', style={'color': 'white'}),
            dcc.RadioItems(id='w_season',
                           labelStyle={'display': 'inline-block'},
                           value='Summer',
                           options=[{'label': i, 'value': i} for i in df9['Season'].unique()],
                           style={'color': 'white'},

                           className='dcc_component'),






        ], className='create_container three columns'),

        html.Div([
            dcc.Graph(id='line_chart', config={'displayModeBar': 'hover'})

        ], className='create_container nine columns'),



    ], className='row flex-display'),






html.Div([
        html.Div([

            html.P('Select Year', className='fix_label', style={'color': 'white'}),
            dcc.RangeSlider(id='select_year6',
                            min=1896,
                            max=2016,
                            dots=False,
                            marks={
                                1896: '1896',
                                2016: '2016',
                            },
                            value=[1970, 2005],
                            tooltip={"placement": "bottom", "always_visible": True}),

            html.P('Select Country', className='fix_label', style={'color': 'white'}),
            dcc.Dropdown(id='w_countries3',
                         multi=False,
                         clearable=True,
                         searchable=True,
                         disabled=False,
                         style={'display': True},
                         value='United States',
                         placeholder='Select Country',
                         options=[{'label': c, 'value': c}
                                  for c in df3['Team'].unique()],
                         className='dcc_component'),

            html.P('Select Sport', className='fix_label', style={'color': 'white'}),
            dcc.Dropdown(id='w_sports',
                         multi=False,
                         clearable=True,
                         disabled=False,
                         style={'display': True},
                         value='Athletics',
                         placeholder='Select Sport',
                         options=[{'label': c, 'value': c}
                                  for c in df3['Sport'].unique()],
                         className='dcc_component'),







        ], className='create_container three columns'),

    html.Div([
        dcc.Graph(id='bar_chart2', config={'displayModeBar': 'hover'})

    ], className='create_container six columns'),
    html.Div([
        dcc.Graph(id='pie_chart2', config={'displayModeBar': 'hover'})

    ], className='create_container2 three columns')



    ], className='row flex-display'),





html.Div([
        html.Div([

            html.P('Select Year', className='fix_label', style={'color': 'white'}),
            dcc.RangeSlider(id='select_year7',
                            min=1896,
                            max=2016,
                            dots=False,
                            marks={
                                1896: '1896',
                                2016: '2016',
                            },
                            value=[1970, 2005],
                            tooltip={"placement": "bottom", "always_visible": True}),

            html.P('Select Event', className='fix_label', style={'color': 'white'}),
            dcc.Dropdown(id='w_event',
                         multi=False,
                         clearable=True,
                         disabled=False,
                         style={'display': True},
                         value="Ice Hockey Men's Ice Hockey",
                         placeholder='Select Event',
                         options=[{'label': c, 'value': c}
                                  for c in df3['Event'].unique()],
                         className='dcc_component'),







        ], className='create_container three columns'),

        html.Div([
            dcc.Graph(id='line_chart2', config={'displayModeBar': 'hover'})

        ], className='create_container nine columns'),



    ], className='row flex-display'),


html.Div([
        html.Div([

            html.P('Select Year', className='fix_label', style={'color': 'white'}),
            dcc.RangeSlider(id='select_year8',
                            min=1896,
                            max=2016,
                            dots=False,
                            marks={
                                1896: '1896',
                                2016: '2016',
                            },
                            value=[1970, 2005],
                            tooltip={"placement": "bottom", "always_visible": True}),

            html.P('Select Country', className='fix_label', style={'color': 'white'}),
            dcc.Dropdown(id='w_country',
                         multi=False,
                         clearable=True,
                         disabled=False,
                         style={'display': True},
                         value="Canada",
                         placeholder='Select Country',
                         options=[{'label': c, 'value': c}
                                  for c in df3['Team'].unique()],
                         className='dcc_component'),







        ], className='create_container three columns'),

        html.Div([
            dcc.Graph(id='bar_chart3', config={'displayModeBar': 'hover'})

        ], className='create_container nine columns'),



    ], className='row flex-display'),











], id='mainContainer', style={'display': 'flex', 'flex-direction': 'column'})







@app.callback(Output('bar_chart1', 'figure'),
              [Input('w_countries', 'value')],
              [Input('w_gender', 'value')],
              [Input('select_year', 'value')
               ])
def update_graph( w_countries,w_gender, select_year):
    df5 = df3.groupby(['Team','Sex', 'Year'])[['Gold', 'Silver', 'Bronze']].sum().reset_index()
    df6 = df5[(df5['Team'] == w_countries) &
              (df5['Sex'] == w_gender) &
              (df5['Year'] >= select_year[0]) & (df5['Year'] <= select_year[1])]

    return {
        'data': [go.Bar(
                x=df6['Year'],
                y=df6['Gold'],
                text=df6['Gold'],
                texttemplate='%{text:,0f}',
                textposition='auto',
                name='Gold',
                marker=dict(color='orange'),
                hoverinfo='text',
                hovertext=
                '<b>Team</b>:' + df6['Team'].astype(str) + '<br>' +
                '<b>Gender</b>:' + df6['Sex'].astype(str) + '<br>' +
                '<b>Year</b>:' + df6['Year'].astype(str) + '<br>' +
                '<b>Gold</b>:' + [f'{x:,.0f}' for x in df6['Gold']] + '<br>'

            ),
            go.Bar(
                x=df6['Year'],
                y=df6['Silver'],
                text=df6['Silver'],
                texttemplate='%{text:,0f}',
                textposition='auto',
                name='Silver',
                marker=dict(color='gray'),
                hoverinfo='text',
                hovertext=
                '<b>Team</b>:' + df6['Team'].astype(str) + '<br>' +
                '<b>Gender</b>:' + df6['Sex'].astype(str) + '<br>' +
                '<b>Year</b>:' + df6['Year'].astype(str) + '<br>' +
                '<b>Silver</b>:' + [f'{x:,.0f}' for x in df6['Silver']] + '<br>'

            ),
            go.Bar(
                x=df6['Year'],
                y=df6['Bronze'],
                text=df6['Bronze'],
                texttemplate='%{text:,0f}',
                textposition='auto',
                name='Bronze',
                marker=dict(color='#cd7f32'),
                hoverinfo='text',
                hovertext=
                '<b>Team</b>:' + df6['Team'].astype(str) + '<br>' +
                '<b>Gender</b>:' + df6['Sex'].astype(str) + '<br>' +
                '<b>Year</b>:' + df6['Year'].astype(str) + '<br>' +
                '<b>Bronze</b>:' + [f'{x:,.0f}' for x in df6['Bronze']] + '<br>'

            )
        ],

        'layout': go.Layout(
            barmode='stack',
            title={'text': ' Medal Count of : ' + (w_countries) + ' ' + '<br>'
                + ' - '.join([str(y) for y in select_year]) + '</br>',
                   'y': 0.93,
                   'x': 0.5,
                   'xanchor': 'center',
                   'yanchor': 'top'},
            titlefont={'color': 'white',
                       'size': 20},
            font=dict(family='sans-serif',
                      color='white',
                      size=12),
            hovermode='closest',
            paper_bgcolor='#1f2c56',
            plot_bgcolor='#1f2c56',
            legend={'orientation': 'h',
                    'bgcolor': '#1f2c56',
                    'xanchor': 'center', 'x': 0.5, 'y': -0.7},
            margin=dict(r=0),
            xaxis=dict(title='<b>Year</b>',
                       color='white',
                       showline=True,
                       showgrid=True,
                       showticklabels=True,
                       linecolor='white',
                       linewidth=2,
                       ticks='outside',
                       tickfont=dict(
                           family='Arial',
                           color='white',
                           size=12
                       )),
            yaxis=dict(title='<b>Medal</b>',
                       color='white',
                       showline=True,
                       showgrid=True,
                       showticklabels=True,
                       linecolor='white',
                       linewidth=2,
                       ticks='outside',
                       tickfont=dict(
                           family='Arial',
                           color='white',
                           size=12
                       )
                       )

        )
    }



@app.callback(Output('multi_chart1', 'figure'),
              [Input('select_year2', 'value')],
              [Input('radio_items1', 'value')])
def update_graph(select_year2, radio_items1):
    terr1 = df3.groupby(['Team', 'Year'])[['Gold', 'Silver','Bronze']].sum().reset_index()
    gold = terr1[(terr1['Year'] == select_year2)][['Year', 'Team', 'Gold']].sort_values(by=['Gold'],ascending=False).nlargest(10, columns=['Gold']).reset_index()
    silver = terr1[(terr1['Year'] == select_year2)][['Year', 'Team', 'Silver']].sort_values(by=['Silver'],ascending=False).nlargest(10,columns=['Silver']).reset_index()
    bronze = terr1[(terr1['Year'] == select_year2)][['Year', 'Team', 'Bronze']].sort_values(by=['Bronze'],ascending=False).nlargest(10,columns=['Bronze']).reset_index()

    if radio_items1 == 'top1':
        return {
        'data': [go.Bar(
            x=gold['Gold'],
            y=gold['Team'],
            text=gold['Gold'],
            texttemplate=gold['Team'].astype(str) + ' ' + ':' + ' ' + '%{text:s}' + ' ' + 'Medals',
            textposition='auto',
            marker=dict(color='orange'),
            name='Gold',
            orientation='h',
            hoverinfo='text',
            hovertext=
            '<b>Country</b>: ' + gold['Team'].astype(str) + '<br>' +
            '<b>Year</b>: ' + gold['Year'].astype(str) + '<br>' +
            '<b>Gold</b>: ' + [f'{x:,.0f}' for x in gold['Gold']] + '<br>'

        ),
            go.Bar(
                x=silver['Silver'],
                y=silver['Team'],
                text=silver['Silver'],
                texttemplate=silver['Team'].astype(str) + ' ' + ':' + ' ' + '%{text:s}' + ' ' + 'Silver',
                textposition='auto',
                marker=dict(color='#cd7f32'),
                name='Silver',
                orientation='h',
                hoverinfo='text',
                hovertext=
                '<b>Country</b>: ' + silver['Team'].astype(str) + '<br>' +
                '<b>Year</b>: ' + silver['Year'].astype(str) + '<br>' +
                '<b>Silver</b>: ' + [f'{x:,.0f}' for x in silver['Silver']] + '<br>'

            ),
            go.Bar(
                x=bronze['Bronze'],
                y=bronze['Team'],
                text=bronze['Bronze'],
                texttemplate=bronze['Team'].astype(str) + ' ' + ':' + ' ' + '%{text:s}' + ' ' + 'Bronze',
                textposition='auto',
                marker=dict(color='gray'),
                name='Bronze',
                orientation='h',
                hoverinfo='text',
                hovertext=
                '<b>Country</b>: ' + bronze['Team'].astype(str) + '<br>' +
                '<b>Year</b>: ' + bronze['Year'].astype(str) + '<br>' +
                '<b>Bronze</b>: ' + [f'{x:,.0f}' for x in bronze['Bronze']] + '<br>'

            )

        ],

        'layout': go.Layout(
            barmode='stack',
            paper_bgcolor='#1f2c56',
            plot_bgcolor='#1f2c56',
            title={
                'text': 'Top 10 Countries by medals count: '+'<br>'+'Year: ' + ' ' + str(select_year2),

                'y': 0.9,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
            titlefont={
                'color': 'white',
                'size': 15},

            hovermode='closest',

            margin=dict(l=100),
            xaxis=dict(title='<b>Medals</b>',
                       color='white',
                       showline=True,
                       showgrid=True,
                       showticklabels=True,
                       linecolor='black',
                       linewidth=1,
                       ticks='outside',
                       tickfont=dict(
                           family='Arial',
                           size=12,
                           color='white'

                       )),
            yaxis=dict(title='<b>Country</b>',
                       autorange='reversed',
                       color='white',
                       showline=False,
                       showgrid=False,
                       showticklabels=True,
                       linecolor='black',
                       linewidth=1,
                       ticks='outside',
                       tickfont=dict(
                           family='Arial',
                           size=12,
                           color='white'
                       )

                       ),
            legend={
                'orientation': 'h',

                'x': 0.5,
                'y': -0.7,
                'xanchor': 'center',
                'yanchor': 'bottom'},
            font=dict(
                family="sans-serif",
                size=12,
                color='white',
            )
        )

    }


@app.callback(Output('multi_chart2', 'figure'),
              [Input('select_year3', 'value')],
              [Input('radio_items2', 'value')])
def update_graph(select_year3, radio_items2):
    terr1 = df3.groupby(['Name', 'Year'])[['Gold', 'Silver', 'Bronze']].sum().reset_index()
    terr2 = terr1[(terr1['Year'] == select_year3)][['Year', 'Name', 'Gold']].sort_values(by=['Gold'],ascending=False).nlargest(10,columns=['Gold']).reset_index()
    terr3 = terr1[(terr1['Year'] == select_year3)][['Year', 'Name', 'Silver']].sort_values(by=['Silver'],ascending=False).nlargest(10,columns=['Silver']).reset_index()
    terr4 = terr1[(terr1['Year'] == select_year3)][['Year', 'Name', 'Bronze']].sort_values(by=['Bronze'],ascending=False).nlargest(10,columns=['Bronze']).reset_index()

    if radio_items2 == 'top1':
        return {
            'data': [go.Bar(
                x=terr2['Gold'],
                y=terr2['Name'],
                text=terr2['Gold'],
                texttemplate=terr2['Name'].astype(str) + ' ' + ':' + ' ' + '%{text:s}' + ' ' + 'Gold',
                textposition='auto',
                marker=dict(color='orange'),
                orientation='h',
                hoverinfo='text',
                hovertext=
                '<b>Atheletes</b>: ' + terr2['Name'].astype(str) + '<br>' +
                '<b>Year</b>: ' + terr2['Year'].astype(str) + '<br>' +
                '<b>Gold</b>: ' + [f'{x:,.0f}' for x in terr2['Gold']] + '<br>'

            )],

            'layout': go.Layout(
                paper_bgcolor='#1f2c56',
                plot_bgcolor='#1f2c56',
                title={
                    'text': 'Top 10 Athletes by Gold medals count :'+'<br>'+'Year: ' + ' ' + str(select_year3),

                    'y': 0.9,
                    'x': 0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'},
                titlefont={
                    'color': 'white',
                    'size': 15},

                hovermode='closest',

                margin=dict(l=150),
                xaxis=dict(title='<b>Gold</b>',
                           color='white',
                           showline=True,
                           showgrid=True,
                           showticklabels=True,
                           linecolor='black',
                           linewidth=1,
                           ticks='outside',
                           tickfont=dict(
                               family='Arial',
                               size=12,
                               color='white'

                           )),
                yaxis=dict(title='<b>Athletes</b>',
                           autorange='reversed',
                           color='white',
                           showline=False,
                           showgrid=False,
                           showticklabels=True,
                           linecolor='black',
                           linewidth=1,
                           ticks='outside',
                           tickfont=dict(
                               family='Arial',
                               size=12,
                               color='white'
                           )

                           ),
                legend={
                    'orientation': 'h',
                    'bgcolor': '#F2F2F2',
                    'x': 0.5,
                    'y': 1.25,
                    'xanchor': 'center',
                    'yanchor': 'top'},
                font=dict(
                    family="sans-serif",
                    size=12,
                    color='white',
                )
            )

        }
    if radio_items2 == 'top2':
        return {
            'data': [go.Bar(
                x=terr3['Silver'],
                y=terr3['Name'],
                text=terr3['Silver'],
                texttemplate=terr3['Name'].astype(str) + ' ' + ':' + ' ' + '%{text:s}' + ' ' + 'Silver',
                textposition='auto',
                marker=dict(color='gray'),
                orientation='h',
                hoverinfo='text',
                hovertext=
                '<b>Atheletes</b>: ' + terr3['Name'].astype(str) + '<br>' +
                '<b>Year</b>: ' + terr3['Year'].astype(str) + '<br>' +
                '<b>Silver</b>: ' + [f'{x:,.0f}' for x in terr3['Silver']] + '<br>'

            )],

            'layout': go.Layout(
                paper_bgcolor='#1f2c56',
                plot_bgcolor='#1f2c56',
                title={
                    'text': 'Top 10 Athletes by Silver medals count :'+'<br>'+'Year: ' + ' ' + str(select_year3),

                    'y': 0.9,
                    'x': 0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'},
                titlefont={
                    'color': 'white',
                    'size': 15},

                hovermode='closest',

                margin=dict(l=150),
                xaxis=dict(title='<b>Silver</b>',
                           color='white',
                           showline=True,
                           showgrid=True,
                           showticklabels=True,
                           linecolor='black',
                           linewidth=1,
                           ticks='outside',
                           tickfont=dict(
                               family='Arial',
                               size=12,
                               color='white'

                           )),
                yaxis=dict(title='<b>Athletes</b>',
                           autorange='reversed',
                           color='white',
                           showline=False,
                           showgrid=False,
                           showticklabels=True,
                           linecolor='black',
                           linewidth=1,
                           ticks='outside',
                           tickfont=dict(
                               family='Arial',
                               size=12,
                               color='white'
                           )

                           ),
                legend={
                    'orientation': 'h',
                    'bgcolor': '#F2F2F2',
                    'x': 0.5,
                    'y': 1.25,
                    'xanchor': 'center',
                    'yanchor': 'top'},
                font=dict(
                    family="sans-serif",
                    size=12,
                    color='white',
                )
            )

        }
    if radio_items2 == 'top3':
        return {
            'data': [go.Bar(
                x=terr4['Bronze'],
                y=terr4['Name'],
                text=terr4['Bronze'],
                texttemplate=terr4['Name'].astype(str) + ' ' + ':' + ' ' + '%{text:s}' + ' ' + 'Bronze',
                textposition='auto',
                marker=dict(color='#00FFFF'),
                orientation='h',
                hoverinfo='text',
                hovertext=
                '<b>Atheletes</b>: ' + terr4['Name'].astype(str) + '<br>' +
                '<b>Year</b>: ' + terr4['Year'].astype(str) + '<br>' +
                '<b>Bronze</b>: ' + [f'{x:,.0f}' for x in terr4['Bronze']] + '<br>'

            )],

            'layout': go.Layout(
                paper_bgcolor='#1f2c56',
                plot_bgcolor='#1f2c56',
                title={
                    'text': 'Top 10 Athletes by Bronze medals count :'+'<br>'+'Year: ' + ' ' + str(select_year3),

                    'y': 0.9,
                    'x': 0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'},
                titlefont={
                    'color': 'white',
                    'size': 15},

                hovermode='closest',

                margin=dict(l=150),
                xaxis=dict(title='<b>Silver</b>',
                           color='white',
                           showline=True,
                           showgrid=True,
                           showticklabels=True,
                           linecolor='black',
                           linewidth=1,
                           ticks='outside',
                           tickfont=dict(
                               family='Arial',
                               size=12,
                               color='white'

                           )),
                yaxis=dict(title='<b>Athletes</b>',
                           autorange='reversed',
                           color='white',
                           showline=False,
                           showgrid=False,
                           showticklabels=True,
                           linecolor='black',
                           linewidth=1,
                           ticks='outside',
                           tickfont=dict(
                               family='Arial',
                               size=12,
                               color='white'
                           )

                           ),
                legend={
                    'orientation': 'h',
                    'bgcolor': '#F2F2F2',
                    'x': 0.5,
                    'y': 1.25,
                    'xanchor': 'center',
                    'yanchor': 'top'},
                font=dict(
                    family="sans-serif",
                    size=12,
                    color='white',
                )
            )

        }

@app.callback(Output('multi_chart3', 'figure'),
                  [Input('select_year4', 'value')],
                  [Input('radio_items3', 'value')])
def update_graph(select_year4, radio_items3):
        terr1 = df3.groupby(['Sport', 'Year'])[['Gold', 'Silver', 'Bronze']].sum().reset_index()
        gold = terr1[(terr1['Year'] == select_year4)][['Year', 'Sport', 'Gold']].sort_values(by=['Gold'],ascending=False).nlargest(10, columns=['Gold']).reset_index()
        silver = terr1[(terr1['Year'] == select_year4)][['Year', 'Sport', 'Silver']].sort_values(by=['Silver'],ascending=False).nlargest(10, columns=['Silver']).reset_index()
        bronze = terr1[(terr1['Year'] == select_year4)][['Year', 'Sport', 'Bronze']].sort_values(by=['Bronze'],ascending=False).nlargest(10, columns=['Bronze']).reset_index()

        if radio_items3 == 'top1':
            return {
                'data': [go.Bar(
                    x=gold['Gold'],
                    y=gold['Sport'],
                    text=gold['Gold'],
                    texttemplate=gold['Sport'].astype(str) + ' ' + ':' + ' ' + '%{text:s}' + ' ' + 'Medals',
                    textposition='auto',
                    marker=dict(color='orange'),
                    name='Gold',
                    orientation='h',
                    hoverinfo='text',
                    hovertext=
                    '<b>Sport</b>: ' + gold['Sport'].astype(str) + '<br>' +
                    '<b>Year</b>: ' + gold['Year'].astype(str) + '<br>' +
                    '<b>Gold</b>: ' + [f'{x:,.0f}' for x in gold['Gold']] + '<br>'

                ),

                    go.Bar(
                        x=silver['Silver'],
                        y=silver['Sport'],
                        text=silver['Silver'],
                        texttemplate=silver['Sport'].astype(str) + ' ' + ':' + ' ' + '%{text:s}' + ' ' + 'Medals',
                        textposition='auto',
                        marker=dict(color='gray'),
                        name='Silver',
                        orientation='h',
                        hoverinfo='text',
                        hovertext=
                        '<b>Sport</b>: ' + silver['Sport'].astype(str) + '<br>' +
                        '<b>Year</b>: ' + silver['Year'].astype(str) + '<br>' +
                        '<b>Silver</b>: ' + [f'{x:,.0f}' for x in silver['Silver']] + '<br>'

                    ),
                    go.Bar(
                        x=bronze['Bronze'],
                        y=bronze['Sport'],
                        text=bronze['Bronze'],
                        texttemplate=bronze['Sport'].astype(str) + ' ' + ':' + ' ' + '%{text:s}' + ' ' + 'Medals',
                        textposition='auto',
                        marker=dict(color='#cd7f32'),
                        name='Bronze',
                        orientation='h',
                        hoverinfo='text',
                        hovertext=
                        '<b>Sport</b>: ' + bronze['Sport'].astype(str) + '<br>' +
                        '<b>Year</b>: ' + bronze['Year'].astype(str) + '<br>' +
                        '<b>Bronze</b>: ' + [f'{x:,.0f}' for x in bronze['Bronze']] + '<br>'

                    )
                ],

                'layout': go.Layout(
                    barmode='stack',
                    paper_bgcolor='#1f2c56',
                    plot_bgcolor='#1f2c56',

                    title={
                        'text': 'Top 10 Sports by medals count'+'<br>'+'Year: ' + ' ' + str(select_year4),

                        'y': 0.9,
                        'x': 0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                    titlefont={
                        'color': 'white',
                        'size': 15},

                    hovermode='closest',

                    margin=dict(l=150),
                    xaxis=dict(title='<b>Medals</b>',
                               color='white',
                               showline=True,
                               showgrid=True,
                               showticklabels=True,
                               linecolor='black',
                               linewidth=1,
                               ticks='outside',
                               tickfont=dict(
                                   family='Arial',
                                   size=12,
                                   color='white'

                               )),
                    yaxis=dict(title='<b>Sports</b>',
                               autorange='reversed',
                               color='white',
                               showline=False,
                               showgrid=False,
                               showticklabels=True,
                               linecolor='black',
                               linewidth=1,
                               ticks='outside',
                               tickfont=dict(
                                   family='Arial',
                                   size=12,
                                   color='white'
                               )

                               ),
                    legend={
                        'orientation': 'h',

                        'x': 0.5,
                        'y': -0.7,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                    font=dict(
                        family="sans-serif",
                        size=12,
                        color='white',
                    )
                )

            }

        if radio_items3 == 'top2':
            return {
                'data': [go.Bar(
                    x=gold['Gold'],
                    y=gold['Sport'],
                    text=gold['Gold'],
                    texttemplate=gold['Sport'].astype(str) + ' ' + ':' + ' ' + '%{text:s}' + ' ' + 'Gold',
                    textposition='auto',
                    marker=dict(color='orange'),
                    name='Gold',
                    orientation='h',
                    hoverinfo='text',
                    hovertext=
                    '<b>Sport</b>: ' + gold['Sport'].astype(str) + '<br>' +
                    '<b>Year</b>: ' + gold['Year'].astype(str) + '<br>' +
                    '<b>Gold</b>: ' + [f'{x:,.0f}' for x in gold['Gold']] + '<br>'

                )


                ],

                'layout': go.Layout(
                    barmode='stack',
                    paper_bgcolor='#1f2c56',
                    plot_bgcolor='#1f2c56',

                    title={
                        'text': 'Top 10 Sports by Gold medal'+'<br>'+'Year: ' + ' ' + str(select_year4),

                        'y': 0.9,
                        'x': 0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                    titlefont={
                        'color': 'white',
                        'size': 15},

                    hovermode='closest',

                    margin=dict(l=150),
                    xaxis=dict(title='<b>Medals</b>',
                               color='white',
                               showline=True,
                               showgrid=True,
                               showticklabels=True,
                               linecolor='black',
                               linewidth=1,
                               ticks='outside',
                               tickfont=dict(
                                   family='Arial',
                                   size=12,
                                   color='white'

                               )),
                    yaxis=dict(title='<b>Sports</b>',
                               autorange='reversed',
                               color='white',
                               showline=False,
                               showgrid=False,
                               showticklabels=True,
                               linecolor='black',
                               linewidth=1,
                               ticks='outside',
                               tickfont=dict(
                                   family='Arial',
                                   size=12,
                                   color='white'
                               )

                               ),
                    legend={
                        'orientation': 'h',

                        'x': 0.5,
                        'y': -0.7,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                    font=dict(
                        family="sans-serif",
                        size=12,
                        color='white',
                    )
                )

            }

        if radio_items3 == 'top3':

            return {
                'data': [go.Bar(
                    x=silver['Silver'],
                    y=silver['Sport'],
                    text=silver['Silver'],
                    texttemplate=silver['Sport'].astype(str) + ' ' + ':' + ' ' + '%{text:s}' + ' ' + 'Silver',
                    textposition='auto',
                    marker=dict(color='gray'),
                    name='Silver',
                    orientation='h',
                    hoverinfo='text',
                    hovertext=
                    '<b>Sport</b>: ' + silver['Sport'].astype(str) + '<br>' +
                    '<b>Year</b>: ' + silver['Year'].astype(str) + '<br>' +
                    '<b>Silver</b>: ' + [f'{x:,.0f}' for x in silver['Silver']] + '<br>'

                )


                ],

                'layout': go.Layout(
                    barmode='stack',
                    paper_bgcolor='#1f2c56',
                    plot_bgcolor='#1f2c56',

                    title={
                        'text': 'Top 10 Sports by Silver Medal '+'<br>'+'Year: ' + ' ' + str(select_year4),

                        'y': 0.9,
                        'x': 0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                    titlefont={
                        'color': 'white',
                        'size': 15},

                    hovermode='closest',

                    margin=dict(l=150),
                    xaxis=dict(title='<b>Medals</b>',
                               color='white',
                               showline=True,
                               showgrid=True,
                               showticklabels=True,
                               linecolor='black',
                               linewidth=1,
                               ticks='outside',
                               tickfont=dict(
                                   family='Arial',
                                   size=12,
                                   color='white'

                               )),
                    yaxis=dict(title='<b>Sports</b>',
                               autorange='reversed',
                               color='white',
                               showline=False,
                               showgrid=False,
                               showticklabels=True,
                               linecolor='black',
                               linewidth=1,
                               ticks='outside',
                               tickfont=dict(
                                   family='Arial',
                                   size=12,
                                   color='white'
                               )

                               ),
                    legend={
                        'orientation': 'h',

                        'x': 0.5,
                        'y': -0.7,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                    font=dict(
                        family="sans-serif",
                        size=12,
                        color='white',
                    )
                )

            }

        if radio_items3 == 'top4':
            return {
                'data': [go.Bar(
                    x=bronze['Bronze'],
                    y=bronze['Sport'],
                    text=bronze['Bronze'],
                    texttemplate=bronze['Sport'].astype(str) + ' ' + ':' + ' ' + '%{text:s}' + ' ' + 'Bronze',
                    textposition='auto',
                    marker=dict(color='#00FFFF'),
                    name='Bronze',
                    orientation='h',
                    hoverinfo='text',
                    hovertext=
                    '<b>Sport</b>: ' + gold['Sport'].astype(str) + '<br>' +
                    '<b>Year</b>: ' + gold['Year'].astype(str) + '<br>' +
                    '<b>Bronze</b>: ' + [f'{x:,.0f}' for x in bronze['Bronze']] + '<br>'

                )


                ],

                'layout': go.Layout(
                    barmode='stack',
                    paper_bgcolor='#1f2c56',
                    plot_bgcolor='#1f2c56',

                    title={
                        'text': 'Top 10 Sports by Bronze Medal'+'<br>'+'Year: ' + ' ' + str(select_year4),

                        'y': 0.9,
                        'x': 0.5,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                    titlefont={
                        'color': 'white',
                        'size': 15},

                    hovermode='closest',

                    margin=dict(l=150),
                    xaxis=dict(title='<b>Medals</b>',
                               color='white',
                               showline=True,
                               showgrid=True,
                               showticklabels=True,
                               linecolor='black',
                               linewidth=1,
                               ticks='outside',
                               tickfont=dict(
                                   family='Arial',
                                   size=12,
                                   color='white'

                               )),
                    yaxis=dict(title='<b>Sports</b>',
                               autorange='reversed',
                               color='white',
                               showline=False,
                               showgrid=False,
                               showticklabels=True,
                               linecolor='black',
                               linewidth=1,
                               ticks='outside',
                               tickfont=dict(
                                   family='Arial',
                                   size=12,
                                   color='white'
                               )

                               ),
                    legend={
                        'orientation': 'h',

                        'x': 0.5,
                        'y': -0.7,
                        'xanchor': 'center',
                        'yanchor': 'top'},
                    font=dict(
                        family="sans-serif",
                        size=12,
                        color='white',
                    )
                )

            }


@app.callback(Output('pie_chart1', 'figure'),
              [Input('w_countries', 'value')],
              [Input('select_year', 'value')])
def update_graph(w_countries,select_year):
    df7 = df3.groupby([ 'Team', 'Year'])[['Gold', 'Silver', 'Bronze']].sum().reset_index()
    gold = df7[(df7['Team'] == w_countries) &
              (df7['Year'] >= select_year[0]) & (df7['Year'] <= select_year[1])]['Gold'].sum()
    silver = df7[(df7['Team'] == w_countries) &
               (df7['Year'] >= select_year[0]) & (df7['Year'] <= select_year[1])]['Silver'].sum()
    bronze = df7[(df7['Team'] == w_countries) &
               (df7['Year'] >= select_year[0]) & (df7['Year'] <= select_year[1])]['Bronze'].sum()
    colors=['orange','gray','#cd7f32']

    return{
        'data':[go.Pie(
            labels=['Total Gold','Total Silver','Total Bronze'],
            values=[gold, silver, bronze],
            marker=dict(colors=colors),
            hoverinfo='label+value+percent',
            textinfo='label+percent',
            hole=.6,
            rotation=45,
            insidetextorientation='radial'
        )],

        'layout':go.Layout(
            title={'text': ' Total Medal Count of:' +'<br>'+ (w_countries) + '</br>'+' ' + '<br>'
                           + ' - '.join([str(y) for y in select_year]) + '</br>',
                   'y': 0.95,
                   'x': 0.5,
                      'xanchor':'center',
                      'yanchor':'top'},
                titlefont={'color':'white',
                           'size':20},
                font=dict(family='sans-serif',
                          color='white',
                          size=12),
                hovermode='closest',
                paper_bgcolor='#1f2c56',
                plot_bgcolor='#1f2c56',
                legend={'orientation':'h',
                        'bgcolor':'#1f2c56',
                        'xanchor':'center','x':0.5,'y':-0.7}

            )
    }




@app.callback(Output('bar_chart2', 'figure'),
              [Input('w_countries3', 'value')],
              [Input('w_sports', 'value')],
              [Input('w_gender', 'value')],
              [Input('select_year6', 'value')
               ])
def update_graph( w_countries3,w_sports,w_gender, select_year6):
    df5 = df3.groupby(['Team', 'Sport','Year','Sex'])[['Gold', 'Silver', 'Bronze']].sum().reset_index()
    df6 = df5[(df5['Team'] == w_countries3) &
              (df5['Sport'] == w_sports) &
              (df5['Sex'] == w_gender) &
              (df5['Year'] >= select_year6[0]) & (df5['Year'] <= select_year6[1])]

    return {
        'data': [go.Bar(
                x=df6['Year'],
                y=df6['Gold'],
                text=df6['Gold'],
                texttemplate='%{text:,0f}',
                textposition='auto',
                name='Gold',
                marker=dict(color='orange'),
                hoverinfo='text',
                hovertext=
                '<b>Sport</b>:' + df6['Sport'].astype(str) + '<br>' +
                '<b>Gender</b>:' + df6['Sex'].astype(str) + '<br>' +
                '<b>Team</b>:' + df6['Team'].astype(str) + '<br>' +
                '<b>Year</b>:' + df6['Year'].astype(str) + '<br>' +
                '<b>Gold</b>:' + [f'{x:,.0f}' for x in df6['Gold']] + '<br>'

            ),
            go.Bar(
                x=df6['Year'],
                y=df6['Silver'],
                text=df6['Silver'],
                texttemplate='%{text:,0f}',
                textposition='auto',
                name='Silver',
                marker=dict(color='gray'),
                hoverinfo='text',
                hovertext=
                '<b>Sport</b>:' + df6['Sport'].astype(str) + '<br>' +
                '<b>Gender</b>:' + df6['Sex'].astype(str) + '<br>' +
                '<b>Team</b>:' + df6['Team'].astype(str) + '<br>' +
                '<b>Year</b>:' + df6['Year'].astype(str) + '<br>' +
                '<b>Silver</b>:' + [f'{x:,.0f}' for x in df6['Silver']] + '<br>'

            ),
            go.Bar(
                x=df6['Year'],
                y=df6['Bronze'],
                text=df6['Bronze'],
                texttemplate='%{text:,0f}',
                textposition='auto',
                name='Bronze',
                marker=dict(color='#cd7f32'),
                hoverinfo='text',
                hovertext=
                '<b>Sport</b>:' + df6['Sport'].astype(str) + '<br>' +
                '<b>Gender</b>:' + df6['Sex'].astype(str) + '<br>' +
                '<b>Team</b>:' + df6['Team'].astype(str) + '<br>' +
                '<b>Year</b>:' + df6['Year'].astype(str) + '<br>' +
                '<b>Bronze</b>:' + [f'{x:,.0f}' for x in df6['Bronze']] + '<br>'

            )
        ],

        'layout': go.Layout(
            barmode='stack',
            title={'text': ' Sports Wise Medal Count '+ '<br>''Sports : '+(w_sports) + ' '+'<br>'+'Country :'+ ' ' + (w_countries3) + ' ' + '<br>'
                + ' - '.join([str(y) for y in select_year6]) + '</br>',
                   'y': 0.93,
                   'x': 0.5,
                   'xanchor': 'center',
                   'yanchor': 'top'},
            titlefont={'color': 'white',
                       'size': 20},
            font=dict(family='sans-serif',
                      color='white',
                      size=12),
            hovermode='closest',
            paper_bgcolor='#1f2c56',
            plot_bgcolor='#1f2c56',
            legend={'orientation': 'h',
                    'bgcolor': '#1f2c56',
                    'xanchor': 'center', 'x': 0.5, 'y': -0.7},
            margin=dict(r=0),
            xaxis=dict(title='<b>Year</b>',
                       color='white',
                       showline=True,
                       showgrid=True,
                       showticklabels=True,
                       linecolor='white',
                       linewidth=2,
                       ticks='outside',
                       tickfont=dict(
                           family='Arial',
                           color='white',
                           size=12
                       )),
            yaxis=dict(title='<b>Medal</b>',
                       color='white',
                       showline=True,
                       showgrid=True,
                       showticklabels=True,
                       linecolor='white',
                       linewidth=2,
                       ticks='outside',
                       tickfont=dict(
                           family='Arial',
                           color='white',
                           size=12
                       )
                       )

        )
    }

@app.callback(Output('pie_chart2', 'figure'),
              [Input('w_countries3', 'value')],
              [Input('select_year6', 'value')])
def update_graph2(w_countries3,select_year6):
    df15=df9.groupby(['Team','Sex','Year'])[['M','F']].sum().reset_index()
    male = df15[(df15['Team'] == w_countries3) &
              (df15['Year'] >= select_year6[0]) & (df15['Year'] <= select_year6[1])]['M'].sum()
    female = df15[(df15['Team'] == w_countries3) &
               (df15['Year'] >= select_year6[0]) & (df15['Year'] <= select_year6[1])]['F'].sum()

    colors=['orange','#gray']

    return{
        'data':[go.Pie(
            labels=['Total Male','Total Female'],
            values=[male, female],
            marker=dict(colors=colors),
            hoverinfo='label+value+percent',
            textinfo='label+percent',
            hole=.6,
            rotation=45,
            insidetextorientation='radial'
        )],

        'layout':go.Layout(
            title={'text': ' Gender wise medal count: ' +'<br>'+ (w_countries3) + '</br>'
                           + ' - '.join([str(y) for y in select_year6]) + '</br>',
                      'y':0.93,
                      'x':0.5,
                      'xanchor':'center',
                      'yanchor':'top'},
                titlefont={'color':'white',
                           'size':20},
                font=dict(family='sans-serif',
                          color='white',
                          size=12),
                hovermode='closest',
                paper_bgcolor='#1f2c56',
                plot_bgcolor='#1f2c56',
                legend={'orientation':'h',
                        'bgcolor':'#1f2c56',
                        'xanchor':'center','x':0.5,'y':-0.7}

            )
    }




@app.callback(Output('line_chart', 'figure'),
              [Input('w_countries2', 'value')],
              [Input('w_season', 'value')],
              [Input('select_year5', 'value')
               ])
def update_graph(w_countries2,w_season, select_year5):
    df10 = df9.groupby(['Year','Season','Team'])[['M', 'F']].sum().reset_index()
    df11 = df10[(df10['Team'] == w_countries2) &
                (df10['Season'] == w_season) &
              (df10['Year'] >= select_year5[0]) & (df10['Year'] <= select_year5[1])]

    return {
        'data': [go.Scatter(
            x=df11['Year'],
            y=df11['M'],
            text=df11['M'],
            name='Male',
            mode='markers+lines',
            line=dict(shape='spline', smoothing=1.3, width=3, color='#800000'),
            marker=dict(color='#19AAE1', size=18,symbol='circle',
                        line=dict(color='#19AAE1', width=2)),
            hoverinfo='text',
            hovertext=
            '<b>Team</b>:' + df11['Team'].astype(str) + '<br>' +
            '<b>Year</b>:' + df11['Year'].astype(str) + '<br>' +
            '<b>Male</b>:' + [f'{x:,.0f}' for x in df11['M']] + '<br>'

        ),
            go.Scatter(
                x=df11['Year'],
                y=df11['F'],
                name='Female',
                mode='markers+lines',
                line=dict(shape='spline', smoothing=1.3, width=3, color='#008000'),
                marker=dict(color='#19AAE1', size=18, symbol='circle',
                            line=dict(color='#19AAE1', width=2)),
                hoverinfo='text',
                hovertext=
                '<b>Team</b>:' + df11['Team'].astype(str) + '<br>' +
                '<b>Year</b>:' + df11['Year'].astype(str) + '<br>' +
                '<b>Female</b>:' + [f'{x:,.0f}' for x in df11['F']] + '<br>'

            )

        ],

        'layout': go.Layout(
            barmode='stack',
            title={'text': ' Total Participation of : ' + (w_season) + ' ' + '<br>'
                           + ' - '.join([str(y) for y in select_year5]) + '</br>',
                   'y': .93,
                   'x': 0.5,
                   'xanchor': 'center',
                   'yanchor': 'top'},
            titlefont={'color': 'white',
                       'size': 20},
            font=dict(family='sans-serif',
                      color='white',
                      size=12),
            hovermode='closest',
            paper_bgcolor='#1f2c56',
            plot_bgcolor='#1f2c56',
            legend={'orientation': 'h',
                    'bgcolor': '#1f2c56',
                    'xanchor': 'center', 'x': 0.5, 'y': -0.7},
            margin=dict(r=0),
            xaxis=dict(title='<b>Year</b>',
                       color='white',
                       showline=True,
                       showgrid=True,
                       showticklabels=True,
                       linecolor='white',
                       linewidth=2,
                       ticks='outside',
                       tickfont=dict(
                           family='Arial',
                           color='white',
                           size=12
                       )),
            yaxis=dict(title='<b>Male vs Female</b>',
                       color='white',
                       linecolor='white',
                       linewidth=2,
                       ticks='outside',
                       tickfont=dict(
                           family='Arial',
                           color='white',
                           size=12
                       )
                       )

        )
    }



@app.callback(Output('line_chart2', 'figure'),
              [Input('w_event', 'value')],
              [Input('select_year7', 'value')
               ])
def update_graph( w_event, select_year7):
    df5 = df3.groupby(['Event', 'Year'])[['Gold', 'Silver','Bronze']].sum().reset_index()
    df6 = df5[(df5['Event'] == w_event) &
              (df5['Year'] >= select_year7[0]) & (df5['Year'] <= select_year7[1])]

    return {
        'data': [go.Scatter(
                x=df6['Year'],
                y=df6['Gold'],
                text=df6['Gold'],

                name='Gold',
                mode='markers+lines',
                line=dict(shape='spline', smoothing=1.3, width=3, color='orange'),
                marker=dict(color='#19AAE1', size=18, symbol='circle',
                        line=dict(color='#19AAE1', width=2)),
                hoverinfo='text',
                hovertext=

                '<b>Event</b>:' + df6['Event'].astype(str) + '<br>' +
                '<b>Year</b>:' + df6['Year'].astype(str) + '<br>' +
                '<b>Gold</b>:' + [f'{x:,.0f}' for x in df6['Gold']] + '<br>'

            ),
            go.Scatter(
                x=df6['Year'],
                y=df6['Bronze'],
                text=df6['Bronze'],

                name='Bronze',
                mode='markers+lines',
                line=dict(shape='spline', smoothing=1.3, width=3, color='#cd7f32'),
                marker=dict(color='#19AAE1', size=18, symbol='circle',
                            line=dict(color='#19AAE1', width=2)),
                hoverinfo='text',
                hovertext=

                '<b>Event</b>:' + df6['Event'].astype(str) + '<br>' +
                '<b>Year</b>:' + df6['Year'].astype(str) + '<br>' +
                '<b>Bronze</b>:' + [f'{x:,.0f}' for x in df6['Bronze']] + '<br>'

            ),
            go.Scatter(
                x=df6['Year'],
                y=df6['Silver'],
                text=df6['Silver'],

                name='Silver',
                mode='markers+lines',
                line=dict(shape='spline', smoothing=1.3, width=3, color='gray'),
                marker=dict(color='#19AAE1', size=18, symbol='circle',
                            line=dict(color='#19AAE1', width=2)),
                hoverinfo='text',
                hovertext=

                '<b>Event</b>:' + df6['Event'].astype(str) + '<br>' +
                '<b>Year</b>:' + df6['Year'].astype(str) + '<br>' +
                '<b>Silver</b>:' + [f'{x:,.0f}' for x in df6['Silver']] + '<br>'

            )

        ],

        'layout': go.Layout(
            barmode='stack',
            title={'text': ' Medal Counts of Event: ' + ' '+''+ ' ' + (w_event) + ' ' + '<br>'
                + ' - '.join([str(y) for y in select_year7]) + '</br>',
                   'y': 0.93,
                   'x': 0.5,
                   'xanchor': 'center',
                   'yanchor': 'top'},
            titlefont={'color': 'white',
                       'size': 20},
            font=dict(family='sans-serif',
                      color='white',
                      size=12),
            hovermode='closest',
            paper_bgcolor='#1f2c56',
            plot_bgcolor='#1f2c56',
            legend={'orientation': 'h',
                    'bgcolor': '#1f2c56',
                    'xanchor': 'center', 'x': 0.5, 'y': -0.7},
            margin=dict(r=0),
            xaxis=dict(title='<b>Year</b>',
                       color='white',
                       showline=True,
                       showgrid=True,
                       showticklabels=True,
                       linecolor='white',
                       linewidth=2,
                       ticks='outside',
                       tickfont=dict(
                           family='Arial',
                           color='white',
                           size=12
                       )),
            yaxis=dict(title='<b>Medal</b>',
                       color='white',
                       showline=True,
                       showgrid=True,
                       showticklabels=True,
                       linecolor='white',
                       linewidth=2,
                       ticks='outside',
                       tickfont=dict(
                           family='Arial',
                           color='white',
                           size=12
                       )
                       )

        )
    }



@app.callback(Output('bar_chart3', 'figure'),
              [Input('w_country', 'value')],
              [Input('select_year8', 'value')
               ])
def update_graph( w_country, select_year8):
    df5 = df3.groupby(['Team','Year','Age'])[['Gold']].sum().reset_index()
    df6 = df5[(df5['Team'] == w_country) &
    (df5['Year'] >= select_year8[0]) & (df5['Year'] <= select_year8[1])]

    return {
        'data': [go.Bar(
                x=df6['Age'],
                y=df6['Gold'],
                text=df6['Gold'],
                texttemplate='%{text:,0f}',
                textposition='auto',
                name='Gold',
                marker=dict(color='orange'),
                hoverinfo='text',
                hovertext=

                '<b>Team</b>:' + df6['Team'].astype(str) + '<br>' +
                '<b>Year</b>:' + df6['Year'].astype(str) + '<br>' +
                '<b>Age</b>:' + df6['Age'].astype(str) + '<br>' +
                '<b>Gold</b>:' + [f'{x:,.0f}' for x in df6['Gold']] + '<br>'


            )
        ],

        'layout': go.Layout(
            barmode='stack',
            title={'text': 'Distribution of Gold Medals by Age '+ ' ' + ' '+' ' + '<br>''Country: '+(w_country) + ' ' + '<br>'
                + ' - '.join([str(y) for y in select_year8]) + '</br>',
                   'y': 0.93,
                   'x': 0.5,
                   'xanchor': 'center',
                   'yanchor': 'top'},
            titlefont={'color': 'white',
                       'size': 20},
            font=dict(family='sans-serif',
                      color='white',
                      size=12),
            hovermode='closest',
            paper_bgcolor='#1f2c56',
            plot_bgcolor='#1f2c56',
            legend={'orientation': 'h',
                    'bgcolor': '#1f2c56',
                    'xanchor': 'center', 'x': 0.5, 'y': -0.7},
            margin=dict(r=0),
            xaxis=dict(title='<b>Age</b>',
                       color='white',
                       showline=True,
                       showgrid=True,
                       showticklabels=True,
                       linecolor='white',
                       linewidth=2,
                       ticks='outside',
                       tickfont=dict(
                           family='Arial',
                           color='white',
                           size=12
                       )),
            yaxis=dict(title='<b>Medal count</b>',
                       color='white',
                       showline=True,
                       showgrid=True,
                       showticklabels=True,
                       linecolor='white',
                       linewidth=2,
                       ticks='outside',
                       tickfont=dict(
                           family='Arial',
                           color='white',
                           size=12
                       )
                       )

        )
    }


if __name__ == '__main__':
    app.run_server(debug=True)