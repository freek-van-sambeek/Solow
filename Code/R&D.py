# This will be the class for the R&D model
class RnD:
  def __init__(self, a, g, n, d, s, u, m, K_0, A_0, L_0):
    self.K = [K_0]
    self.A = [A_0]
    self.L = [L_0]

    self.a = a
    self.g = g
    self.n = n
    self.d = d
    self.s = s
    self.u = u
    self.m = m

    self.Y = [(self.K[0] ** self.a) * ((self.u * self.A[0] * self.L[0]) ** (1 - self.a))]
    self.I = [self.s * self.Y[0]]
    self.C = [self.Y[0] - self.I[0]]
    self.D = [self.d * self.K[0]]

  def step(self):
    self.K.append(self.K + self.I - self.D)
    self.A.append(self.A[-1] * (1 + ((1 - self.u) * self.N) / self.m))
    self.L.append((1 + self.n) * self.L[-1])

    self.Y.append((self.K[-1] ** self.a) * ((self.u * self.A[-1] * self.L[-1]) ** (1 - self.a)))

    self.I.append(self.s * self.Y[-1])
    self.C.append((1 - self.s) * self.Y[-1])
    self.D.append(self.d * self.K[-1])