import numpy as np
import matplotlib.pyplot as plt

def fonction(x):
    return np.exp(x)

def interpolation_tchebychev(a, b):
    N = 100
    M = 10000

    I = np.linspace(a, b, M+1)

    liste_zn = []
    liste_xn = []
    f = []

    for n in range(1, N + 1):

        z_n = np.cos((2 * n - 1) * np.pi / (2 * N))
        liste_zn.append(z_n)
        x_n = (a + b) / 2 + (b - a) / 2 * z_n
        liste_xn.append(x_n)
        f.append(fonction(x_n))

    A = np.zeros((N, N))

    for i in range(N):

        z_i = (2 * liste_xn[i] - a - b) / (b - a)

        for j in range(N):

            A[i, j] = np.cos(j * np.arccos(z_i))


    f = np.array(f)
    c = np.linalg.solve(A, f)


    I = np.array(I)
    z_red = (2 * I - a - b) / (b - a)
    approx = np.zeros_like(I)

    for k in range(N):
        approx += c[k] * np.cos(k * np.arccos(z_red))

    f_fonction = fonction(I)
    err = np.max(np.abs(approx - f_fonction))

    return err, I, f_fonction, approx

err, I, f_reelle, interpolant = interpolation_tchebychev(-10, 10)
print("Erreur maximale :", err)

plt.plot(I, f_reelle, label="f(x) réelle")
plt.plot(I, interpolant, label="Interpolant de Tchebychev", linestyle="--")
plt.legend()
plt.grid(True)
plt.title(f"Interpolation de la fonction choisie (erreur max = {err:.2e})")
plt.show()
