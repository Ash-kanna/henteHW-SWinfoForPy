import os as opperativsystem

def hvilketOprativsystem():
    #Retunerer navnet på det nåværende opprativsystemmet
    osNavn = opperativsystem.name
    return osNavn

print("Det nåværende opprativsystemmet er:", hvilketOprativsystem())

def hvorMyeLedigPlass():
    #Retunerer mengden ledig plass på disken i byte
    statvfs = opperativsystem.statvfs('/')
    ledigPlass = statvfs.f_bavail * statvfs.f_frsize
    return ledigPlass

print("Mengden ledig plass på disken er:", hvorMyeLedigPlass(), "byte")

def hvemBrukerErLoggetInn():
    #Retunerer navnet på den nåværende innloggede brukeren
    brukerNavn = opperativsystem.getlogin()
    return brukerNavn

#print(f"Den nåværende innloggede brukeren er: {hvemBrukerErLoggetInn()}")

def hvilkenIPAdresse():
    #Retunerer den nåværende IP-adressen til maskinen
    import socket
    brukerNavn = socket.gethostname()
    ipAdresse = socket.gethostbyname(brukerNavn)
    return ipAdresse

print("Den nåværende IP-adressen til maskinen er:", hvilkenIPAdresse())


