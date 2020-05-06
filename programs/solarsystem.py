'''
programmanaam:     solarsystem
auteur:            Dariush Mirkarimi & Milan Hak
datum:             28-4-2020
functionaliteit:   Weergeeft een live-simulatie van de baan van planeten om de zon, met behulp van matplotlib
'''

from scipy.constants import G
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

realistic = {
    'real_G':  False,
    'real_calculations': False
}

#Een class word gemaakt. De hemellichamen worden allemaal object van deze class.
class CelestialBody:
    def __init__(self, name, orbiting, radius, mass, pos, momentum, colour=None, data={}):
        self.name = name
        self.orbiting = orbiting
        self.radius = radius
        self.mass = float(mass)  # kg
        self.pos = np.asarray(pos, dtype=np.float64)
        self.momentum = np.asarray(momentum, dtype=np.float64)
        self.force = np.zeros(3)
        self.colour = colour

        #Arrays worden gemaakt waar elke simulatie cycle de positie van een object bij word toegevoegd
        self.x_path = np.empty(1, dtype=np.float64)
        self.y_path = np.empty(1, dtype=np.float64)
        self.z_path = np.empty(1, dtype=np.float64)

        #Arrays krijgen de eerste positie al toegevoegd, zodat np.append later correct kan functioneren
        self.x_path[0] = self.pos[0]
        self.y_path[0] = self.pos[1]
        self.z_path[0] = self.pos[2]

#gebruikt de echte G
if realistic['real_G'] is True:
    def gravity(x, y):
    
        '''
        Functie die ervoor zorgt dat gravitatiekracht tussen hemellichamen kan worden berekent
        Dat gebeurt hier met de echte gravitatieconstante
        '''
        
        r_vec = x.pos - y.pos
        r_mag = np.linalg.norm(r_vec)
        r_hat = r_vec / r_mag
        # Calculate force magnitude.
        force_mag = G * x.mass * y.mass / r_mag ** 2
        # Calculate force vector.
        force_vec = -force_mag * r_hat

        return force_vec
else:
    #gebruikt 1 in plaats van G
    def gravity(x, y):
    
        '''
        Functie die ervoor zorgt dat gravitatiekracht tussen hemellichamen kan worden berekent
        Dat gebeurt hier met het getal 1 in plaats van de echte de echte gravitatieconstante
        '''
        
        r_vec = x.pos - y.pos
        r_mag = np.linalg.norm(r_vec)
        r_hat = r_vec / r_mag
        # Calculate force magnitude.
        force_mag = 1 * x.mass * y.mass / r_mag ** 2
        # Calculate force vector.
        force_vec = -force_mag * r_hat

        return force_vec

#Hemellichamen als objecten van de CelestialBody class initialiseren
Sun = CelestialBody('Sun', None, 1000, 2000, [0, 0, 0], [0, 0, 0], colour='C1')
Earth = CelestialBody('Earth', [Sun], 200, 4.5, [1.3, 0, 0], [0, -100, 80], colour='C0')
Moon = CelestialBody('Moon', [Sun, Earth], 5, 0.5, [1.38, 0, 0], [-1, -13.99291, 12], colour='purple')
Mercurius = CelestialBody('Mercurius', [Sun], 20, 4.5, [0.7, 0, 0], [0, -225, 0], colour='red')
Jupiter = CelestialBody('Jupiter', [Sun], 1000, 2000, [1.7, 0, 0], [19000, 15000, 225*250], colour='green')
Saturnus = CelestialBody('Saturnus', [Sun], 20, 4.5, [0.7, 0, 0], [0, -225, 0], colour='red')

#een list maken van de planeten
bodies = [Sun, Earth, Moon, Mercurius, Jupiter]

#stelt het plot in om 3d te tonen
fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')
ax.grid(True, linestyle='-', color='0.75')
#initialiseert het plot met de positie van de aarde
scat = plt.scatter(Earth.pos[0], Earth.pos[1], 0)

#berekent de krachten op de planeten op een wijze vergelijkbaar met coach maar dan beter en in 3d
#de simulatie functie 
def sim(scatter_plot):

    '''
    Deze functie simuleert de beweging van de hemellichamen. 
    Dat gebeurt behulp van de simulatie functie die ervoor zorgt dat krachten tussen de hemellichamen worden berekent.
    '''


    dt = 0.001
    t = 0
    #gebruikt realistische berekeningen waarin alles met alles rekening houdt
    if realistic['real_calculations'] is True:
        force_list = []
        for current_body in bodies:
            temp = bodies.copy()
            temp.pop(temp.index(current_body))
            #past posities van hemellichamen aan op basis van de krachten die op hen werken
            forces = np.zeros(3, dtype=np.float64)
            for affecting_body in temp:
                forces += gravity(current_body, affecting_body)
                
            force_list.append(forces)
                
                
        for i, current_body in enumerate(bodies): 
            
            current_body.force = force_list[i]
            current_body.momentum += current_body.force * dt
            current_body.pos += current_body.momentum / current_body.mass * dt
            
            #past trails toe om de vorige posities te kunnen zien
            current_body.x_path = np.append(current_body.x_path, current_body.pos[0])
            current_body.y_path = np.append(current_body.y_path, current_body.pos[1])
            current_body.z_path = np.append(current_body.z_path, current_body.pos[2])
            
        t += dt
    #gebruikt versimpelde berekeningen waarin de planeten alleen met de orbiting bodies rekening houden
    else:
        force_list = []
        for current_body in bodies:
            forces = np.zeros(3, dtype=np.float64)

            #past posities van hemellichamen aan op basis van de krachten die op hen werken
            if current_body.orbiting is not None and current_body is not Sun:
                for i in current_body.orbiting:
                    forces += gravity(current_body, i)
                    
                force_list.append(forces)
            else:
                force_list.append((0,0,0))
                
        for i, current_body in enumerate(bodies):
            if current_body.orbiting is not None and current_body is not Sun:
                current_body.force = force_list[i]
                current_body.momentum += current_body.force * dt
                current_body.pos += current_body.momentum / current_body.mass * dt

                #past trails toe om de vorige posities te kunnen zien
                current_body.x_path = np.append(current_body.x_path, current_body.pos[0])
                current_body.y_path = np.append(current_body.y_path, current_body.pos[1])
                current_body.z_path = np.append(current_body.z_path, current_body.pos[2])

        t += dt
    #stelt de grootte van het assenstelsel in
    plt.cla()
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-2, 2)
    ax.set_clip_on(False)

    #zet de waardes van het stelsel in het plot
    for i in bodies:
        ax.plot(i.x_path[-100::], i.y_path[-100::], i.z_path[-100::], color=i.colour, zorder=3.9, alpha=0.5)
        if i.colour is not None:
            ax.scatter(i.pos[0], i.pos[1], i.pos[2], s=i.radius, color=i.colour, zorder=2)
            ax.text(i.pos[0], i.pos[1], i.pos[2], s=i.name, zorder=10.,
                    verticalalignment='center_baseline', horizontalalignment='center', fontsize=8)

        

    return scatter_plot


animation = FuncAnimation(fig, func=sim, frames=100, interval=1)
