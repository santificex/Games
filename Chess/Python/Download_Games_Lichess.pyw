import lichess.api
from lichess.format import PGN, SINGLE_PGN, PYCHESS
from io import *
import os
import glob
#Import required libraries
usuario = input('Insert username: ')
user = lichess.api.user(usuario)
pgn = lichess.api.user_games(usuario,max=1000000, format=SINGLE_PGN)
#print(pgn)
games=open("games.txt","w+")
games.write(pgn)
games.close()
archivo=open('games.txt',"r",encoding="utf8") #read pgn
textolineas=archivo.readlines() #extract each line of the pgn
consolidado=open("chess_stats_"+str(usuario)+".txt","w+") #Create new txt doc to dump the processed info
i=0 #start at 0
for lineas in range(len(textolineas)): #start loop
	try:
		if str(textolineas[i+14]).replace('\n','') == '': #write lines if game has no elo difference
			try:
				consolidado.write(str(textolineas[i]).replace('\n',',')+str(textolineas[i+1]).replace('\n',',')+str(textolineas[i+2]).replace('\n',',')+
				str(textolineas[i+3]).replace('\n',',')+
				str(textolineas[i+4]).replace('\n',',')+str(textolineas[i+5]).replace('\n',',')+
				str(textolineas[i+6]).replace('\n',',')+str(textolineas[i+7]).replace('\n',',')+str(textolineas[i+8]).replace('\n',',')+
				str(textolineas[i+9]).replace('\n',',')+str(textolineas[i+10]).replace('\n',',')+str(textolineas[i+11]).replace('\n',',')+
				str(textolineas[i+12]).replace('\n',',')+str(textolineas[i+13]).replace('\n',',')+str(textolineas[i+14]).replace('\n',',')+
				','+','+str(textolineas[i+15]).replace('\n',',')+','+','+'\n')
				i+=18
			except:
				pass
			finally:
				pass
		else: #write lines if game has elo difference
			try:
				consolidado.write(str(textolineas[i]).replace('\n',',')+str(textolineas[i+1]).replace('\n',',')+str(textolineas[i+2]).replace('\n',',')+
				str(textolineas[i+3]).replace('\n',',')+
				str(textolineas[i+4]).replace('\n',',')+str(textolineas[i+5]).replace('\n',',')+
				str(textolineas[i+6]).replace('\n',',')+str(textolineas[i+7]).replace('\n',',')+str(textolineas[i+8]).replace('\n',',')+
				str(textolineas[i+9]).replace('\n',',')+str(textolineas[i+10]).replace('\n',',')+str(textolineas[i+11]).replace('\n',',')+
				str(textolineas[i+12]).replace('\n',',')+str(textolineas[i+13]).replace('\n',',')+str(textolineas[i+14]).replace('\n',',')+
				str(textolineas[i+15]).replace('\n',',')+str(textolineas[i+16]).replace('\n',',')+str(textolineas[i+17]).replace('\n',',')+
				str(textolineas[i+18]).replace('\n',',')+str(textolineas[i+19]).replace('\n',',')+'\n')
				i+=20
			except:
				pass
			finally:
				pass
	except:
		pass
	finally:
		pass
consolidado.close()
archivo.close()
os.remove('games.txt')
print('Keep on playing')
input('Press Enter to exit...')