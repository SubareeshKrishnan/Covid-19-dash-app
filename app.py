import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input, State
import webbrowser
import requests
import plotly.offline as pyo
import plotly.graph_objs as go

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
url = 'https://covid.ourworldindata.org/data/owid-covid-data.json'
r = requests.get(url)
data = r.json()
l = []
for i, j in data.items():
    l.append(j)
fig = {'data': [], 'layout': ''}

countries = ['Aruba',
             'Afghanistan',
             'Angola',
             'Anguilla',
             'Albania',
             'Andorra',
             'United Arab Emirates',
             'Argentina',
             'Armenia',
             'Antigua and Barbuda',
             'Australia',
             'Austria',
             'Azerbaijan',
             'Burundi',
             'Belgium',
             'Benin',
             'Bonaire Sint Eustatius and Saba',
             'Burkina Faso',
             'Bangladesh',
             'Bulgaria',
             'Bahrain',
             'Bahamas',
             'Bosnia and Herzegovina',
             'Belarus',
             'Belize',
             'Bermuda',
             'Bolivia',
             'Brazil',
             'Barbados',
             'Brunei',
             'Bhutan',
             'Botswana',
             'Central African Republic',
             'Canada',
             'Switzerland',
             'Chile',
             'China',
             "Cote d'Ivoire",
             'Cameroon',
             'Democratic Republic of Congo',
             'Congo',
             'Colombia',
             'Comoros',
             'Cape Verde',
             'Costa Rica',
             'Cuba',
             'Curacao',
             'Cayman Islands',
             'Cyprus',
             'Czech Republic',
             'Germany',
             'Djibouti',
             'Dominica',
             'Denmark',
             'Dominican Republic',
             'Algeria',
             'Ecuador',
             'Egypt',
             'Eritrea',
             'Western Sahara',
             'Spain',
             'Estonia',
             'Ethiopia',
             'Finland',
             'Fiji',
             'Falkland Islands',
             'France',
             'Faeroe Islands',
             'Gabon',
             'United Kingdom',
             'Georgia',
             'Guernsey',
             'Ghana',
             'Gibraltar',
             'Guinea',
             'Gambia',
             'Guinea-Bissau',
             'Equatorial Guinea',
             'Greece',
             'Grenada',
             'Greenland',
             'Guatemala',
             'Guam',
             'Guyana',
             'Hong Kong',
             'Honduras',
             'Croatia',
             'Haiti',
             'Hungary',
             'Indonesia',
             'Isle of Man',
             'India',
             'Ireland',
             'Iran',
             'Iraq',
             'Iceland',
             'Israel',
             'Italy',
             'Jamaica',
             'Jersey',
             'Jordan',
             'Japan',
             'Kazakhstan',
             'Kenya',
             'Kyrgyzstan',
             'Cambodia',
             'Saint Kitts and Nevis',
             'South Korea',
             'Kuwait',
             'Laos',
             'Lebanon',
             'Liberia',
             'Libya',
             'Saint Lucia',
             'Liechtenstein',
             'Sri Lanka',
             'Lesotho',
             'Lithuania',
             'Luxembourg',
             'Latvia',
             'Morocco',
             'Monaco',
             'Moldova',
             'Madagascar',
             'Maldives',
             'Mexico',
             'Marshall Islands',
             'Macedonia',
             'Mali',
             'Malta',
             'Myanmar',
             'Montenegro',
             'Mongolia',
             'Northern Mariana Islands',
             'Mozambique',
             'Mauritania',
             'Montserrat',
             'Mauritius',
             'Malawi',
             'Malaysia',
             'Namibia',
             'New Caledonia',
             'Niger',
             'Nigeria',
             'Nicaragua',
             'Netherlands',
             'Norway',
             'Nepal',
             'New Zealand',
             'Oman',
             'Pakistan',
             'Panama',
             'Peru',
             'Philippines',
             'Papua New Guinea',
             'Poland',
             'Puerto Rico',
             'Portugal',
             'Paraguay',
             'Palestine',
             'French Polynesia',
             'Qatar',
             'Romania',
             'Russia',
             'Rwanda',
             'Saudi Arabia',
             'Sudan',
             'Senegal',
             'Singapore',
             'Solomon Islands',
             'Sierra Leone',
             'El Salvador',
             'San Marino',
             'Somalia',
             'Serbia',
             'South Sudan',
             'Sao Tome and Principe',
             'Suriname',
             'Slovakia',
             'Slovenia',
             'Sweden',
             'Swaziland',
             'Sint Maarten (Dutch part)',
             'Seychelles',
             'Syria',
             'Turks and Caicos Islands',
             'Chad',
             'Togo',
             'Thailand',
             'Tajikistan',
             'Timor',
             'Trinidad and Tobago',
             'Tunisia',
             'Turkey',
             'Taiwan',
             'Tanzania',
             'Uganda',
             'Ukraine',
             'Uruguay',
             'United States',
             'Uzbekistan',
             'Vatican',
             'Saint Vincent and the Grenadines',
             'Venezuela',
             'British Virgin Islands',
             'United States Virgin Islands',
             'Vietnam',
             'Vanuatu',
             'Wallis and Futuna',
             'Kosovo',
             'Yemen',
             'South Africa',
             'Zambia',
             'Zimbabwe',
             'World',
             'International']
