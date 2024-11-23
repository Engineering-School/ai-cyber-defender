import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from django_plotly_dash import DjangoDash
from dash.dependencies import Input, Output
from CyberDefender.models import UserVisit

app = DjangoDash('SimpleExample')   # replaces dash.Dash

# Отримання даних з бази даних
try:
    user_visits = UserVisit.objects.all()
    #df = read_frame(user_visits)
    df = pd.DataFrame(user_visits.values('timestamp'))

    # Конвертація типу timestamp в тип дати
    df['timestamp'] = pd.to_datetime(df['timestamp']).dt.date

    # Групування за датою та підрахунок кількості відвідувань по днях
    daily_visits = df.groupby('timestamp').size().reset_index(name='visits')
except Exception as e:
    print(f"Error retrieving data: {e}")
    daily_visits = pd.DataFrame()

# Створення Dash layout
app.layout = html.Div([
    html.H1('User Visits Dashboard'),
    dcc.Graph(id='user-visits-graph'),
])

# Callback для оновлення графіку залежно від вибору користувача
@app.callback(
    Output('user-visits-graph', 'figure'),
    Input('user-visits-graph', 'relayoutData')
)
def update_graph(relayout_data):
    # Якщо relayoutData не пустий, оновіть графік
    if relayout_data:
        # Отримання нових даних з бази даних
        user_visits = UserVisit.objects.all()
        df = pd.DataFrame(user_visits.values('timestamp'))
        df['timestamp'] = pd.to_datetime(df['timestamp']).dt.date
        daily_visits = df.groupby('timestamp').size().reset_index(name='visits')

    # Створення графіку
    fig = px.line(daily_visits, x='timestamp', y='visits', title='User Visits per Day')
    return fig

