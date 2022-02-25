import math

# This file contains the class for the Solow model
class Solow:
  def __init__(self, a=1/3, g=0, n=0, d=0.02, s=0.1, K_0=1, A_0=1, L_0=1, country_iso='Zombieland', starting_year=2022):
    # Parameter values
    self.a = a                                                                    # 'a' is the share of output that will be attributed to capital, '(1 - a)' will be that attributed to effective labour 
    self.g = g                                                                    # 'g' is the growth rate of tfp per time period
    self.n = n                                                                    # 'n' is the population growth rate 
    self.d = d                                                                    # 'd' is the year to year depreciation rate of capital 
    self.s = s                                                                    # 's' is the saving rate
    
    # Aggregate variables
    self.K = [K_0]                                                                # 'K' is the total capital in the economy, L_0 being the initial value
    self.A = [A_0]                                                                # 'A' is the total tfp of the economy, A_0 being the initial value   
    self.L = [L_0]                                                                # 'L' is the total level of labour in the economy, K_0 being the inital value
    self.Y = [(self.K[0] ** self.a) * ((self.A[0] * self.L[0]) ** (1 - self.a))]  # 'Y' The output level of the Solow model economy
    self.I = [self.s * self.Y[0]]                                                 # 'I' is the investment level when a rate s of total level of capital is saved
    self.C = [(1 - self.s) * self.Y[0]]                                           # 'C' is the aggregate consumption level
    self.D = [self.d * self.K[0]]                                                 # 'D' is the aggregate depreciation level

    self.country_iso = country_iso
    self.years = [starting_year]

  # A function returning the steady state level of capital per effecitve labour
  def steady_state(self):
    ke_star = 0
    # Checking if we don't divide by zero
    try: 
      ke_star = (self.s / (self.g + self.n + self.d + self.g * self.n)) ** (1 / (1 - self.a)) # 'ke_star' is the steady state level of per worker capital, where capital in the next period is equal to capital in the current period
    except:
      if self.s > 0 and self.K[-1] > 0 and self.A[-1] > 0 and self.L[-1] > 0:
        print('Congratulations, you will have sustained economic growth!')
    return ke_star

  # A function that adds the new period values to the class property arrays
  def step(self):
    # Adding the new period values for the properties that are used to calculate output
    self.K.append(self.K[-1] + self.I[-1] - self.D[-1])
    self.A.append((1 + self.g) * self.A[-1])
    self.L.append((1 + self.n) * self.L[-1])

    # Adding the new output value to the output array
    self.Y.append((self.K[-1] ** self.a) * ((self.A[-1] * self.L[-1]) ** (1 - self.a)))

    # Adding the new period values of the remaining properties
    self.I.append(self.s * self.Y[-1])
    self.C.append((1 - self.s) * self.Y[-1])
    self.D.append(self.d * self.K[-1])

    self.years.append(self.years[-1] + 1)

  def simulate(self, steps, shock_year=-1, a=None, g=None, n=None, d=None, s=None, K=None, A=None, L=None):
    title = f'Solow model simulation with the initial parameter values of a={self.a}, g={self.g}, n={self.n}, d={self.d}, s={self.s}.'
    
    # Resetting some of the property arrays if the simulation is called multiple times
    self.K = [self.K[0]]                                                                
    self.A = [self.A[0]]                                                                
    self.L = [self.L[0]]                                                                
    self.Y = [self.Y[0]]  
    self.I = [self.I[0]]                                                 
    self.C = [self.C[0]]                                          
    self.D = [self.D[0]] 

    self.years = [self.years[0]]

    # Adding the new property values for each year in the simulation
    for i in range(steps):
      # Update the parameters in the year of the shock
      if i == shock_year:
        self.update_parameters(a, g, n, d, s, K, A, L)
      self.step()
    return {'title': title, 'header': ['Country Iso', 'Year', 'Output', 'Capital', 'TFP', 'Labour', 'Investment', 'Consumption', 'Depreciation'], 'dataset': self.dataset()}
  
  # A function that permanently updates the parameter values that are put in
  def update_parameters(self, a, g, n, d, s, K, A, L):    
    # If the argument is not none, change the parameter value of the class
    if a:
      self.a = a
    if g:
      self.g = g
    if n:
      self.n = n
    if d:
      self.d = d
    if s:
      self.s = s
    if K:
      self.K = K
    if A:
      self.A = A
    if L:
      self.L = L

  # Return an array from the class that can be used to quickly create a pandas dataframe
  def dataset(self):
    dataset = []
    for i in range(len(self.Y)):
      dataset.append([self.
      country_iso, self.years[i], self.Y[i], self.K[i], self.A[i], self.L[i], self.I[i], self.C[i], self.D[i]])
    return dataset

  # Return the per capita array of that put in
  def per_capita(self, array):
    per_capita = []
    for i in range(len(array)):
      per_capita.append(array[i] / self.L[i])
    return per_capita

  # Return the log values of an array
  @staticmethod
  def log_array(array):
    log_array = []
    for i in range(len(array)):
      log_array.append(math.ln(array[i]))
    return log_array

  # Return an array of the absolute change of the values in an array
  @staticmethod
  def absolute_change(array):
    differences = [0]
    for i in range(1, len(array)):
      differences.append(array[i] - array[i - 1])
    return differences