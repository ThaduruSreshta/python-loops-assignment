import numpy as np

# ---------------- TASK 1 ----------------
np.random.seed(42)

# Generate scores (5 students × 4 subjects)
scores = np.random.randint(50, 101, size=(5, 4))

print("Scores:\n", scores)

# 1. Score of 3rd student in 2nd subject
print("\n3rd student, 2nd subject:", scores[2, 1])

# 2. Last 2 students (all subjects)
print("\nLast 2 students:\n", scores[-2:, :])

# 3. First 3 students, subjects 2 and 3
print("\nFirst 3 students, subjects 2 & 3:\n", scores[:3, 1:3])


# ---------------- TASK 2 ----------------

# Column-wise mean (rounded)
col_mean = np.round(scores.mean(axis=0), 2)
print("\nColumn-wise mean:", col_mean)

# Add curve using broadcasting
curve = np.array([5, 3, 7, 2])
curved_scores = scores + curve

# Ensure no score exceeds 100
curved_scores = np.clip(curved_scores, None, 100)

print("\nCurved scores:\n", curved_scores)

# Row-wise max (best subject per student)
row_max = curved_scores.max(axis=1)
print("\nBest score per student:", row_max)


# ---------------- TASK 3 ----------------

# Min-max normalization per row
row_min = curved_scores.min(axis=1, keepdims=True)
row_max = curved_scores.max(axis=1, keepdims=True)

normalized = (curved_scores - row_min) / (row_max - row_min)

print("\nNormalized scores:\n", normalized)

# Index of highest value in normalized array
max_index = np.unravel_index(np.argmax(normalized), normalized.shape)
print("\nHighest normalized value at (student, subject):", max_index)

# Values strictly above 90
above_90 = curved_scores[curved_scores > 90]
print("\nScores above 90:", above_90)