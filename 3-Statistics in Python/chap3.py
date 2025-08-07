# THE NORMAL DISTRIBUTION


# Histogram of amount with 10 bins and show plo
plt.hist(amir_deals['amount'],bins=10)
plt.show()

# Probability of deal < 7500
prob_less_7500 = norm.cdf(7500,5000,2000)

print(prob_less_7500)

# Probability of deal > 1000
prob_over_1000 = 1-norm.cdf(1000,5000,2000)

print(prob_over_1000)

# Probability of deal between 3000 and 7000
prob_3000_to_7000 = norm.cdf(7000,5000,2000)-norm.cdf(3000,5000,2000)

print(prob_3000_to_7000)

# Calculate amount that 25% of deals will be less than
pct_25 = norm.ppf(0.25,5000,2000)

print(pct_25)


# Calculate new average amount
new_mean = 5000+0.2*5000

# Calculate new standard deviation
new_sd = 2000+0.3*2000

# Simulate 36 new sales
new_sales = norm.rvs(new_mean,new_sd,size=36)

print(new_sales)

# Create histogram and show
plt.hist(new_sales)
plt.show()
plt.clf()


# Create a histogram of num_users and show
amir_deals['num_users'].hist()
plt.show()

# Set seed to 104
np.random.seed(104)

# Sample 20 num_users with replacement from amir_deals
samp_20 = amir_deals['num_users'].sample(20,replace=True)

# Take mean of samp_20
print(np.mean(samp_20))

# Set seed to 104
np.random.seed(104)

# Sample 20 num_users with replacement from amir_deals and take mean
samp_20 = amir_deals['num_users'].sample(20, replace=True)
np.mean(samp_20)

sample_means = []
# Loop 100 times
for i in range(100):
  # Take sample of 20 num_users
  samp_20 = samp_20 = amir_deals['num_users'].sample(20, replace=True)
  # Calculate mean of samp_20
  samp_20_mean = np.mean(samp_20)
  # Append samp_20_mean to sample_means
  sample_means.append(samp_20_mean)
  
print(sample_means)

# Convert to Series and plot histogram
sample_means_series = pd.Series(sample_means)
sample_means_series.hist()
# Show plot
plt.show()



# Set seed to 321
np.random.seed(321)

sample_means = []
# Loop 30 times to take 30 means
for i in range(30):
  # Take sample of size 20 from num_users col of all_deals with replacement
  cur_sample = all_deals['num_users'].sample(20,replace=True)
  # Take mean of cur_sample
  cur_mean = np.mean(cur_sample)
  # Append cur_mean to sample_means
  sample_means.append(cur_mean)

# Print mean of sample_means
print(np.mean(sample_means))

# Print mean of num_users in amir_deals
print(np.mean(amir_deals['num_users']))


# Import poisson from scipy.stats
from scipy.stats import poisson
# Probability of 5 responses
prob_5 = poisson.pmf(5,4)

print(prob_5)

# Probability of 5 responses
prob_coworker = poisson.pmf(5,5.5)

print(prob_coworker)

# Probability of 2 or fewer responses
prob_2_or_less = poisson.cdf(2,4)

print(prob_2_or_less)

# Probability of > 10 responses
prob_over_10 = 1-poisson.cdf(10,4)

print(prob_over_10)


# Print probability response takes < 1 hour
print(expon.cdf(1, scale=2.5))

# Print probability response takes > 4 hours
print(1-expon.cdf(4,scale=2.5))

# Print probability response takes 3-4 hours
print(expon.cdf(4,scale=2.5) - expon.cdf(3,scale=2.5))