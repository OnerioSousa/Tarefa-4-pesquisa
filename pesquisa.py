#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pesquisa.py
#  
#  Copyright 2018 20181bsi0121 <20181bsi0121@SR6192>
#  
# 

def main():

	sexo = ''; olhos = ''; cabelo = ''; idade = '';
	maior_idade = 0; total = 0; total_filtro = 0; porcentagem = 0;
	
	# recebendo valores
	print((total+1),'º) CADASTRO: ')

	sexo = input('Sexo (feminino, masculino): ')
	olhos = input('Cor do olho (azuis, verdes, castanho): ')
	cabelo = input('Cor do cabelo (louros, catanhos, pretos): ')
	idade = float(input('Idade: '))
	
	while idade != -1:
		
		#cont registros
		total = total+1
		
		# acumula os valores da idade maiores
		if idade > maior_idade:
			maior_idade = idade

		# porcentagem do (sexo feminino) (idade entre 18 e 35) (olhos verdes) (cabelos claros)
		if idade >= 18 and idade <= 35 and sexo == 'feminino' and olhos == 'verdes' and cabelo == 'louros':
			total_filtro = total_filtro + 1	
				
		print('----------------------//----------------------')

		# recebendo valores
		print((total+1),'º) CADASTRO: ')
		sexo = input('Sexo (femino, masculino): ')
		olhos = input('Cor do olho (azuis, verdes, castanho): ')
		cabelo = input('Cor do cabelo (louros, catanhos, pretos): ')
		idade = float(input('Idade: '))
		
	# fim while

	porcentagem = (100*total_filtro)/total #ultima linha não corresponde a ninguem, logo não tenho que contabilzar ela
	
	print('\n\nRESULTADO----------------------')
	print('Maior idade: ',maior_idade)
	print('Porcentagem (femino , idade entre 18 e 35 anos , olhos verdes, cabelos loiros): %2.f *porcento'%porcentagem)	


	return 0

if __name__ == '__main__':
	main()
