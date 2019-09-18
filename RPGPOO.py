#!/usr/bin/env python

class personagem:
	def __init__(self):

		self.pdh = 0

		self.nome = raw_input('Digite o nome do seu personagem: ')

		while self.pdh != 5:
			self.forca = input('Digite a foca do personagem: ')	
			self.habilidade = input('Digite a habilidade do personagem: ')
			self.pdh = self.forca + self.habilidade
			if self.pdh != 5:
				print('digite novamente ate distribuir os 5 pontos')

	def print_pdh(self):
		print('seu nome eh:' + str(self.nome))
		print('forca: ' + str(self.forca))
		print('habilidade: ' + str(self.habilidade))


def main():
	char = personagem()
	char.print_pdh()


if __name__ == '__main__':
	main()
