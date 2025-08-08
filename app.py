import dash
from dash import html

app = dash.Dash(__name__)
server = app.server  # For Gunicorn in production

app.layout = html.Div([
    html.H1("CI/CD Pipeline Demo App"),
    html.P("Hello from our automated pipeline!")
])

if __name__ == "__main__":
    app.run_server(host="127.0.0.1", port=8050, debug=True)
