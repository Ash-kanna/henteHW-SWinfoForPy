import os as opperativsystem
from shutil import disk_usage 
mappeNavn2 = "maskin"
listeProgrammer = []

def hvilketOprativsystem():
    #Retunerer navnet på det nåværende opprativsystemmet
    osNavn = opperativsystem.name
    return osNavn


def hvorMyeLedigPlass():
    #Retunerer mengden ledig plass på disken i byte
    statvfsVar = disk_usage('C:/').free
    ledigPlass = statvfsVar / (2**30)
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
                    listeProgrammer.append(program)
        except:
            print("Kunne ikke finne listen over installerte programmer.")
    elif opperativsystem.name == "nt": #Windows
        try:
            programmer = []
            # Sjekk Program Files mappen
            program_files = "C:\\Program Files"
            program_files_x86 = "C:\\Program Files (x86)"
            
            if opperativsystem.path.exists(program_files):
                programmer.extend(opperativsystem.listdir(program_files))
            if opperativsystem.path.exists(program_files_x86):
                programmer.extend(opperativsystem.listdir(program_files_x86))
            
            print("Instalerte programmer på systemet:")
            for program in sorted(set(programmer)):  # Fjern duplikater og sorter
                print(program)
                listeProgrammer.append(program)
        except:
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
    filForOpen.write(f"Opprativsystemmet er:  {hvilketOprativsystem()} \nMengden ledig plass er:  {hvorMyeLedigPlass()} \nInnloggede brukeren er:  {hvemBrukerErLoggetInn()}. \nIP-adressen til maskinen er:  {hvilkenIPAdresse()} \nSkriver ut de instalerte programmene: {listeProgrammer}")
    filForOpen.close()

lagerMaskinMappe()
instalerteProgrammer()
print(samleAltIMappe())