countries_list = [{'label': str(i), 'value': str(i)} for i in countries]
global data_list
data_list = [{'label': 'total_cases', 'value': 'total_cases'}, {
    'label': 'total_deaths', 'value': 'total_deaths'}]
app.layout = html.Div([
    dbc.Container(
        [
            dbc.Jumbotron(
                html.H1('Covid - 19 Real-time Tracker',
                        className='display-2', style={'text-align': 'center'})
            )
        ],
        className='mt-2'
    ),
    dbc.Container([
        dcc.Tabs(id='Tabs', children=[

            dcc.Tab(label="Cases & Deaths", children=[
                  dbc.Row([
                      dbc.Col([
                          dcc.Dropdown(id='dropdown-1', placeholder='Select Country',
                                       options=countries_list, clearable=False)
                      ]),
                      dbc.Col([
                          dcc.Dropdown(id='dropdown-2', placeholder='Select Category',
                                       options=data_list, value=data_list, clearable=False, multi=True)
                      ])
                  ]),
                  dcc.Loading(
                      dcc.Graph(id='graph-1')
                  )
                  ]),
            dcc.Tab(label='Country Comparison', children=[
                 dbc.Row([
                     dbc.Col([
                          dcc.Dropdown(id='dropdown-21', placeholder='Select Country',
                                       options=countries_list, clearable=True, multi=True)
                     ]),
                     dbc.Col([
                         dcc.Dropdown(
                             id='dropdown-22', options=data_list, value='total_cases', clearable=False)
                     ])
                 ]),
                 dcc.Loading(
                     dcc.Graph(id='graph-2')
                 ),
                 ])
        ]),


    ]),

])


@app.callback(Output('graph-2', 'figure'),
              [
                  Input('dropdown-21', 'value'),
                  Input('dropdown-22', 'value')
])
def update_graph_1(countries, category1):
    global l
    global fig
    if countries is not None:
        date_list = []
        cases_list = []
        if category1 == 'total_cases':
            for country in countries:
                cases = []
                date = []
                for i in range(215):
                    if l[i]['location'] == country:
                        for j in range(len(l[i]['data'])):
                            date.append(l[i]['data'][j]['date'])
                            if 'total_cases' in l[i]['data'][j]:
                                cases.append(
                                    int(l[i]['data'][j]['total_cases']))
                            else:
                                cases.append(int(0))
                cases_list.append(cases)
                date_list.append(date)

            if countries == None:
                return None
            else:
                fig = {'data': [
                    go.Scatter(x=date_list[i], y=cases_list[i], name=countries[i]) for i in range(len(cases_list))
                ],
                    'layout': go.Layout(title='Country wise', xaxis=dict(title='Date'), yaxis=dict(title='Cases'))
                }
        else:
            date_list = []
            death_list = []
            for country in countries:
                death = []
                date = []
                for i in range(215):
                    if l[i]['location'] == country:
                        for j in range(len(l[i]['data'])):
                            date.append(l[i]['data'][j]['date'])
                            if 'total_deaths' in l[i]['data'][j]:
                                death.append(
                                    int(l[i]['data'][j]['total_deaths']))
                            else:
                                death.append(int(0))
                date_list.append(date)
                death_list.append(death)

            if countries == None:
                return None
            else:
                fig = {'data': [
                    go.Scatter(x=date_list[i], y=death_list[i], name=countries[i]) for i in range(len(death_list))
                ],
                    'layout': go.Layout(title='Country wise', xaxis=dict(title='Date'), yaxis=dict(title='Deaths'))
                }
    else:
        return fig
    return fig


@app.callback(Output('graph-1', 'figure'),
              [
    Input('dropdown-1', 'value'),
    Input('dropdown-2', 'value')
]
)
def update_graph(country, category):
    global l
    global fig
    date = []
    total_cases = []
    total_deaths = []
    fig = 0
    global data_list
    for i, j in data.items():
        l.append(j)
    for i in range(215):
        if l[i]['location'] == country:
            for j in range(len(l[i]['data'])):
                date.append(l[i]['data'][j]['date'])
                if 'total_cases' in l[i]['data'][j]:
                    total_cases.append(int(l[i]['data'][j]['total_cases']))
                else:
                    total_cases.append(int(0))
            for k in range(len(l[i]['data'])):
                if 'total_deaths' in l[i]['data'][k]:
                    total_deaths.append(int(l[i]['data'][k]['total_deaths']))
                else:
                    total_deaths.append(int(0))
    if category == None:
        return None
    else:
        if 'total_deaths' in category:

            fig = {'data': [
                go.Scatter(x=date, y=total_deaths, mode='lines')
            ],
                'layout': go.Layout(title=country, xaxis=dict(title='Date'), yaxis=dict(title='Cases'))
            }
        if 'total_cases' in category:

            fig = {'data': [
                go.Scatter(x=date, y=total_cases, mode='lines')
            ],
                'layout': go.Layout(title=country, xaxis=dict(title='Date'), yaxis=dict(title='Cases'))
            }
        if len(category) == 2:

            fig = {'data': [
                go.Scatter(x=date, y=total_deaths, mode='lines',
                           name='Total Deaths', text='Total Deaths'),
                go.Scatter(x=date, y=total_cases, mode='lines',
                           name='Total Cases',  text='Total Cases')
            ],
                'layout': go.Layout(title=country, xaxis=dict(title='Date'), yaxis=dict(title='Cases & Deaths'))
            }
    return fig


if __name__ == '__main__':
    app.run_server()
