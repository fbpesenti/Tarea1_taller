import requests
from django.shortcuts import render
# Create your views here.

def home(request):

   if requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes').status_code == 200:
      response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes').json()
   season_breaking = []
   season_better = []
   for elemento in response:
      if elemento['series'] == 'Breaking Bad':
         if elemento['season'] not in season_breaking:
            season_breaking.append(elemento['season'])
      elif elemento['series'] == 'Better Call Saul':
         if elemento['season'] not in season_better:
            season_better.append(elemento['season'])

   return render(request, "tarea0/home.html", {'breaking':season_breaking , 'better':season_better})

def breaking(request, i):

   if requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad').status_code == 200:
      response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Breaking+Bad').json()
   episodes = []
   for elemento in response:
      if elemento['season'] == i:
         episodes.append(elemento)


   return render(request, "tarea0/breakingbad.html", {'episodes':episodes})

def better(request, season):

   if requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul').status_code == 200:
      response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes?series=Better+Call+Saul').json()
   episodes = []
   for elemento in response:
      if elemento['season'] == season:
         episodes.append(elemento)
   
   return render(request, "tarea0/bettercallsaul.html", {'episodes':episodes})

def episode(request, episode):

   if requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes/'+str(episode)).status_code == 200:
      response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/episodes/'+str(episode)).json()
   
   return render(request, "tarea0/episode.html", {'response': response})

def personaje(request, personaje):

   personaje = personaje.replace('-','+')
   if requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/characters?name='+str(personaje)).status_code == 200 and requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/quote?author='+str(personaje)).status_code == 200:
      response = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/characters?name='+str(personaje)).json()
      quotes = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/quote?author='+str(personaje)).json()
   return render(request, "tarea0/personaje.html", {'response': response, 'quotes': quotes})

def busqueda_personajes(request):
   personajes = []
   personaje = request.GET['personaje']
   personaje = personaje.replace(' ','+')
   i = 0
   count = 10
   while count>=10:
      if requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/characters?name='+str(personaje)+'&offset='+str(i)).status_code == 200:
         personaje = requests.get('https://tarea-1-breaking-bad.herokuapp.com/api/characters?name='+str(personaje)+'&offset='+str(i)).json()
      personajes.append(personaje)
      count = len(personaje)
      print(personajes)
      i+=10
   return render(request, "tarea0/busqueda_personaje.html", {'personaje': personajes})