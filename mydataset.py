import pandas as pd
import matplotlib.pyplot as plt

# Sample data for demonstration purpose
# For simplicity, I'm using sample data in the form of a dictionary.

data = {
    'date': ['2023-09-01', '2023-09-02', '2023-09-03', '2023-09-04', '2023-09-05'],
    'views': [500000, 600000, 700000, 550000, 750000],
    'likes': [25000, 28000, 30000, 22000, 32000],
    'comments': [1500, 1700, 1800, 1400, 1900],
    'shares': [500, 600, 700, 550, 800],
}

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Calculate key performance indicators
total_views = df['views'].sum()
average_likes = df['likes'].mean()
average_comments = df['comments'].mean()
average_shares = df['shares'].mean()

# Calculate engagement rate
engagement_rate = (average_likes + average_comments + average_shares) / total_views

# Visualize the data
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['views'], label='Views')
plt.plot(df['date'], df['likes'], label='Likes')
plt.plot(df['date'], df['comments'], label='Comments')
plt.plot(df['date'], df['shares'], label='Shares')
plt.xlabel('Date')
plt.ylabel('Counts')
plt.title('IGTV Metrics Over Time')
plt.legend()
plt.show()

# Print the results
print(f"Total Views: {total_views}")
print(f"Average Likes: {average_likes}")
print(f"Average Comments: {average_comments}")
print(f"Average Shares: {average_shares}")
print(f"Engagement Rate: {engagement_rate:.2%}")
