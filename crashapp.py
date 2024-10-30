import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns




def load_data():
    file = "aircrahesFullDataUpdated_2024.csv"
    df = pd.read_csv(file)

    df["Country/Region"]= df["Country/Region"].str.replace("'-","unknown").str.strip()
    df.fillna("Not Available")
    df["Country/Region"]= df["Country/Region"].replace("10"," ", regex=True)
    df['Aircraft Manufacturer'].str.strip()
    df['Country/Region'].str.strip()
    df['Aircraft'].str.strip()
    df['Location'].str.strip()
    df['Location'].str.replace("-"," ").str.strip()
    df['Operator'].str.strip()
    df[['Month','Day']].astype('category')
    return df
df =load_data()  
st.title("CRASHAPP ANALYSIS")


crash_counts = df['Year'].value_counts() # 1

sns.set(style="whitegrid")
plt.figure(figsize=(12,6))
sns.lineplot(x=crash_counts.index,y=crash_counts.values, palette='viridis')
plt.title('Number of Air crashes per year',fontsize=16)
plt.xlabel('Year',fontsize=14)
plt.ylabel('Number of crashes',fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
st.pyplot(plt)

aircraft_count = df['Aircraft'].value_counts() #2

top_aircraft = aircraft_count.head(10)

sns.set(style="whitegrid")
plt.figure(figsize=(12,6))
sns.barplot(x=top_aircraft.index,y=top_aircraft.values, palette='viridis')
plt.title('Topten distribution of aircraft types involved in crashes',fontsize=16)
plt.xlabel('Aircraft',fontsize=14)
plt.ylabel('Number of aircraft crashes',fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
st.pyplot(plt)

crashes_by_month = df['Month'].value_counts() #3

crashes_by_month.plot(kind='bar',figsize=(12,6),title='Number of crashes by Month') 
plt.xlabel('Month')
plt.ylabel('Number of crashes')
st.pyplot(plt)

crashes_by_year = df['Year'].value_counts()

sns.set(style="whitegrid")
plt.figure(figsize=(12,6))
sns.lineplot(x=crashes_by_year.index,y=crashes_by_year.values, palette='viridis')

plt.title('Number of Air crashes per year',fontsize=16)
plt.xlabel('Year',fontsize=14)
plt.ylabel('Number of crashes',fontsize=14)
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt)

air_manufacturer_count= df['Aircraft Manufacturer'].value_counts() #4
top_Aircraft_Manufacturer = air_manufacturer_count.head(10)
top_Aircraft_Manufacturer.plot(kind='bar',figsize=(12,6),title= 'top aircraft manufacturers')
plt.xlabel('aircraft_manufacturer')
plt.ylabel('production rate')
st.pyplot(plt)


country_count = df['Country/Region'].value_counts() #5
top_country_count = country_count.head(10)
top_country_count.plot(kind='bar',figsize=(12,6),title='Number of crashes that occured in countries') 
plt.xlabel('countries that has the most plane crash')
plt.ylabel('Number of crashes')
st.pyplot(plt)


plt.figure(figsize=(12, 6))   # 8
plt.bar(df['Year'], df['Aboard'])
plt.xlabel('Year', fontsize=14)
plt.ylabel('Aboard', fontsize=14)
plt.title('People Aboard per Year')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt)


plt.figure(figsize=(12, 6))
plt.bar(df['Year'],df['Fatalities (air)']) #9
plt.xlabel('year',fontsize=14)
plt.ylabel('fatalities',fontsize=14)
plt.title('Dead per year')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt)

df['survivals_(air)'] = df['Aboard'] - df['Fatalities (air)']
survivals_per_year = df.groupby('Year')['survivals_(air)'].sum()
survivals_per_year_df = survivals_per_year.reset_index().rename(columns={'survivals_(air)':'Survivials in a year'})
Negative_survivals = df[df['survivals_(air)']< 0]
cleaned_Survivals = df[df["survivals_(air)"] >=0]
cleaned_Survivals

plt.figure(figsize=(12, 6))
plt.bar(df['Year'],df['survivals_(air)']) #10
plt.xlabel('Year',fontsize=14)
plt.ylabel('No of survivals_(air) ',fontsize=14)
plt.title('survivals_(air)')
plt.xticks(rotation=45)
plt.tight_layout()
st.pyplot(plt)

fatalities_by_year = df.groupby('Year')['Fatalities (air)'].sum() #6
year_with_max_fatalities = fatalities_by_year.idxmax()
max_fatalities = fatalities_by_year.max()
st.write(f"Year with maximum fatalities: {year_with_max_fatalities}")
st.write(f"Fatalities: {max_fatalities}")
st.write(f"Year: {year_with_max_fatalities}, Fatalities: {max_fatalities}")

st.write(f"The rate of plane crashes has significantly decreased over time,largeely due to advancement in safety regualtions and technology.The aircraft rate has dropped in year 2000's reflecting improvement in aircraft design and materials"
         ) #7