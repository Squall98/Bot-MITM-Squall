from map.contants import *
import yaswfp.swfparser as swfparser
from map.cell import Cell
from urllib.parse import unquote


class Map():

    def __init__(self, interface):
        self.interface = interface
        self.binairemap = []
        self.carreau = []
        self.mapswidth = 0
        self.sun = []
        self.entity = []
        self.resource = []
        self.width = 0  # Initialisez width et height à une valeur par défaut
        self.height = 0
        self.cells = []

    def data(self, mapID, map_date, decryption_key):
        self.mapID = mapID
        self.map_date = map_date
        self.decryption_key = decryption_key
        MAP_DIR = (PATH + "/data/maps")
        self.path = '{}/{}_{}{}.swf'.format(MAP_DIR, mapID, map_date, 'X' if decryption_key else '')
        print(self.path)  # Pour vérifier le chemin du fichier SWF
        pos = MAPID_TO_POS[mapID]
        self.x = pos[0]
        self.y = pos[1]

        # Initialise raw_map_data à None
        raw_map_data = None

        # Chargement du fichier SWF
        swf = swfparser.parsefile(self.path)

        # Ajouter des logs pour chaque tag dans swf.tags
        for index, tag in enumerate(swf.tags):
            print(f"Index: {index}, Type de tag: {type(tag).__name__}")
            if hasattr(tag, 'Actions'):
                print(f"Actions trouvées dans le tag d'index {index}")
                if hasattr(tag.Actions[0], 'ConstantPool') and tag.Actions[0].ConstantPool:
                    print(f"ConstantPool trouvé dans les Actions du tag d'index {index}")
                    # Utilisez le dernier élément du ConstantPool
                    raw_map_data = tag.Actions[0].ConstantPool[-1]
                    break
                else:
                    print(f"Pas de ConstantPool dans les Actions du tag d'index {index}")
            else:
                print(f"Aucune Actions dans le tag d'index {index}")

        # Vérifier si raw_map_data a été trouvé
        if raw_map_data is None:
            print("Aucune donnée de carte brute trouvée dans le fichier SWF.")
        else:

            # Utiliser raw_map_data pour continuer le traitement...
            data = self.decrypt_mapdata(raw_map_data, decryption_key)
            raw_cells = [data[i:i + 10] for i in range(0, len(data), 10)]
            self.cells = [Cell(raw_cells[i], i) for i in range(len(raw_cells))]

    def decrypt_mapdata(self, raw_data, raw_key):
        # Vérifie que la clé n'est pas vide
        if not raw_key:
            print("Erreur : la clé de décryptage est vide.")
            return ''  # Retourne une chaîne vide pour éviter les erreurs

        # Génère la clé de décryptage à partir de raw_key
        key = unquote(''.join([chr(int(raw_key[i:i + 2], 16)) for i in range(0, len(raw_key), 2)]))
        key_length = len(key)
        
        # Vérifie que key_length n'est pas zéro pour éviter la division par zéro
        if key_length == 0:
            print("Erreur : longueur de la clé de décryptage égale à zéro.")
            return ''

        checksum = int(HEX_CHARS[sum(map(lambda x: ord(x) & 0xf, key)) & 0xf], 16) * 2
        data = ''
        for i in range(0, len(raw_data), 2):
            try:
                hex_value = int(raw_data[i:i + 2], 16)
                data += chr(hex_value ^ ord(key[(int(i / 2) + checksum) % key_length]))
            except ValueError:
                print(f"Invalid hex data at position {i}: {raw_data[i:i + 2]}")
                continue
        return data


