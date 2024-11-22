import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.colors as mcolors

# Load the CSV data into a DataFrame
file_path = '/Users/shanedixon/Developer/SQL_Project_Data_Job_Analysis/csv_files/1_top_paying_jobs.csv'
df = pd.read_csv(file_path)

# Sort the data by salary in ascending order
df_sorted = df.sort_values(by='salary_year_avg', ascending=True)

# Set up the figure and axes with a dark background
plt.style.use('dark_background')
fig, ax = plt.subplots(figsize=(12, 6))
fig.set_facecolor('#0D1117')
ax.set_facecolor('#0D1117')

# Create a color gradient for the bars (green shades)
colors = mcolors.LinearSegmentedColormap.from_list("green_gradient", ['#C9E7D1', '#1F8F45'])
norm = plt.Normalize(df_sorted['salary_year_avg'].min(), df_sorted['salary_year_avg'].max())
bar_colors = [colors(norm(salary)) for salary in df_sorted['salary_year_avg']]

# Plot horizontal bars with the color gradient
bars = ax.barh(df_sorted['job_title'], df_sorted['salary_year_avg'], color=bar_colors, zorder=2)

# Add a vertical dotted line (with transparency) behind the bars
ax.axvline(x=0, color='white', linestyle=':', linewidth=1, alpha=0.3, zorder=1)

# Set the title of the plot
plt.title('Top 10 Paying Data Analyst Jobs in 2023', fontsize=16, fontweight='bold', pad=20, loc='center')

# Format the x-axis labels to show salary in 'K' (thousands)
ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x/1000)}K'))

# Add padding to the y-axis labels for better readability
ax.tick_params(axis='y', labelsize=10, pad=20)

# Add salary values inside the bars with proper formatting
for bar, salary in zip(bars, df_sorted['salary_year_avg']):
    ax.text(salary - 0.05 * salary, bar.get_y() + bar.get_height() / 2, f'${salary:,.0f}', va='center', ha='right', fontsize=10, color='black')

# Add gridlines to the x-axis (dotted, white color)
ax.grid(True, axis='x', linestyle=':', color='white', linewidth=1, zorder=0)

# Adjust layout to fit everything properly
plt.tight_layout()

# Display the plot
plt.show()