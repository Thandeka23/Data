import pandas as pd
import matplotlib.pyplot as plt

# Sample data from the provided context
# This is a simplified dataset for demonstration purposes
data = {
    "Parental_Involvement": ["Low", "Low", "Medium", "Medium", "Medium", "High", "High", "Medium", "Medium", "Low", "Medium", "High"],
    "Exam_Score": [67, 61, 74, 71, 70, 76, 72, 68, 65, 64, 66, 69]
}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)

# 1. Bar Chart: Average Exam Scores by Parental Involvement
# Group the data by Parental_Involvement and calculate the mean Exam_Score for each group
avg_scores = df.groupby('Parental_Involvement')['Exam_Score'].mean()

# Create a new figure with a specific size
plt.figure(figsize=(10, 6))

# Create a bar plot using the average scores
avg_scores.plot(kind='bar', color=['red', 'blue', 'green'])

# Set the title of the plot
plt.title('Average Exam Scores by Parental Involvement', fontsize=16)

# Label the x-axis
plt.xlabel('Parental Involvement Level', fontsize=12)

# Label the y-axis
plt.ylabel('Average Exam Score', fontsize=12)

# Rotate x-axis labels for better readability
plt.xticks(rotation=0)

# Add a grid for easier score comparison
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add value labels on top of each bar
for i, v in enumerate(avg_scores):
    plt.text(i, v, f'{v:.2f}', ha='center', va='bottom')

# Adjust layout and display the plot
plt.tight_layout()
plt.show()

# 2. Histogram: Distribution of Exam Scores
# Create a new figure with a specific size
plt.figure(figsize=(10, 6))

# Create a histogram of Exam_Scores
# bins=10 divides the score range into 10 equal intervals
plt.hist(df['Exam_Score'], bins=10, color='lightblue', edgecolor='black')

# Set the title of the plot
plt.title('Distribution of Exam Scores', fontsize=16)

# Label the x-axis
plt.xlabel('Exam Score', fontsize=12)

# Label the y-axis
plt.ylabel('Frequency', fontsize=12)

# Add a grid for easier reading
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Add text to show mean and median
mean_score = df['Exam_Score'].mean()
median_score = df['Exam_Score'].median()
plt.text(0.7, 0.95, f'Mean: {mean_score:.2f}\nMedian: {median_score:.2f}', 
         transform=plt.gca().transAxes, verticalalignment='top')

# Adjust layout and display the plot
plt.tight_layout()
plt.show()

# Additional analysis: Correlation between Parental Involvement and Exam Score
# Convert Parental_Involvement to numeric values
involvement_map = {'Low': 1, 'Medium': 2, 'High': 3}
df['Involvement_Numeric'] = df['Parental_Involvement'].map(involvement_map)

# Calculate correlation
correlation = df['Involvement_Numeric'].corr(df['Exam_Score'])

print(f"Correlation between Parental Involvement and Exam Score: {correlation:.2f}")

