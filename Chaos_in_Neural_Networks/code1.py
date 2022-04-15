import numpy as np

Ni = 100
N = 1000
tau = 1
time = 1000 * tau
alpha = 2  # 1-100 range is usually used, with alpha << N
g = 0.5  # g < 1 mean no chaotic activity
# gs
dt = 0.1  # integration step size
steps = time / dt
learn_step = 2
scale = 1 / np.sqrt(N * dt)

x0 = 0.5 * np.random.randn(1, N)  # random initial input
z0 = 0.5 * np.random.randn(N)  # random initial output
x = x0
r = np.tanh(g * x)
z = z0

inputs = np.zeros(1, steps)
z_test = np.zeros(1, steps)
u = 2.0 * (np.random.rand(1, N) - 0.5)
# J_gg = pass
