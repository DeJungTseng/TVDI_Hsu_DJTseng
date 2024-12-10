from dash import Dash,html,dcc,callback,Input, Output,dash_table,_dash_renderer
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc

_dash_renderer._set_react_version('18.2.0')

df=pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')


# establish an instancs "app" in class Dash
app = Dash(__name__,external_stylesheets=dmc.styles.ALL)

app.layout = dmc.MantineProvider(
    [
        
    dmc.Container(
        html.H1(f"國家人口壽命、GDP", style={"textAlign": "center"}),
        fluid=True, # 100% width
        ta='center',
        my='20'
    )
    ,
        # dash_table.DataTable(data=[],page_size=10,id='datatable',columns=[])
    dmc.Flex(
        [
            dmc.Stack(
                [
                    dcc.RadioItems(['pop','lifeExp','gdpPercap'],value='pop',inline=True,id='radio_item')
                ,
                    dcc.Dropdown(df.country.unique(),value='Taiwan',id='dropdown-selection')
                ],
                w=500
            )
        ,
        dmc.Center(
                    dash_table.DataTable(data=[],page_size=10,id='datatable',columns=[]),
                    w = 500
                )
        ],
        direction={"base": "column", "sm": "row"},
        gap={"base": "sm", "sm": "lg"},
        justify={"base": "center"},
    )
    ,
        
    dmc.Container(
        dcc.Graph(id='graph-content')
    )
    ]
)

# 圖表顯示的物件
@callback(    
    Output('graph-content','figure'),
    Input('dropdown-selection','value'),
    Input('radio_item','value')
)
def update_graph(country_value,radio_value):
    dff = df[df.country == country_value]

    if radio_value =='pop':
        title=f'{country_value}人口'
    elif radio_value =='lifeExp':
        title=f'{country_value}預期壽命'
    else:
        title=f'{country_value}人均GDP'
    return px.line(dff,x='year',y=radio_value, title=title)


# present on table
@callback(    
    Output('datatable','data'),
    Output('datatable','columns'),    
    Input('dropdown-selection','value'),
    Input('radio_item','value') 
)
def update_table(country_value,radio_value):
    dff = df[df.country == country_value]
    columns = [
        {'id':'country','name':'country'},
        {'id':'year','name':'year'}        
    ]
    if radio_value == 'pop':
        columns.append({'id':'pop','name':'pop'})
    elif radio_value == 'lifeExp':
        columns.append({'id':'lifeExp','name':'lifeExp'})
    elif radio_value == 'gdpPercap':
        columns.append({'id':'gdpPercap','name':'gdpPercap'})
    return dff.to_dict('records'),columns

if __name__ == '__main__':
    app.run(debug=True)