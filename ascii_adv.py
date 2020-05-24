##try:
import tcod
import sys
import random
import copy
import math

Dorsum = [
    ['Dur', 'Dor'],
    ['sum', 'sam']]

FRBL = [
    'F',
    'FR',
    'R',
    'BR',
    'B',
    'BL',
    'L',
    'FL']

NINE = [
    ' ^ \n   \n   ',
    '  /\n   \n   ',
    '   \n  >\n   ',
    '   \n   \n  \\',
    '   \n   \n v ',
    '   \n   \n/  ',
    '   \n<  \n   ',
    '\\  \n   \n   ']

NESW = [   
    'N',
    'NE',
    'E',
    'SE',
    'S',
    'SW',
    'W',
    'NW']

'''
     1
   16 2
  15   3
 14     4
13   0   5
 12     6
  11   7
   10 8
     9
'''

CARDINAL4 = ['F', 'R', 'B', 'L']

COMPASS4 = [
    0,
    'F', 'F',
    'R', 'R', 'R', 'R', 'R',
    'B', 'B', 'B',
    'L', 'L', 'L', 'L', 'L',
    'F']

COMPASS8 = [
    0,
    'F', 'F',
    'FR',
    'R', 'R', 'R',
    'BR',
    'B', 'B', 'B',
    'BL',
    'L', 'L', 'L',
    'FL',
    'F']

COMPASS16 = [
    0,
    'F',
    'FRF',
    'FR',
    'FRR',
    'R',
    'BRR',
    'BR',
    'BRB',
    'B',
    'BLB',
    'BL',
    'BLL',
    'L',
    'FLL',
    'FL',
    'FLF']

COMPASS_CARDINAL = [
    0,
    'N', 'N',
    'NE',
    'E', 'E', 'E',
    'SE',
    'S', 'S', 'S',
    'SW',
    'W', 'W', 'W',
    'NW',
    'N']

VECTOR = {
    'N': (0, 1),
    'NE': (1, 1),
    'E': (1, 0),
    'SE': (1, -1),
    'S': (0, -1),
    'SW': (-1, -1),
    'W': (-1, 0),
    'NW': (-1, 1)}

##Only used in Scope() as the coordinate is based on @
VECTORF = {
    'F': (0, 1),
    'FR': (1, 1),
    'R': (1, 0),
    'BR': (1, -1),
    'B': (0, -1),
    'BL': (-1, -1),
    'L': (-1, 0),
    'FL': (-1, 1)}

VECTOR1 = [
    ['SW', 'W', 'NW'],
    ['S', 0, 'N'],
    ['SE', 'E', 'NE']]

MATERIAL = [
    'iron',
    'bronze',
    'copper',
    'wooden',
    'cotton',
    'leather',
    'stone',
    'diamond',
    'animal']

SOFTM = [
    'cotton',
    'leather']

METALM = [
    'iron',
    'bronze',
    'copper']

WOODM = [
    'wooden']

FURNITURE = [
    'door',
    'incensor',
    'gate',
    'table',
    'hook',
    'bell']

DOOR = [
    'door',
    'gate']

FLAT_FURN = [
    'table']

HOOKED_FURN = [
    'hook']

HANG = [
    'key',
    'pouch',
    'shield',
    'sheath',
    'scabbard']

SHEATH = [
    'scabbard',
    'sheath']

HUMAN = [
    'adv',
    'shopkeeper',
    'guard',
    'guard1',
    'smith',
    'alchemist',
    'cobbler',
    'mayor']

DWARF = [
    'goblin',
    'dwarf']

ALICE = [
    'Alice',
    'Bahar',
    'Charlene',
    'Cici',
    'Coco',
    'Doris',
    'Ellen',
    'Faustina',
    'Gabriela',
    'Helene',
    'Ilsa',
    'Jesse',
    'Jenny',
    'Jo',
    'Kacey',
    'Liza',
    'Marion',
    'Norah',
    'Oxana',
    'Penelope',
    'Priscilla',
    'Rose',
    'Undine',
    'Yasmine']

BOB = [
    'Adrian',
    'Bob',
    'Bart',
    'Bert',
    'Cameron',
    'Dan',
    'Edward',
    'Elliot',
    'Federick',
    'Gabriel',
    'Harold',
    'Idris',
    'Jack',
    'Jackie',
    'Johan',
    'Kevin',
    'Lars',
    'Manfred',
    'Michael',
    'Noah',
    'Novak',
    'Norman',
    'Omer',
    'Oswald',
    'Peter',
    'Ryan',
    'Silvester',
    'Toby',
    'Tony',
    'Ulric',
    'Vadim',
    'Vince',
    'Walter',
    'Yaqub']
    
ALICEBOB = ALICE + BOB

TWINNAMES = [
    ['Adam', 'Amanda'],
    ['Carlos', 'Carla'],
    ['Donald', 'Dana'],
    ['Eric', 'Erica'],
    ['Frank', 'Francesca'],
    ['Gerard', 'Gerardine'],
    ['Henry', 'Heidi'],
    ['Mike', 'Michelle'],
    ['Paul', 'Pauline'],
    ['Salman', 'Sarah'],
    ['Tom', 'Tori'],
    ['Viktor', 'Vicky']]

GNOME = [
    'gnome']

GIANT = [
    'ogre']

HUMANOID = HUMAN + DWARF + GNOME + GIANT

ANIMATE = HUMANOID

CUTSDEEP = {
    'axe': 20,
    'pickaxe': 25}

WEAPONSTAB = [
    'sword',
    'scimitar',
    'dagger']

WEAPONBASH = [
    'hammer']

WEAPONHACK = [
    'axe',
    'pickaxe']

WEAPON = WEAPONSTAB + WEAPONBASH + WEAPONHACK

SHIELD = [
    'shield',
    'buckler']

ARMOR = [
    'pouch',
    'scabbard',
    'sheath']

SOFT = [
    'pouch']

LEATHER = [
    'scabbard',
    'sheath',
    'boot',]

BAG = [
    'pouch',
    'scabbard',
    'sheath']

MURAL = [
    'inscription',
    'glisten']

TREE = [
    'tree',
    'branch']

CANTPICK = ANIMATE + FURNITURE + MURAL + TREE

CURVED_WEAPON = [
    'scimitar']


SMALL = [
    'gold']

POUCHABLE = [
    'gold',
    'diamond',
    'key',
    'potion']

def Coins(value):
    co = value // 100
    if value % 100 > 0:
        co += 1
    return co

TEMPLATE = {
    'door': {
        'le': 250,
        'wi': 100,
        'th': 5,
        'pr': 1000,
        'gl': '+'},
    'gate': {
        'le': 250,
        'wi': 100,
        'th': 5,
        'pr': 1000,
        'gl': '+'},
    'incensor': {
        'le': 100,
        'wi': 30,
        'th': 30,
        'pr': 1000,
        'gl': '<>'},
    'table': {
        'le': 100,
        'wi': 60,
        'th': 60,
        'pr': 1000,
        'gl': '=='},
    'hook': {
        'le': 5,
        'wi': 1,
        'th': 5,
        'pr': 1000,
        'gl': '?'},
    'bell': {
        'le': 5,
        'wi': 5,
        'th': 5,
        'pr': 1000,
        'gl': ':'},
    'inscription': {
        'le': 10,
        'wi': 10,
        'th': 1,
        'pr': 1000,
        'gl': '...'},
    'glisten': {
        'le': 10,
        'wi': 10,
        'th': 1,
        'pr': 1000,
        'gl': '...'},
    'sword': {
        'le': 60,
        'wi': 5,
        'th': 1,
        'pr': 500,
        'gl': '/'},
    'scimitar': {
        'le': 50,
        'wi': 15,
        'th': 1,
        'pr': 500,
        'gl': '/'},
    'hammer': {
        'le': 30,
        'wi': 15,
        'th': 5,
        'pr': 400,
        'gl': '/'},
    'pickaxe': {
        'le': 50,
        'wi': 5,
        'th': 50,
        'pr': 500,
        'gl': '/'},
    'axe': {
        'le': 60,
        'wi': 5,
        'th': 20,
        'pr': 500,
        'gl': '/'},
    'dagger': {
        'le': 30,
        'wi': 5,
        'th': 1,
        'pr': 300,
        'gl': '/'},
    'shield': {
        'le': 3,
        'wi': 90,
        'th': 90,
        'pr': 500,
        'gl': ']'},
    'buckler': {
        'le': 3,
        'wi': 60,
        'th': 60,
        'pr': 400,
        'gl': ']'},
    'potion': {
        'le': 10,
        'wi': 3,
        'th': 3,
        'pr': 300,
        'gl': '!'},
    'pouch': {
        'le': 15,
        'wi': 15,
        'th': 15,
        'pr': 200,
        'gl': ')'},
    'scabbard': {
        'le': 65,
        'wi': 12,
        'th': 3,
        'pr': 400,
        'gl': ')'},
    'sheath': {
        'le': 35,
        'wi': 12,
        'th': 3,
        'pr': 300,
        'gl': ')'},
    'boot': {
        'le': 30,
        'wi': 10,
        'th': 30,
        'pr': 400,
        'gl': ')'},
    'key': {
        'le': 10,
        'wi': 3,
        'th': 1,
        'pr': 1000,
        'gl': ':'},
    'shopkeeper': {
        'le': 170,
        'wi': 60,
        'th': 20,
        'pr': 1000,
        'gl': '@'},
    'guard': {
        'le': 170,
        'wi': 60,
        'th': 20,
        'pr': 1000,
        'gl': '@'},
    'guard1': {
        'le': 170,
        'wi': 60,
        'th': 20,
        'pr': 1000,
        'gl': '@'},
    'adv': {
        'le': 170,
        'wi': 60,
        'th': 20,
        'pr': 1000,
        'gl': '@'},
    'mayor': {
        'le': 170,
        'wi': 60,
        'th': 20,
        'pr': 1000,
        'gl': '@'},
    'smith': {
        'le': 170,
        'wi': 60,
        'th': 20,
        'pr': 1000,
        'gl': '@'},
    'cobbler': {
        'le': 170,
        'wi': 60,
        'th': 20,
        'pr': 1000,
        'gl': '@'},
    'alchemist': {
        'le': 170,
        'wi': 60,
        'th': 20,
        'pr': 1000,
        'gl': '@'},
    'goblin': {
        'le': 100,
        'wi': 30,
        'th': 15,
        'pr': 1000,
        'gl': 'g'},
    'dwarf': {
        'le': 100,
        'wi': 40,
        'th': 20,
        'pr': 1000,
        'gl': 'h'},
    'gnome': {
        'le': 60,
        'wi': 20,
        'th': 10,
        'pr': 1000,
        'gl': 'gn'},
    'ogre': {
        'le': 250,
        'wi': 100,
        'th': 50,
        'pr': 1000,
        'gl': 'O'},
    'tree': {
        'le': 500,
        'wi': 50,
        'th': 50,
        'pr': 1000,
        'gl': 'T'},
    'branch': {
        'le': 100,
        'wi': 10,
        'th': 10,
        'pr': 1000,
        'gl': '/'},
    'gold': {
        'le': 1,
        'wi': 1,
        'th': 1,
        'pr': 100,
        'gl': '$'},
    'diamond': {
        'le': 1,
        'wi': 1,
        'th': 1,
        'pr': 1000,
        'gl': '*'}}
    

SHKSPELLEFF = [
    'burning coal rolling in',
    'ice boulders shattering in',
    'lava washing over',
    'elephantelopes kicking',
    'chains lashing at',
    'crows pecking',
    'someone pinching',
    'someone squeezing',
    'someone stretching',
    'someone twisting']

def Spelltx(castertype):
    '''Only used when @ is attacked'''
    text = random.choice(SHKSPELLEFF)
    if castertype == 'dwarf':
        text = 'lava washing over'
    if text.startswith('antelopes') or text.startswith('chain'):
        text = random.choice(METALM) + ' ' + text
    elif text.startswith('lava'):
        text = random.choice(['spiked', 'jagged', 'serrated']) + ' ' + text
    text = 'you feel ' + text + ' your ' + random.choice(INNARD)

    return text    

INNARD = [
    'heart',
    'liver',
    'lungs',
    'kidneys',
    'stomach']

CHEM = [
    'lead',
    'mercury']

CHEM_EFFECT = {
    'lead': 'heavy',
    'mercury': 'free'}

PCHEMN = {
    'lead': ['heavy', 'slow', 'thick', 'rough'],
    'mercury': ['free', 'light', 'quick', 'smooth']}

POTIONTYPE = ['water', 'juice', 'brine', 'brew']

CHEMN = {}
for ch, ps in PCHEMN.items():
    CHEMN[ch] = random.choice(ps) + ' ' + random.choice(POTIONTYPE)

##Anatomy
##Arms cannot be more than 10
##Humanoid top down view
HUMAN_TDV = {
    'head': [
        'F',
        'FR',
        'R',
        'BR',
        'B',
        'BL',
        'L',
        'FL'],
    'body': [
        'F',
        'FR',
        'R',
        'BR',
        'B',
        'BL',
        'L',
        'FL'],
    'arm0': [        
        'F',
        'B',
        'BL',
        'L',
        'FL'],
    'arm1': [
        'F',
        'FR',
        'R',
        'BR',
        'B'],
    'leg0': [        
        'F',
        'B',
        'BL',
        'L',
        'FL'],
    'leg1': [
        'F',
        'FR',
        'R',
        'BR',
        'B']}

##Humanoid side view. 'head': (9, 1) means head starts from 9 and has a height of 1 and occupies the height of 10
HUMAN_SDV = {
    'head': (9, 1),
    'body': (5, 4),
    'arm0': (5, 4),
    'arm1': (5, 4),
    'leg0': (0, 5),
    'leg1': (0, 5)}

##Humanoid blocking position top down view
HUMAN_BTDV = [[
        'F',
        'FL',
        'L'],
        ['F',
        'FR',
        'R']]

HUMANOID_AP = [
    'body',
    'leg0',
    'leg1',
    'arm0',
    'arm1',
    'head']

STANCE_GLYPH = [
    '_',
    '+',
    '|']

GREETINGS = [
    ['hello', 'hello'],
    ['hi', 'hi'],
    ['good day!', 'good day!']]

MAYORSPEECH = [
    'Ziumni is the most beautiful city',
    'Ziumni is facing a great danger']

PURPOSE = [
    ['I am an adventurer', 'adv'],
    ['I\'m seeing the world', 'tourist'],
    ['I am a craftsman', 'craft'],
    ['I am a hired killer', 'assassin'],
    ['I am a merchant', 'merchant'],
    ['I am an anthropologist', 'anthrop'],
    ['I am a detective', 'detective'],
    ['I am a Health Officer', 'health'],
    ['I\'m seeking refuge', 'refuge'],
    ['I am looking for an artifact', 'thief'],
    ['I am looking for bees', 'bee'],
    ['I am looking for exotic plants', 'plant'],
    ['I am looking for a job', 'job'],
    ['I am looking for my lost child', 'lost child'],
    ['I am drawn here by a strong magnetic power', 'magnetic'],
    ['I am a hunter', 'hunt'],
    ['I come here to visit an old friend', 'friend'],
    ['I come here to pay my debt', 'debt'],
    ['I come here for a heritage', 'heritage'],
    ['I come here to shoot some videos', 'video'],
    ['I come here to save your people', 'save'],
    ['I come here to destroy your people', 'destroy'],
    ['I come here to liberate your people', 'liberate'],
    ['I\'d rather not disclose', 'secret']]

def DefaultStance(tipo):
    stance = 2
    if tipo in HUMANOID:
        stance = 2
    else:  ##To add quadruped and reptilian
        stance = 2
    return stance

class Site:
    '''A site on worldmap'''
    def __init__(self, x, y, tipht=0, wallht=0, name=None, natfl='GRAVEL', walltype='stone wall'):

        self.x = x
        self.y = y
        self.tipht = tipht
        self.wallht = wallht
        self.name = name
        self.natfl = natfl  ##Natural floor
        self.walltype = walltype
        self.room_list = []
        Field(400, 400, self)
        self.citizen = []
        self.guest = []
        self.suspect = []
        self.guard = []
        self.goblin = []
        self.mayor = None
        self.usedn = []
        worldmap.append(self)

class Room:
    '''A room'''
    ##bmap = block map, Room shouldn't be smaller than 3x3
    def __init__(
        self, x, y, site, ceiling=True, name=None, flomat=None, wlmat=None):

        self.x = x
        self.y = y
        self.site = site
        site.room_list.append(self)
        self.ceiling = ceiling
        if flomat is None:
            self.flomat = site.natfl
        else:
            self.flomat = flomat
        if wlmat is None:
            self.wlmat = site.walltype
        else:
            self.wlmat = wlmat
        self.name = name
        self.item_list = []
        self.aoe_list = []
        self.portal = {}
        self.bmap = [[0 for i in range(y)] for j in range(x)]
        for i in range(x):
            self.bmap[i][0] = 1
            self.bmap[i][y-1] = 1
        for i in range(y):
            self.bmap[0][i] = 1
            self.bmap[x-1][i] = 1

class Field:
    '''A field'''
    def __init__(
        self, x, y, site, name=None, flomat=None):
        
        self.x=x
        self.y=y
        self.site = site
        site.room_list.append(self)
        self.name = name
        self.item_list=[]
        self.aoe_list = []
        self.portal={}
        self.bmap = [[0 for i in range(y)] for j in range(x)]
        self.town = False
        self.ceiling = False
        if flomat is None:
            self.flomat = site.natfl
        else:
            self.flomat = flomat
        self.wlmat = site.walltype

class Door:
    '''A door'''
    ##Door cannot be on the corner of a room
    def __init__(
        self, room0, x0, y0, room1, x1, y1, doortype='door',
        closed=True, lock=None,
        name0='', name1='', name=None, flomat=None, wlmat=None):
        
        self.site = room0.site  ##room0 and room1 should be on the same site
        self.site.room_list.append(self)
        self.portal={room0: (0, 0), room1: (0, 0)}
        if closed:
            door_status = 3
        else:
            door_status = 2
        ##room0
        if isinstance(room0, Field):  ##Only used in forming city gate
            room0.town = True
            for i in range(100, 300):
                for j in range(100, 300):
                    room0.bmap[j][i] = 1
        room0.bmap[x0][y0]=door_status
        room0.portal[self]=(x0, y0)
        if isinstance(room0, Room):
            if x0 == 0:
                vector0 = (1, 0)
            else:
                if x0 == room0.x - 1:
                    vector0 = (-1, 0)
                else:
                    if y0 == 0:
                        vector0 = (0, 1)
                    else:
                        vector0 = (0, -1)
        else:
            vector0 = None
        ##room1
        if isinstance(room1, Field):  ##Only used in forming city gate
            room1.town = True
            for i in range(100, 300):
                for j in range(100, 300):
                    room1.bmap[j][i] = 1
        room1.bmap[x1][y1]=door_status
        room1.portal[self]=(x1, y1)
        if isinstance(room1, Room):
            if x1 == 0:
                vector1 = (1, 0)
            else:
                if x1 == room1.x - 1:
                    vector1 = (-1, 0)
                else:
                    if y1 == 0:
                        vector1 = (0, 1)
                    else:
                        vector1 = (0, -1)
        else:
            vector1 = None

        if vector0 is None:
            z, w = vector1
            vector0 = (-z, -w)
        if vector1 is None:
            z, w = vector0
            vector1 = (-z, -w)
            
        self.vectors = {room0: vector0, room1: vector1}
        self.bmap = [[door_status]]
        self.name = name
        self.doortype = doortype
        self.ceiling = True
        if flomat is None:
            self.flomat = room0.flomat
        else:
            self.flomat = flomat
        if wlmat is None:
            self.wlmat = room0.wlmat
        else:
            self.wlmat = wlmat
        self.item_list = []
        self.door = (Item(doortype, 0, 0, self, names={room0: name0, room1: name1}, lock=lock))
        self.aoe_list = []

class Order:
    '''Buyer, price, seller, good'''
    def __init__(
        self, buyer, price, seller, good):

        self.buyer = buyer
        self.price = price
        self.seller = seller
        self.good = good
        self.paid = 0
        self.status = 'UNPAID'

class Task:
    def __init__(
        self, name, detail):

        self.name = name
        self.detail = detail

class AOE:
    '''Area of effect'''
    def __init__(
        self, chem, x, y, room, strength, radius=5):

        self.tipo = 'aoe'
        self.chem = chem
        self.x = x
        self.y = y
        self.room = room
        self.strength = strength
        self.radius = radius
        self.name = 'mist of ' + CHEMN[chem]

    def Name(self):
        return self.name

