import os as opperativsystem

def hvilketOprativsystem():
    #Retunerer navnet på det nåværende opprativsystemmet
    osNavn = opperativsystem.name
    return osNavn

print("Det nåværende opprativsystemmet er:", hvilketOprativsystem())