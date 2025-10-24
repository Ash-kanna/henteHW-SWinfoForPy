import os as opperativsystem

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



print("Det nåværende opprativsystemmet er:", hvilketOprativsystem())
print("Mengden ledig plass på disken er:", hvorMyeLedigPlass(), "byte")
print("Den nåværende innloggede brukeren er: ", hvemBrukerErLoggetInn())
print("Den nåværende IP-adressen til maskinen er:", hvilkenIPAdresse())
print("Skriver ut de instalerte programmene: \n", instalerteProgrammer())