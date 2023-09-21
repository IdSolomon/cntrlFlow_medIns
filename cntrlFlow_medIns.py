# In this project, I will examine how factors such as age, sex, number of children, and 
# smoking status contribute to medical insurance costs.
# This is code that gives people advice on how to lower their medical insurance costs.

# This function analyzes an individual's smoking status.

def analyze_smoker(smoker_status):
  if smoker_status == 1:
    print("To lower your cost, you should consider quitting smoking.")
  else:
    print("Smoking is not an issue for you.")
 
# This function estimates the medical insurance cost for an individual, based on four variables --
# age
# sex: 0 for female, 1 for male
# num_of_children
# smoker: 0 for non-smoker, 1 for smoker

def estimate_insurance_cost(name, age, sex, num_of_children, smoker):
  estimated_cost = 400*age - 128*sex + 425*num_of_children + 10000*smoker - 2500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  analyze_smoker(smoker)
  return estimated_cost
 
# Estimate an individual's insurance cost

scottSummers_insurance_cost = estimate_insurance_cost(name = 'Scott Summers', age = 30, sex = 1, num_of_children = 9, smoker = 0)
reedRichards_insurance_cost = estimate_insurance_cost(name = 'Reed Richards', age = 21, sex = 1, num_of_children = 2, smoker = 1)

# OUTPUT: Scott Summers's Estimated Insurance Cost: 13197 dollars.
# OUTPUT: Smoking is not an issue for you.
# OUTPUT: Reed Richards's Estimated Insurance Cost: 16622 dollars. 
# OUTPUT: To lower your cost, you should consider quitting smoking.