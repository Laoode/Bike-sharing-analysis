import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set the title for the dashboard
st.title("📊🚲 Bike Sharing Data Dashboard")
st.markdown("📈 This dashboard provides visualizations for the Bike Sharing Dataset.")

# Load the datasets
@st.cache_data
def load_data():
    bikes_day = pd.read_csv("app/final_bikes_day.csv")
    bikes_hour = pd.read_csv("app/final_bikes_hour.csv")
    return bikes_day, bikes_hour

bikes_day, bikes_hour = load_data()

# --- Correlation matrix and Heatmap ---
st.subheader("Correlation Heatmap")
bikes_corr = bikes_hour.corr(numeric_only=True)
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(bikes_corr, annot=True, fmt='.2f')  # Set fmt='.2f' for 2 decimal places
ax.set(title="Correlation Heatmap")
st.pyplot(fig)

# --- Count of Trips by Hour of the Day ---
st.subheader("Distribution of Bike Rentals by Hour of the Day")
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x='hour', y='count', data=bikes_hour, palette='rocket', ax=ax)
plt.title('Distribution of bike rentals per hour of the day')
st.pyplot(fig)

# --- Monthly Bike Rentals ---
st.subheader("Monthly Distribution of Bike Demand")
fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=bikes_day, x="month", y="count", linewidth=0, palette='rocket', ax=ax)
ax.set(title="Monthly distribution of bike demand")
st.pyplot(fig)

# --- Boxplot for Season and Weather ---
st.subheader("Bike Rentals by Season")
fig, ax = plt.subplots(figsize=(12, 6))
sns.boxplot(x='season', y='count', data=bikes_day, palette="husl", ax=ax)
plt.title('Relationship between season V/S bike rentals')
st.pyplot(fig)

st.subheader("Bike Rentals by Weather Conditions")
fig, ax = plt.subplots(figsize=(12, 6))
sns.boxplot(x='weather', y='count', data=bikes_day, palette="husl", ax=ax)
plt.title('Relationship between weather conditions V/S bike rentals')
st.pyplot(fig)

# --- Rider Type Distribution (Pie Chart) ---
st.subheader("Rider Type Distribution: Casual vs Registered")
total_casual = bikes_day['casual'].sum()
total_registered = bikes_day['registered'].sum()

# Data for the pie chart
totals = [total_casual, total_registered]
labels = ['Casual', 'Registered']
colors = ['#ff9999', '#66b3ff']

# Create a pie chart
fig, ax = plt.subplots(figsize=(8, 6))
ax.pie(totals, labels=labels, colors=colors, autopct='%1.0f%%', startangle=90, wedgeprops={'edgecolor': 'black'})
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig.gca().add_artist(centre_circle)

plt.axis('equal')
plt.title('Rider Type Distribution: Casual vs Registered')
st.pyplot(fig)

# --- Relationship between Temperature, Humidity, Wind Speed with Bike Rentals ---
st.subheader("Relation of Temperature with Bike Rentals")
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(data=bikes_hour, x="temperature", y="count", ax=ax)
plt.title("Relation with the Temperature and Number of Bicycle Rentals")
plt.xlabel("Temperature")
st.pyplot(fig)

st.subheader("Relation of Humidity with Bike Rentals")
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(data=bikes_hour, x="humidity", y="count", ax=ax)
plt.title("Relation with the Humidity and Number of Rides")
plt.xlabel("Humidity")
st.pyplot(fig)

st.subheader("Relation of Wind Speed with Bike Rentals")
fig, ax = plt.subplots(figsize=(12, 6))
sns.lineplot(data=bikes_hour, x="wind_speed", y="count", ax=ax)
plt.title("Relation with the Wind Speed and Number of Rides")
plt.xlabel("Wind Speed")
st.pyplot(fig)

# --- Number of Trips by Members and Casual Riders by Weekday ---
st.subheader("Number of Trips by Members and Casual Riders by Weekday")
weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
bikes_day['weekday'] = pd.Categorical(bikes_day['weekday'], categories=weekday_order, ordered=True)
grouped_data = bikes_day.groupby('weekday')[['casual', 'registered']].sum()

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
grouped_data.plot(kind='bar', stacked=False, color=['#ff9999','#66b3ff'], ax=ax, width=0.8)
plt.title('Number of Trips by Members and Casual Riders by Weekday')
plt.xlabel('Weekday')
plt.ylabel('Number of Trips')
plt.xticks(rotation=0)
st.pyplot(fig)

# --- Number of Trips on Working Days vs Holidays ---
st.subheader("Number of Trips on Working Days vs Holidays")
grouped_working_day = bikes_day.groupby('working_day')[['casual', 'registered']].sum()
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(grouped_working_day.index - 0.2, grouped_working_day['casual'], width=0.4, label='Casual', color='#ff9999')
ax.bar(grouped_working_day.index + 0.2, grouped_working_day['registered'], width=0.4, label='Registered', color='#66b3ff')
plt.title('Number of Trips on Working Days vs Holidays')
plt.xlabel('Day Type')
plt.ylabel('Number of Trips')
plt.xticks([0, 1], ['Holiday', 'Working Day'])
st.pyplot(fig)

# --- Number of Trips by Weather Condition ---
st.subheader("Number of Trips by Weather Condition")
grouped_weather = bikes_day.groupby('weather')[['casual', 'registered']].sum()
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(grouped_weather.index, grouped_weather['casual'], width=0.4, label='Casual', color='#ff9999', align='center')
ax.bar(grouped_weather.index, grouped_weather['registered'], width=0.4, label='Registered', color='#66b3ff', align='edge')
plt.title('Number of Trips by Weather Condition')
plt.xlabel('Weather Condition')
plt.ylabel('Number of Trips')
st.pyplot(fig)
