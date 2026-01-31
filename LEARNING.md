# 📚 MicroPython Essentials / Základy MicroPythonu

EN: This page serves as a quick reference for the core concepts used in our projects.  
CZ: Tato stránka slouží jako rychlý přehled hlavních pojmů, které používáme v našich projektech.

---

## 📦 Organization / Organizační prvky

| Concept / Pojem | What is it? / Co to je? | Example / Příklad | Meaning / Význam |
| :--- | :--- | :--- | :--- |
| **Module / Modul** | 🧰 Toolbox / Krabice s nářadím | `import machine` | Library of functions. / Balík funkcí pro hardware. |
| **Import** | 🔧 Taking a tool out / Vytažení nářadí | `from machine import Pin` | Ready for use. / Příprava nástroje k použití. |
| **Variable / Proměnná** | 🏷️ Data box / Krabička na data | `delay_time = 0.5` | Storage for values. / Místo, kam si ukládáš hodnoty. |

## 🤖 OOP (Objects & Classes) / Objektové programování

| Concept / Pojem | What is it? / Co to je? | Example / Příklad | Meaning / Význam |
| :--- | :--- | :--- | :--- |
| **Class / Třída** | 📐 Blueprint / Forma, Předpis | `Pin(...)` | Template for behavior. / Šablona, jak se má věc chovat. |
| **Object / Objekt** | 🛠️ Concrete piece / Konkrétní kus | `my_led = Pin(25, ...)` | Instance in memory. / Tvůj zástupce součástky v paměti. |
| **Method / Metoda** | ⚡ Action / Schopnost | `my_led.value(1)` | Command for the object. / Příkaz, aby objekt něco udělal. |
| **Argument** | 📝 Specification / Upřesnění | `(1)` or `(0.5)` | Data sent to method. / Data, která posíláš do metody. |

## ⚙️ Hardware Setup / Nastavení hardwaru

| Concept / Pojem | What is it? / Co to je? | Example / Příklad | Meaning / Význam |
| :--- | :--- | :--- | :--- |
| **Constant / Konstanta** | ⚓ Fixed setting / Pevné nastavení | `Pin.OUT` / `Pin.IN` | Setting direction. / Určení směru (ven/dovnitř). |

---

## 💻 Code Example / Příklad v kódu

```python
# 1. IMPORT: Taking tools from the box / Vytažení nářadí z krabice
from machine import Pin
import time

# 2. VARIABLE: Data storage (English name) / Krabička na data (anglický název)
delay_time = 0.5 

# 3. OBJECT: Creating a specific LED / Vytvoření konkrétní LED
# 'Pin' is the Class (Blueprint) / 'Pin' je třída (předpis)
# 'Pin.OUT' is a Constant (Setting) / 'Pin.OUT' je konstanta (nastavení)
my_led = Pin(15, Pin.OUT)

# 4. METHOD: Command for the object / Příkaz pro objekt
# '(1)' is the Argument (Action) / '(1)' je argument (upřesnění akce)
my_led.value(1)        # Turn ON / Zapnout

time.sleep(delay_time) # Use the variable / Použití proměnné
my_led.value(0)        # Turn OFF / Vypnout
