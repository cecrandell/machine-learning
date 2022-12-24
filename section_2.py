# Section 2

# The Machine Learning Process

# Data Pre-Processing

# • Import the data
# • Clean the data
# • Split into training and test sets

# Modelling (the fun part)

# • Build the model
# • Train the model
# • Make predictions

# Evaluation

# • Calculate performance metrics
# • Make a verdict

# First we will split the dataset into a test set and a training set

# Let's pretend you are tasked to predict sales prices, and the car is your dependent variable and the mileage and age are your independent variables

# 20 cars in total in the dataset

# Before you do anything, split out 20% percent of the data. For 20 cars, that 4 cars we separate out

# The bulk of our data, 80%, will be our training set, and the separated 20% will be our test set.

# We use the training set to build the model (in this case, a linear regression), then we'll take the cars from the test set and apply our model to them (the test set has not been a part of the model creation process). The model has no information about these 4 cars. Applying the model will predict certain values and prices.

# Because we separated the test set in advance, we do know the actual values, so we can compare predicted values and actual prices.

# Then we can ask if it's doing a good job, or a not so good job.

# Feature Scaling

