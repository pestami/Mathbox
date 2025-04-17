import plotly.graph_objects as go

# Data for the scatter plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
labels = ['M123456 // FLM123456', 'B', 'C', 'D', 'E']

# Create the scatter plot
fig = go.Figure(data=[go.Scatter(x=x, y=y, mode='markers', text=labels,
                                 textposition='top center')])

# Customize the plot
fig.update_layout(title='Scatter Plot Example',
                  xaxis_title='X Axis',
                  yaxis_title='Y Axis')

# Save the plot as an HTML file
fig.write_html('scatter_plot_with_visible_labels.html')
