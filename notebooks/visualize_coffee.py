import pandas as pd
import json

# Load the data
df = pd.read_csv('data/raw/cavalier_coffee_sales.csv')

# Aggregate revenue by location
revenue_by_location = df.groupby('cart_location')['revenue_usd'].sum().sort_values(ascending=False)
cups_by_location = df.groupby('cart_location')['cups_sold'].sum().sort_values(ascending=False)

# Aggregate by day of week
revenue_by_day = df.groupby('day_of_week')['revenue_usd'].sum()
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
revenue_by_day = revenue_by_day.reindex(day_order)

# Print summaries
print("Revenue by Location:")
print(revenue_by_location)
print("\nCups by Location:")
print(cups_by_location)
print("\nRevenue by Day of Week:")
print(revenue_by_day)

# Export as JSON for visualization
viz_data = {
    'by_location': {
        'locations': revenue_by_location.index.tolist(),
        'revenue': revenue_by_location.values.tolist(),
        'cups': cups_by_location.reindex(revenue_by_location.index).values.tolist()
    },
    'by_day': {
        'days': day_order,
        'revenue': revenue_by_day.values.tolist()
    }
}

with open('data/processed/viz_data.json', 'w') as f:
    json.dump(viz_data, f, indent=2)

print("\nVisualization data saved to data/processed/viz_data.json")
