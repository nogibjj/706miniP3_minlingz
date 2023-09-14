import polars as pl
import plotly.express as px

# Read csv file "world-small.csv" using Polars
data = pl.read_csv("world-small.csv")

# Convert "gdppcap08" column to integer
data = data.with_columns(data["gdppcap08"].cast(pl.Int32))

# Print out statistics summary of "gdppcap08" & "polityIV"
summary = data.select(["gdppcap08", "polityIV"]).describe()
print(summary)

# plot "gdppcap08" & "polityIV" using plotly.express
fig = px.scatter(data, x="gdppcap08", y="polityIV")
fig.show()
fig.write_image("plot.png")
