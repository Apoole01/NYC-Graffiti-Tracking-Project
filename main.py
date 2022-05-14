import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('DSNY_Graffiti_tracking_FINAL - Sheet2.csv')

borough = data['BOROUGH_UNIQUE'].dropna()
incidents_by_borough = data['INCIDENTS_BY_BOROUGH'].dropna()
date = data['DATE_UNIQUE'].dropna()
incidents_by_date = data['INCIDENTS_BY_DATE'].dropna()
month = data['MONTH'].dropna()
incidents_by_month = data['INCIDENTS_BY_MONTH'].dropna()

plt.bar(borough, incidents_by_borough, color = 'blue')
plt.title('Graffiti Incidents by Borough', fontsize = 20)
plt.xlabel('Borough', fontsize = 15)
plt.ylabel('Number of Incidents', fontsize = 15)
plt.show()

plt.plot(month, incidents_by_month, color = 'blue')
plt.title('Graffiti Incidents by Month', fontsize = 20)
plt.xlabel('Month', fontsize = 10)
plt.ylabel('Number of Incidents', fontsize = 10)
plt.show()