import os
while True:
    os.system("cls" if os.name == "nt" else "clear")

    print("=========================")
    print("  Umstatzsteuerrechner   ")
    print("=========================")
    print("v Volle Umsatzsteuer berechnen")
    print("e Ermäßigte Umsatzsteuer berechnen")
    print("q Programm beenden")
    print("=========================")
    auswahl = input("Bitte treffen Sie ihre Wahl: ").lower().strip()
    if auswahl == "q":
        print("\nDas Programm wird beendet. Ich hoffe es hat Ihnen gefallen. Einen schönen Tag noch!")
        break
    elif auswahl == "v" or auswahl =="e":
        if auswahl == "v":
            steuersatz = 0.19
            print("\nDie volle Umsatzsteuer beträgt 19%")
        else:
            steuersatz =0.07
            print("\nDer ermäßigte Steuersatz beträgt 7%")
        try:
            netto = float(input("Bitte geben Sie den Nettopreis in Euro ein, beachten Sie die Eingabe in halben, vollen Zahlen: "))
            ust_betrag = netto * steuersatz
            brutto = netto + ust_betrag
            print(f"\nNettobetrag: {netto:,.2f} €")
            print(f"\nUmsatzsteuer: {ust_betrag:,.2f} €")
            print(f"\nBruttobetrag: {brutto:,.2f} €")

        except ValueError:
            print("\nFehler: Bitte geben Sie eine gültige Zahl ein(z.B. 15.50)!")
        print("-------------------------")
        input("Weiter mit Enter...")
    else:
        print("\nUngültige Auswahl! Bitte versuchen Sie es erneut.")
        input("Weiter mit Enter...")

