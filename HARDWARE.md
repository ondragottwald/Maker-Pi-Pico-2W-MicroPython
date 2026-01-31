# 🛠️ Hardware & Software Setup / Nastavení HW a SW

EN: Technical information about the components and links to the necessary firmware.  
CZ: Technické informace o komponentách a odkazy na potřebný firmware.

---

## 🏗️ Hardware Components / Hardwarové komponenty

### 1. Raspberry Pi Pico 2 W
EN: The brain of the project. A powerful microcontroller with Wi-Fi and Bluetooth (RP2350).  
CZ: Mozek celého projektu. Výkonný mikrokontrolér s Wi-Fi a Bluetooth (čip RP2350).
* [👉 Official Page / Oficiální stránka (Raspberry Pi Foundation)](https://www.raspberrypi.com/products/raspberry-pi-pico-2/)

### 2. Cytron Maker Pi Pico Base
EN: Development board that simplifies wiring, adds LEDs for every GPIO, buttons, and a buzzer.  
CZ: Vývojová deska, která zjednodušuje zapojování, přidává LED pro každý GPIO, tlačítka a bzučák.
* [👉 Product Page / Stránka produktu (Cytron)](https://www.cytron.io/p-maker-pi-pico-base?srsltid=AfmBOoo6m3WgHxUjCycBb8a9sENatWQkNiM0VswFUOfH0-OlPAsLJCcm)

---

## 💾 Software & Firmware

### MicroPython Firmware (UF2)
EN: To run our code, you need to flash the MicroPython firmware onto your Pico 2 W.  
CZ: Pro běh našeho kódu je potřeba nahrát MicroPython firmware do tvého Pico 2 W.

* [📥 Download latest UF2 / Stáhnout nejnovější UF2 (micropython.org)](https://micropython.org/download/RPI_PICO2_W/)
    * *Note: Hold the BOOTSEL button while connecting USB, then drag and drop the downloaded file.*
    * *Poznámka: Držte tlačítko BOOTSEL při připojování USB, pak nahrajte stažený soubor.*

---

## 🔌 Pinout Summary / Přehled zapojení

| Component / Komponenta | GPIO Pin | Note / Poznámka |
| :--- | :--- | :--- |
| **Buzzer / Bzučák** | GP18 | Can be muted by a switch / Lze vypnout vypínačem. |
| **Audio Jack** | GP18, GP19 | Left & Right channel / Levý a pravý kanál. |
| **Button / Tlačítko 1** | GP20 | |
| **Button / Tlačítko 2** | GP21 | |
| **Button / Tlačítko 3** | GP22 | |
| **RGB LED (NeoPixel)** | GP28 | |
| **Micro SD Card** | GP10 - GP15 | SPI interface. |

### 🌳 Grove Connectors / Grove konektory
EN: These connectors allow easy connection of sensors without soldering.  
CZ: Tyto konektory umožňují snadné připojení senzorů bez pájení.

| Port | Pins (GPIO) | Ideal for / Ideální pro |
| :--- | :--- | :--- |
| **GROVE 1** | GP0, GP1 | Digital, UART, I2C |
| **GROVE 2** | GP2, GP3 | Digital, I2C |
| **GROVE 3** | GP4, GP5 | Digital, I2C |
| **GROVE 4** | GP16, GP17 | Digital, UART |
| **GROVE 5** | GP6, GP7 | Digital |
| **GROVE 6** | GP26, GP27 | **Analog (ADC)**, Digital |
