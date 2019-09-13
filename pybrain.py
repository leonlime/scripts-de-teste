# python 2.7

from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer

# Criacao de um dataset com 2 entradas e 1 saida
# ENTRADAS: Quantas horas o aluno dormiu e quantas ele estudou
# SAIDA: A nota que o aluno tirou na prova
ds = SupervisedDataSet(2, 1)

# Add exemplos no dataset divididos sempre por 10
ds.addSample((0.8, 0.4), (0.7))
ds.addSample((0.5, 0.7), (0.5))
ds.addSample((1.0, 0.8), (0.95))

# Criacao da arquitetura da rede neural
# 2 neuronios de entrada, 4 na camada oculta e 1 na saida
# bias ativado. geralmente aprendem mais rapido
nn = buildNetwork(2, 4, 1, bias=True)

# Criacao do trainer que vai linkar a rede neural ao dataset
trainer = BackpropTrainer(nn, ds)

# Treinamento e print do treinamento da rede neural
for i in xrange(2000):
	print(trainer.train())

# input e previsao da nota
while True:
	dormiu = float(raw_input('Dormiu\n'))
	estudou = float(raw_input('Estudou\n'))
	z = nn.activate((dormiu, estudou))[0] * 10.0
	print('Previsao de nota: ', str(z))

