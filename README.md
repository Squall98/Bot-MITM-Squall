# Dofus-Retro-MITM
Mitm for dofus retro:

~~you just have to add:~~
~~connserver name="MITM" ip="127.0.0.1" port="443"~~
~~in the dofus config file after:~~

Using frida for hook dofus, so you need fritm.
```
pip install fritm
```


Change Log:  
Login  
Map Gestion (Load entity, move, resource il can be use or not)  
Pathfinding  
Auto Fight(Move, lauch spells)  
Job (Recolte)  
 
you need to change the variable PATH in : LeafMITM/map/contants.py


~~You need pywin32, https://pypi.org/project/pywin32/ to simulate a click otherwise the bot will not work
(it is not a pixel bot, it only simulates a click without using your mouse)
pip install pywin32~~

you also needed to install:
```
pip install lxml 

pip install Pillow

pip install yaswfp
```

# Dofus-Retro-MITM
Mitm pour Dofus Rétro :

~~il suffit d'ajouter :~~
~~connserver nom="MITM" ip="127.0.0.1" port="443"~~
~~dans le fichier de configuration de Dofus après :~~

Utilisation de Frida pour accrocher Dofus, donc vous avez besoin de fritm.
```
pip install fritm
```


Journal des modifications :  
Connexion  
Gestion de la carte (Chargement d'entité, déplacement, ressource pouvant être utilisée ou non)  
Pathfinding  
Combat Automatique (Déplacement, lancement de sorts)  
Métier (Récolte)  
 
vous devez changer la variable PATH dans : LeafMITM/map/constants.py


~~Vous avez besoin de pywin32, https://pypi.org/project/p
