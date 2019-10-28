from math import sqrt

#T é periodo
def ler_dados_do_arquivo():
	Dados= []
	arq = open('fisica.txt','r')
	linhas = arq.readlines();
	arq.close()
	for linha in linhas:
		Dados.append(float(linha))
	return Dados

def media(T):
	soma = 0
	media = 0
	for i in  range(0,len(T)):
		soma+=T[i]
	media = soma/len(T)
	return media

def desvios(media, T):
	D = []
	for i in range(0, len(T)):
		x = T[i]-media
		if x < 0:
			x*=(-1)
		D.append(x)
	return D
	

def printT(T, D):
	print('\n{0}	{1}	{2}'.format('Med.nº', 'Ti(s)','Desv(s)'))
	for i in range(0,len(T)):
		print('{0}	{1}	{2:3.3f}'.format(str(i+1), T[i],D[i]))

#programa principal
T = ler_dados_do_arquivo() 										#carregar os periodos medidos
mediaT = media(T)														#calcular o period médio
D = desvios(mediaT, T)												#calcular os desviso em realação ao periodo médio
mediaD = media(D)														#calcular o desvio médio
pi=3.14
l=0.3
lmin = 0.299
lmax = 0.301
tmax = mediaT+mediaD
tmin = mediaT-mediaD
gmax = (4*(pi**2)*lmax)/(tmin**2)
gmin = (4*(pi**2)*lmin)/(tmax**2)
gmed = (4*(pi**2)*l)/(mediaT**2)

printT(T, D)															#exibir a tabela de peirodos e seus desvios
print('\nPerioso Médio<T>: {0} (s)'.format(mediaT))				#exibir o periodo medio
print('Desvio medio <delta>: {0:3.3f} (s)'.format(mediaD))			#exibir o desvio medio
print('Incerteza instrumental: {0} (s)'.format(0.01))
print('Tmax: {0:3.3f} (s)'.format(tmax))
print('Tmin: {0:3.3f} (s)'.format(tmin))
print('Tmed: {0:3.3f} (s)'.format(mediaT))
print('Gmax: {0:3.3f} (m*s^-2)'.format(gmax))
print('Gmin: {0:3.3f} (m*s^-2)'.format(gmin))
print('Gmed: {0:3.3f} (m*s^-2)'.format(gmed))

print('\n')
