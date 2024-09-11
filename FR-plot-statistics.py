import pandas as pd
import plotly.graph_objects as go
import numpy as np
from scipy.optimize import curve_fit



df = pd.read_csv('FR-Monat.csv')

# scipy fit that was not used in the end
# slots = np.array(df['Slots'])
# xvalues = np.arange(0, len(slots))
# def lin_fit(x, a, b):
#     return a * x**2 + b * x
# popt, pcov = curve_fit(lin_fit, xvalues, slots)
# yvalues = lin_fit(xvalues, *popt)
# print(yvalues)

# Abholungen = Slots
slots = np.array(df['Slots'])
xvalues = np.arange(0, len(slots))
ps = np.polyfit(xvalues, slots, 2)
yvalues = ps[0]*xvalues**2 + ps[1]*xvalues + ps[2]

fig = go.Figure(
    go.Scatter(
        x = df['Monat'],
        y = df['Slots'],
        mode = 'lines+markers',
        name = 'Abholungen',
        line = dict(color='rgb(100,174,36)', width=3, dash='solid')
        )
    )

fig.add_trace(
        go.Scatter(
            x = df['Monat'],
            y = yvalues,
            mode = 'lines',
            name = '',
            line = dict(color='rgb(100,174,36)', width=2, dash='dot')
            )
        )

# Akkumulierte Abholungen / 100
cumslots = np.array(df['Slots'].reindex(index=df['Slots'].index[::-1]).cumsum() / 100)
xvalues = np.arange(0, len(cumslots))
ps = np.polyfit(xvalues, cumslots, 2)
yvalues = ps[0]*xvalues**2 + ps[1]*xvalues + ps[2]

print(cumslots)
print(yvalues)
fig.add_trace(
        go.Scatter(
            x = df['Monat'].reindex(index=df['Monat'].index[::-1]),
            y = df['Slots'].reindex(index=df['Slots'].index[::-1]).cumsum() / 100,
            mode = 'lines+markers',
            name = 'Akk. Abholungen / 100',
            line = dict(color='rgb(83,58,36)', width=3, dash='solid')
            )
        )

fig.add_trace(
        go.Scatter(
            x = df['Monat'].reindex(index=df['Monat'].index[::-1]),
            y = yvalues,
            mode = 'lines',
            name = '',
            line = dict(color='rgb(83,58,36)', width=2, dash='dot')
            )
        )

# Aktive Foodsaver
fs = np.array(df['FS'])
xvalues = np.arange(0, len(fs))
ps = np.polyfit(xvalues, fs, 2)
yvalues = ps[0]*xvalues**2 + ps[1]*xvalues + ps[2]
fig.add_trace(
        go.Scatter(
            x = df['Monat'],
            y = df['FS'],
            mode = 'lines+markers',
            name = 'Aktive Foodsaver:innen',
            line = dict(color='rgb(220,53,59)', width=3, dash='solid')
            )
        )

fig.add_trace(
        go.Scatter(
            x = df['Monat'],
            y = yvalues,
            mode = 'lines',
            name = '',
            line = dict(color='rgb(220,53,59)', width=2, dash='dot')
            )
        )

# Aktive Betriebe
betriebe = np.array(df['Betriebe'])
xvalues = np.arange(0, len(betriebe))
ps = np.polyfit(xvalues, betriebe, 2)
yvalues = ps[0]*xvalues**2 + ps[1]*xvalues + ps[2]

fig.add_trace(
    go.Scatter(
        x = df['Monat'],
        y = df['Betriebe'],
        mode = 'lines+markers',
        name = 'Aktive Betriebe',
        line = dict(color='rgb(255,163,57)', width=3, dash='solid')
        )
    )

fig.add_trace(
        go.Scatter(
            x = df['Monat'],
            y = yvalues,
            mode = 'lines',
            name = '',
            line = dict(color='rgb(255,163,57)', width=2, dash='dot')
            )
        )

# fig.add_trace(
#         go.Scatter(
#             x = df['Monat'],
#             y = df['Termine'],
#             mode = 'lines+markers',
#             name = 'Termine',
#             line_color='blue'
#             )
#         )

# df['FS/Betriebe'] = df['FS']/df['Betriebe']
# fig.add_trace(
#     go.Scatter(
#         x = df['Monat'],
#         y = 10*df['FS']/df['Betriebe'],
#         name = 'FS pro Betrieb * 10'
#         )
#     )

# fig.add_trace(
#     go.Scatter(
#         x = df['Monat'],
#         y = 100*df['Betriebe']/(df['FS']),
#         mode = 'lines+markers',
#         name = 'Betriebe pro 100 FS',
#         line_color = 'rgb(0, 0, 0)'
#         )
#     )

# fig.add_trace(
#     go.Scatter(
#         x = df['Monat'],
#         y = df['Slots'],
#         name = 'Slots'
#         )
#     )

fig.update_layout(
    title = 'Foodsharing Freiburg (2013-2024)',
    plot_bgcolor = 'rgba(241, 231,201, 0.5)',
    showlegend = True,
    font=dict(
        family="alfa_slab_oneregular",  # Font for the whole plot
        size=25,  # Font size
        color="#533a24"  # Font color
    ),
    
    # Position legend in the top-left corner
    legend=dict(
        x=0.02,
        y=0.98,
        xanchor='left',
        yanchor='top',
        bgcolor='rgba(241, 231, 201, 1)',  # Semi-transparent background for the legend
        bordercolor='#533a24',
        borderwidth=3
    )
)


fig.write_html("output2.html")
## ADD THIS LINE MANUALLY TO HTML BELOW BODY TAG FOR FONT TO BE WORKING (without #)
# <link rel="stylesheet" href="stylesheet.css" type="text/css" charset="utf-8">
fig.show()
