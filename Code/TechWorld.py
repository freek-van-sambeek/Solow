# This is the class to simulate a world with international tech transfer
class TechWorld:
  def __init__(self, countries):
    self.countries = countries

  # A function that returns an array that can be used to create animated plots
  @staticmethod
  def animation_dataset(data, starting_year):
    animation_dataset = []
    starting_index = 0
    for i in range(len(data)):
      year = data[i][1]
      if year == starting_year:
        starting_index = i
      for j in range(starting_index, i + 1):
        animation_dataset.append(data[j] + [year])
    return animation_dataset

  def simulate_tech_world(self, steps, shock_year=-1, a=None, n=None, d=None, s=None, u=None, K=None, A=None, L=None, animation=True):
    dataset = []
    header = ['Country Iso', 'Year', 'Output', 'Capital', 'TFP', 'Labour', 'Investment', 'Consumption', 'Depreciation']
    max_A = 1

    # Simulating the world economy while updating the values for the innovation costs every year
    for i in range(steps):
      if i == shock_year:
        country.update_parameters(a, n, d, s, u, K, A, L)
      for country in self.countries:
        if country.A[-1] > max_A:
          max_A = country.A[-1]
      for country in self.countries:
        country.m = 50000000 * country.A[-1] / max_A
        country.step()
    
    # Generating the final dataset
    for country in self.countries:
      dataset += country.dataset()
    if animation:
      dataset = self.animation_dataset(dataset, self.countries[0].years[0])
      header.append('Up To')
    return {'title': 'Simulating the world', 'header': header, 'dataset': dataset}