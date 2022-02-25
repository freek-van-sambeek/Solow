# This is the class for the R&D model
class RnD:
  def __init__(self, a=0.33, n=0, d=0.02, s=0.1, u=0.05, K_0=1, A_0=1, L_0=1, country_iso='Zombieland', starting_year=2022):
    self.K = [K_0]
    self.A = [A_0]
    self.L = [L_0]

    self.a = a
    self.n = n
    self.d = d
    self.s = s
    self.u = u
    self.m = 1

    self.Y = [(self.K[0] ** self.a) * ((self.u * self.A[0] * self.L[0]) ** (1 - self.a))]
    self.I = [self.s * self.Y[0]]
    self.C = [self.Y[0] - self.I[0]]
    self.D = [self.d * self.K[0]]

    self.country_iso = country_iso
    self.years = [starting_year]

  def step(self):
    self.K.append(self.K + self.I - self.D)
    self.A.append(self.A[-1] * (1 + ((1 - self.u) * self.N) / self.m))
    self.L.append((1 + self.n) * self.L[-1])

    self.Y.append((self.K[-1] ** self.a) * ((self.u * self.A[-1] * self.L[-1]) ** (1 - self.a)))

    self.I.append(self.s * self.Y[-1])
    self.C.append((1 - self.s) * self.Y[-1])
    self.D.append(self.d * self.K[-1])

    self.years.append(self.years[-1] + 1)

# A function that permanently updates the parameter values that are put in
def update_parameters(self, a, n, d, s, u, K, A, L):    
  # If the argument is not none, change the parameter value of the class
  if a:
    self.a = a
  if n:
    self.n = n
  if d:
    self.d = d
  if s:
    self.s = s
  if u:
    self.u = u
  if K:
    self.K[-1] = K
  if A:
    self.A[-1] = A
  if L:
    self.L[-1] = L

# Return an array from the class that can be used to quickly create a pandas dataframe
def dataset(self):
  dataset = []
  for i in range(len(self.Y)):
    dataset.append([self.
    country_iso, self.years[i], self.Y[i], self.K[i], self.A[i], self.L[i], self.I[i], self.C[i], self.D[i]])
  return dataset