# PLM Applicatie - Product Lifecycle Management Tool

## Overzicht
Deze applicatie stelt gebruikers in staat om een collectie kledingstijlen te beheren, inclusief het toevoegen, bekijken en verwijderen van stijlen. Het is ontworpen voor een productiemanager om een actuele collectie productinformatie bij te houden.

---

## Functionaliteiten
- **Stijlen toevoegen**:
  Vul informatie in zoals:
  - Naam van de stijl
  - Productcategorie
  - Gebruikte textielmaterialen
  - Matenreeks
  - Opmerkingen
- **Stijlen bekijken**:
  Gebruik de "VIEW" knop om alle stijlen in een overzichtelijke boomstructuur te zien.
- **Stijlen verwijderen**:
  Selecteer een stijl en gebruik de "DELETE" knop om deze te verwijderen.
- **Automatische opslag**:
  Alle gegevens worden automatisch opgeslagen in een CSV-bestand en hergebruikt bij een nieuwe sessie.

---

## Vereisten
1. **Besturingssysteem**: Windows of macOS.
2. **Geen installatie nodig voor de `.exe`**:
   U hoeft alleen het uitvoerbare bestand te openen.

---

## Installatie-instructies
### **Stap 1: Het uitvoerbare bestand uitvoeren**
1. Download het bestand `PLM_Application.exe`.
2. Plaats het bestand in een map op uw computer.
3. Dubbelklik op `PLM_Application.exe` om de applicatie te starten.

---

## Bestanden die worden aangemaakt:
- **Season_1.csv**: Bevat alle opgeslagen stijlen.
- **deleted_ids.txt**: Houdt de verwijderde stijl-ID's bij voor consistentie tussen sessies.

---

## Belangrijk
- Zorg ervoor dat de applicatie in dezelfde map blijft staan waarin het is gedownload.
- De gegenereerde bestanden (`Season_1.csv` en `deleted_ids.txt`) worden automatisch aangemaakt in dezelfde map als het programma.

---

## Veelgestelde vragen
1. **Wat als ik het CSV-bestand verwijder?**
   - De applicatie maakt automatisch een nieuw CSV-bestand aan.

2. **Kan ik handmatig iets in de bestanden aanpassen?**
   - Dit wordt niet aanbevolen. Laat de applicatie deze bestanden beheren.

3. **Kan ik de applicatie op een andere computer uitvoeren?**
   - Ja, zorg er wel voor dat alle bestanden in dezelfde map staan.

---

Bedankt voor het gebruiken van de PLM Applicatie!

