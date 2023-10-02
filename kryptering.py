
alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def kryptering(start_tekst, plassering, kryperingsretning):
    slutt_tekst = ""

    if kryperingsretning == "dekode":
        plassering *= -1

    for karakter in start_tekst:
        if karakter in alfabet:
            posisjon = alfabet.index(karakter)  
            ny_posisjon = posisjon + plassering
            slutt_tekst += alfabet[ny_posisjon]
        else:
            slutt_tekst += karakter
    
    print(f"\nHer er din {kryperingsretning}de setning: {slutt_tekst}")

gjenta = input("\nVelkommen! Vil du kryptere/dekryptere tekst, skriv 'ja' eller 'nei': ").lower()

while gjenta == "ja":
    krypteringsmodus = input("Skriv 'kode' for å kryptere og 'dekode' for å dekryptere: \n").lower()
    tekst = input("Skriv din melding: \n").lower()
    nummer_skift = int(input("Skriv et nummer du ønsker å forskyve bokstavene: \n"))
    nummer_skift = nummer_skift % 26
    kryptering(start_tekst=tekst, plassering=nummer_skift, kryperingsretning=krypteringsmodus)
    gjenta = input("\nVil du fortsette å kryptere/dekryptere, skriv 'ja' eller 'nei': ").lower()
else:
    print("Program slutt:)")
