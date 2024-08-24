# 1.Outline for the Dashboard:
## Overview Dashboard:
- Display key metrics like total products, total orders, and total suppliers.
- Show visualizations such as bar charts for stock levels, pie charts for order status distribution, and line charts for supplier performance.

## Interactive Features:
- Allow users to filter data based on categories, date ranges, or supplier names.
- Provide real-time updates when data is added or modified.

# 2.Explanation of Key Components:
## Dash Layout:
- The layout includes a dropdown for selecting the product category, and placeholders for three types of charts: a bar chart for stock levels, a pie chart for order status distribution, and a line chart for supplier performance.

## Callbacks:
- Each chart is dynamically updated based on the selected category using Dash's callback functionality.
- The update_stock_bar_chart, update_order_pie_chart, and update_supplier_line_chart functions retrieve the relevant data from the SQLite database and create visualizations using Plotly Express.

## fetch_data Function:
- This function handles database queries and returns data as a Pandas DataFrame, making it easy to integrate with Plotly for visualization.

# 3.Summary
## Dashboard Overview: 
- The dashboard provides an interactive way to visualize the inventory data.  
- Users can filter the data by category, view stock levels, analyze order status distribution, and 
  track supplier performance over time.

## Real-Time Updates: 
- The dashboard will update the visualizations in real-time as new data is added or existing data is modified, giving users a current view of the inventory system.
## Potential Enhancements:
### Additional Filters: 
- Add more dropdowns or sliders to filter by date range, specific suppliers, or product price ranges.
### Interactivity: 
- Allow users to click on data points to drill down into more detailed views or to trigger specific actions (e.g., reorder a product).
- This implementation should help you score the 10 marks allocated to Dashboard Design & Visualization.