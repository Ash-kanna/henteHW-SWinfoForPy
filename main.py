import os as opperativsystem
mappeNavn2 = "maskin"

def hvilketOprativsystem():
    #Retunerer navnet på det nåværende opprativsystemmet
    osNavn = opperativsystem.name
    return osNavn


def hvorMyeLedigPlass():
    #Retunerer mengden ledig plass på disken i byte
    statvfs = opperativsystem.statvfs('/')
    ledigPlass = statvfs.f_bavail * statvfs.f_frsize
    return ledigPlass


def hvemBrukerErLoggetInn():
    #Retunerer navnet på den nåværende innloggede brukeren
    brukerNavn = opperativsystem.getlogin()
    return brukerNavn


def hvilkenIPAdresse():
    #Retunerer den nåværende IP-adressen til maskinen
    import socket
    brukerNavn = socket.gethostname()
    ipAdresse = socket.gethostbyname(brukerNavn)
    return ipAdresse


def instalerteProgrammer():
    #Skriver ut de installerte programmene på systemet
    if opperativsystem.name == 'posix': #Linux eller MacOS
        try:
            with open('/var/lib/dpkg/status', 'r') as filLeser:
                data = filLeser.read()
                #liste over installerte programmer blir hentet fra dpkg status filen
                #dpkg beholder informasjon om installerte pakker på Linux og MacOS systemer
                programmer = [line.split(': ')[1] for line in data.split('\n') if line.startswith('Package: ')]
                print("Instalerte programmer på systemet:")
                for program in programmer:
                    print(program)
        except FileNotFoundError:
            print("Kunne ikke finne listen over installerte programmer.")
    else:
        print("Vi kan ikke vsie de instalerte programmene.")

def lagerMaskinMappe():
    if not opperativsystem.path.isdir(mappeNavn2):
        opperativsystem.mkdir(mappeNavn2)

def samleAltIMappe():
    #Samler all informasjon i en mappe
    global mappeNavn2
    filForOpen = open(opperativsystem.path.join(mappeNavn2, "maskinen.txt"), "w")

    innhold = filForOpen.write("Det nåværende opprativsystemmet er:", hvilketOprativsystem(), 
                               "\nMengden ledig plass på disken er:", hvorMyeLedigPlass(), "byte\n", 
                               "\nDen nåværende innloggede brukeren er: ", hvemBrukerErLoggetInn(), 
                               "\nDen nåværende IP-adressen til maskinen er:", hvilkenIPAdresse(), 
                               "\n\nSkriver ut de instalerte programmene: \n", instalerteProgrammer())
    print(innhold)
    filForOpen.close()

lagerMaskinMappe()
print(samleAltIMappe())
