# 🎮 Mario Spectrum Player

EN: An audiovisual performance using the Raspberry Pi Pico 2 W and Maker Pi Pico base. 
CZ: Audiovizuální představení využívající Raspberry Pi Pico 2 W a desku Maker Pi Pico.

---

## 💡 Project Idea / Myšlenka projektu
EN: The goal was to map the Super Mario Main Theme to a visual spectrum. Each note has a unique frequency, which we assigned to a specific blue LED and a specific color on the RGB NeoPixel.  
CZ: Cílem bylo namapovat hlavní motiv Super Maria na vizuální spektrum. Každá nota má svou frekvenci, kterou jsme přiřadili konkrétní modré LEDce a konkrétní barvě na RGB NeoPixelu.

---

## 🌈 Color & Note Spectrum / Spektrum barev a not

EN: This table shows the exact mapping of musical notes to the hardware visual output.  
CZ: Tato tabulka ukazuje přesné mapování hudebních not na vizuální výstup hardwaru.

| Note / Nota | Frequency / Frekvence | LED Index | RGB Color / Barva | Visual / Vizuál |
| :--- | :--- | :--- | :--- | :--- |
| **E4** | 330 Hz | GP0 | Red / Červená | 🔴 |
| **G4** | 392 Hz | GP1 | Orange / Oranžová | 🟠 |
| **A4** | 440 Hz | GP2 | Yellow / Žlutá | 🟡 |
| **AS4** | 466 Hz | GP3 | Yellow-Green / Žlutozelená | 🟢🟡 |
| **B4** | 494 Hz | GP4 | Green / Zelená | 🟢 |
| **C5** | 523 Hz | GP5 | Turquoise / Tyrkysová | 💎 |
| **D5** | 587 Hz | GP6 | Cyan / Světle modrá | 🧊 |
| **E5** | 659 Hz | GP7 | Azure / Azurová | 🌊 |
| **F5** | 698 Hz | GP8 | Blue / Modrá | 🔵 |
| **G5** | 784 Hz | GP9 | Purple / Fialová | 🟣 |
| **A5** | 880 Hz | GP10 | Pink / Růžová | 🌸 |



---

## 🛠️ Features / Funkce
* **Dual Language Code:** Bilingual comments (EN/CZ) for better learning. / Dvojjazyčné komentáře pro snazší studium.
* **Hardware Sync:** Synchronized PWM buzzer, 13x blue LEDs, and 1x RGB NeoPixel. / Synchronizovaný bzučák, 13 modrých LED a 1 RGB NeoPixel.
* **Extended Melody:** Includes the bridge and main theme for a longer show. / Rozšířená melodie včetně "mostu" a hlavního tématu pro delší show.

## 🚀 How to run it / Jak to spustit
1. **EN:** Copy the code from `main.py` to your Pico 2 W.  
   **CZ:** Zkopírujte kód z `main.py` do vašeho Pico 2 W.
2. **EN:** Ensure you have the `neopixel` library (standard in MicroPython).  
   **CZ:** Ujistěte se, že máte knihovnu `neopixel` (standardní součást MicroPythonu).
3. **EN:** Press **Run** in Thonny and enjoy the show!  
   **CZ:** Stiskněte **Run** v Thonny a užijte si show!

---
*Created by Ondra Gottwald | Týniště nad Orlicí*
