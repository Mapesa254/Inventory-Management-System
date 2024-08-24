# dashboard.py
# Script to create a dashboard for visualizing inventory data.

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import sqlite3
import pandas as pd

# Initialize the Dash app
app = dash.Dash(__name__)

# Connect to the SQLite database
def fetch_data(query):
    conn = sqlite3.connect('inventory_management.db')
    df = pd.read_sql_query(query, conn)
    conn.close()
    return df

# Layout of the dashboard
app.layout = html.Div(children=[
    html.H1(children='Inventory Management Dashboard'),

    # Dropdown to select product category
    html.Label('Select Category'),
    dcc.Dropdown(id='category-dropdown',
                 options=[
                     {'label': 'Category 1', 'value': 'Category 1'},
                     {'label': 'Category 2', 'value': 'Category 2'},
                     # Add more categories as needed
                 ],
                 value='Category 1'),

    # Bar chart for stock levels
    dcc.Graph(id='stock-level-bar-chart'),

    # Pie chart for order status distribution
    dcc.Graph(id='order-status-pie-chart'),

    # Line chart for supplier performance
    dcc.Graph(id='supplier-performance-line-chart'),
])

# Callback to update stock level bar chart based on selected category
@app.callback(
    Output('stock-level-bar-chart', 'figure'),
    [Input('category-dropdown', 'value')]
)
def update_stock_bar_chart(selected_category):
    query = f"SELECT name, stock FROM products WHERE category = '{selected_category}'"
    df = fetch_data(query)
    fig = px.bar(df, x='name', y='stock', title=f'Stock Levels for {selected_category}')
    return fig

# Callback to update order status pie chart
@app.callback(
    Output('order-status-pie-chart', 'figure'),
    [Input('category-dropdown', 'value')]
)
def update_order_pie_chart(selected_category):
    query = f"""
    SELECT status, COUNT(*) as count FROM orders 
    WHERE product_name IN (SELECT name FROM products WHERE category = '{selected_category}')
    GROUP BY status
    """
    df = fetch_data(query)
    fig = px.pie(df, names='status', values='count', title=f'Order Status Distribution for {selected_category}')
    return fig

# Callback to update supplier performance line chart
@app.callback(
    Output('supplier-performance-line-chart', 'figure'),
    [Input('category-dropdown', 'value')]
)
def update_supplier_line_chart(selected_category):
    # For simplicity, assuming performance is a score over time
    query = """
    SELECT s.name, p.date, p.performance_score 
    FROM suppliers s 
    JOIN performance p ON s.supplier_id = p.supplier_id
    """
    df = fetch_data(query)
    fig = px.line(df, x='date', y='performance_score', color='name', title='Supplier Performance Over Time')
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
