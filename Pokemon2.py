#Script en python que consulta el api de pokemon
#para listar los nombres de pokemon pero se le agrego
#interaccion para que listara pokemons segun se vaya requiriendo
#Contribuyo: Diego Andres Rodriguez Lugo
#Fecha: 15/09/2022
import requests
#nombre:Diego Andres Rodriguez Lugo
#matricula:182020
def get_pokemons (url='https://pokeapi.co/api/v2/pokemon-form', offset=0):
	args={'offset':offset} if offset else {}
	response= requests.get(url, params=args)
	if response.status_code ==200:
		payload=response.json()
		results=payload.get('results',[])
		if results:
			for pokemon in results:
				name=pokemon['name']
				print(name)
		next = input ("¿Continuar listando [Y/N]").lower()
		if next=="y"or next=="Y":
			get_pokemons(offset=offset+20)
if __name__=='__main__':
	url='https://pokeapi.co/api/v2/pokemon-form'
	get_pokemons()
