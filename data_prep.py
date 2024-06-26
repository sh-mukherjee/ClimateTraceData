import pandas as pd
import country_converter as coco
from pathlib import Path

file_path = Path(__file__).parent / "road-transportation_country_emissions.csv"

df = pd.read_csv(file_path)

# Convert the 'end_time' column to datetime
# Extract the year and create a new column

df['year'] = pd.to_datetime(df['end_time']).dt.strftime('%Y')


# convert the ISO3 country column to a list and passing it to the convert method to add the short name of the country
df['country'] = coco.convert(names=df.iso3_country.tolist(), to='name_short', not_found=None)

countries = df.country.unique().tolist()
gases = df.gas.unique().tolist()
years = df.year.unique().tolist()
# Convert the list of characters to a list of integers
#years = [int(year) for year in years]

