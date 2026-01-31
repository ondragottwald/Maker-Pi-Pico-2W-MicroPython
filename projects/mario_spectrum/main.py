# --- MARIO THEME: EXTENDED SPECTRUM MODE ---
# EN: Extended melody with fixed LED and color per note
# CZ: Rozšířená melodie s pevnou LED a barvou pro každou notu

from machine import Pin, PWM
import time
import neopixel

# 1. SETUP: Hardware / Nastavení hardwaru
buzzer = PWM(Pin(18))
led_pins = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
leds = [Pin(p, Pin.OUT) for p in led_pins]
rgb = neopixel.NeoPixel(Pin(28), 1)

# 2. DATA: Frequencies / Hudební frekvence
NOTE_E4 = 330
NOTE_G4 = 392
NOTE_A4 = 440
NOTE_AS4 = 466
NOTE_B4 = 494
NOTE_C5 = 523
NOTE_D5 = 587
NOTE_E5 = 659
NOTE_F5 = 698
NOTE_G5 = 784
NOTE_A5 = 880

# 3. MAPPING: Assign LED and Color to each Note
# CZ: Přiřazení LEDky a barvy (R, G, B) každé notě
note_map = {
    NOTE_E4:  (0,  (40, 0, 0)),    # Red
    NOTE_G4:  (1,  (40, 20, 0)),   # Orange
    NOTE_A4:  (2,  (40, 40, 0)),   # Yellow
    NOTE_AS4: (3,  (20, 40, 0)),   # Light Green
    NOTE_B4:  (4,  (0, 40, 0)),    # Green
    NOTE_C5:  (5,  (0, 40, 20)),   # Turquoise
    NOTE_D5:  (6,  (0, 40, 40)),   # Cyan
    NOTE_E5:  (7,  (0, 20, 40)),   # Azure
    NOTE_F5:  (8,  (0, 0, 40)),    # Blue
    NOTE_G5:  (9,  (20, 0, 40)),   # Purple
    NOTE_A5:  (10, (40, 0, 20))    # Pink
}

# 4. MELODY: Extended Main Theme / Rozšířená hlavní melodie
mario_melody = [
    # Main Theme / Hlavní motiv
    NOTE_E5, NOTE_E5, 0, NOTE_E5, 0, NOTE_C5, NOTE_E5, 0, NOTE_G5, 0, NOTE_G4, 0,
    NOTE_C5, 0, NOTE_G4, 0, NOTE_E4, 0, NOTE_A4, 0, NOTE_B4, 0, NOTE_AS4, NOTE_A4,
    NOTE_G4, NOTE_E5, NOTE_G5, NOTE_A5, 0, NOTE_F5, NOTE_G5, 0, NOTE_E5, 0, NOTE_C5, NOTE_D5, NOTE_B4,
    0,
    # Second part / Druhá část
    NOTE_C5, 0, NOTE_G4, 0, NOTE_E4, 0, NOTE_A4, 0, NOTE_B4, 0, NOTE_AS4, NOTE_A4,
    NOTE_G4, NOTE_E5, NOTE_G5, NOTE_A5, 0, NOTE_F5, NOTE_G5, 0, NOTE_E5, 0, NOTE_C5, NOTE_D5, NOTE_B4,
    # Bridge / Most
    NOTE_G5, NOTE_F5, NOTE_E5, NOTE_AS4, NOTE_A4, NOTE_G4, 
    NOTE_E5, NOTE_E5, 0, NOTE_E5, 0, NOTE_C5, NOTE_E5, 0, NOTE_G5, 0, NOTE_G4
]

# 5. SETTINGS / Nastavení
tempo = 0.15 

# 6. METHODS / Metody
def play_note(frequency, duration):
    if frequency in note_map:
        led_idx, color = note_map[frequency]
        
        rgb[0] = color
        rgb.write()
        leds[led_idx].value(1)
        
        buzzer.freq(frequency)
        buzzer.duty_u16(32768)
        
        time.sleep(duration)
        
        buzzer.duty_u16(0)
        leds[led_idx].value(0)
        rgb[0] = (0, 0, 0)
        rgb.write()
    else:
        time.sleep(duration)
    
    time.sleep(0.05)

# 7. MAIN LOOP / Hlavní smyčka
print("🎼 Playing EXTENDED Mario Spectrum! / Hraji ROZŠÍŘENÉ Mario spektrum!")

for note in mario_melody:
    play_note(note, tempo)

print("🏁 Performance finished! / Představení skončilo!")