class Item:
    '''An item'''
    def __init__(
        self, tipo, x, y, room, name=None, names=None, material=None,
        dodge_sk=10, fight_sk=10,
        facing=None,
        eqstyle = None,
        flask=None, lock=None, key_to=None, bag=False, ins=None, tree=None,
        ore=None, cutsdeep = 0,
        owner=None, shk=False):

        self.tipo=tipo
        if tipo in WEAPON:
            self.material = random.choice(METALM)
        elif tipo in SHIELD:
            self.material = random.choice(METALM + WOODM)
        elif tipo in SOFT:
            self.material = random.choice(SOFTM)
        elif tipo in LEATHER:
            self.material = 'leather'
        else:
            self.material = None
        if material:  ##Override default material
            self.material = material
        self.x=x
        self.y=y
        self.room=room
        room.item_list.append(self)

        if self.tipo in ANIMATE:
            self.anim = True
        else:
            self.anim = False
        if self.tipo in HUMAN:
            self.gender = random.choice(['man', 'woman'])
        self.paralyzed = False
        self.suffocate = None
        self.fixedto = None
        self.charisma = random.randint(0, 1)

        if name:
            self.name = name
        else:
            if tipo in ANIMATE:
                count = 0
                while True:
                    count += 1
                    if tipo in HUMAN:
                        if self.gender == 'man':
                            pname = random.choice(BOB)
                        else:
                            pname = random.choice(ALICE)
                    else:
                        pname = random.choice(ALICEBOB)
                    if pname not in room.site.usedn:
                        self.name = pname
                        room.site.usedn.append(pname)
                        break
                    if count >= 100:
                        self.name = 'Jo'
            elif tree:
                if 'banyan' in tree.name:
                    self.name = 'banyan vine'
                else:
                    self.name = 'branch'
            else:
                self.name = tipo
        if self.material:
            self.name = self.material + ' ' + self.name
        self.names=names

        self.skill = {
            'dodge': dodge_sk,
            'fight': fight_sk}
        self.watch = []
        self.attack = None
        self.attacksp = None
        self.tls = None  ##Target last seen
        self.destination = None
        if facing is None:
            self.facing = random.choice(NESW)
        else:
            self.facing = facing
        self.defaultstance = DefaultStance(tipo)
        self.stance = self.defaultstance
        self.display_move = False
        self.dismovg = '>'  ##glyph for display_move
        self.balance = 0
        self.blocking = {}
        self.length = TEMPLATE[tipo]['le']
        self.thick = TEMPLATE[tipo]['th']
        self.width = TEMPLATE[tipo]['wi']
        if self.tipo in HUMANOID:
            self.body = {
                'head': 1,
                'body': 1,
                'arm0': 1,
                'arm1': 1,
                'leg0': 1,
                'leg1': 1}
            for part, hp in self.body.items():
                self.body[part] = hp * TEMPLATE[tipo]['th']
        else:
            self.body = {
                'body': self.thick}
        if self.tipo == 'tree':
            self.branch = []
            for i in range(random.randint(3, 5)):
                self.branch.append(Item('branch', self.x, self.y, self.room, tree=self))
        self.maxhp = copy.copy(self.body)

        self.inv=[]
        self.wield = []
        if self.tipo in HUMANOID:
            self.wield = [None, None]
        if self.tipo in HUMANOID:
            self.sdv = {}
            for part, dimension in HUMAN_SDV.items():
                start, height = dimension
                self.sdv[part] = (self.length*start//10, self.length*height//10)
        self.wear = []
        self.stock=[]
        if eqstyle is None:
            if self.tipo in HUMANOID:
                if self.tipo.startswith('guard'):
                    eqstyle = 'melee'
                elif self.tipo == 'smith':
                    eqstyle = 'civilian_smith'
                elif self.tipo == 'goblin':
                    eqstyle = 'melee_s'
                elif self.tipo in ['gnome', 'ogre']:
                    eqstyle = 'wild'
                elif self.tipo == 'dwarf':
                    eqstyle = 'dwarf'
                else:
                    eqstyle = 'civilian'
        if eqstyle is not None:
            if eqstyle.startswith('melee'):
                po = Item('pouch', self.x, self.y, self.room)
                self.wear.append(po)
                self.inv.append(po)
                if eqstyle == 'melee':
                    sh = Item('shield', self.x, self.y, self.room)
                    self.wield[0] = sh
                    self.inv.append(sh)
                    sc = Item('scabbard', self.x, self.y, self.room)
                    self.wear.append(sc)
                    self.inv.append(sc)
                    sw = Item('sword', self.x, self.y, self.room)
                    sc.bag.append(sw)
                    self.inv.append(sw)
                elif eqstyle == 'melee_s':
                    bu = Item('buckler', self.x, self.y, self.room)
                    self.wield[0] = bu
                    self.inv.append(bu)
                    sc = Item('sheath', self.x, self.y, self.room)
                    self.wear.append(sc)
                    self.inv.append(sc)
                    dg = Item('dagger', self.x, self.y, self.room)
                    sc.bag.append(dg)
                    self.inv.append(dg)
            elif eqstyle.startswith('civilian'):
                po = Item('pouch', self.x, self.y, self.room)
                self.wear.append(po)
                self.inv.append(po)
                if eqstyle == 'civilian_smith':
                    hm = Item('hammer', self.x, self.y, self.room)
                    self.wield[1] = hm
                    self.inv.append(hm)
                else:
                    sc = Item('sheath', self.x, self.y, self.room)
                    self.wear.append(sc)
                    self.inv.append(sc)
                    dg = Item('dagger', self.x, self.y, self.room)
                    sc.bag.append(dg)
                    self.inv.append(dg)
            elif eqstyle == 'dwarf':
                    po = Item('pouch', self.x, self.y, self.room)
                    self.wear.append(po)
                    self.inv.append(po)
                    ax = Item('axe', self.x, self.y, self.room)
                    self.wield[1] = ax
                    self.inv.append(ax)
            elif eqstyle == 'wild':
                pass
        if bag:
            self.bag = []
        if tipo in BAG:
            self.bag = []
        if tipo in FURNITURE:
            self.finvt = []  ##Furniture inv "on the top"
        if flask:
            self.flask = flask
            text = 'flask of '
            for ch in flask.keys():
                text += CHEMN[ch] + ' '
            text = text[:-1]
            self.name = text
        else:
            self.flask = {}
        if lock:
            self.lock = lock
            self.locked = True
        else:
            self.lock = None
            self.locked = False
        self.cutsdeep = cutsdeep
        if tipo in WEAPONHACK:
            self.cutsdeep = CUTSDEEP[tipo]
        self.key_to = key_to
        self.ins = ins
        self.tree = tree
        self.bird = []
        self.looped = False
        self.ore = ore
        if ore is not None:
            self.minecounter = 3

        self.poison = {}
        self.epoi = []  ##Effects of poison

        self.speaking = 0
        self.order = []
        self.shk = shk

        self.task = []
        if self.anim:
            self.task.append(Task('manage inv', None))
        if shk:
            self.task.append(Task('shop guard', []))
        if tipo.startswith('guard'):
            self.task.append(Task('guard', room.site))
        if tipo == 'gnome':
            self.task.append(Task('gnome guard', None))
        if tipo == 'mayor':
            self.task.append(Task('assassin alert', None))
        if tipo == 'dwarf':
            self.task.append(Task('diamwatch', []))
            
        self.owner = owner

        if tipo in ANIMATE:
            if isinstance(room, Room) or isinstance(room, Door):
                self.room.site.citizen.append(self)
        self.time = 0

    def Name(self):
        n = self.name
        if self.looped:
            n += ' loop'
        return n

    def PocketGold(self):
        au = 0
        for g in self.inv:
            if g.tipo == 'gold':
                au += 100
        return au

    def BagContent(self):
        '''Content of a container'''
        content = []
        if hasattr(self, 'bag'):
            for i in self.bag:
                content.append(i)
                content += i.BagContent()
        return content

    def TakeOff(self, equipment):
        if isinstance(equipment, list) or isinstance(equipment, tuple):
            for eq in equipment:
                self.TakeOff(eq)
        else:
            for weapon in self.wield:
                if weapon == equipment:
                    i = self.wield.index(weapon)
                    self.wield[i] = None
                    break
                elif isinstance(weapon, list):
                    if equipment in weapon:
                        weapon.remove(equipment)
                        if weapon == []:
                            i = self.wield.index(weapon)
                            self.wield[i] = None
                        break
            if equipment in self.wear:
                self.wear.remove(equipment)
            for b in self.inv:
                if hasattr(b, 'bag') and equipment in b.bag:
                    b.bag.remove(equipment)

    def FreeHand(self):
        free_hand = None
        for part, hp in self.body.items():
            if part.startswith('arm') and hp > 0:
                i = int(part[-1])
                if self.wield[i] is None:
                    free_hand = i
                    break
        return free_hand

    def HasPart(self, part):
        has = False
        if self.tipo in HUMANOID:
            if part in ['arm', 'leg']:
                for part1, hp1 in self.body.items():
                    if part1.startswith(part) and hp1 > 0:
                        has = True
                        break
            elif part == 'legs':
                has = True
                for part1, hp1 in self.body.items():
                    if part1.startswith('leg') and hp1 <= 0:
                        has = False
                        break
            else:
                if part in self.body and self.body[part] > 0:
                    has = True
        return has

    def Say(self, speech, prompt=False, pr=True): ##pr: prompt refresh
        has_said = False
        if self.speaking <= 0:
            cs = CanSee(self, at)
            ch = CanHear(at, self)
            if cs or ch:
                if cs:
                    speaker = self.name
                elif ch:
                    speaker = 'someone'
                if speech.startswith('verb_'):
                    text = speaker + ' ' + speech[5:]
                else:
                    text = speaker + ': ' + speech
                Message(text)
                if prompt:
                        Prompt(text, refresh=pr)
            self.speaking = 10
            has_said = True
        return has_said

    def TurnTo(self, obj):
        '''Turn one's face to the obj'''
        d = Direction(self, obj, dn='cardinal')
        if d != 0:
            self.facing = d

    def MoveInv(self):
        '''Haul inv around'''
        for item in self.inv:
            item.x = self.x
            item.y = self.y
            if item.room != self.room:
                item.room.item_list.remove(item)
                self.room.item_list.append(item)
                item.room = self.room                

    def Move(self, to, translate=False):
        '''North east south west'''
        self.display_move = True
        result = 'BLOCKED'
        has_leg = False
        for part, hp in self.body.items():
            if part.startswith('leg') and hp > 0:
                has_leg = True
                break
        if not has_leg:
            result = 'NO_LEG'
        elif self.fixedto:
            result = 'FIXED'
        elif self.paralyzed:
            result = 'WEAK'
        else:
            ##This takes (0, 1) or 'N' and gets dx, dy and facing
            if to in VECTOR:
                dx, dy = VECTOR[to]
                if not translate:
                    self.facing = to
            else:
                dx, dy = to
                if not translate:
                    if not (dx==0 and dy==0):
                        fa = VECTOR1[dx+1][dy+1]
                        if fa != 0:
                            self.facing = fa
            if self.stance != self.defaultstance:
                self.stance = self.defaultstance
                result = 'GET_UP'
            else:
                ##Room, Field
                if isinstance(self.room, Room) or isinstance(self.room, Field):
                    x1 = self.x + dx
                    y1 = self.y + dy
                    ##Within one room(or field)
                    if x1 in range(self.room.x) and y1 in range(self.room.y):
                        block = self.room.bmap[x1][y1]
                        if block == 0:
                            self.x = x1
                            self.y = y1
                            self.MoveInv()
                            result = 'CAN_PASS'
                        elif block in [1, 3]:
                            result = 'BLOCKED'
                        elif block == 2:
                            ##Enter doorway
                            self.room.item_list.remove(self)
                            for door, coordinate in self.room.portal.items():
                                m, n = coordinate
                                if x1 == m and y1 == n:
                                    if not translate:
                                        u, v = door.vectors[self.room]
                                        u = -u
                                        v = -v
                                        for d, vector in VECTOR.items():
                                            p, q = vector
                                            if u == p and v == q:
                                                self.facing = d
                                                break
                                    self.room = door
                                    self.x = 0
                                    self.y = 0
                                    self.room.item_list.append(self)
                                    self.MoveInv()
                                    result = 'CAN_PASS'
                                    break
                    ##Stuck in wall(room). Go to another Field. Go beyond the range(but still on the same field).
                    else:
                        if isinstance(self.room, Field):
                            followed = False
                            for ir in self.room.item_list:
                                if ir.attack == self and Distance(ir, self) <= 30:
                                    followed = True
                                    break
                            if followed:
                                ##Hits the edge of field when being followed
                                self.facing = random.choice(NESW)
                                result = 'CAN_PASS'
                            else:
                                sx = self.room.site.x
                                sy = self.room.site.y
                                sx1 = sx + dx
                                sy1 = sy + dy
                                newst = None
                                for st in worldmap:
                                    if sx1 == st.x and sy1 == st.y:
                                        newst = st
                                if newst is None:
                                    newst = Site(sx1, sy1)
                                self.room.item_list.remove(self)
                                self.room = newst.room_list[0]
                                if x1 < 0:
                                    x1 = 399
                                elif x1 >= self.room.x:
                                    x1 = 0
                                if y1 < 0:
                                    y1 = 399
                                elif y1 >= self.room.x:
                                    y1 = 0
                                self.x = x1
                                self.y = y1
                                self.room.item_list.append(self)
                                self.MoveInv()
                                result = 'CAN_PASS'
                        else:
                            result = 'BLOCKED'
                ##Door                        
                elif isinstance(self.room, Door):
                    for room in self.room.portal.keys():
                        m, n = room.portal[self.room]
                        m1 = m + dx
                        n1 = n + dy
                        if m1 in range(room.x) and n1 in range(room.y):
                            block = room.bmap[m1][n1]
                            if block == 0:
                                self.room.item_list.remove(self)
                                self.room = room
                                self.x = m1
                                self.y = n1
                                self.room.item_list.append(self)
                                self.MoveInv()
                                result = 'CAN_PASS'
                                break
                            elif block in [1, 2, 3]:
                                result = 'BLOCKED'
                                break
        if result in ['CAN_PASS', 'GET_UP']:
            self.time -= 10
            if result == 'GET_UP':
                self.balance = 0
                if CanSee(self, at):
                    if self.defaultstance >= 2:
                        verb = ' stands up'
                    else:
                        verb = ' gets up'
                    Message(self.Name() + verb)
        return result

    def Drift(self, to):
        '''Moving involuntarily'''
        result = 'BLOCKED'
        ##This takes (0, 1) or 'N' and gets dx, dy
        if to in VECTOR:
            dx, dy = VECTOR[to]
        else:
            dx, dy = to
        ##Room, Field
        if isinstance(self.room, Room) or isinstance(self.room, Field):
            x1 = self.x + dx
            y1 = self.y + dy
            ##Within one room(or field)
            if x1 in range(self.room.x) and y1 in range(self.room.y):
                block = self.room.bmap[x1][y1]
                if block == 0:
                    self.x = x1
                    self.y = y1
                    self.MoveInv()
                    result = 'CAN_PASS'
                elif block in [1, 3]:
                    result = 'BLOCKED'
                elif block == 2:
                    self.room.item_list.remove(self)
                    for door, coordinate in self.room.portal.items():
                        m, n = coordinate
                        if x1 == m and y1 == n:
                            u, v = door.vectors[self.room]
                            u = -u
                            v = -v
                            self.room = door
                            self.x = 0
                            self.y = 0
                            self.room.item_list.append(self)
                            self.MoveInv()
                            result = 'CAN_PASS'
                            break
            ##Stuck in wall(room). Go to another Field. Go beyond the range(but still on the same field).
            else:
                result = 'BLOCKED'
        ##Door                        
        elif isinstance(self.room, Door):
            for room in self.room.portal.keys():
                m, n = room.portal[self.room]
                m1 = m + dx
                n1 = n + dy
                if m1 in range(room.x) and n1 in range(room.y):
                    block = room.bmap[m1][n1]
                    if block == 0:
                        self.room.item_list.remove(self)
                        self.room = room
                        self.x = m1
                        self.y = n1
                        self.room.item_list.append(self)
                        self.MoveInv()
                        result = 'CAN_PASS'
                        break
                    elif block in [1, 2, 3]:
                        result = 'BLOCKED'
                        break
        return result
        

    def MoveRm(self, p, q):
        '''Move to a point(p, q) in a room'''
        ##This avoids getting stuck while moving along the wall to a door
        dx = p - self.x
        dy = q - self.y
        if dx > 1:
            dx1 = 1
        elif -1 <= dx <= 1:
            dx1 = 0
        else:
            dx1 = -1
        if dy > 1:
            dy1 = 1
        elif -1 <= dy <= 1:
            dy1 = 0
        else:
            dy1 = -1
        if max(abs(dx), abs(dy)) <= 1:
            dx1 = dx
            dy1 = dy
        m = self.x + dx1
        n = self.y + dy1
        if self.room.bmap[m][n] == 3:
            for door, coordinate in self.room.portal.items():
                u, v = coordinate
                if m == u and v == n:
                    if door.door.locked:
                        pass
                    else:
                        if self.HasPart('arm'):
                            door.bmap = [[2]]
                            for room in door.portal.keys():
                                z, w = room.portal[door]
                                room.bmap[z][w] = 2
                            if CanSee(at, self):
                                text = self.name + ' opens ' + door.door.Name()
                                Message(text)
                                Prompt(text)
                            elif CanSee(at, door.door):
                                text = door.door.Name() + ' is opened'
                                Message(text)
                                Prompt(text)
                            self.time -= 10
                    break
        else:
            self.Move((dx1, dy1))
    
    def MoveTo(self, target):
        mt = None
        onestep = None
        if CanSee(self, target):
            if self.room == target.room:
                p = target.x
                q = target.y
                mt = (p, q)
                self.tls = (p, q)
            elif self.room in target.room.portal:
                m, n = self.room.portal[target.room]
                if  m == self.x and n == self.y:
                ##Enter room when already at the door
                    onestep = self.room.vectors[target.room]
                    self.tls = (target.x, target.y)
                else:
                ##Go to the door where the target is. Target.room is the door.
                    mt = (m, n)
                    self.tls = (m, n)
        else:
            if self.tls:
                p, q = self.tls
                if self.x == p and self.y == q:
                    onestep = self.facing
                    self.tls = None
                elif 0<=p<self.room.x and 0<=q<self.room.y:
                    mt = (p, q)
                else:
                    self.tls = None
        if onestep:
            self.Move(onestep)
        elif mt:
            self.MoveRm(mt[0], mt[1])

    def Walk(self, to, translate=False):
        '''Forward backward left right'''
        result = None
        direction = FRBLtoNESW(self.facing, to)
        if self == at:
            walk = False
            if at.order:
                u, v = VECTOR[direction]
                leave = False
                if isinstance(at.room, Door):
                    for o in at.order:
                        if o.status == 'UNPAID':
                            rs = o.seller.room
                            if at.room in rs.portal:
                                p, q = rs.portal[at.room]
                                x1 = p + u
                                y1 = q + v
                                if x1<0 or x1>=rs.x or y1<0 or y1>=rs.y:
                                    leave = True
                                    break
                if leave:
                    selec = [['yes', 'y'], ['no', 'n']]
                    chosen = Menu('Do you want to leave without paying?', selec, escapable=False)
                    if chosen == 'y':
                        walk = True
                else:
                    walk = True
            else:
                walk = True
            if walk:
                result = self.Move(direction, translate=translate)
        return result

    def Disinv(self, dr):
        '''Remove from inv'''
        if isinstance(dr, Item):
            self.inv.remove(dr)
            for bgc in dr.BagContent():
                self.inv.remove(bgc)
        elif isinstance(dr, list) or isinstance(dr, tuple):
            for dr1 in dr:
                self.inv.remove(dr1)
                for bgc in dr1.BagContent():
                    self.inv.remove(bgc)

    def Entrinv(self, en):
        '''Add to inv'''
        if isinstance(en, Item):
            self.inv.append(en)
            en.x = self.x
            en.y = self.y
            for bgc in en.BagContent():
                self.inv.append(bgc)
                bgc.x = self.x
                bgc.y = self.y
        elif isinstance(en, list) or isinstance(en, tuple):
            for en1 in en:
                self.Entrinv(en1)

    def Skmod(self, skill_name):
        '''Skill modified by poison, etc'''
        if 'lead' in self.poison and 'mercury' not in self.poison:
            return 1
        else:
            return self.skill[skill_name]
        
    def Block(self, direction, attacker):
        '''Block attack from direction'''
        blocked = False
        shield = None
        can_block = False
        ##If self can block an attack from the direction or not
        for weapon, direction1 in self.blocking.items():
            if direction == direction1:
                can_block = True
                shield = weapon
                break
        if not can_block:
            for weapon in self.wield:
                if isinstance(weapon, Item) and weapon not in self.blocking.keys():
                    if weapon.tipo in SHIELD or weapon.length > 25:
                        i = self.wield.index(weapon)
                        if direction in HUMAN_BTDV[i]:
                            can_block = True
                            self.blocking[weapon] = direction
                            shield = weapon
                            break
        ##If self successfully blocks or not
        d = self.Skmod('fight')
        f = attacker.Skmod('fight')
        if can_block:
            if shield.tipo == 'shield':
            ##With shield
                if random.randint(0, 2):
                ##66% chance to block with a shield
                    blocked = True
                else:
                    if d >= f and random.randint(0, 9):
                    ##97% chance vs. equally-or-lower-skilled attacker
                        blocked = True
            else:
            ##With an ordinary weapon or a tool
                if random.randint(0, 9) == 0:
                    ##10% chance to block
                    blocked = True
                else:
                    if d >= f and random.randint(0, 9):
                    ##91% vs. equally-or-lower-skilled attacker
                        blocked = True
            if blocked and self.balance < 0 and random.randint(0, 1):
                blocked = False
            self.time -= 2

        return (blocked, shield)

    def Dodge(self, attacker):
        dodged = False
        d = self.Skmod('dodge')
        f = attacker.Skmod('fight')
        if d >= f and random.randint(0, 9):
            dodged = True
            if self.balance < 0 and random.randint(0, 1):
                dodged = False
        self.time -= 2
        return dodged

    def BreakLeg(self, part):
        global scope, autoscope
        if self.tipo in HUMANOID:
            if part.startswith('arm'):
                i = int(part[-1])
                if self.wield[i]:
                    dropped = self.wield[i]
                    self.wield[i] = None
                    self.Disinv(dropped)
                    Fall(dropped)
            elif part.startswith('leg') and self.stance == 2:
                has_leg = False
                for part1, hp1 in self.body.items():
                    if part1.startswith('leg') and hp1 > 0:
                        has_leg = True
                        break
                if not has_leg:
                    self.stance = 0
                    if CanSee(self, at) and self.fixedto is None:
                        Message(self.name + ' falls over')
            elif part in ['head', 'body']:
                if self.anim:
                    self.anim = False
                    for ics in CanSeeList(self):
                        if self in ics.watch:
                            ics.watch.remove(self)
                    self.blocking = {}
                    if scope == self:
                        scope = None
                    if autoscope == self:
                        autoscope = None
                    if self.stance > 0:
                        if CanSee(self, at) and self.fixedto is None:
                            Message(self.name + ' falls over')
                            self.stance = 0
                    if self == at:
                        Message('you die')
                    for part in self.body.keys():
                        if part.startswith('arm'):
                            i = int(part[-1])
                            if self.wield[i]:
                                dropped = self.wield[i]
                                self.wield[i] = None
                                self.Disinv(dropped)
                                Fall(dropped)

    def Hit(self, target):
        ##Assuming both self and target are humanoid
        has_attacked = False
        is_blocked = False
        has_hit = False
        both_legs = self.HasPart('legs')
        ##Turn face to target
        d0 = Direction(self, target, dn='cardinal')
        if d0 != 0:
            self.facing = d0
        ##Get attack angle (from the target's perspective)
        d = Direction(target, self, dn=8)
        ##Get all possible ways to attack, (verb, weapon, low range, high range)
        swing_list = []
        for part, hp in self.body.items():
            if hp > 0:
                if part.startswith('arm'):
                    low, high = self.sdv[part]
                    if self.stance == 1:
                        low = low // 2
                        high = high // 2
                    elif self.stance == 0:
                        low = 0
                        high = self.thick
                    i = int(part[-1])
                    if isinstance(self.wield[i], Item):
                        weapon = self.wield[i]
                        weaponl = weapon.length
                        swing_list.append(('strikes', weapon, low-weaponl, high+weaponl))
                    else:
                        swing_list.append(('punches', 'fist', low, high))
                elif part.startswith('leg') and both_legs and not self.paralyzed:
                    low, high = self.sdv[part]
                    i = int(part[-1])
                    swing_list.append(('kicks', 'leg', low, high))
        ##Get all parts that can be reached
        can_reach = []
        for part, hp in target.body.items():
            if hp > 0:
                if d in HUMAN_TDV[part]:
                    low1, high1 = target.sdv[part]
                    if target.stance == 1:
                        low1 = low1 // 2
                        high1 = high1 // 2
                    elif target.stance == 0:
                        low = 0
                        high = target.thick
                    for swing in swing_list:
                        verb, wp, low, high = swing
                        if low+high >= low1 and low1+high1 >= low:
                            dam = WeaponDam(wp, self)
                            can_reach.append((part, verb, dam))
        ##Attack by priority
        can_reach.sort(reverse=True, key=lambda part_attack: part_attack[-1])
        for part in HUMANOID_AP:
            for i in can_reach:
                if part == i[0]:
                    part, verb, dam = i
                    blocked, shield = target.Block(d, self)
                    if self.balance >= 0:
                        missed = False
                    else:
                        if random.randint(0, 1):
                            missed = True
                        else:
                            missed = False
                    if not missed:
                        if blocked:
                            if CanSee(self, at):
                                Message(self.name + ' ' + verb + ' at ' + target.name + ' but the attack is blocked by the ' + shield.name)
                            is_blocked = True
                            if verb == 'punches' and shield.tipo in WEAPONSTAB:
                                for ar, hp in self.body.items():
                                    if ar.startswith('arm'):
                                        if hp >  0:
                                            self.body[ar] -= WeaponDam(shield, target)//5
                                            if self.body[ar] <= 0:
                                                self.BreakLeg(ar)
                                            break
                            elif verb == 'kicks' and shield.tipo in WEAPONSTAB:
                                for lg, hp in self.body.items():
                                    if lg.startswith('leg'):
                                        if hp >  0:
                                            self.body[lg] -= WeaponDam(shield, target)//5
                                            if self.body[lg] <= 0:
                                                self.BreakLeg(lg)
                                            break
                        else:
                            if target.Dodge(self):
                                if CanSee(self, at):
                                    Message(self.name + ' misses ' + target.name)
                            else:
                                complete = ''
                                if part != 'body':
                                    complete += ' on ' + PartN(part)
                                if verb == 'strikes':
                                    verb = 'hits'
                                if CanSee(self, at):
                                    Message(self.name + ' ' + verb + ' ' + target.name + complete)
                                target.body[part] -= dam
                                if target.body[part] <= 0:
                                    target.BreakLeg(part)
                                has_hit = True
                    else:
                        if CanSee(self, at):
                            Message(self.name + ' misses ' + target.name)
                    has_attacked = True
                    self.time -= 10
                    break
            if has_attacked:
                break
        if is_blocked or has_hit:
            if self.thick >= target.thick * 2:
                target.balance -= 15
                if random.randint(0, 1):
                    target.balance -= 5
                    target.facing = random.choice(NESW)
                    if random.randint(0, 1):
                        if target.stance > 0:
                            if CanSee(target, at):
                                Message(target.Name() + ' is thrown to the ground')
                            target.stance = 0
                    else:
                        target.Drift(self.facing)
                        if target.stance > 0:
                            if CanSee(target, at):
                                Message(target.Name() + ' is thrown to the ground')
                            target.stance = 0
                        else:
                            if CanSee(target, at):
                                Message('the blow throws ' + target.Name() + ' away')
        return (has_attacked, is_blocked)

    def LocTar(self, target):
        if self.room == target.room:
            p = target.x
            q = target.y
            self.tls = (p, q)
        elif self.room in target.room.portal:
            m, n = self.room.portal[target.room]
            if  m == self.x and n == self.y:
            ##Look at target from doorway
                self.tls = (target.x, target.y)
            else:
            ##Go to the door where the target is. Target.room is the door.
                self.tls = (m, n)        

    def Defense(self, attacker):
        if self.shk and (self.room == self.shk or self.shk in self.room.portal):
            self.attacksp = attacker
        else:
            if not self.attack and self in self.room.site.citizen:
                self.task.append(Task('enemy alarm', attacker))
            self.attack = attacker
            self.LocTar(attacker)

    def Prepare(self):
        prepared = False
        freehand = None
        for w in item.wield:
            if w is None:
                freehand = item.wield.index(w)
            elif not isinstance(w, list) and w.tipo in WEAPON:
                prepared = True
        if not prepared and freehand is not None:
            has_weapon = False
            for w in item.inv:
                if w.tipo in WEAPON:
                    has_weapon = True
                    item.TakeOff(w)
                    item.wield[freehand] = w
                    if CanSee(at, item):
                        Message(item.Name() + ' wields ' + w.Name())
                    item.time -= 10
                    prepared = True
                    break
            if not has_weapon:
                prepared = True
        return prepared
                                    
def WeaponDam(weapon, attacker):
    '''The damage a weapon can inflict'''
    force = (attacker.thick // 20) ** 2
    if force <= 0:
        force = 1
    if weapon in ['fist', 'leg']:
        d = random.randint(0, 2) * force
    elif weapon.tipo in WEAPON:
        d = random.randint(0, 2) * force
        if weapon.tipo in WEAPONSTAB:
            d += random.randint(1, weapon.length)
        elif weapon.tipo in WEAPONBASH:
            d += random.randint(1, 5) * force
        elif weapon.tipo in WEAPONHACK:
            d += random.randint(1, weapon.cutsdeep)
    else:
        d = random.randint(0, 1) * force
    return d

def Fall(faller, fallmsg=True):
    cs = False
    if isinstance(faller, Item):
        if CanSee(faller, at):
            cs = True
            if fallmsg:
                Message(faller.name + ' falls to the ground')
        if faller.flask:
            faller.room.item_list.remove(faller)
            cur_item_list.remove(faller)
            if cs:
                Message(faller.name + ' shatters')
            for chem, quantity in faller.flask.items():
                faller.room.aoe_list.append(AOE(chem, faller.x, faller.y, faller.room, quantity))
                if cs:
                    Message('a cloud of ' + CHEMN[chem])
    elif isinstance(faller, list) or isinstance(faller, tuple):
        if faller:
            if CanSee(faller[0], at):
                cs = True
                if fallmsg:
                    tx = ''
                    for fl in faller:
                        tx += fl.Name() + ' '
                    tx = tx[:-1]
                    if len(faller) > 1:
                        Message(tx + ' fall to the ground')
                    else:
                        Message(tx + ' falls to the ground')
            for fl in faller:
                if fl.flask:
                    fl.room.item_list.remove(fl)
                    cur_item_list.remove(fl)
                    if cs:
                        Message(fl.name + ' shatters')
                    for chem, quantity in fl.flask.items():
                        fl.room.aoe_list.append(AOE(chem, fl.x, fl.y, fl.room, quantity))
                        if cs:
                            Message('a cloud of ' + CHEMN[chem])
                

def VAB(a, b):
    '''Vector from a to b'''
    if isinstance(b, Site):
    ##Vector from Site of a (which may be an item) to b (which is a Site)
        m = a.room.site.x
        n = a.room.site.y
        dx = b.x - m
        dy = b.y - n
    elif isinstance(b, tuple) or isinstance(b, list):
        bx, by = b
        dx = bx - a.x
        dy = by - a.y
    else:
    ##a and b on the same Site
        if a.room == b.room:
            dx = b.x - a.x
            dy = b.y - a.y
        elif a.room in b.room.portal:
            m, n = a.room.portal[b.room]
            p, q = b.room.portal[a.room]
            dx = (m-a.x) + (b.x-p)
            dy = (n-a.y) + (b.y-q)
        else:
            sharedoor = False
            for po in a.room.portal:
                if b.room in po.portal:
                    sharedoor = True
                    m, n = a.room.portal[po]
                    p, q = b.room.portal[po]
                    dx = (m-a.x) + (b.x-p)
                    dy = (n-a.y) + (b.y-q)
            if not sharedoor:
                dx = 999
                dy = 999
    return (dx, dy)

def Direction(a, b, dn=4):
    '''b in which direction to a, based on tangent'''
    direction = ''
    f = a.facing
    dx, dy = VAB(a, b)
    if dx == 0:
        if dy > 0:
            compass = 1
        elif dy == 0:
            compass = 0
        else:
            compass = 9
    else:
        tan = dy/dx
        if dx > 0:
            if tan > 0:
                if tan > 1:
                    compass = 2
                elif tan == 1:
                    compass = 3
                else:
                    compass = 4
            elif tan == 0:
                compass = 5
            else:
                if tan > -1:
                    compass = 6
                elif tan == -1:
                    compass = 7
                else:
                    compass = 8
        elif dx < 0:
            if tan > 0:
                if tan > 1:
                    compass = 10
                elif tan == 1:
                    compass = 11
                else:
                    compass = 12
            elif tan == 0:
                compass = 13
            else:
                if tan > -1:
                    compass = 14
                elif tan == -1:
                    compass = 15
                else:
                    compass = 16
    if dn == 'cardinal':
        d = COMPASS_CARDINAL[compass]
    else:
        if compass == 0:
            d = 'F'
        else:
            i = compass - NESW.index(f)*2
            if i <= 0:
                i += 16
            if dn == 4:
                d = COMPASS4[i]
            elif dn == 8:
                d = COMPASS8[i]
            elif dn == 16:
                d = COMPASS16[i]
    return d

def NESWtoFRBL(f, d):
    if d == 0:
        return 'F'
    else:
        i = NESW.index(d) - NESW.index(f)
        if i < 0:
            i = i + 8
        return FRBL[i]

def FRBLtoNESW(f, d):
    i = NESW.index(f) + FRBL.index(d)
    if i > 7:
        i = i - 8
    return NESW[i]

def Iscloseddoor(item):
    if item.tipo in DOOR:
        if item.room.bmap[item.x][item.y] == 3:
            return True

def Distance(a, b):
    '''Distance from a(here) to b'''
    dx, dy = VAB(a, b)
    d = max(abs(dx), abs(dy))
    if isinstance(b, Site):
        d *= 1000
    return d

def Discen(x, y):
    '''Only used in 400-400-200-200 Field'''
    p, q = (199, 199)
    radius = 100
    dx = abs(x-p)
    dy = abs(y-q)
    if dx > dy:
        if x > p:
            d = dx - radius
        else:
            d = dx - radius + 1
    else:
        if y > q:
            d = dy - radius
        else:
            d = dy - radius + 1
    return d

def DFW(item, to):
    '''Distance from walls'''
    d = 'no wall'
    if isinstance(item.room, Room):
        if to == 'N':
            d = item.room.y - 1 - item.y
        elif to == 'NE':
            d = min((item.room.x - 1 - item.x), (item.room.y - 1 - item.y))
        elif to == 'E':
            d = item.room.x - 1 - item.x
        elif to == 'SE':
            d = min((item.room.x - 1 - item.x), item.y)
        elif to == 'S':
            d = item.y
        elif to == 'SW':
            d = min(item.x, item.y)
        elif to == 'W':
            d = item.x
        elif to == 'NW':
            d = min(item.x, (item.room.y - 1 - item.y))
    elif isinstance(item.room, Door):
        for room in item.room.portal.keys():
            if isinstance(room, Room):
                m, n = room.portal[item.room]
                if to == 'N':
                    if n == room.y - 1:
                        continue
                    elif m == 0 or m == room.x - 1:
                        d = 0
                    else:
                        d = room.y
                elif to == 'NE':
                    if m == room.x - 1 or n == room.y - 1:
                        continue
                    else:
                        d = min(room.x - m, room.y - n)
                elif to == 'E':
                    if m == room.x - 1:
                        continue
                    elif n == 0 or n == room.y - 1:
                        d = 0
                    else:
                        d = room.x
                elif to == 'SE':
                    if m == room.x - 1 or n == 0:
                        continue
                    else:
                        d = min(room.x - m, n)
                elif to == 'S':
                    if n == 0:
                        continue
                    elif m == 0 or m == room.x - 1:
                        d = 0
                    else:
                        d = room.y
                elif to == 'SW':
                    if m == 0 or n == 0:
                        continue
                    else:
                        d = min(m, n)
                elif to == 'W':
                    if m == 0:
                        continue
                    elif n == 0 or n == room.y - 1:
                        d = 0
                    else:
                        d = room.x
                elif to == 'NW':
                    if m == 0 or n == room.y - 1:
                        continue
                    else:
                        d = min(m, room.y - n)
##    .....#
##    .....#
##    .@>>>#
##    .v\..+
##    .v.\.#
##    ######
    elif isinstance(item.room, Field):
        u, v = VECTOR[to]
        p = item.x
        q = item.y
        d = 0
        while True:
            d += 1
            p += u
            q += v
            if p in range(0, item.room.x) and q in range(0, item.room.y):
                if item.room.bmap[p][q] in [1, 2, 3]:
                    break
            else:
                d = 'no wall'
                break
    ##When item is next to door
    u, v = VECTOR[to]
    m = item.x + u
    n = item.y + v
    if not isinstance(item.room, Door):
        if 0 <= m < item.room.x and 0 <= n < item.room.y and item.room.bmap[m][n] in [2, 3]:
            d = 'door'
    return d

def TimeIncrement():
    r = random.randint(0, 49)
    if r == 0:
        t = 0
    elif r < 49:
        t = 1
    else:
        t = 2
    return t

def FieldVis(a, b, field):
    '''Given the town-on-field's 200-200-400-400 shape'''
    if isinstance(a, tuple) or isinstance(a, list):
        xa, ya = a
    else:
        xa = a.x
        ya = a.y
    if isinstance(b, tuple) or isinstance(b, list):
        xb, yb = b
    else:
        xb = b.x
        yb = b.y
    xmx = max(xa, xb)
    xmn = min(xa, xb)
    ymx = max(ya, yb)
    ymn = min(ya, yb)
    ymd = (ymx+ymn) // 2
    xmd = (xmx+xmn) // 2
    line0 = True
    line1 = True
    for x in range(xmn, xmx+1):
        if field.bmap[x][ya] == 1:
            line0 = False
            break
    if line0:
        for y in range(ymn, ymx+1):
            if field.bmap[xb][y] == 1:
                line0 = False
                break
    for x in range(xmn, xmx+1):
        if field.bmap[x][yb] == 1:
            line1 = False
            break
    if line1:
        for y in range(ymn, ymx+1):
            if field.bmap[xa][y] == 1:
                line1 = False
                break
    cs = False
    if line0 and line1:
        cs = True
    elif line0 or line1:
        if field.bmap[xa][ya] == 2 or field.bmap[xb][yb] == 2:
            cs = True
    if cs:
        if xmd not in [xa, xb] and ymd not in [ya, yb] and field.bmap[xmd][ymd] == 1:
            cs = False
    return cs

def CanSee(a, b):
    '''If a and b can see each other, being in bag or not is not checked'''
    cs = False
    if a.room == b.room:
        if isinstance(a.room, Field):
            cs = FieldVis(a, b, a.room)
        else:
            cs = True
    elif a.room in b.room.portal:
        if isinstance(a.room, Field):
            x, y = a.room.portal[b.room]
            cs = FieldVis(a, (x, y), a.room)
        elif isinstance(b.room, Field):
            x, y = b.room.portal[a.room]
            cs = FieldVis(b, (x, y), b.room)
        else:
            cs = True
    return cs

def CanHear(a, b):
    if Distance(a, b) <= 100:
        return True

def CanSeeList(a):
    '''A list of all items a can see'''
    list0 = copy.copy(a.room.item_list)
    for r in a.room.portal:
        list0 += r.item_list
    list1 = []
    for i in list0:
        if CanSee(a, i):
            list1.append(i)
    return list1

def CanHearList(a):
    list0 = copy.copy(a.room.item_list)
    for r in a.room.portal:
        list0 += r.item_list
        for r1 in r.portal:
            if r1 != a.room:
                list0 += r1.item_list
    list1 = []
    for i in list0:
        if CanHear(a, i):
            list1.append(i)
    return list1

def CSmL(o):
    '''A list of AOE's that may affect o'''
    list0 = copy.copy(o.room.aoe_list)
    for r in o.room.portal:
        list0 += r.aoe_list
    list1 = []
    for ao in list0:
        if CanSee(o, ao):
            list1.append(ao)
        elif Distance(o, ao) <= ao.radius:
            list1.append(ao)
    return list1

def CanHold(it, bag):
    can = False
    if (
        it.length*2//3 < bag.length
        and it.thick <= bag.thick-2
        and it.width <= bag.width-2):
        
        can = True
        if it.tipo in WEAPON and bag.tipo in SHEATH:
            for ib in bag.bag:
                if ib.tipo in WEAPON:
                    can = False

    return can

def FreeSt(rider=False):  ##rider: include items on furniture/branch/etc.
    '''Free standing visible items'''
    items = CanSeeList(at)
    to_remove = set()
    for item in items:
        for item1 in item.inv:
            to_remove.add(item1)
        for item2 in item.BagContent():
            to_remove.add(item2)
        if not rider:
            if hasattr(item, 'finvt'):
                for item3 in item.finvt:
                    to_remove.add(item3)
            if hasattr(item, 'branch'):
                for item3 in item.branch:
                    to_remove.add(item3)
            for item3 in item.bird:
                to_remove.add(item3)
    for tr in to_remove:
        items.remove(tr)
    return items

def Use():
    '''Interact with another item'''
    selec = []
    result = None
    refresh = True
    ##Write the choices
    for item in FreeSt(rider=True):        
        if item != at:
            dis = Distance(at, item)
            if dis <= 0:
                if item.tipo not in CANTPICK:
                    ##Pick up
                    text = 'pick up ' + NameSco(item)
                    for o in at.order:
                        if o.status == 'WAITING FOR PICKUP' and o.good == item:
                            text += '    BOUGHT'
                    selec.append([text, ('p', item)])
                else:
                    if item.tipo == 'bell':
                        ##Bell
                        selec.append(['pull bell string', ('pbs', item)])
                    elif item.tipo == 'branch' and 'banyan' in item.name:
                        if item.looped:
                            selec.append(['untie banyan vine loop', ('utbnlp', item)])
                            if not item.bird:
                                selec.append(['put banyan vine loop around neck', ('hang', item)])
                        else:
                            selec.append(['tie banyan vine into a loop', ('bnlp', item)])
            elif dis <= 1:
                if item.tipo == 'glisten':
                    haspick = False
                    for w in at.wield:
                        if isinstance(w, Item) and w.tipo == 'pickaxe':
                            haspick = w
                            break
                    if haspick:
                        d = NESWtoFRBL(at.facing, Direction(at, item, dn='cardinal'))
                        selec.append(['mine     ' + d, ('mine', (item, w))])
            ##Trade
            if at.speaking <= 0 and item.shk:
                d = '    ' + NESWtoFRBL(at.facing, Direction(at, item, dn='cardinal'))
                selec.append(['trade with ' + item.name + d, ('t', item)])
                refresh = False
    ##Open or close door
    if isinstance(at.room, Room) or isinstance(at.room, Field):
        for door, coordinate in at.room.portal.items():
            m, n = coordinate
            if abs(m - at.x) <= 1 and abs(n - at.y) <= 1:
                ##To differentiate doors when multiple are adjacent to @
                door_furn = door.item_list[0]
                d = NESWtoFRBL(at.facing, Direction(at, door_furn, dn='cardinal'))
                if at.room.bmap[m][n] == 3:
                    selec.append(['open ' + door.doortype + '     ' + d, ('o', door)])
                else:
                    selec.append(['close ' + door.doortype + '     ' + d, ('c', door)])
                if door.door.locked:
                    for i in at.inv:
                        if i.tipo == 'key':
                            selec.append(['unlock ' + door.doortype + '     ' + d, ('k', door)])
                    selec.append(['smash ' + door.door.lock + '     ' + d, ('s', door)])
    ##Open a menu and let @ choose
    if selec:
        chosen = Menu('?', selec, refresh=False, multismall=True, fnote=PMMC)
        if chosen:
            ##Execute the chosen action
            if isinstance(chosen[0], str):
                action, obj = chosen
                ##Pick
                if action == 'p':
                    has_hand = False
                    free_hand = False
                    for part, hp in at.body.items():
                        if part.startswith('arm') and hp > 0:
                            has_hand = True
                            i = int(part[-1])
                            if at.wield[i] is None:
                                free_hand = True
                                at.inv.append(obj)
                                at.MoveInv()
                                at.wield[i] = obj
                                for j in obj.BagContent():
                                    at.inv.append(j)
                                for f in obj.room.item_list:
                                    if hasattr(f, 'finvt'):
                                        if obj in f.finvt:
                                            f.finvt.remove(obj)
                                Message(at.Name() + ' picks up ' + obj.Name())
                                result = ('p', obj)
                                at.time -= 15
                                if obj.owner and CanSee(obj.owner, at):
                                    obj.owner.task.append(Task('theft alarm', at))
                                    obj.owner.attacksp = at
                                    for ts in obj.owner.task:
                                        if ts.name == 'shop guard':
                                            ts.detail.append(at)
                                            break
                                break
                    if not has_hand:
                        Message('you have no hand')
                    elif not free_hand:
                        Message('your hands are full')
                ##Bell
                elif action == 'pbs':
                    if at.HasPart('arm'):
                        text = at.Name() + ' pulls the string'
                        Message(text)
                        Prompt(text, refresh=False)
                        text = 'ding ding ding'
                        Message(text)
                        Prompt(text)
                        at.time -= 10
                    else:
                        Message('you have no hand')
                elif action == 'bnlp':
                    if at.HasPart('arm'):
                        Message(at.Name() + ' ties banyan vine into a loop')
                        obj.looped = True
                        at.time -= 10
                    else:
                        Message('you have no hand')
                elif action == 'utbnlp':
                    if at.HasPart('arm'):
                        Message(at.Name() + ' unties banyan vine loop')
                        obj.looped = False
                        at.time -= 10
                        for bd in obj.bird:
                            if bd.fixedto == obj:
                                bd.fixedto = None
                                Message(bd.Name() + ' falls down')
                                if bd.suffocate is not None:
                                    bd.suffocate = None
                        obj.bird = []
                    else:
                        Message('you have no hand')
                elif action == 'hang':
                    tx = at.Name() + ' puts banyan vine around neck'
                    Message(tx)
                    Prompt(tx, refresh=False)
                    obj.bird.append(at)
                    at.fixedto = obj
                    Prompt('banyan vine loop tightens!')
                    at.suffocate = turn
                    at.time -= 10
                elif action == 'mine':
                    ore, ax = obj
                    Message('DING')
                    Message(at.Name() + ' swings ' + ax.Name())
                    if random.randint(0, 1):
                        ore.minecounter -= 1
                        if ore.minecounter <= 0:
                            Message('diamond!')
                            diax, diay, diar = WallSpill(ore.x, ore.y, ore.room)
                            diamond = Item('diamond', diax, diay, diar)
                            cur_item_list.append(diamond)
                            ore.room.item_list.remove(ore)
                            if autoscope == ore:
                                autoscope == None
                            cur_item_list.remove(ore)                            
                    at.time -= 10
                ##Another menu for trading
                elif action == 't':
                    if at in [obj.attack, obj.attacksp]:
                        Prompt('the shopkeeper is hostile to you')
                    else:
                        selec = []
                        for item in obj.stock:
                            ordered = False
                            for o in obj.order:
                                if o.good == item:
                                    ordered = True
                                    break
                            if not ordered:
                                estmtxt = 'about ' + str(Coins(TEMPLATE[item.tipo]['pr'])) + ' gold    '
                                selec.append([estmtxt + NameSco(item), item])
                        if selec:
                            chosen = Menu('ask the price of', selec, refresh=False)
                            if chosen:
                                item = chosen
                                at.Say('how much is ' + NameSco(chosen) + '?', prompt=True, pr=False)
                                obj.task.append(Task('price', [item, at]))
                        else:
                            obj.task.append(Task('out of stock', None))
                ##Open or close door, or smash lock
                elif action == 'o':
                    if at.HasPart('arm'):
                        if obj.door.locked:
                            Message(obj.door.Name() + ' is locked')
                        else:
                            Message(at.Name() + ' opens ' + obj.door.Name())
                            obj.bmap = [[2]]
                            for room in obj.portal.keys():
                                u, v = room.portal[obj]
                                room.bmap[u][v] = 2
                            result = ('o', obj)
                        at.time -= 10
                        if obj.doortype == 'gate':
                            for ics in CanSeeList(obj.door):
                                if ics.tipo.startswith('guard') and ics.attack != at:
                                    ics.task.append(Task('donttouchgate', at))
                                    ics.attack = at
                                    break
                    else:
                        Message('you have no hand')
                elif action == 'c':
                    if at.HasPart('arm'):                
                        if obj.doortype == 'gate':
                            for ics in CanSeeList(obj.door):
                                if ics.tipo.startswith('guard') and ics.attack != at:
                                    ics.task.append(Task('donttouchgate', at))
                                    ics.task.append(Task('opengate', obj))
                                    ics.attack = at
                                    break
                        if len(obj.item_list) > 1:
                            Message('something is in the way')
                        else:
                            Message(at.Name() + ' closes ' + obj.door.Name())
                            obj.bmap = [[3]]
                            for room in obj.portal.keys():
                                u, v = room.portal[obj]
                                room.bmap[u][v] = 3
                            result = ('c', obj)
                        at.time -= 10
                    else:
                        Message('you have no hand')
                elif action == 'k':
                    if at.HasPart('arm'):
                        selec = []
                        for i in at.inv:
                            if i.tipo == 'key':
                                selec.append(['unlock ' + obj.door.Name() + ' with ' + NameSco(i), i])
                                if selec:
                                    chosen = Menu('?', selec)
                                    if chosen:
                                        if hasattr(chosen, 'key_to') and chosen.key_to == door:
                                            Message(at.Name() + ' unlocks ' + obj.door.Name() + ' with ' + NameSco(i))
                                            obj.door.locked = False
                                        else:
                                            Message('wrong key')
                                        at.time -= 10                                    
                    else:
                        Message('you have no hand')
                elif action == 's':
                    if at.HasPart('arm'):
                        Message('CLANG')
        ##                Message(obj.door.lock + ' shatters')
        ##                obj.door.lock = None
        ##                obj.door.locked = False
                        at.time -= 10
                    else:
                        Message('you have no hand')
                
            elif isinstance(chosen[0], tuple):
                has_hand = False
                free_hand = False
                for part, hp in at.body.items():
                    if part.startswith('arm') and hp > 0:
                        has_hand = True
                        i = int(part[-1])
                        if at.wield[i] is None:
                            at.wield[i] = []
                            free_hand = True
                            text = ''
                            for c in chosen:
                                pick, coin = c
                                at.inv.append(coin)
                                at.MoveInv()
                                at.wield[i].append(coin)
                                text += coin.Name() + ' '
                            Message(at.Name() + ' picks up ' + text)
                            at.time -= 15
                            break
                if not has_hand:
                    Message('you have no hand')
                elif not free_hand:
                    Message('your hands are full')                    
    if result:
        result = (at, result)
    return result

def CheckChem():
    ef0 = copy.copy(at.epoi)
    ef1 = []
    if 'lead' in at.poison and 'mercury' not in at.poison:
        ef1.append('heavy')
    if 'heavy' in ef0 and 'heavy' not in ef1:
        Message('you feel free')
    elif 'heavy' not in ef0 and 'heavy' in ef1:
        Message('you feel heavy')
    at.epoi = copy.copy(ef1)

def Au(g):
    '''The value of gold'''
    v = 0
    if isinstance(g, list):
        for g1 in g:
            if g1.tipo == 'gold':
                v += 100
    else:
        if g.tipo == 'gold':
            v += 100
    return v

def Transaction(buyer, seller, gold):
    for o in buyer.order:
        if o.status == 'UNPAID' and o.seller == seller:
            o.paid += Au(gold)
            if o.paid >= o.price:
                o.status = 'WAITING FOR PICKUP'
                seller.stock.remove(o.good)
                o.good.owner = None
            break

def Give():
    has_given = False
    refused = False
    selec = []
    for weapon in at.wield:
        if weapon is not None:
            if isinstance(weapon, list):
                for w in weapon:
                    selec.append(['give ' + NameSco(w) + ' to...', w])
            else:
                selec.append(['give ' + NameSco(weapon) + ' to...', weapon])
    receiver = []
    for li in FreeSt():
        if li != at and li.anim and Distance(at, li) <= 1:
            receiver.append(li)
            
    if not selec:
        Message('your hands are empty')
    elif not receiver:
        Message('nobody is near you')
    else:
        chosen = Menu('?', selec, refresh=False, multismall=True, fnote=PMMC)
        if chosen:
            selec1 = []
            text = ''
            if isinstance(chosen, list):
                for c in chosen:
                    text += NameSco(c) + ' '
                text = text[:-1]
            else:
                text += NameSco(chosen)
            for r in receiver:
                selec1.append(['give ' + text + ' to ' + r.Name(), r])
            chosen1 = Menu('?', selec1)
            if chosen1:
                if chosen1.HasPart('arm'):
                    debt = False
                    for o in chosen1.order:
                        if o.buyer == at and o.seller == chosen1:
                            debt = True
                            break
                    if debt:
                        is_gold = False
                        if isinstance(chosen, list):
                            if chosen[0].tipo == 'gold':
                                is_gold = True
                        elif chosen.tipo == 'gold':
                            is_gold = True
                        if is_gold:
                            free_hand = False
                            for w in chosen1.wield:
                                if w is None:
                                    free_hand = True
                                    has_given = True
                                    i = chosen1.wield.index(w)
                                    at.Disinv(chosen)
                                    at.TakeOff(chosen)
                                    chosen1.Entrinv(chosen)
                                    chosen1.wield[i] = chosen
                                    Message(at.Name() + ' gives ' + NamePile(chosen) + ' to ' + chosen1.Name())
                                    Transaction(at, chosen1, chosen)
                                    break
                            if not free_hand:
                                Message(chosen1.Name() + ' has no free hand')
                        else:
                            refused = True
                    else:
                        refused = True
                else:
                    Message(chosen1.Name() + ' has no hand')
    if refused:
        Message(chosen1.Name() + ' ignores your offering')
        at.time -= 10
    elif has_given:
        at.time -= 10
    return has_given

def Pouch():
    storesmall = None
    for w in at.wield:
        if isinstance(w, list):
            for w1 in w:
                if w1.tipo in POUCHABLE:
                    storesmall = w1
                    break
        elif w is not None:
            if w.tipo in POUCHABLE:
                storesmall = w
                break
    if storesmall:
        pouch = []
        for ati in at.inv:
            if ati.tipo == 'pouch':
                pouch.append(ati)
        if pouch:
            for po in pouch:
                if CanHold(storesmall, po):
                    at.TakeOff(storesmall)
                    po.bag.append(storesmall)
                    Message(at.Name() + ' puts ' + storesmall.Name() + ' into ' + NameSco(po))
                    at.time -= 10
                    break
    else:
        smalls = []
        gotosmalls = []
        for ics in FreeSt(rider=True):
            if ics.tipo in POUCHABLE and ics.owner is None:
                icsd = Distance(ics, at)
                if icsd <= 0:
                    smalls.append(ics)
                else:
                    gotosmalls.append([ics, icsd])
        if smalls:
            has_hand = False
            free_hand = False
            for part, hp in at.body.items():
                if part.startswith('arm') and hp > 0:
                    has_hand = True
                    i = int(part[-1])
                    if at.wield[i] is None:
                        free_hand = True
                        at.Entrinv(smalls)
                        at.wield[i] = smalls
                        Message(at.Name() + ' picks up ' + NamePile(smalls))
                        at.time -= 15
                        break
            if not has_hand:
                Message('you have no hand')
            elif not free_hand:
                Message('your hands are full')
        elif gotosmalls:
            goto = sorted(gotosmalls, key=lambda item: item[-1])[0][0]
            at.MoveTo(goto)

def Pay():
    '''Wield gold coins'''
    if not at.HasPart('arm'):
        Message('you have no hand')
    else:
        freehand = False
        for w in at.wield:
            if w is None:
                freehand = True
                break
            elif isinstance(w, Item):
                if w.tipo == 'gold':
                    freehand = True
                    break
            elif isinstance(w, list) or isinstance(w, tuple):
                if w and w[0].tipo == 'gold':
                    freehand = True
                    break
        if not freehand:
            Message('you have no free hand')
        else:
            od = None
            near = False
            for o in at.order:
                if o.status == 'UNPAID':
                    od = o
                    if Distance(o.seller, at) <= 1:
                        near = True
                        break
            if od is None:
                Message('you have no unpaid order')
            else:
                if not near:
                    Message('there is no one nearby you can pay to')
                else:
                    coins = []
                    value = 0
                    for co in at.inv:
                        if co.tipo == 'gold':
                            coins.append(co)
                            value += 100
                            if value >= od.price - od.paid:
                                break
                    if not coins:
                        Message('you have no money')
                    else:
                        receive = None
                        for w in od.seller.wield:
                            if w is None:
                                receive = od.seller.wield.index(w)
                                break
                        if receive is None:
                            Message(od.seller.Name() + ' has no free hand')
                        else:
                            at.Disinv(coins)
                            at.TakeOff(coins)
                            od.seller.Entrinv(coins)
                            od.seller.wield[receive] = coins
                            Transaction(at, od.seller, coins)
                            Message(at.Name() + ' gives ' + NamePile(coins) + ' to ' + od.seller.Name())
                            at.time -= 10
                        
def CarryArm(a):
    armed = False
    for w in a.wield:
        if isinstance(w, Item) and w.tipo in WEAPON:
            armed = True
            if a.room.site == hill and w.tipo == 'pickaxe':
                armed = False
            if armed == True:
                break
    return armed

def BagSpace(item, depth):
    '''Indentation for inv menu'''
    selec = []
    space = '  ' * depth
    selec.append([space+item.Name(), item])
    if hasattr(item, 'bag'):
        for item1 in item.bag:
            selec += BagSpace(item1, depth+1)
    return selec            

def Inv():
    '''View inv and do things'''
    selec = []
    for item in at.wield + at.wear:
        if item:
            if isinstance(item, list):
                for i in item:
                    selec += BagSpace(i, 0)
            else:
                selec += BagSpace(item, 0)
    if selec:
        chosen = Menu('your inventory', selec, refresh=False, multismall=True, fnote=PMMC)
        if chosen:
            refresh1 = True
            free_hand = at.FreeHand()
            furnitures_f = []
            furnitures_h = []
            for f in at.room.item_list:
                if hasattr(f, 'finvt') and f.x == at.x and f.y == at.y:
                    if f.tipo in FLAT_FURN:
                        furnitures_f.append(f)
                    elif f.tipo in HOOKED_FURN and chosen.tipo in HANG:
                        furnitures_h.append(f)
            if isinstance(chosen, list) and len(chosen)>1:
                textd = 'drop '
                if free_hand is not None:
                    textw = 'wield '
                    for w in at.wield:
                        if isinstance(w, list) and chosen[0] in w:
                            textw = 'switch '
                            break
                else:
                    textw = ''
                if furnitures_f:
                    textp = 'put '
                    refresh1 = False
                else:
                    textp = ''
                if furnitures_h:
                    texth = 'hang '
                    refresh1 = False
                else:
                    texth = ''
                for c in chosen:
                    textd += c.Name() + ' '
                    if textw:
                        textw += c.Name() + ' '
                    if textp:
                        textp += c.Name() + ' '
                    if texth:
                        texth += c.Name() + ' '
                if textw.startswith('switch'):
                    textw += 'to another hand'
                if textp:
                    textp += 'onto...'
                if texth:
                    texth += 'onto...'
                selec1 = [[textd, ('dm', chosen)]]
                if textw:
                    selec1.append([textw, ('hm', chosen)])
                if textp:
                    selec1.append([textp, ('pom', chosen)])
                if texth:
                    selec1.append([textp, ('hom', chosen)])
            else:
                if isinstance(chosen, list):
                    chosen = chosen[0]
                selec1 = [['drop ' + chosen.Name(), ('d', chosen)]]
                if chosen.tipo == 'potion':
                    selec1.append(['quaff ' + chosen.name, ('q', chosen)])
                if chosen.tipo in ARMOR and chosen not in at.wear:
                    selec1.append(['put on ' + chosen.name, ('w', chosen)])
                if free_hand is not None:
                    textw = 'wield '
                    for w in at.wield:
                        if chosen == w or (isinstance(w, list) and chosen in w):
                            textw = 'switch '
                            break
                    if textw == 'wield ':
                        selec1.append([textw + chosen.Name(), ('h', chosen)])
                    else:
                        selec1.append([textw + chosen.Name() + ' to another hand', ('h', chosen)])
                put_into_these = []
                for b in at.inv:
                    if hasattr(b, 'bag'):
                        if b != chosen and chosen not in b.bag:
                            put_into_these.append(b)
                if put_into_these:
                    selec1.append(['put ' + chosen.Name() + ' into...', ('pi', chosen)])
                    refresh1 = False
                if furnitures_f:
                    selec1.append(['put ' + chosen.Name() + ' onto...', ('po', chosen)])
                    refresh1 = False
                if furnitures_h:
                    selec1.append(['hang ' + chosen.Name() + ' onto...', ('ho', chosen)])
                    refresh1 = False
            chosen1 = Menu('?', selec1, refresh=refresh1)
            if chosen1:
                verb, item = chosen1
                if verb == 'd':
                    at.inv.remove(item)
                    at.TakeOff(item)
                    for j in item.BagContent():
                        at.inv.remove(j)
                    Message(at.name + ' drops ' + item.Name())
                    at.time -= 10
                    Fall(item, fallmsg=False)
                elif verb == 'dm':
                    text = ''
                    for item1 in item:
                        text += item1.Name() + ' '
                        at.inv.remove(item1)
                        at.TakeOff(item1)
                        for j in item1.BagContent():
                            at.inv.remove(j)
                    at.time -= 10
                    Message(at.name + ' drops ' + text)
                    Fall(item, fallmsg=False)
                elif verb == 'q':
                    if at.HasPart('arm'):
                        at.inv.remove(item)
                        at.TakeOff(item)
                        item.room.item_list.remove(item)
                        cur_item_list.remove(item)
                        Message(at.name + ' quaffs ' + item.name)
                        for chem, quantity in item.flask.items():
                            at.poison.setdefault(chem, 0)
                            at.poison[chem] += quantity * 1000
                        at.time -= 15
                    else:
                        Message('you have no hand')
                elif verb == 'w':
                    if at.HasPart('arm'):
                        at.TakeOff(item)  ##Free up the hand that holds the armor
                        at.wear.append(item)
                        Message(at.name + ' puts on ' + item.name)
                        at.time -= 15
                    else:
                        Message('you have no hand')
                elif verb == 'h':
                    at.TakeOff(item)
                    at.wield[free_hand] = item
                    Message(at.name + ' wields ' + item.Name())
                    at.time -= 15
                elif verb == 'hm':
                    text = ''
                    at.wield[free_hand] = []
                    for item1 in item:
                        at.TakeOff(item1)
                        at.wield[free_hand].append(item1)
                        text += item1.Name() + ' '
                    Message(at.name + ' wields ' + text)
                    at.time -= 15
                elif verb == 'pi':
                    if at.HasPart('arm'):
                        select2 = []
                        for bag in put_into_these:
                            select2.append(['put ' + item.Name() + ' into ' + bag.name, bag])
                        if select2:
                            chosen2 = Menu('?', select2)
                            if chosen2:
                                bag = chosen2
                                if CanHold(item, bag):
                                    at.TakeOff(item)  ##Free up the hand that holds the armor
                                    bag.bag.append(item)
                                    if item.tipo in WEAPON and bag.tipo in SHEATH:
                                        Message(at.name + ' sheathes ' + item.Name())
                                    else:
                                        Message(at.name + ' puts ' + item.Name() + ' into ' + bag.name)
                                else:
                                    Message(item.Name() + ' cannot fit into ' + bag.name)
                    else:
                        Message('you have no hand')
                elif verb == 'po':
                    if at.HasPart('arm'):
                        select2 = []
                        for f in furnitures_f:
                            select2.append(['put ' + item.Name() + ' onto ' + f.name, f])
                        if select2:
                            chosen2 = Menu('?', select2)
                            if chosen2:
                                f = chosen2
                                at.TakeOff(item)
                                at.inv.remove(item)
                                f.finvt.append(item)
                                Message(at.name + ' puts ' + item.Name() + ' onto ' + f.name)
                    else:
                        Message('you have no hand')
                elif verb == 'pom':
                    if at.HasPart('arm'):
                        select2 = []
                        text = ''
                        for item1 in item:
                            text += item1.Name() + ' '
                        text = text[:-1]
                        for f in furnitures_f:
                            select2.append(['put ' + text + ' onto ' + f.name, f])
                        if select2:
                            chosen2 = Menu('?', select2)
                            if chosen2:
                                f = chosen2
                                for item1 in item:
                                    at.TakeOff(item1)
                                    at.inv.remove(item1)
                                    f.finvt.append(item1)
                                Message(at.name + ' puts ' + text + ' onto ' + f.name)
                    else:
                        Message('you have no hand')
                elif verb == 'ho':
                    if at.HasPart('arm'):
                        select2 = []
                        for f in furnitures_h:
                            select2.append(['hang ' + item.Name() + ' onto ' + f.name, f])
                        if select2:
                            chosen2 = Menu('?', select2)
                            if chosen2:
                                f = chosen2
                                at.TakeOff(item)
                                at.inv.remove(item)
                                f.finvt.append(item)
                                Message(at.name + ' hangs ' + item.Name() + ' onto ' + f.name)
                    else:
                        Message('you have no hand')
                elif verb == 'hom':
                    if at.HasPart('arm'):
                        select2 = []
                        text = ''
                        for item1 in item:
                            text += item1.Name() + ' '
                        text = text[:-1]
                        for f in furnitures_h:
                            select2.append(['hang ' + text + ' onto ' + f.name, f])
                        if select2:
                            chosen2 = Menu('?', select2)
                            if chosen2:
                                f = chosen2
                                for item1 in item:
                                    at.TakeOff(item1)
                                    at.inv.remove(item1)
                                    f.finvt.append(item1)
                                Message(at.name + ' hangs ' + text + ' onto ' + f.name)
                    else:
                        Message('you have no hand')
                        
def Hit(tab=False):
    global autoscope
    selec = []
    for item in cur_item_list:
        if Distance(at, item) <= 1 and item != at and item.anim:
            selec.append(['hit ' + item.name, item])
    if selec:
        if tab:
            target = selec[0][1]
            at.Hit(target)
            autoscope = target
            target.Defense(at)
        else:
            chosen = Menu('?', selec)
            if chosen:
                target = chosen
                at.Hit(target)
                autoscope = target
                target.Defense(at)

def Wield():
    armed = None
    freehand = None
    for w in at.wield:
        if w is None:
            freehand = at.wield.index(w)
        elif isinstance(w, Item) and w.tipo in WEAPON:
            armed = w
    if armed is None:
        if freehand is not None:
            for w in at.inv:
                if w.tipo in WEAPON and w not in at.wield:
                    at.TakeOff(w)
                    at.wield[freehand] = w
                    Message(at.Name() + ' wields ' + w.Name())
                    at.time -= 10
                    break
    else:
        for w in at.wear:
            if CanHold(armed, w):
                at.TakeOff(armed)
                w.bag.append(armed)
                Message(at.Name() + ' sheathes ' + armed.Name())
                break

def Shop():
    selec = []
    for o in at.order:
        selec.append([o.buyer.name + ' : ' + str(Coins(o.price)) + ' gold : ' + o.seller.name + ' : ' + o.good.Name() + ' ' + o.status, o])
    if selec:
        chosen = Menu('orders', selec, refresh=False)
        if chosen is not None:
            if chosen.status == 'UNPAID':
                selec1 = [['pay', 'p'], ['cancel the order', 'c']]
            else:
                selec1 = [['this order is already paid', 'ap']]
            chosen1 = Menu('?', selec1, refresh=False)
            if chosen1:
                if chosen1 == 'p':
                    Prompt('[g]ive or [p]ay gold to the shopkeeper')
                elif chosen1 == 'c':
                    at.task.append(Task('cancel order', order))
    else:
        Prompt('no active order')

def PartN(part, long_form=True):
    '''Name of body part'''
    if part.startswith('arm') or part.startswith('leg'):
        p = part[:-1]
        lr = int(part[-1])
        if long_form:
            if lr == 0:
                n = 'left ' + p
            elif lr == 1:
                n = 'right ' + p
        else:
            if lr == 0:
                n = p + 'l'
            elif lr == 1:
                n = p + 'r'
    else:
        n = part
    return n

def NamePile(i):
    n = ''
    if len(i) > 1:
        count = 0
        name = i[0].Name()
        nsth = False
        for small in i:
            if name == small.Name(): 
                count += 1
            else:
                nsth = True
                break
        n = str(count) + ' ' + name
        if count > 1:
            n += 's'
        if nsth:
            n += ' &s'
    elif len(i) > 0:
        n = i[0].Name()
    return n

def NameSco(i):
    n = ''
    if isinstance(i, Item):
        n = i.Name()
        if i.tipo in SHEATH:
            for ibg in i.bag:
                if ibg.tipo in WEAPON:
                    n += ' |hilt'
                    break
        elif i.tipo in DOOR:
            n = DoorPlate(i, True)
    elif isinstance(i, list) or isinstance(i, tuple):
        n = NamePile(i)
    return n

def Scope(target, selfscope=False):
    '''Inspect an item'''
    if selfscope:
        panel = view_pnl
        H = VIEW_HT
        W = VIEW_WD
        T = VIEW_TP
        L = VIEW_LF
    else:
        panel = view1_pnl
        H = VIEW1_HT
        W = VIEW1_WD
        T = VIEW1_TP
        L = VIEW1_LF
    tcod.console_clear(panel)
    if target is not None:
        ##Name
        if target.tipo in DOOR:
            text = target.tipo
        elif target.tipo == 'inscription':
            text = target.tipo + ' on ' + target.room.wlmat.lower()
        else:
            text = NameSco(target)
        if target.display_move:
            text += '    ' + target.dismovg
            target.display_move = False
            if target.dismovg == '>':
                target.dismovg = ' >'
            elif target.dismovg == ' >':
                target.dismovg = '> >'
            elif target.dismovg == '> >':
                target.dismovg = '  >'
            elif target.dismovg == '  >':
                target.dismovg = '>'
        text += '\n'
        ##Facing, stance, species, status, wound
        f = NESWtoFRBL(at.facing, target.facing)
        j = FRBL.index(f)
        if  target.tipo in ANIMATE:
            fac_sta = NINE[j]
            fac_sta = fac_sta[:5] + STANCE_GLYPH[target.stance] + fac_sta[6:]
            if target.tipo in HUMAN:
                species = target.gender
            else:
                species = target.tipo
            status = ''
            if 'heavy' in target.epoi:
                status = 'heavy'
            wound = ''
            for part, hp in target.body.items():
                if hp <= 0:
                    wound += PartN(part, False) + ' x\n'
                elif hp < target.maxhp[part]:
                    wound += PartN(part, False) + ' -\n'
            text += fac_sta + '\n\n' + species + '\n\n' + status + '\n\n' + wound
            if target == at and target.balance < 0:
                text += '\nU'
        ##Print name, facing, wound
        tcod.console_print_ex(
            panel, 1, 1,
            tcod.BKGND_NONE, tcod.LEFT,
            text)
        ##Equipment
        if target.tipo in HUMANOID:
            w0, w1 = target.wield
            p, q = SCOCEN
            m = SCOGRIDWD
            n = SCOGRIDHT
            if w0:
                j0 = j - 1
                u0, v0 = VECTORF[FRBL[j0]]
                m0 = m*u0
                n0 = -n*v0
                tcod.console_print_ex(
                    panel, p+m0, q+n0,
                    tcod.BKGND_NONE, tcod.LEFT,
                    NameSco(w0))
            if w1:
                j1 = j + 1
                if j1 > 7:
                    j1 -= 8
                u1, v1 = VECTORF[FRBL[j1]]
                m1 = m*u1
                n1 = -n*v1
                tcod.console_print_ex(
                    panel, p+m1, q+n1,
                    tcod.BKGND_NONE, tcod.LEFT,
                    NameSco(w1))
            y = q
            for armor in target.wear:
                tcod.console_print_ex(
                    panel, p, y,
                    tcod.BKGND_NONE, tcod.LEFT,
                    NameSco(armor))
                y += 1
        elif target.tipo in DOOR:
            p, q = SCOCEN
            text = DoorPlate(target)
            if target.lock:
                text += target.lock
            tcod.console_print_ex(
                panel, p, q,
                tcod.BKGND_NONE, tcod.LEFT,
                text)
        elif target.tipo == 'inscription':
            text = target.ins
            tcod.console_print_ex(
                panel, 5, H//3,
                tcod.BKGND_NONE, tcod.LEFT,
                text)
        elif hasattr(target, 'finvt') and target.finvt:
            p, q = SCOCEN
            y = q
            for i in target.finvt:
                tcod.console_print_ex(
                    panel, p, y,
                    tcod.BKGND_NONE, tcod.LEFT,
                    NameSco(i))
                y += 1
        elif target.tipo == 'tree':
            p, q = SCOCEN
            y = q
            for br in target.branch:
                tcod.console_print_ex(
                    panel, p, y,
                    tcod.BKGND_NONE, tcod.LEFT,
                    br.Name())
                y += 1
        elif target.bird:
            p, q = SCOCEN
            y = q
            for bd in target.bird:
                tcod.console_print_ex(
                    panel, p, y,
                    tcod.BKGND_NONE, tcod.LEFT,
                    bd.Name())
                y += 1
            
    tcod.console_blit(
        panel, 0, 0,
        W, H, 0,
        L, T)
    tcod.console_flush()

def PView(i, marg):
    '''Used in View()'''
    selec = []
    space = ' ' * (marg+2)
    if i.inv:
        for weapon in i.wield:
            if weapon:
                if isinstance(weapon, list):
                    for w in weapon:
                        selec.append([space + NameSco(w), w])
                else:
                    selec.append([space + NameSco(weapon), weapon])
        for armor in i.wear:
            selec.append([space + NameSco(armor), armor])
    elif hasattr(i, 'finvt'):
        for j in i.finvt:
            selec.append([space + NameSco(j), j])
            selec += PView(j, marg+2)
    elif hasattr(i, 'branch'):
        for br in i.branch:
            selec.append([space + NameSco(br), br])
            for bd in br.bird:
                space1 = space + '  '
                selec.append([space1 + NameSco(bd), bd])
                selec += PView(bd, marg+4)
    return selec

def View():
    '''View visible items'''
    selec = []
    for i in FreeSt():
        d = Direction(at, i, dn=8)
        dis = Distance(at, i)
        text = d + ' ' + str(dis) + '    '
        ##For getting indentation when showing wielded or worn items, or items on table
        selec.append([text + NameSco(i), i])
        selec += PView(i, len(text))
    if isinstance(at.room, Field):
        if at.room.town:
            wl = Discen(at.x, at.y)
            if wl <= 1:
                wl = '///'
            d = Direction(at, (199, 199), dn='cardinal')
            d = NESWtoFRBL(at.facing, d)
            selec.append([d + ' ' + str(wl) + '    ' + at.room.wlmat, 'wall'])
    else:
        for d in ['N', 'E', 'S', 'W']:
            wl = DFW(at, d)
            if isinstance(wl, int):
                d = NESWtoFRBL(at.facing, d)
                selec.append([d + ' ' + str(wl) + '    ' + at.room.wlmat, 'wall'])
        
    if selec:
        chosen = Menu('view?', selec)
        if chosen:
            if isinstance(chosen, Item):
                item = chosen
                Scope(item)
                return item

def SetDest():
    selec = []
    for i in FreeSt():
        if i != at:
            d = Direction(at, i, dn=8)
            dis = Distance(at, i)
            text = d + ' ' + str(dis) + '    '
            ##For getting indentation when showing wielded or worn items, or items on table
            selec.append([text + NameSco(i), i])
            selec += PView(i, len(text))

    if selec:
        chosen = Menu('select destination:', selec)
        if chosen:
            if isinstance(chosen, Item):
                at.destination = chosen
            
def Autotravel():
    if at.destination is None:
        at.Move(at.facing)
    else:
        if Distance(at, at.destination) <= 0:
            at.destination = None
            at.Move(at.facing)
        else:
            at.MoveTo(at.destination)
            
##Interface
init = open('init.txt', 'r')
initlst = ['']
for lt in init.read():
    if lt == '|':
        initlst.append('')
    else:
        initlst[-1] += lt
initwd, initht, initfont = initlst

initwd = initwd[22:]
initwd = int(initwd)
initwd = max(90, initwd)
initwd = min(200, initwd)

initht = initht[23:]
initht = int(initht)
initht = max(60, initht)
initht = min(100, initht)

initfont = int(initfont[16:])
initfont = max(1, initfont)
initfont = min(3, initfont)
fontd = [
    'terminal8x8_gs_tc.png',
    'dejavu_wide12x12_gs_tc.png',
    'dejavu_wide16x16_gs_tc.png']

fontpath = fontd[initfont-1]

SCREEN_WD = initwd
SCREEN_HT = initht

MESSAGE_PNL_LF = SCREEN_WD // 2
MESSAGE_PNL_TP = 0
MESSAGE_PNL_WD = SCREEN_WD - MESSAGE_PNL_LF
MESSAGE_PNL_HT = SCREEN_HT // 2

DEBUG_PNL_LF = SCREEN_WD // 2
DEBUG_PNL_TP = 0
DEBUG_PNL_WD = SCREEN_WD // 2
DEBUG_PNL_HT = SCREEN_HT // 2

SKY_LF = 0
SKY_TP = 0
SKY_WD = SCREEN_WD // 2
SKY_HT = 3

FLOOR_WD = SCREEN_WD // 2
FLOOR_HT = 3
FLOOR_LF = 0
FLOOR_TP = SCREEN_HT - FLOOR_HT

FOUR_VIEWS_PNL_LF = 0
FOUR_VIEWS_PNL_TP = SKY_HT
FOUR_VIEWS_PNL_WD = SCREEN_WD // 2
FOUR_VIEWS_PNL_HT = SCREEN_HT - FLOOR_HT - FOUR_VIEWS_PNL_TP
SUB_V = [
    (1, 1, 'F'),
    (FOUR_VIEWS_PNL_WD // 2, 1, 'R'),
    (1, FOUR_VIEWS_PNL_HT // 2, 'L'),
    (FOUR_VIEWS_PNL_WD // 2, FOUR_VIEWS_PNL_HT // 2, 'B')]
DISPWALLWD = 8

VIEW_WD = MESSAGE_PNL_WD // 2
VIEW_HT = MESSAGE_PNL_HT
VIEW_LF = MESSAGE_PNL_LF
VIEW_TP = MESSAGE_PNL_HT
VIEW1_WD = VIEW_WD
VIEW1_HT = VIEW_HT
VIEW1_LF = MESSAGE_PNL_LF + VIEW_WD
VIEW1_TP = MESSAGE_PNL_HT
SCOGRIDWD = VIEW_WD // 3
SCOGRIDHT = VIEW_HT // 3
SCOCEN = (SCOGRIDWD+5, SCOGRIDHT+5)

font_path = fontpath
font_flags = tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD
tcod.console_set_custom_font(font_path, font_flags)
window_title = 'ASCII Adventure 2020'
fullscreen = False
tcod.console_init_root(SCREEN_WD, SCREEN_HT, window_title, fullscreen)
tcod.console_set_default_foreground(0, tcod.white)
tcod.console_set_default_background(0, tcod.grey)

four_views_pnl = tcod.console_new(FOUR_VIEWS_PNL_WD, FOUR_VIEWS_PNL_HT)
tcod.console_set_default_background(four_views_pnl, tcod.grey)
tcod.console_clear(four_views_pnl)

sky_pnl = tcod.console_new(SKY_WD, SKY_HT)
tcod.console_set_default_background(sky_pnl, tcod.grey)
tcod.console_clear(sky_pnl)

floor_pnl = tcod.console_new(FLOOR_WD, FLOOR_HT)
tcod.console_set_default_background(floor_pnl, tcod.grey)
tcod.console_clear(floor_pnl)

message_pnl = tcod.console_new(MESSAGE_PNL_WD, MESSAGE_PNL_HT)
tcod.console_set_default_background(message_pnl, tcod.grey)
tcod.console_clear(message_pnl)

debug_pnl = tcod.console_new(DEBUG_PNL_WD, DEBUG_PNL_HT)
tcod.console_set_default_background(debug_pnl, tcod.blue)
tcod.console_clear(debug_pnl)

view_pnl = tcod.console_new(VIEW_WD, VIEW_HT)
tcod.console_set_default_background(view_pnl, tcod.grey)
tcod.console_clear(view_pnl)

view1_pnl = tcod.console_new(VIEW1_WD, VIEW1_HT)
tcod.console_set_default_background(view1_pnl, tcod.grey)
tcod.console_clear(view1_pnl)

KEY_DICT = {
    '.': 'WAIT',
    'k': 'F',
    'u': 'FR',
    'l': 'R',
    'n': 'BR',
    'j': 'B',
    'b': 'BL',
    'h': 'L',
    'y': 'FL',
    'K': 'tF',
    'U': 'tFR',
    'L': 'tR',
    'N': 'tBR',
    'J': 'tB',
    'B': 'tBL',
    'H': 'tL',
    'Y': 'tFL',
    'e': 'USE',
    'i': 'INV',
    'a': 'ATTACK',
    'f': 'AUTO-ATTACK',
    'v': 'VIEW',
    'O': 'SHOP',
    'g': 'GIVE',
    'w': 'WIELD',
    'm': 'POUCH',
    'p': 'PAY',
    's': 'SETDEST',
    'd': 'AUTOTRAVEL',
    'M': 'MAP',
    '?': 'HELP',
    'ESC': 'EXIT'}

def GetCommand(DICT):
    '''Convert signal to name of key'''
    key = None
    while key not in DICT:
        pressed = tcod.console_wait_for_keypress(True)
        if pressed.vk == tcod.KEY_ESCAPE:
            key = 'ESC'
        elif pressed.vk == tcod.KEY_SPACE:
            key = 'space'
        elif pressed.vk == tcod.KEY_ENTER:
            key = 'ENT'
        elif pressed.vk == tcod.KEY_CHAR:
            key = chr(pressed.c)
            if pressed.shift:
                if key == '/':
                    key = '?'
                else:
                    key = chr(pressed.c).capitalize()
        elif pressed.vk == tcod.KEY_1:
            key = 1
        elif pressed.vk == tcod.KEY_2:
            key = 2
        elif pressed.vk == tcod.KEY_3:
            key = 3
        elif pressed.vk == tcod.KEY_4:
            key = 4
        elif pressed.vk == tcod.KEY_5:
            key = 5
        elif pressed.vk == tcod.KEY_6:
            key = 6
        elif pressed.vk == tcod.KEY_7:
            key = 7
        elif pressed.vk == tcod.KEY_8:
            key = 8
        elif pressed.vk == tcod.KEY_9:
            key = 9
    return DICT[key]

def DoorPlate(door, plain=False):
    if door.room != at.room:
        text = door.names[at.room]
    else:
        n0, n1 = door.names.values()
        if len(n0) >= len(n1):
            text = n0
        else:
            text = n1
    if text:
        text = '{ ' + text + ' }'
    else:
        if plain:
            text = door.tipo
    return text

def Glyph(item):
##Only used in FourViews()
    glyph = ''
    if isinstance(item, Item):
        if item.tipo in DOOR:
            if item.room.bmap[0][0] == 3:
                glyph = '+'
            else:
                glyph = '\''
            if item.tipo == 'door':
                glyph = '|' + glyph + '|'
            else:
                glyph = '[' + glyph + ']'
            if item.lock:
                if item.locked:
                    glyph += 'L'
                else:
                    glyph += 'l'
        elif hasattr(item, 'finvt'):
            glyph = TEMPLATE[item.tipo]['gl']
            for item1 in item.finvt:
                if item1.tipo == 'gold' and '$' in text:
                    pass
                else:
                    glyph += TEMPLATE[item1.tipo]['gl']
        else:
            glyph = TEMPLATE[item.tipo]['gl']
            if hasattr(item, 'wield'):
                for weapon in item.wield:
                    if weapon is not None:
                        if isinstance(weapon, list):
                            weapon = weapon[0]
                        glyph += TEMPLATE[weapon.tipo]['gl']
            if item.tipo in SHEATH:
                for ibg in item.bag:
                    if ibg.tipo in WEAPON:
                        glyph += '*'
                        break
            if item.tipo == 'tree':
                for br in item.branch:
                    for bd in br.bird:
                        glyph += TEMPLATE[bd.tipo]['gl']
    elif isinstance(item, AOE):
        glyph = '~ ~ ~'
    return glyph

def WMap():
    text = ''
    xmin, xmax = (0, 40)
    ymin, ymax = (0, 40)
    p, q = (20, 20)
    radius = 17
    for y in range(ymin, ymax+1):
        for x in range(xmin, xmax+1):
            if abs(x-p) <= radius and abs(y-p) <= 1:
                text += '~'
            elif abs(x-p) <= 1 and p<=y<=p+radius:
                text += '~'
            else:
                d = (abs(x-p)**2 + abs(y-q)**2)**0.5
                d = math.ceil(d)
                if abs(d-radius) <= 1:
                    text += '*'
                else:
                    text += ' '
        text += '\n'
    window = tcod.console_new(SCREEN_WD, SCREEN_HT)
    tcod.console_set_default_foreground(window, tcod.white)
    tcod.console_set_default_background(window, tcod.grey)
    tcod.console_clear(window)
    tcod.console_print_ex(
        window, 0, 0,
        tcod.BKGND_NONE, tcod.LEFT,
        text)
    for st, coordinate in wmapsite.items():
        glyph = ''
        if 'mountain' in st.name:
            glyph = 'MONT.'
        elif 'Town' in st.name:
            glyph = 'TOWN'
        x, y = coordinate
        tcod.console_print_ex(
            window, x-len(glyph)//2, y,
            tcod.BKGND_NONE, tcod.LEFT,
            glyph)
    mare = 'M~A~R~E~H~O~U~D~I~N~A~&'
    tcod.console_print_ex(
        window, p-len(mare)//2, q,
        tcod.BKGND_NONE, tcod.LEFT,
        mare)
    tcod.console_blit(
        window, 0, 0,
        SCREEN_WD, SCREEN_HT, 0,
        0, 0)
    tcod.console_flush()
    command_dict = {
        'ESC': 'exit'}
    command = GetCommand(command_dict)

def Clock():
    sec = turn // 2
    hour = sec//3600
    minute = sec%3600//60
    if hour >= 24:
        hour = 0
    return (hour, minute)

def Sun(hour):
    if hour <= 11:
        d = 'E'
    elif hour <= 13:
        d = 0
    else:
        d = 'W'
    return d

def Moon(hour):
    if hour <= 1:
        d = 0
    elif 1 < hour <= 12:
        d = 'W'
    elif 12 < hour < 23:
        d = 'E'
    else:
        d = 0
    return d

SKYFRBL = {
    'F': (-2, -1),
    'FR': (-1, -1),   
    'R': (2, -1),
    'BR': (2, 0),
    'B': (2, 1),
    'BL': (1, 1),
    'L': (-2, 1),
    'FL': (-2, 0)}

MOONPH = ['NO', 'NEW', 'HALF', 'FULL']

def Sky():
    ##Sky
    tcod.console_clear(sky_pnl)
    if (isinstance(at.room, Room) or isinstance(at.room, Door)) and at.room.ceiling:        
        text = 'CEILING'
    else:
        ho, mi = Clock()
        sun = False
        moon = False
        if 6 <= ho <= 18:
            if cloud <= 0:
                weather = 'BLUE SKY'
                sun = True
            elif cloud <= 1:
                weather = 'SOME CLOUDS'
                sun = True
            else:
                weather = 'CLOUDY'
        else:
            if cloud <= 0:
                weather = 'STARRY SKY'
                moon = True
            elif cloud <= 1:
                weather = 'SOME NIGHT CLOUDS'
                moon = True
            else:
                weather = 'GLOOMY NIGHT SKY'
        text = weather
    p, q = (SKY_WD//2, SKY_HT//2)
    txtlen = len(text)
    xw = p - txtlen
    tcod.console_print_ex(
        sky_pnl, xw, q,
        tcod.BKGND_NONE, tcod.LEFT,
        text)
    if not at.room.ceiling:
        cele = ''
        if sun:
            ds = Sun(ho)
            cele = 'SUN'
        elif moonph > 0 and moon:
            ds = Moon(ho)
            cele = MOONPH[moonph] + ' MOON'
        if cele:
            if ds == 0:
                xs = p - txtlen//2 - 2
                ys = 0
            else:
                ds1 = NESWtoFRBL(at.facing, ds)
                u, v = SKYFRBL[ds1]
                xs = (xw+p)//2 + txtlen//2*u
                if u < 0:
                    xs -= len(cele)
                ys = q + v
            tcod.console_print_ex(
                sky_pnl, xs, ys,
                tcod.BKGND_NONE, tcod.LEFT,
                cele)
    tcod.console_blit(
        sky_pnl, 0, 0,
        SKY_WD, SKY_HT, 0,
        SKY_LF, SKY_TP)
    ##Floor
    tcod.console_clear(floor_pnl)
    text = at.room.flomat
    txtlen = len(text)
    tcod.console_print_ex(
        floor_pnl, FLOOR_WD//2-txtlen//2-4, FLOOR_HT//2,
        tcod.BKGND_NONE, tcod.LEFT,
        text)
    tcod.console_blit(
        floor_pnl, 0, 0,
        FLOOR_WD, FLOOR_HT, 0,
        FLOOR_LF, FLOOR_TP)
    tcod.console_flush()

def XMa(dis):
    '''Only used in FourViews()'''
    if dis <= 5:
        marg = dis
    else:
        marg = dis//10 + 6
    return marg

def Disdrtx(dis, dr):
    '''Only used in FourViews()'''
    if dr == 'F':
        dis = dis + '*'
    elif dr == 'FRF':
        dis = dis + '^'
    elif dr == 'FR':
        dis = dis + '^'
    elif dr == 'FRR':
        dis = dis + '^'
    elif dr == 'R':
        dis = dis + '-'
    elif dr == 'BRR':
        dis = dis + '_'
    elif dr == 'BR':
        dis = dis + '_'
    elif dr == 'BRB':
        dis = dis + '_'
    elif dr == 'B':
        dis = dis + '.'
    elif dr == 'BLB':
        dis = '_' + dis
    elif dr == 'BL':
        dis = '_' + dis
    elif dr == 'BLL':
        dis = '_' + dis
    elif dr == 'L':
        dis = '-' + dis
    elif dr == 'FLL':
        dis = '^' + dis
    elif dr == 'FL':
        dis = '^' + dis
    elif dr == 'FLF':
        dis = '^' + dis

    return dis

def Elem0(pile):
    e = None
    if isinstance(pile, list) or isinstance(pile, tuple):
        if pile:
            e = pile[0]
    else:
        e = pile

    return e

def FourViews():
    global scope, autoscope
    tcod.console_clear(four_views_pnl)

    ##Items
    item_distance_dict = {}
    piles = {}
    for i in FreeSt():
        if i != at:
            idis = Distance(at, i)
            if i.tipo in SMALL:
                if idis in piles:
                    piles[idis].append(i)
                else:
                    piles[idis] = [i]
            else:
                item_distance_dict[i] = Distance(at, i)
    for dis, pile in piles.items():
        item_distance_dict[tuple(pile)] = dis
    for aoe in CSmL(at):
        d = Distance(aoe, at)
        d -= aoe.radius
        if d < 0:
            d = 0
        item_distance_dict[aoe] = d
    direction_item_dict = {
        'F': [],
        'R': [],
        'L': [],
        'B': []}
    ##Sort items by distance from @
    for i in sorted(item_distance_dict.items(), key=lambda item: item[1]):
        drc = Direction(at, Elem0(i[0]))
        direction_item_dict[drc].append(i[0])
    ##Sites
    site_distance_dict = {}
    for site in worldmap:
        if site != at.room.site and site.name is not None:
            site_distance_dict[site] = Distance(at, site)
    direction_site_dict = {
        'F': [],
        'R': [],
        'L': [],
        'B': []}
    ##Sort sites by distance from @
    for i in sorted(site_distance_dict.items(), key=lambda item: item[1]):
        direction_site_dict[Direction(at, i[0])].append(i[0])
    ##Print the four views
    p, q = (FOUR_VIEWS_PNL_WD//2, FOUR_VIEWS_PNL_HT//2)
    pxmarg = FOUR_VIEWS_PNL_WD // 40
    pymarg = FOUR_VIEWS_PNL_HT // 20
    ystep = 3
    crowded = False
    for d, lst in direction_item_dict.items():
        if len(lst) > FOUR_VIEWS_PNL_HT // 10:
            crowded = True
            pxmarg = FOUR_VIEWS_PNL_WD // 80
            pymarg = FOUR_VIEWS_PNL_HT // 40
            ystep = 2
            break
    for d in CARDINAL4:
        x = p
        y = q
        y1 = q
        x1 = p
        ##Door frame
        doorframe = False
        halfwall = False
        if isinstance(at.room, Door):
            u, v = VECTOR[at.facing]
            u1, v1 = list(at.room.vectors.values())[0]
            if u*u1 + v*v1 == 0:
            ##Right angle
                if d in ['F', 'B']:
                    doorframe = True
            elif (u==u1 and v==v1) or (u==u1 and v+v1==0) or (u+u1==0 and v==v1):
            ##Parallel
                if d in ['R', 'L']:
                    doorframe = True
            else:
                if d in ['R', 'L']:
                    doorframe = True
                    halfwall = True
                
            if doorframe:
                wallwd = DISPWALLWD
                if halfwall:
                    wallwd = wallwd // 2
                textw = ('/'*wallwd+'\n')*2 + '\n'
                xmarg = pxmarg
                ymarg = pymarg
                xmarg = max(1, xmarg)
                ymarg = max(1, ymarg)
                if d == 'F':
                    tcod.console_print_ex(
                        four_views_pnl, p-wallwd-xmarg, y-ymarg,
                        tcod.BKGND_NONE, tcod.LEFT,
                        textw)
                    y1 = y-ymarg
                elif d == 'R':
                    tcod.console_print_ex(
                        four_views_pnl, p+xmarg, y-ymarg,
                        tcod.BKGND_NONE, tcod.LEFT,
                        textw)
                    y1 = y-ymarg
                elif d == 'B':
                    tcod.console_print_ex(
                        four_views_pnl, p+xmarg, y+ymarg,
                        tcod.BKGND_NONE, tcod.LEFT,
                        textw)
                    y1 = y+ymarg
                else:
                    tcod.console_print_ex(
                        four_views_pnl, p-wallwd-xmarg, y+ymarg,
                        tcod.BKGND_NONE, tcod.LEFT,
                        textw)
                    y1 = y+ymarg
        ##Items
        y = y1
        for i in direction_item_dict[d]:
            dis = item_distance_dict[i]
            if isinstance(i, Item) and i.tipo in DOOR+MURAL and dis == 1:
                distx = '///'
            else:
                distx = str(dis)
            idr = Elem0(i)
            dr = Direction(at, idr, dn=16)
            distx = Disdrtx(distx, dr)

            xmarg = XMa(dis)
            xmarg += pxmarg
            if xmarg >= FOUR_VIEWS_PNL_WD // 4:
                xmarg = FOUR_VIEWS_PNL_WD // 4
            if not crowded:
                if dis > 10:
                    ymarg = FOUR_VIEWS_PNL_HT // 6
                elif dis > 5:
                    ymarg = FOUR_VIEWS_PNL_HT // 12
                else:
                    ymarg = pymarg
            else:
                ymarg = pymarg
            xmarg = max(1, xmarg)
            ymarg = max(1, ymarg)

            if isinstance(i, tuple):
                nm = NamePile(i)
                gl = Glyph(i[0])
            else:
                if i.tipo in DOOR:
                    nm = DoorPlate(i, True)
                else:
                    nm = i.Name()
                gl = Glyph(i)
            if dis <= 1:
                sp = ' ' * 2
            else:
                sp = ' ' * 4
            if isinstance(i, Item) and i.tipo in ANIMATE:
                st = STANCE_GLYPH[i.stance]
            else:
                st = ''            

            if d == 'F':
                tx = st + ' ' + nm + '  ' + distx + sp + gl
                tcod.console_print_ex(
                    four_views_pnl, p-len(tx)-xmarg, y-ymarg,
                    tcod.BKGND_NONE, tcod.LEFT,
                    tx)
                y -= ystep
                y1 = y-ymarg
                x1 = p-xmarg
            elif d == 'R':
                tx = gl + sp + distx + '  ' + nm + ' ' + st
                tcod.console_print_ex(
                    four_views_pnl, p+xmarg, y-ymarg,
                    tcod.BKGND_NONE, tcod.LEFT,
                    tx)
                y -= ystep
                y1 = y-ymarg
                x1 = p+xmarg
            elif d == 'B':
                tx = gl + sp + distx + '  ' + nm + ' ' + st
                tcod.console_print_ex(
                    four_views_pnl, p+xmarg, y+ymarg,
                    tcod.BKGND_NONE, tcod.LEFT,
                    tx)
                y += ystep
                y1 = y+ymarg
                x1 = p+xmarg
            else:
                tx = st + ' ' + nm + '  ' + distx + sp + gl
                tcod.console_print_ex(
                    four_views_pnl, p-len(tx)-xmarg, y+ymarg,
                    tcod.BKGND_NONE, tcod.LEFT,
                    tx)
                y += ystep
                y1 = y+ymarg
                x1 = p-xmarg
        ##Wall
        dfw = None
        if not doorframe:
            textw = ''
            to = FRBLtoNESW(at.facing, d)
            dfw = DFW(at, to)
            if isinstance(dfw, int):
                wallwd = DISPWALLWD - dfw//2
                if wallwd < 2:
                    wallwd = 2
            else:
                if dfw == 'no wall' and isinstance(at.room, Field) and at.room.town:
                    ##..^##
                    ##..^##
                    ##<<@>>
                    ##..v..
                    cx, cy = (199, 199)
                    if d == Direction(at, (cx, cy)):
                        dfw = Discen(at.x, at.y)
                        wallwd = DISPWALLWD // 2  ##Corner wall is half wall
            if isinstance(dfw, int):
                if dfw > 10:
                    wall = '-'*wallwd+'\n'
                elif dfw > 1:
                    wall = ('-'*wallwd+'\n') * 2
                else:
                    wall = ('/'*wallwd+'\n') * 2
                textw += wall + '\n'
                if dfw > 1:
                    textw += str(dfw) + '\n'
                        
                xmarg = XMa(dfw)
                xmarg += pxmarg
                if xmarg >= FOUR_VIEWS_PNL_WD // 2:
                    xmarg = FOUR_VIEWS_PNL_WD // 2
                xmarg = max(1, xmarg)
                if abs(x1-p) >= xmarg:
                    x = x1
                    xmarg = 8
                if not crowded:
                    if dfw > 10:
                        ymarg = FOUR_VIEWS_PNL_HT // 6
                    elif dfw > 5:
                        ymarg = FOUR_VIEWS_PNL_HT // 12
                    else:
                        ymarg = pymarg
                else:
                    ymarg = pymarg
                ymarg = max(1, ymarg)
                if abs(y1-q) > ymarg:
                    ymarg = 3
                    y = y1

                if d == 'F':
                    tcod.console_print_ex(
                        four_views_pnl, x-wallwd-xmarg, y-ymarg,
                        tcod.BKGND_NONE, tcod.LEFT,
                        textw)
                    y1 = y-ymarg
                elif d == 'R':
                    tcod.console_print_ex(
                        four_views_pnl, x+xmarg, y-ymarg,
                        tcod.BKGND_NONE, tcod.LEFT,
                        textw)
                    y1 = y-ymarg
                elif d == 'B':
                    tcod.console_print_ex(
                        four_views_pnl, x+xmarg, y+ymarg,
                        tcod.BKGND_NONE, tcod.LEFT,
                        textw)
                    y1 = y+ymarg
                else:
                    tcod.console_print_ex(
                        four_views_pnl, x-wallwd-xmarg, y+ymarg,
                        tcod.BKGND_NONE, tcod.LEFT,
                        textw)
                    y1 = y+ymarg
        ## Distant landmarks
        if not at.room.ceiling and direction_site_dict[d]:
            xmarg = FOUR_VIEWS_PNL_WD // 6 + 8
            if abs(y1-q) <= FOUR_VIEWS_PNL_HT // 4:
                ymarg = FOUR_VIEWS_PNL_HT//4 + 4
                y = q
            else:
                ymarg = 4
                y = y1
            for i in direction_site_dict[d]:
                cansee = True
                if isinstance(dfw, int):
                    if at.room.site.wallht * 20 >= i.tipht:
                        cansee = False
                if cansee:
                    tx = i.name
                    if d == 'F':
                        tcod.console_print_ex(
                            four_views_pnl, p-len(tx)-xmarg, y-ymarg,
                            tcod.BKGND_NONE, tcod.LEFT,
                            tx + '  ^')
                        y -= ystep
                    elif d == 'R':
                        tcod.console_print_ex(
                            four_views_pnl, p+xmarg, y-ymarg,
                            tcod.BKGND_NONE, tcod.LEFT,
                            '^  ' + tx)
                        y -= ystep
                    elif d == 'B':
                        tcod.console_print_ex(
                            four_views_pnl, p+xmarg, y+ymarg,
                            tcod.BKGND_NONE, tcod.LEFT,
                            '^  ' + tx)
                        y += ystep
                    else:
                        tcod.console_print_ex(
                            four_views_pnl, p-len(tx)-xmarg, y+ymarg,
                            tcod.BKGND_NONE, tcod.LEFT,
                            tx + '  ^')
                        y += ystep
        
    tcod.console_blit(
        four_views_pnl, 0, 0,
        FOUR_VIEWS_PNL_WD, FOUR_VIEWS_PNL_HT, 0,
        FOUR_VIEWS_PNL_LF, FOUR_VIEWS_PNL_TP)
    tcod.console_flush()

    if scope and CanSee(at, scope):
        Scope(scope)
        scope = None
    else:
        scope = None
        nearest = None
        item_distance_dict = {}
        for i in FreeSt(rider=True):
            if i != at:
                item_distance_dict[i] = Distance(at, i)
        for item, distance in sorted(item_distance_dict.items(), key=lambda item: item[1]):
            if item.tipo in ANIMATE:
                nearest = item
                break
        if autoscope and nearest:
            dau = Distance(at, autoscope)
            dne = Distance(at, nearest)
            if dau <= 1 or dau <= dne:
                Scope(autoscope)
            else:
                autoscope = None
                Scope(nearest)
        elif autoscope:
            if CanSee(at, autoscope):
                Scope(autoscope)
            else:
                autoscope = None
                Scope(None)
        elif nearest:
            Scope(nearest)
        else:
            Scope(None)

    Scope(at, True)

def Message(text):
    global message_x, messagebuffer
    buffered = False
    if message_x > MESSAGE_PNL_HT - 1:
        buffered = True
        text = messagebuffer + text
        messagebuffer = ''
        message_x = 0
        tcod.console_clear(message_pnl)
    elif message_x > MESSAGE_PNL_HT - 9:
        messagebuffer += text + '\n\n'
    tcod.console_print_ex(
        message_pnl, 1, message_x + 1,
        tcod.BKGND_NONE, tcod.LEFT,
        text)
##    print(text)
    tcod.console_blit(
        message_pnl, 0, 0,
        MESSAGE_PNL_WD, MESSAGE_PNL_HT, 0,
        MESSAGE_PNL_LF, MESSAGE_PNL_TP)
    tcod.console_flush()
    if buffered:
        message_x = 10
    else:
        message_x += 2

def Prompt(content, refresh=True):
    wd = SCREEN_WD // 2
    ht = SCREEN_HT
    window = tcod.console_new(wd, ht)
    tcod.console_set_default_foreground(window, tcod.white)
    tcod.console_set_default_background(window, tcod.grey)
    tcod.console_clear(window)
    x = wd//2 - len(content)//2
    y = ht//2
    content += '\n'*10 + '  press SPACE to continue'
    tcod.console_print_ex(
        window, x, y,
        tcod.BKGND_NONE, tcod.LEFT,
        content)
    tcod.console_blit(
        window, 0, 0,
        SCREEN_WD, SCREEN_HT, 0,
        0, 0)
    tcod.console_flush()

    while True:
        command = GetCommand({'space': 'continue'})
        if command == 'continue':
            break
    if refresh:
        tcod.console_blit(
            sky_pnl, 0, 0,
            SKY_WD, SKY_HT, 0,
            SKY_LF, SKY_TP)
        tcod.console_blit(
            four_views_pnl, 0, 0,
            FOUR_VIEWS_PNL_WD, FOUR_VIEWS_PNL_HT, 0,
            FOUR_VIEWS_PNL_LF, FOUR_VIEWS_PNL_TP)
        tcod.console_blit(
            floor_pnl, 0, 0,
            FLOOR_WD, FLOOR_HT, 0,
            FLOOR_LF, FLOOR_TP)
        tcod.console_flush()

PMMC = '''Press 'm' to select multiple coins'''

def Menu(title, items, escapable=True, refresh=True, multismall=False, fnote=None):
    if items:
        window = tcod.console_new(SCREEN_WD//2, SCREEN_HT)
        tcod.console_set_default_foreground(window, tcod.white)
        tcod.console_set_default_background(window, tcod.grey)
        tcod.console_clear(window)
        tcod.console_print_ex(
            window, 0, 0,
            tcod.BKGND_NONE, tcod.LEFT,
            ' ' + title)
        number = 1
        entries = []
        for item in items:
            entries.append(item[0])
            number += 1            
        y = 2
        ## Print choices
        for entry in entries:
            tcod.console_print_ex(
                window, 4, y,
                tcod.BKGND_NONE, tcod.LEFT,
                entry)
            y += 1
        if fnote:
            tcod.console_print_ex(
                window, 3, SCREEN_HT-3,
                tcod.BKGND_NONE, tcod.LEFT,
                fnote)
        ## Print cursor '>'
        cursor = 0
        tcod.console_print_ex(
            window, 1, cursor + 2,
            tcod.BKGND_NONE, tcod.LEFT,
            '>')
        tcod.console_blit(
            window, 0, 0,
            SCREEN_WD, SCREEN_HT, 0,
            0, 0)
        tcod.console_flush()
        if multismall:
            chosen = []
            marked = []
        else:
            chosen = None
        ## Let cursor go up and down and to and fro
        while True:
            cursor0 = cursor
            command_dict = {
                'j': -1,
                'k': 1,
                'ENT': 'enter',
                'ESC': 'exit'}
            if multismall:
                command_dict['m'] = 'mark'
            command = GetCommand(command_dict)
            if command == 'enter':
                if multismall and marked:
                    for n in marked:
                        chosen.append(items[n][1])
                else:
                    chosen = items[cursor][1]
                break
            elif command == 'exit':
                if escapable:
                    break
                else:
                    continue
            elif command == 'mark':
                if cursor not in marked:
                    if len(marked) <= 10:
                        small = items[cursor][1]
                        if isinstance(small, Item):
                            if small.tipo in SMALL:
                                marked.append(cursor)
                        elif isinstance(small, tuple):
                            small_1 = small[1]
                            if isinstance(small_1, Item) and small_1.tipo in SMALL:
                                marked.append(cursor)
                else:
                    marked.remove(cursor)
                for n in range(len(items)):
                    if n in marked:
                        glyph = 'M'
                    else:
                        glyph = ' '
                    tcod.console_print_ex(
                        window, 2, n + 2,
                        tcod.BKGND_NONE, tcod.LEFT,
                        glyph)                
                tcod.console_blit(
                    window, 0, 0,
                    SCREEN_WD, SCREEN_HT, 0,
                    0, 0)
                tcod.console_flush()
            else:
                cursor -= command
                if cursor < 0:
                    cursor = 0
                elif cursor > len(items) - 1:
                    cursor = len(items) - 1
                tcod.console_print_ex(
                    window, 1, cursor0 + 2,
                    tcod.BKGND_NONE, tcod.LEFT,
                    ' ')
                tcod.console_print_ex(
                    window, 1, cursor + 2,
                    tcod.BKGND_NONE, tcod.LEFT,
                    '>')
                tcod.console_blit(
                    window, 0, 0,
                    SCREEN_WD, SCREEN_HT, 0,
                    0, 0)
                tcod.console_flush()
        if refresh:
            tcod.console_blit(
                sky_pnl, 0, 0,
                SKY_WD, SKY_HT, 0,
                SKY_LF, SKY_TP)
            tcod.console_blit(
                four_views_pnl, 0, 0,
                FOUR_VIEWS_PNL_WD, FOUR_VIEWS_PNL_HT, 0,
                FOUR_VIEWS_PNL_LF, FOUR_VIEWS_PNL_TP)
            tcod.console_blit(
                floor_pnl, 0, 0,
                FLOOR_WD, FLOOR_HT, 0,
                FLOOR_LF, FLOOR_TP)
            tcod.console_flush()
        
        return chosen

def Debug():
    tcod.console_clear(debug_pnl)

    roomitem = ''
    for room in town.room_list:
        roomitem += str(room) + ' '
        for item in room.item_list:
            roomitem += str(item.name) + ' '
        roomitem += '\n'
    wield = ''
    for weapon in at.wield:
        if isinstance(weapon, Item):
            wield += weapon.name + ' '
        elif isinstance(weapon, list):
            wield += str(weapon)
        else:
            wield += 'None'
    diatx = ''
    for i in cur_item_list:
        if i.tipo == 'diamond':
            dia = i
            diatx = str(dia.x) + ' ' + str(dia.y) + ' ' + str(dia.room) + '\n'
            break
    text = (
        '@ ' + str(at.x) + ' ' + str(at.y) + ' ' + str(at.room) + '\n'
        + str(at.body) + '\n'
        + str(at.stance) + '\n'
        + str(at.balance) + '\n'
        + str(at.sdv) + '\n'        
        + 'facing ' + at.facing + '\n'
        + str(at.poison) + '\n'
        + wield + '\n'
        + roomitem + '\n')
    
    tcod.console_print_ex(
        debug_pnl, 1, 1,
        tcod.BKGND_NONE, tcod.LEFT,
        text)
    tcod.console_blit(
        debug_pnl, 0, 0,
        DEBUG_PNL_WD, DEBUG_PNL_HT, 0,
        DEBUG_PNL_LF, DEBUG_PNL_TP)
    tcod.console_flush()

def Help():
    text = '''
KEY BINDING

    .    WAIT
    k    MOVEMENT KEY
    u    MOVEMENT KEY
    l    MOVEMENT KEY
    n    MOVEMENT KEY
    j    MOVEMENT KEY
    b    MOVEMENT KEY
    h    MOVEMENT KEY
    y    MOVEMENT KEY
    K    MOVEMENT KEY
    U    MOVEMENT KEY
    L    MOVEMENT KEY
    N    MOVEMENT KEY
    J    MOVEMENT KEY
    B    MOVEMENT KEY
    H    MOVEMENT KEY
    Y    MOVEMENT KEY
    e    PICK UP ITEM, INTERACT WITH FURNITURE...
    i    INVENTORY
    f    ATTACK
    a    ATTACK (WITH TARGETTING)
    v    VIEW ITEM, MONSTER, FURNITURE...
    O    SHOPPING CART
    g    GIVE
    p    PAY
    w    WIELD/SHEATHE
    m    AUTOPICKUP/AUTOSTORE/AUTOMOVETO NEARBY VALUABLES
    s    SET AUTOMOVE DESTINATION
    d    AUTOMOVE TO DESTINATION
    M    MAP
    ?    HELP
    ESC  EXIT

INTERFACE

        WEATHER       LOG 
    WALL      WALL
    FRONT    RIGHT    PLAYER     MONSTER

                      STATUS     STATUS
    LEFT      BACK      EQUIPMENT  EQUIPMENT
    WALL      WALL
  ^     TERRAIN
  |     
<-+->  *              | STANDING
  |   ^ ^
  v  ^   ^            + CROUCHING
    -  @  -
     _   _            _ PRONING
      _ _
       .              U UNBALANCED
'''
    
    window = tcod.console_new(SCREEN_WD, SCREEN_HT)
    tcod.console_set_default_foreground(window, tcod.white)
    tcod.console_set_default_background(window, tcod.grey)
    tcod.console_clear(window)
    tcod.console_print_ex(
        window, 0, 0,
        tcod.BKGND_NONE, tcod.LEFT,
        text)    
    tcod.console_blit(
        window, 0, 0,
        SCREEN_WD, SCREEN_HT, 0,
        0, 0)
    tcod.console_flush()

    command_dict = {
        'ESC': 'exit'}
    command = GetCommand(command_dict)

def Intro(resume=False):
    window = tcod.console_new(SCREEN_WD, SCREEN_HT)
    tcod.console_set_default_foreground(window, tcod.white)
    tcod.console_set_default_background(window, tcod.grey)
    tcod.console_clear(window)
    p = SCREEN_WD//2
    q = SCREEN_HT//2
    y = 0
    ## Print choices
    entrylst = ['START', 'HELP', 'EXIT']
    if resume:
        entrylst[0] = 'RESUME'
    for entry in entrylst:
        tcod.console_print_ex(
            window, p+2, q+y,
            tcod.BKGND_NONE, tcod.LEFT,
            entry)
        y += 1
    ## Print cursor '>'
    cursor = 0
    tcod.console_print_ex(
        window, p, q,
        tcod.BKGND_NONE, tcod.LEFT,
        '>')
    tcod.console_blit(
        window, 0, 0,
        SCREEN_WD, SCREEN_HT, 0,
        0, 0)
    tcod.console_flush()
    ## Let cursor go up and down and to and fro
    command_dict = {
        'j': -1,
        'k': 1,
        'ENT': 'enter'}
    while True:
        cursor0 = cursor
        command = GetCommand(command_dict)
        if command == 'enter':
            if cursor == 0:
                break
            elif cursor == 1:
                Help()
                tcod.console_blit(
                    window, 0, 0,
                    SCREEN_WD, SCREEN_HT, 0,
                    0, 0)
                tcod.console_flush()
            elif cursor == 2:
                sys.exit()
        else:
            cursor -= command
            if cursor < 0:
                cursor = 0
            elif cursor > 2:
                cursor = 2
            tcod.console_flush()
            tcod.console_print_ex(
                window, p, q+cursor0,
                tcod.BKGND_NONE, tcod.LEFT,
                ' ')
            tcod.console_print_ex(
                window, p, q+cursor,
                tcod.BKGND_NONE, tcod.LEFT,
                '>')
            tcod.console_blit(
                window, 0, 0,
                SCREEN_WD, SCREEN_HT, 0,
                0, 0)
            tcod.console_flush()

TOWN_SIZE = [50, 50]
WORLD_SIZE = 1000
ROOM_SIZE = [10, 20]
BASICSHOP = [
    'mayor']
RANDOMSHOP = [
    'alchemist',
    'smith',
    'cobbler',
    'gnome']
WEAPONSHOP = [
    'smith',
    'mineshop']

SHOPDOOR = {
    'mayor': 'MAYOR\'S OFFICE',
    'alchemist': 'ALCHEMIST\'S SHOP',
    'smith': 'SMITH\'S SHOP',
    'cobbler': 'COBBLER\'S SHOP',
    'gnome': ''}


##     0
##    3 1
##     2

SIDE_COMPASS = ['N', 'E', 'S', 'W']

def ReverseSide(side):
    side1 = side + 2
    if side1 > 3:
        side1 -= 4
    return side1

def Siding(side, width, length, middle=False, drift=False, edgible=True):
    '''Used in MakeTown()'''
    rx = random.randint(1, width -2)
    ry = random.randint(1, length -2)
    xmax = width - 1
    ymax = length - 1
    xmd = width // 2
    ymd = length // 2
    xdr = random.randint(0, xmd-1)
    ydr = random.randint(0, ymd-1)
    if middle:
        if side == 0:
            x = xmd
            y = ymax
        elif side == 1:
            x = xmax
            y = ymd
        elif side == 2:
            x = xmd
            y = 0
        elif side == 3:
            x = 0
            y = ymd
    else:
        if side == 0:
            x = rx
            y = ymax
            if drift:
                y -= ydr
        elif side == 1:
            x = xmax
            if drift:
                x -= xdr
            y = ry
        elif side == 2:
            x = rx
            y = 0
            if drift:
                y += ydr
        elif side == 3:
            x = 0
            if drift:
                x += xdr
            y = ry
    if not edgible:
        if  x <= 0:
            x = 1
        elif x >= width - 1:
            x = width - 2
        if y <= 0:
            y = 1
        elif y >= width - 1:
            y = width - 2
    return (x, y)

def NxDoor(portal, room, pair=False):
    '''The (x, y) of a furniture placed in room next to portal'''
    pos = None
    if portal in room.portal:
        x, y = room.portal[portal]
        u, v = portal.vectors[room]
        if u == 0:
            p = [(x-1, y+v), (x+1, y+v)]
        elif v == 0:
            p = [(x+u, y-1), (x+u, y+1)]
        p2 = []
        for p1 in p:
            m, n = p1
            if room.bmap[m][n] == 0:
                p2.append(p1)
        if pair:
            pos = (p2[0][0], p2[0][1], p2[1][0], p2[1][1])
        else:
            pos = random.choice(p2)
    return pos

def WallSpill(x, y, room):
    '''Only used in mining'''
    r1 = room
    for i in range(100):
        u = random.randint(-1, 1)
        v = random.randint(-1, 1)
        x1 = x + u
        y1 = y + v
        if 0 <= x1 <= room.x-1 and 0 <= y1 <= room.y-1:
            if room.bmap[x1][y1] == 0:
                break
            elif room.bmap[x1][y1] == 2:
                for po, coordinate in room.portal.items():
                    m, n = coordinate
                    if x1 == m and y1 == n:
                        r1 = po
                        break
                break
    return (x1, y1, r1)

def NewDoor(room, doormarg=5, side=None):
    x = 0
    y = 1
    for i in range(1000):
        if side is None:
            side = random.randint(0, 3)
        x, y = Siding(side, room.x, room.y)
        for po, coordinate in room.portal.items():
            u, v = coordinate
            if max(abs(x-u), abs(y-v)) > doormarg:
                break
    return (x, y)


CITYGATEXY = [(200, 299), (299, 200), (200, 100), (100, 200)]

INS = {
    'ogre': [['O G R E', 'M A N', 'G I A N T'], ['of W I L D', 'of M O U N T A I N']],
    '2fish': [['D I P E S K S', 'D I P E S C S']],
    'wolf': [['L I', 'L U', 'L Y'], ['C O D O M I']],
    'ao': [['A >P< UU']],
    'adek': [['A A E K A T OIK E I']],
    '3crows': [['I A T L P S', 'C A M cp I O X UU']]}

INSPIC = {
    'ogre': ['broad humanoid', 'muscular humanoid', 'menacing humanoid'],
    '2fish': ['two circles\neach containing a fish'],
    '3crows': ['three-legged crow', 'three-headed crow', 'three-eyed crow', 'three crows'],
    'wolf': ['beast'],
    'ao': ['bird carrying\nwater-spinach']}

def Ins(motif):
    lst = INS[motif]
    ins = ''
    for pt in lst:
        ins += random.choice(pt) + ' '
    if random.randint(0, 1) and motif in INSPIC:
        ins += '\n\n'
        ins += '[picture of ' + random.choice(INSPIC[motif]) + ']'

    return ins
    
def MakeTown(roomnum=3):
    town = Site(2, 2, tipht=500, wallht=300, name='Town', natfl='GRAVEL')
    field = town.room_list[0]
    short, long = TOWN_SIZE
    townsq = Room(short, long, town, ceiling=False)  ##Town square
    side = random.randint(0, 3)
    for n in random.choice(TWINNAMES):
        xgb, ygb = Siding(side, townsq.x, townsq.y, drift=True, edgible=False)
        gb = Item('goblin', xgb, ygb, townsq, facing=random.choice(NESW), name=n)
        town.goblin.append(gb)
    x0, y0 = Siding(side, townsq.x, townsq.y, middle=True)
    x1, y1 = CITYGATEXY[side]
    gate = Door(townsq, x0, y0, field, x1, y1, doortype='gate', closed=False, name1='CITY OF ZIUMNI', flomat='STONE FLOOR')
    ##This is after the gate as the gate builds the town
    for i in range(1000):
        xtr, ytr = Siding(side, field.x, field.y, drift=True, edgible=False)
        if field.bmap[xtr][ytr] == 0:
            break
    tree = Item('tree', xtr, ytr, field, name='large banyan tree')
    fa = SIDE_COMPASS[side]
    g0x, g0y, g1x, g1y = NxDoor(gate, field, pair=True)
    g0 = Item('guard', g0x, g0y, field, facing=fa)
    g1 = Item('guard1', g1x, g1y, field, facing=fa)
    town.guard += [g0, g1]
    town.citizen += [g0, g1]
    shops = BASICSHOP + RANDOMSHOP
    for sh in shops:
        side = random.randint(0, 3)
        side1 = ReverseSide(side)
        ##Make no two doors on town square are too close to each other
        counter = 0
        while True:
            x0, y0 = Siding(side, townsq.x, townsq.y)
            too_close = False
            for coordinate in townsq.portal.values():
                p, q = coordinate
                if max(abs(x0-p), abs(y0-q)) <= 5:
                    too_close = True
            if not too_close:
                break
            counter += 1
            if counter >= 100:
                break
        ##Dig the room
        short, long = ROOM_SIZE
        room = Room(short, long, town, name=sh, flomat='STONE FLOOR')
        ##Dig the door
        x1, y1 = Siding(side1, room.x, room.y)
        if sh == 'gnome':
            lock = 'rusty lock'
        else:
            lock = None
        if sh in ['smith', 'alchemist', 'cobbler']:
            closed = False
        else:
            closed = True
        door = Door(room, x1, y1, townsq, x0, y0, name1=SHOPDOOR[sh], closed=closed, lock=lock, flomat='STONE FLOOR')
        if sh == 'gnome':
            mn = NxDoor(door, townsq)
            if mn:
                m, n = mn
                ho = Item('hook', m, n, townsq, name='hook')
            ho.finvt.append(Item('key', ho.x, ho.y, ho.room, name='crooked key', key_to=door))
        ##Furnish
        x, y = Siding(side, room.x, room.y, drift=True, edgible=False)
        if sh != 'gnome':
            table = Item('table', x, y, room, name='table')
            if sh == 'smith':
                for i in range(random.randint(5, 8)):
                    wptype = random.choice(WEAPONSTAB)
                    wp = Item(wptype, table.x, table.y, table.room)
                    table.finvt.append(wp)
                for i in range(random.randint(3, 5)):
                    sdtype = random.choice(SHIELD)
                    sd = Item(sdtype, table.x, table.y, table.room)
                    table.finvt.append(sd)
            elif sh == 'alchemist':
                for i in range(random.randint(6, 8)):
                    pt = Item('potion', table.x, table.y, table.room, flask={random.choice(CHEM): 1000})
                    table.finvt.append(pt)
            elif sh == 'cobbler':
                for i in range(random.randint(6, 8)):
                    letype = random.choice(SHEATH)
                    le = Item(letype, table.x, table.y, table.room)
                    table.finvt.append(le)
                for i in range(random.randint(2, 6)):
                    le = Item('boot', table.x, table.y, table.room)
                    table.finvt.append(le)
            elif sh == 'mayor':
                x, y = Siding(side, room.x, room.y, drift=True, edgible=False)
                be = Item('bell', x, y, room, name='bell')
        else:
            for i in range(10):
                x, y = Siding(side, room.x, room.y, drift=True, edgible=False)
                Item('gold', x, y, room, name='gold coin')
        ##Occupants
        x, y = Siding(side, room.x, room.y, drift=True, edgible=False)
        fa = SIDE_COMPASS[side1]
        if sh == 'mayor':
            my = Item('mayor', x, y, room, facing=fa)
            town.mayor = my
        elif sh == 'smith':
            occ = Item('smith', x, y, room, facing=fa, shk=room)
            occ.stock = copy.copy(table.finvt)
            for st in occ.stock:
                st.owner = occ
        elif sh == 'alchemist':
            occ = Item('alchemist', x, y, room, facing=fa, shk=room)
            occ.stock = copy.copy(table.finvt)
            for st in occ.stock:
                st.owner = occ
        elif sh == 'cobbler':
            occ = Item('cobbler', x, y, room, facing=fa, shk=room)
            occ.stock = copy.copy(table.finvt)
            for st in occ.stock:
                st.owner = occ
        elif sh == 'gnome':
            occ = Item('gnome', x, y, room, facing=fa)
            pt = Item('potion', occ.x, occ.y, occ.room, flask={'lead': 1000})
            occ.wield[1] = pt
            occ.inv.append(pt)

    for instype in ['ogre']+[random.choice(list(INS.keys()))]:
        side = random.randint(0, 3)
        for i in range(1000):
            insx, insy = Siding(side, townsq.x, townsq.y)
            if townsq.bmap[insx][insy] == 1:
                break
        Item('inscription', insx, insy, townsq, ins=Ins(instype))

    return town

def MakeCave():
    mountain = Site(0, 0, tipht=20000, wallht=20000, name='Snow capped mountain', natfl='SNOW', walltype='rock slope')

    field = mountain.room_list[0]
    cave = Room(30, 30, mountain, flomat='STONE FLOOR', wlmat='ROCK WALL')    
    side = random.randint(0, 3)
    x0, y0 = Siding(side, cave.x, cave.y, middle=True)
    x1, y1 = CITYGATEXY[side]
    caveentry = Door(cave, x0, y0, field, x1, y1, closed=False, flomat='STONE FLOOR')
    
    ##This is after the cave entry as the cave entry builds the mountain
    for i in range(1000):
        xtr, ytr = Siding(side, field.x, field.y, drift=True, edgible=False)
        if field.bmap[xtr][ytr] == 0:
            break
    tree = Item('tree', xtr, ytr, field, name='broccoli')
    
    fa = SIDE_COMPASS[side]
    xog, yog = Siding(ReverseSide(side), cave.x, cave.y, drift=True, edgible=False)
    ogre = Item('ogre', xog, yog, cave, facing=fa)
    ogre.task.append(Task('ambush', 30))
    insx, insy = Siding(ReverseSide(side), cave.x, cave.y)
    Item('inscription', insx, insy, cave, ins=Ins('2fish'))

    return mountain

def MakeHill():
    hill = Site(2, 4, tipht=2000, wallht=2000, name='Stout hill', walltype='rock slope')

    field = hill.room_list[0]
    antechamber = Room(30, 30, hill, flomat='STONE FLOOR', wlmat='ROCK WALL')
    side = random.randint(0, 3)
    x0, y0 = Siding(side, antechamber.x, antechamber.y, middle=True)
    x1, y1 = CITYGATEXY[side]
    caveentry = Door(antechamber, x0, y0, field, x1, y1, closed=False, flomat='STONE FLOOR')
    gx, gy = Siding(ReverseSide(side), antechamber.x, antechamber.y, drift=True, edgible=False)
    dwdg = Item('dwarf', gx, gy, antechamber, facing=SIDE_COMPASS[side])

    for i in range(1000):
        xgo, ygo = Siding(side, field.x, field.y, drift=True, edgible=False)
        if field.bmap[xgo][ygo] == 0:
            break
    for i in range(random.randint(8, 10)):
        Item('gold', xgo, ygo, field, name='gold coin')
    
    for i in range(random.randint(5, 7)):
        side = random.randint(0, 3)
        rm0 = hill.room_list[-2]
        x0, y0 = NewDoor(rm0, side=side)
        rx = random.randint(20, 30)
        ry = random.randint(20, 30)
        rm1 = Room(rx, ry, hill, flomat='STONE FLOOR', wlmat='ROCK WALL')
        x1, y1 = NewDoor(rm1, side=ReverseSide(side))
        door = Door(rm0, x0, y0, rm1, x1, y1, closed=False)
        rm0 = None
        rm1 = None

    ##FieldRoomDoorRoomDoorRoomDoor...
    ind = random.randint(2, 3)
    ind = -ind * 2
    mineshop = hill.room_list[ind]
    mineshop.name = 'mineshop'
    x0, y0 = NewDoor(mineshop, side=side)
    rx = random.randint(20, 30)
    ry = random.randint(20, 30)
    rm1 = Room(rx, ry, hill, flomat='STONE FLOOR', wlmat='ROCK WALL')
    rm1.name = 'branchroom'
    x1, y1 = NewDoor(rm1, side=ReverseSide(side))
    door = Door(mineshop, x0, y0, rm1, x1, y1, closed=False)
    rm0 = None
    rm1 = None

    for i in range(random.randint(2, 3)):
        side = random.randint(0, 3)
        rm0 = hill.room_list[-2]
        x0, y0 = NewDoor(rm0, side=side)
        rx = random.randint(20, 30)
        ry = random.randint(20, 30)
        rm1 = Room(rx, ry, hill, flomat='STONE FLOOR', wlmat='ROCK WALL')
        x1, y1 = NewDoor(rm1, side=ReverseSide(side))
        door = Door(rm0, x0, y0, rm1, x1, y1, closed=False)
        rm0 = None
        rm1 = None

    tabx, taby = Siding(random.randint(0, 3), mineshop.x, mineshop.y, drift=True, edgible=False)
    table = Item('table', tabx, taby, mineshop)
    for i in range(random.randint(2, 6)):
        pk = Item('pickaxe', table.x, table.y, table.room)
        table.finvt.append(pk)
    oocx, occy = Siding(random.randint(0, 3), mineshop.x, mineshop.y, drift=True, edgible=False)
    occ = Item('dwarf', oocx, occy, mineshop, shk=mineshop)
    occ.stock = copy.copy(table.finvt)
    for st in occ.stock:
        st.owner = occ

    
    end = hill.room_list[-2]
    end.name = 'end'
    gx, gy = NewDoor(end)
    Item('glisten', gx, gy, end, ore='diamond')

    return hill            
    
Intro()

#Initialize
cur_item_list = []

cloud = random.randint(0, 2)
moonph = random.randint(0, 3)

worldmap = []
town = MakeTown()
##tower = Site(100, 98, 'Tower')
mountain = MakeCave()
hill = MakeHill()
CITYPLACE = (15, 24, 15, 18)
wmapsite = {}
for st in worldmap:
    if st.name:
        counter = 0
        while True:
            counter += 1
            xmin, xmax, ymin, ymax = CITYPLACE
            x = random.randint(xmin, xmax)
            y = random.randint(ymin, ymax)
            for coordinate in wmapsite.values():
                u, v = coordinate
                if max(abs(x-u), abs(y-v)) > 3:
                    break
            if counter > 100:
                break
        wmapsite[st] = (x, y)

for r in hill.room_list:
    if r.name == 'mineshop':
        rat = r
atx = random.randint(70, 90)
aty = random.randint(70, 90)
at = Item('adv', atx, aty, town.room_list[0], facing=random.choice(NESW), eqstyle='civilian')
##at = Item('adv', 1, 1, town.room_list[1], facing=random.choice(NESW), eqstyle='civilian')
##at = Item('adv', 1, 1, town.room_list[1], facing=random.choice(NESW), eqstyle='civilian')
##Item('diamond', at.x, at.y, at.room)
##for i in range(10):
##    Item('gold', at.x, at.y, at.room, name='gold coin')
at.skill['fight'] = 1
at.skill['dodge'] = 1

for st in worldmap:
    for room in st.room_list:
        cur_item_list += room.item_list

scope = None
autoscope = None
message_x = 0
messagebuffer = ''
Message('')
turn = (3600*5+60*50)*2

#Loop
while not tcod.console_is_window_closed():
    turn += 1
    at.time += TimeIncrement()
    if at.time > 0:
##        Debug()
        Sky()
        FourViews()
        taskf = []
        taskn = []
        if at.anim:
            if at.suffocate is not None:
                tx = 'you can\'t breathe!'
                Message(tx)
                Prompt(tx)
            for ts in at.task:
                name = ts.name
                detail = ts.detail
                if name == 'ask for quest':
                    giver, delay = detail
                    if CanSee(at, giver):
                        if delay > 0:
                            ts.detail = [giver, delay-1]
                        else:
                            if at.Say('Hi, ' + giver.Name() + '! What can I do for you?', True):
                                giver.task.append(Task('give quest', ['gnome', at]))
                                taskf.append(ts)
                elif name == 'answer':
                    ans, interrogator = detail
                    for i in PURPOSE:
                        if i[1] == answer:
                            text = i[0]
                            break                
                    if at.Say(text, True):
                        if answer in ['thief', 'secret']:
                            for gd in interrogator.room.site.guard:
                                gd.attack = at
                                gd.LocTar(at)
                            interrogator.task.append(Task('theft alarm', None))
                        else:
                            interrogator.task.append(Task('huh', None))
                        taskf.append(ts)
                        town.guest.append(at)
                elif name == 'agree on price b':
                    price, seller, good = detail
                    if at.PocketGold() < price:
                        if at.Say('I don\'t have enough money', True):
                            seller.task.append(Task('beat scammer', at))
                            seller.attacksp = at
                            taskf.append(ts)
                    else:
                        if at.Say('deal!', True):
                            ordered = False
                            for o in item.order:
                                if o.good == good:
                                    ordered = True
                            if not ordered:
                                order = Order(at, price, seller, good)
                                at.order.append(order)
                                seller.order.append(order)
                            taskf.append(ts)
                elif name == 'haggle':
                    price1, seller, good = detail
                    text = str(Coins(price1)) + ' gold?'
                    if at.Say(text, True):
                        seller.task.append(Task('agree on price s', [price1, seller, good]))
                        taskf.append(ts)
                elif name == 'cancel order':
                    o = detail
                    text = 'I don\'t want ' + o.good.Name() + ' anymore'
                    if at.Say(text, True):
                        at.order.remove(o)
                        o.seller.task.append(Task('beat scammer', at))
                        o.seller.attacksp = at
                        taskf.append(ts)
                elif name == 'tamarinfavor':
                    favor = detail
                    if favor is None:
                        if random.randint(0, 50) == 0:
                            tx = 'you hear a tamarin saying: you owe me a favor'
                            Message(tx)
                            Prompt(tx)
                            ts.detail = random.randint(1, 100)
            for ts in taskf:
                at.task.remove(ts)
            for ts in taskn:
                at.task.append(ts)
        command = GetCommand(KEY_DICT)
        if command == 'EXIT':
            Intro(resume=True)
        elif command == 'WAIT':
            at.time -= 10
        elif command == 'VIEW':
            scope = View()
        elif command == 'HELP':
            Help()
            tcod.console_blit(
                message_pnl, 0, 0,
                MESSAGE_PNL_WD, MESSAGE_PNL_HT, 0,
                MESSAGE_PNL_LF, MESSAGE_PNL_TP)
            tcod.console_flush()
        elif command == 'MAP':
            WMap()
        elif at.anim:
            if command in FRBL or command.startswith('t'):
                if command.startswith('t'):
                    to = command[1:]
                    result = at.Walk(to, translate=True)
                else:
                    result = at.Walk(command)
                if result == 'CAN_PASS':
                    pass
                elif result == 'BLOCKED':
                    Message('thump')
                elif result == 'NO_LEG':
                    Message('you have no legs')
                elif result == 'WEAK':
                    Message('your legs feel powerless')
                elif result == 'FIXED':
                    Message('you cannot move')
            elif command == 'USE':
                Use()
            elif command == 'INV':
                Inv()
            elif command == 'ATTACK':
                Hit()
            elif command == 'AUTO-ATTACK':
                Hit(tab=True)
            elif command == 'SHOP':
                Shop()
            elif command == 'GIVE':
                Give()
            elif command == 'POUCH':
                Pouch()
            elif command == 'PAY':
                Pay()
            elif command == 'WIELD':
                Wield()
            elif command == 'SETDEST':
                SetDest()
            elif command == 'AUTOTRAVEL':
                Autotravel()
    for item in cur_item_list:
        if item.anim:
            if item != at:
                item.time += TimeIncrement()
                if item.time > 0:
                    item.display_move = False
                    taskf = []
                    taskn = []
                    for ts in item.task:
                        name = ts.name
                        detail = ts.detail
                        if name == 'circle':
                            if item.time > 0:
                                target = detail
                                if CanSee(item, target):
                                    d = random.choice(['FR', 'FL'])
                                    item.Move(FRBLtoNESW(item.facing, d))
                                    f = Direction(item, item.attack, dn='cardinal')
                                    if f != 0:
                                        item.facing = f
                                taskf.append(ts)
                        elif name == 'ambush':
                            radius = detail
                            if item.attack:
                                pass
                            else:
                                for c in CanSeeList(item):
                                    if c.anim and c != item and Distance(item, c) <= radius:
                                        item.attack = c
                                        item.LocTar(c)
                                        if item.tipo == 'ogre':
                                            item.task.append(Task('fingergun', c))
                                        break
                        elif name == 'prepare':
                            if item.time > 0:
                                if item.Prepare():
                                    taskf.append(ts)
                        elif name == 'gnome guard':
                            intruder = detail
                            if intruder:
                                pass
                            else:
                                if item.room.name == 'gnome':
                                    for i in CanSeeList(item):
                                        if i != item and i.anim:
                                            ts.detail = i
                                            taskn.append(Task('curse', 'Mimi-Wiwi-Lini-Ghee!'))
                                            taskn.append(Task('disappear', [50, turn]))
                                            if isinstance(item.wield[1], Item):
                                                taskn.append(Task('gnome grenade', item.wield[1]))
                                            break
                        elif name == 'gnome grenade':
                            if item.time > 0:
                                obj = detail
                                for w in item.wield:
                                    if obj == w:
                                        j = item.wield.index(obj)
                                        item.wield[j] = None
                                        item.inv.remove(obj)
                                if CanSee(at, item):
                                    cs = True
                                    Message(item.name + ' drops ' + obj.Name())
                                else:
                                    cs = False
                                item.time -= 10
                                taskf.append(ts)
                                Fall(obj, fallmsg=False)
                        elif name == 'curse':
                            obj =  detail
                            if item.Say(obj, True):
                                taskf.append(ts)
                        elif name == 'point finger':
                            if item.time > 0:
                                obj = detail
                                if CanSee(item, obj):
                                    if CanSee(at, item):
                                            Message(item.name + ' points a finger at ' + at.name)
                                    item.time -= 10
                                    taskf.append(ts)
                        elif name == 'fingergun':
                            victim = detail
                            if victim.anim:
                                if item.time > 0 and item.speaking <= 0 and random.randint(0, 200) == 0:
                                    if item.HasPart('arm'):
                                        if CanSee(item, victim):
                                            item.time -= 10
                                            item.speaking += 10
                                            if CanSee(at, item):
                                                if CanSee(at, victim):
                                                    Message('BANG')
                                                    Message(item.Name() + ' shoots ' + victim.Name() + ' with finger gun!')
                                                else:
                                                    Message('BANG')
                                                    Message(item.Name() + ' fires finger gun!')
                                    else:
                                        taskf.append(ts)
                            else:
                                taskf.append(ts)
                        elif name == 'disappear':
                            countdown, turn0 = detail
                            if turn - turn0 > countdown:
                                item.room.item_list.remove(item)
                                if autoscope == item:
                                    autoscope == None
                                cur_item_list.remove(item)
                                if CanSee(at, item):
                                    Message(item.name + ' disappears')
                                taskf.append(ts)
                                ##Prevent item from doing anything after disappearance
                                item.time -= 10
                                item.speaking += 10
                                break
                        elif name == 'assassin alert':
                            if item.room.name == 'mayor':
                                assassin = detail
                                if assassin:
                                    pass
                                else:
                                    for i in CanSeeList(item):
                                        if i == at:
                                            ts.detail = i
                                            if item.Say('assassin!', True):
                                                for gb in item.room.site.goblin:
                                                    gb.task.append(Task('save mayor', None))
                                                    gb.attack = i
                                                    gb.LocTar(i)
                                                pass
                                            else:
                                                taskn.append(Task('assassin alarm', i))
                                            taskn.append(Task('pull bell string', i))
                        elif name == 'assassin alarm':
                            if item.Say('assassin!', True):
                                taskf.append(ts)
                        elif name == 'shyw':
                            wielder = detail
                            if item.Say('sheathe your weapon!', True):
                                for ich in CanHearList(item):
                                    if ich in item.room.site.citizen and ich != item:
                                        ich.watch.append(wielder)
                                        ich.task.append(Task('prepare', None))
                                taskf.append(ts)
                        elif name == 'pull bell string':
                            if item.time > 0:
                                assassin = detail
                                end_task = False
                                bell = None
                                for i in item.room.item_list:
                                    if i.tipo == 'bell':
                                        bell = i
                                if bell:
                                    if Distance(item, bell) > 0:
                                        item.MoveTo(bell)
                                    else:
                                        item.time -= 10
                                        if CanSee(item, at):
                                            Message(item.name + ' pulls the string')
                                        if CanHear(at, item):
                                            text = 'ding ding ding'
                                            Message(text)
                                            Prompt(text)
                                        end_task = True
                                else:
                                    end_task = True
                                if end_task:
                                    taskf.append(ts)
                                    item.attack = assassin
                                    item.LocTar(assassin)
                        elif name == 'save mayor':
                            mayordoor = detail
                            if mayordoor is None:
                                for rm in item.room.site.room_list:
                                    if rm.name == 'mayor':
                                        for po in rm.portal:
                                            mayordoor = po.door
                                            break
                            else:
                                if Distance(item, mayordoor) > 0:
                                    item.MoveTo(mayordoor)
                                else:
                                    taskf.append(ts)
                        elif name == 'diamwatch':
                            diamcarrier = detail
                            if item.room.name == 'mineshop':
                                for dc in item.room.item_list:
                                    if dc.anim and dc not in item.room.site.citizen:
                                        if dc not in diamcarrier and dc != item.attack:
                                            for dm in dc.inv:
                                                if dm.tipo == 'diamond':
                                                    ts.detail.append(dc)
                                                    item.task.append(Task('leavedhere', None))
                                                    break
                                notdc = []
                                for dc in diamcarrier:
                                    if not CanSee(item, dc):
                                        for ctz in item.room.site.citizen:
                                            ctz.attack = dc
                                        item.task.append(Task('theft alarm', None))
                                        notdc.append(dc)
                                    carrydiam = False
                                    for dm in dc.inv:
                                        if dm.tipo == 'diamond':
                                            carrydiam = True
                                            break
                                    if not carrydiam:
                                        notdc.append(dc)
                                for ndc in notdc:
                                    ts.detail.remove(ndc)
                        elif name == 'leavedhere':
                            if item.Say('leave the diamond here!', True):
                                taskf.append(ts)
                        elif name == 'guard':
                            guarded = detail
                            interrogate = False
                            if item.tipo == 'guard':
                                interrogate = True
                            else:
                                see_guard = False
                                for gd in item.room.site.guard:
                                    if gd != item and CanSee(item, gd):
                                        see_guard = True
                                        break
                                if not see_guard:
                                    interrogate = True
                            if interrogate:
                                if at not in guarded.citizen+guarded.guest+guarded.suspect and CanSee(item, at) and Distance(item, at) <= 20:
                                    taskn.append(Task('interrogate', at))
                                    guarded.suspect.append(at)
                        elif name == 'interrogate':
                            suspect = detail
                            text = 'hey stranger what are you doing here?'
                            if item.Say(text, prompt=True, pr=False):
                                answer = Menu(text, PURPOSE, escapable=False, refresh=False)
                                if answer:
                                    at.task.append(Task('answer', [answer, item]))
                                taskf.append(ts)
                        elif name == 'donttouchgate':
                            sabotageur = detail
                            if item.Say('don\'t touch that gate!', prompt=True):
                                for ich in CanHearList(item):
                                    if ich in item.room.site.citizen:
                                        ich.attack = sabotageur
                                taskf.append(ts)
                        elif name == 'opengate':
                            gateroom = detail
                            d = Distance(item, gateroom.door)
                            if d <= 0:
                                item.Move(random.choice(gateroom.vectors))
                            elif d <= 1:
                                if item.HasPart('arm'):
                                    gateroom.bmap[0][0] = 2
                                    for room in gateroom.portal.keys():
                                        u, v = room.portal[gateroom]
                                        room.bmap[u][v] = 2
                                    if CanSee(at, item):
                                        Message(item.Name() + ' opens ' + gateroom.door.Name())
                                    elif CanSee(at, gateroom.door):
                                        text = gateroom.door.Name() + ' is opened'
                                        Message(text)
                                        Prompt(text)
                                    item.time -= 10
                                    taskf.append(ts)
                            else:
                                item.MoveTo(gateroom.door)
                        elif name == 'price':
                            good, buyer = detail
                            price = TEMPLATE[good.tipo]['pr']
                            if buyer.charisma > 0:
                                price -= 100
                                if price < 100:
                                    price = 100
                            text = str(Coins(price))+' gold'
                            if item.Say(text, prompt=True, pr=False):
                                selec = [['agree on price', 'a']]
                                price1 = price * 6 // 10
                                if price1 >= 100 and price - price1 > 100:
                                    selec.append(['haggle', 'h'])
                                reply = Menu(text, selec,refresh=False)
                                if reply == 'a':
                                    at.task.append(Task('agree on price b', [price, item, good]))
                                elif reply == 'h':
                                    at.task.append(Task('haggle', [price1, item, good]))
                                taskf.append(ts)
                        elif name == 'out of stock':
                            if item.Say('I have nothing to sell currently', True):
                                taskf.append(ts)
                        elif name == 'beat scammer':
                            scammer = detail
                            if item.Say('scammer!', True):
                                taskf.append(ts)
                        elif name == 'agree on price s':
                            price, seller, good = detail
                            if item.Say('deal!', True):
                                order = Order(at, price, seller, good)
                                at.order.append(order)
                                item.order.append(order)
                                taskf.append(ts)
                        elif name == 'shop guard':
                            thieves = detail
                            new_thief = []
                            abandoned = []
                            finished = []
                            for o in item.order:
                                if not CanSee(item, o.buyer):
                                    if o.status == 'UNPAID':
                                        if o not in thieves:
                                            new_thief.append(o)
                                            taskn.append(Task('theft alarm', o))
                                            item.attacksp = o.buyer
                                    else:
                                        if CanSee(item, o.good):
                                            abandoned.append(o)
                                        else:
                                            finished.append(o)
                            for o in abandoned:
                                o.seller.order.remove(o)
                                o.buyer.order.remove(o)
                                o.seller.stock.append(o.good)
                                o.good.owner = o.seller
                            for o in finished:
                                o.seller.order.remove(o)
                                o.buyer.order.remove(o)
                            thieves += new_thief
                            for pt in item.room.portal.keys():
                                if pt.bmap[0][0] == 3:
                                    pt.bmap[0][0] = 2
                                    for rm in pt.portal.keys():
                                        dox, doy = rm.portal[pt]
                                        rm.bmap[dox][doy] = 2
                                    if CanSee(at, pt.door):
                                        tx = pt.door.Name() + ' opens'
                                        Message(tx)
                                        Prompt(tx)
                        elif name == 'enemy alarm':
                            enemy = detail
                            if item.Say('enemy!', True):
                                taskf.append(ts)
                                for ich in CanHearList(item):
                                    if ich in item.room.site.citizen:
                                        ich.attack = detail
                                        ich.LocTar(detail)
                        elif name == 'theft alarm':
                            if item.Say('thief!', True):
                                taskf.append(ts)
                        elif name == 'quest hint':
                            hint, quest = detail
                            if item.Say(hint, True):
                                taskf.append(ts)
                        elif name == 'give quest':
                            quest, questor = detail
                            success = False
                            if CanSee(item, questor):
                                if quest == 'gnome':
                                    if item.Say('get rid of that gnome for me!', True):
                                        taskn.append(Task('quest given', ['gnome', questor]))
                                        taskn.append(Task('quest hint', ['the key to his base is over there', quest]))
                                        taskf.append(ts)
                        elif name == 'put i on f':
                            if item.time > 0:
                                item1, f1 = detail
                                if Distance(item, f1) == 0:
                                    for i in item.inv:
                                        if i == item1:
                                            if CanSee(item, at):
                                                Message(item.name + ' puts ' + item1.name + ' onto ' + f1.name)
                                            item.inv.remove(item1)
                                            item.TakeOff(item1)
                                            f1.finvt.append(item1)
                                            item.time -= 10
                                            taskf.append(ts)
                        elif name == 'manage inv':
                            if item.time > 0:
                                coin = None
                                weapon = None
                                for w in item.wield:
                                    if isinstance(w, list):
                                        for w1 in w:
                                            if w1.tipo == 'gold':
                                                coin = w1
                                                break
                                    elif w is not None:
                                        if w.tipo == 'gold':
                                            coin = w
                                            break
                                        elif w.tipo in WEAPONSTAB:
                                            weapon = w
                                            break
                                if coin:
                                    for w in item.wear:
                                        if w.tipo == 'pouch':
                                            item.TakeOff(coin)
                                            w.bag.append(coin)
                                            if CanSee(item, at):
                                                Message(item.Name() + ' puts ' + coin.Name() + ' into ' + w.Name())
                                            item.time -= 10
                                            break
                                elif weapon and item.time > 0 and not item.attack and not item.watch:
                                    for w in item.wear:
                                        if CanHold(weapon, w):
                                            item.TakeOff(weapon)
                                            w.bag.append(weapon)
                                            if CanSee(at, item):
                                                Message(item.Name() + ' sheathes ' + weapon.Name())
                                            break
                        elif name == 'mayor speech':
                            if random.randint(0, 999)==0 and random.randint(0, 99)==0:
                                item.Say(random.choice(MAYORSPEECH))
                        elif name == 'huh':
                            if item.Say('huh', True):
                                taskf.append(ts)

                    for ts in taskf:
                        item.task.remove(ts)
                    for ts in taskn:
                        item.task.append(ts)

                    if item in item.room.site.citizen and item.room.name not in WEAPONSHOP:
                        for ics in CanSeeList(item):
                            if ics.anim and ics not in item.room.site.citizen and ics != item.attack:
                                if ics in item.watch:
                                    if not CarryArm(ics):
                                        item.watch.remove(ics)
                                    else:
                                        if random.randint(0, 100) == 0:
                                            item.task.append(Task('enemy alarm', ics))
                                            break
                                else:
                                    if CarryArm(ics):
                                        if item.Say('sheathe your weapon!', True):
                                            for ich in CanHearList(item):
                                                if ich in item.room.site.citizen and ich != item:
                                                    ich.watch.append(ics)
                                                    ich.task.append(Task('prepare', None))
                                        else:
                                            item.task.append(Task('shyw', ics))
                                        item.watch.append(ics)
                                        item.task.append(Task('prepare', None))
                                        break

                    if item.time > 0 and item.attack:
                        if item.Prepare():  ##Get prepared
                            if item.time > 0:
                                if Distance(item, item.attack) > 1:
                                    item.MoveTo(item.attack)
                                else:
                                    has_attacked, is_blocked = item.Hit(item.attack)
                                    item.attack.Defense(item)
                                    if has_attacked and not is_blocked:
                                        if not item.attack.anim:
                                            item.attack = None
                                            item.tls = None
                                    else:
                                        item.task.append(Task('circle', item.attack))

                    if item.speaking <= 0 and item.attacksp:
                        ta = item.attacksp
                        if ta.anim:
                            if ta.stance > 0:
                                item.Say('verb_mumbles', True)
                                ta.stance = 0
                                ta.facing = random.choice(NESW)
                                ta.paralyzed = True
                                if CanSee(at, ta):
                                    Message('a force smashes ' + ta.Name() + ' to the ground')
                            else:
                                item.Say('verb_mumbles', True)
                                ta.body['body'] -= random.randint(1, 10)
                                if ta == at:
                                    Message(Spelltx(item.tipo))
                                if ta.body['body'] <= 0:
                                    ta.BreakLeg('body')
                        else:
                            item.attacksp = None

                    if item.time > 0 and item.watch:
                        wa = item.watch[-1]
                        if CanSee(item, wa):
                            if CarryArm(wa):
                                fa = Direction(item, wa, dn='cardinal')
                                if item.facing != fa:
                                    item.facing = fa
                                    item.time -= 10
                                    if CanSee(item, at):
                                        Message(item.Name() + ' turns around')
                            else:
                                item.watch.remove(wa)
            ##Check if time is out of range
            if item.time > 0:
                item.time = 0
            elif item.time < -20:
                item.time = -20
            if item.speaking:
                item.speaking -= 1
            item.blocking = {}
            if item.balance >= 0:
                item.balance = 0
            elif item.balance >= -20:
                item.balance += 1
            else:
                item.balance = -20
            ##Poison
            for chem, duration in item.poison.items():
                if duration > 0:
                    item.poison[chem] -= 1
                else:
                    item.poison.pop(chem)
                    break
            for aoe in CSmL(item):
                chem = aoe.chem
                if Distance(aoe, item) <= aoe.radius:
                    item.poison.setdefault(chem, 0)
                    item.poison[chem] += 5
            if item == at:
                CheckChem()
            ##Suffocate
            if item.suffocate is not None:
                if turn - item.suffocate > 50:
                    die = True
                    if item == at:
                        tamarinned = False
                        for ts in item.task:
                            if ts.name == 'tamarinfavor':
                                tamarinned = True
                        if not tamarinned:
                            tx = 'you hear a tamarin saying: O, ill-lucked traveller! I can save you.'
                            Message(tx)
                            Prompt(tx, refresh=False)
                            selec = [('yes', 'y'), ('no', 'n')]
                            choice = Menu('accept the aid?', selec, escapable=False)
                            if choice == 'y':
                                at.task.append(Task('tamarinfavor', None))
                                br = at.fixedto
                                br.looped = False
                                for bd in br.bird:
                                    if bd.fixedto == br:
                                        bd.fixedto = None
                                        Message(bd.Name() + ' falls down')
                                        if bd.suffocate is not None:
                                            bd.suffocate = None
                                br.bird = []
                                die = False
                    if die:
                        item.BreakLeg('body')
                        item.suffocate = None
##except Exception as e:
##    print(e)
##input()
