import okta120

m = okta120.matrix3([[3, 1, 2], [0, 2, 4], [6, 8, 9]])
k = okta120.matrix3([[4, 5, 6], [2, 0, 1], [0, 2, 8]])

m.ukuran()

trans = k.T()
print(f"\ntranspose matriks k: {trans}")

plus = m.tambah(m, k)
print(f"\nm + k = {plus} ")

min= m.kurang(m, k)
print(f"m - k = {min}")

dot= k.kali(m,k)
print(f"m * k = {dot}")

det= k.detm()
print(f"\ndeterminan matriks k: {det} ")

minor = k.minor()
print(f"\nminor matriks k: {minor}")

kof = k.kof()
print(f"\nkofaktor matriks k: {kof}")

adj = k.adj()
print(f"\nadjoint matriks k= {adj}")

invers = k.invers()
print(f"\ninvers matriks k: {invers}")


