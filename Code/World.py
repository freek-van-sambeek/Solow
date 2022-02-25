# This class will contain the methods needed to animate a world chart
class World:
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

  def simulate_world(self, steps, shock_year=-1, a=None, g=None, n=None, d=None, s=None, K=None, A=None, L=None, animation=True):
    dataset = []
    header = ['Country Iso', 'Year', 'Output', 'Capital', 'TFP', 'Labour', 'Investment', 'Consumption', 'Depreciation']
    for i in range(len(self.countries)):
      dataset += self.countries[i].simulate(steps, shock_year, a, g, n, d, s, K, A, L)['dataset']
    if animation:
      dataset = self.animation_dataset(dataset, self.countries[0].years[0])
      header.append('Up To')
    return {'title': 'Simulating the world', 'header': header, 'dataset': dataset}