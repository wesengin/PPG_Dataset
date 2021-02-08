import matplotlib.pyplot as plt

f = open('./0_subject/3_1.txt', 'r')
for line in f.readlines():
    dados = [float(x) for x in line.strip().split('\t')]
    plt.plot(dados)
    plt.show()
