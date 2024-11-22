import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.colors as mcolors

# Load the CSV data into a DataFrame
file_path = '/Users/shanedixon/Developer/SQL_Project_Data_Job_Analysis/csv_files/2_top_paying_job_skills.csv'
df = pd.read_csv(file_path)

# Count the frequency of each skill and select the top 10 most frequent skills
skill_frequency = df['skills'].value_counts().head(10).reset_index()
skill_frequency.columns = ['skill', 'frequency']

# Sort the data by frequency in descending order
skill_frequency_sorted = skill_frequency.sort_values(by='frequency', ascending=True)

# Set up the figure and axes with a dark background
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(12, 6))
fig.set_facecolor('#0D1117')
ax.set_facecolor('#0D1117')

# Create a color gradient for the bars (green shades)
colors = mcolors.LinearSegmentedColormap.from_list("green_gradient", ['#C9E7D1', '#1F8F45'])
norm = plt.Normalize(skill_frequency_sorted['frequency'].min(), skill_frequency_sorted['frequency'].max())
bar_colors = [colors(norm(frequency)) for frequency in skill_frequency_sorted['frequency']]

# Plot horizontal bars with the color gradient
bars = ax.barh(skill_frequency_sorted['skill'], skill_frequency_sorted['frequency'], color=bar_colors, zorder=2)

# Add a vertical dotted line (with transparency) behind the bars
ax.axvline(x=0, color='white', linestyle=':', linewidth=1, alpha=0.3, zorder=1)

# Set the title of the plot
plt.title('Top 10 Most Frequent Skills in Data Analyst Jobs', fontsize=16, fontweight='bold', pad=20, loc='center')

# Format the x-axis labels to show frequency
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x)}'))

# Add padding to the y-axis labels for better readability
ax.tick_params(axis='y', labelsize=10, pad=20)

# Add frequency values inside the bars with proper formatting
for bar, frequency in zip(bars, skill_frequency_sorted['frequency']):
    ax.text(frequency - 0.05 * frequency, bar.get_y() + bar.get_height() / 2, f'{frequency}', va='center', ha='right', fontsize=10, color='black')

# Add gridlines to the x-axis (dotted, white color)
ax.grid(True, axis='x', linestyle=':', color='white', linewidth=1, zorder=0)

# Adjust layout to fit everything properly
plt.tight_layout()

# Display the plot
plt.show()