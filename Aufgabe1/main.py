import numpy as np

""" --- Definition des Netzwerkes --- """

nCount = 3      # Anzahl der Neuronen
nInput = 2      # Anzahl Input-Neuronen
nOutput = 1     # Anzahl Output-Neuronen

a = np.array([0, 0, 0])         # Aktivierung
s = np.array([0.5, 0.5, 1.5])   # Schwellenwerte: Ausgabeneuronen: or: 0.5; and: 1.5
x = np.array([1, 1])            # Input

""" Index 0..len(x) des Arrays a wird mit den Werten des Arrays x befüllt. """
a[0:len(x):1] = x

""" 
Hinton Matrix: Initialisiert die Verbindungen zwischen den Neuronen. 
Neuron 1 & 2 (Spalte 1 & 2) sind jeweils verbunden mit Neuron 3 (Verbingsgewicht: 1). 
Neuron 3 besitzt keine weiteren Verbindungen, da es den Output angibt.    
"""
w = np.array([[0, 0, 1],
              [0, 0, 1],
              [0, 0, 0]])


def funcnn(avec, svec, wmat):
    """
    avec: beinhaltet alle Aktivierungswerte der Neuronen (Aktivierung + Input)
    svec: beinhaltet alle definierten Schwellenwerte der Neuronen
    wmat: beinhaltet ein FeedForward Netzwerk welches die Verbindungen der Neuronen beschreibt.
    """
    ncount = len(avec)
    netvec = np.zeros(ncount)                               # Vorbelegung für den Netzinput
    for j in range(ncount):                                 # Schleifen durch alle Neuronen des Netzwerks
        for i in range(ncount):                             # - "" -
            """ 
            Propagierfunktion - berechnet:
            Netzinput = bisherigen netvec Wert + Verbindungsgewichtung * aktuellen Aktivierungswert
            """
            netvec[j] = netvec[j] + wmat[i][j] * avec[i]
            """ 
            Aktivierungsfunktion - berechnet:
            neue Aktivierung / Output = aktuelle Aktivierung + Netzinput
            """
            avec[j] = avec[j] + netvec[j]
            """
            Transferfunktion (Heaviside-Funktion), wenn avec > svec wird 1 in avec gespeichert. 
            Ist svec > avec wird 0 in avec gespeichert.
            """
            avec[j] = avec[j] > svec[j]
    return avec


o = funcnn(a, s, w)
y = o[nCount - 1]                                           # Ausgabe des letzen Wertes der berechneten Ausgabe
print(y)



