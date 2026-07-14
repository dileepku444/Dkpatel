"""Constants for the Raylogic integration."""

DOMAIN = "raylogic"

# Network
DEFAULT_PORT = 5550
CONNECT_TIMEOUT = 5
RECONNECT_DELAY = 30

# ------------------------------------------------------------------ #
# BR40 device codes (byte[1] of BR40 response header)
# Discovered via protocol reverse engineering
# ------------------------------------------------------------------ #
BR40_CODE_H81   = 0x01   # DIN-H81-RS485  — 8ch Triac Dimmer
BR40_CODE_RE16  = 0x09   # DIN-RE16-RS485 — 16ch Relay/Curtain
BR40_CODE_FN4   = 0x19   # DIN-FN4-RS485  — 4ch Fan Dimmer

# To be discovered via capture:
# BR40_CODE_RE8   = ?    # DIN-RE8-RS485  — 8ch Relay/Curtain
# BR40_CODE_HU4   = ?    # DIN-HU4-RS485  — 4ch Universal Dimmer
# BR40_CODE_F8    = ?    # DIN-F8-RS485   — 8ch Analog/DALI/PWM
# BR40_CODE_DALI  = ?    # DIN-DALI-64    — 64ch DALI Dimmer
# BR40_CODE_LDX   = ?    # LDX-405-CV     — 4ch LED Strip

# Device model names (for UI display and entity naming)
DEVICE_MODELS = {
    0x01: ("h81",  "DIN-H81-RS485",  "8ch Triac Dimmer"),
    0x09: ("re16", "DIN-RE16-RS485", "16ch Relay/Curtain Controller"),
    0x19: ("fn4",  "DIN-FN4-RS485",  "4ch Fan Dimmer"),
}

# ------------------------------------------------------------------ #
# RE16 relay channel modes (byte[1] of each BR40 channel record)
# ------------------------------------------------------------------ #
RE16_MODE_UNUSED  = 0x00
RE16_MODE_CURTAIN = 0x01
RE16_MODE_SWITCH  = 0x02

# ------------------------------------------------------------------ #
# Fan speeds: HA percentage → raw device level
# Confirmed via Docklight capture on DIN-FN4:
#   *AR=011A010119 = OFF      (level 01)
#   *AR=011A010219 = Speed 1  (level 02)
#   *AR=011A010319 = Speed 2  (level 03)
#   *AR=011A010419 = Speed 3  (level 04)
#   *AR=011A010519 = Speed 4 / Full (level 05)
# ------------------------------------------------------------------ #
FAN_SPEEDS = {0: 0x01, 25: 0x02, 50: 0x03, 75: 0x04, 100: 0x05}

# Platforms
PLATFORMS = ["light", "cover", "fan", "switch"]

# Sender node ID (app uses 003)
SENDER_NODE = "003"
