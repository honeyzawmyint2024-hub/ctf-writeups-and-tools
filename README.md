# APU Internal CTF 2026 — AvoidImpossible Writeup & Solvers

![CTF Category](https://img.shields.io/badge/Category-Reverse%20Engineering-blue)
![Difficulty](https://img.shields.io/badge/Difficulty-Medium%20(255%20pts)-orange)
![Language](https://img.shields.io/badge/Language-Python%203%20%7C%20C%23-green)

Detailed write-up, analysis, and custom Python solver scripts for the **AvoidImpossible** reverse engineering challenge featured in the **APU Internal CTF (ICTF 2026)** competition.

---

## 📌 Challenge Overview

* **Event:** APU Internal CTF 2026 (FSEC-SS)
* **Team:** SKIBIDI
* **Challenge Name:** AvoidImpossible
* **Category:** Reverse Engineering
* **Difficulty:** Medium (255 points)
* **Flag:** `ICTF26{FF6E45AC-2D3D-4F4C-A72C-03C50ECD5D5E}`

The challenge presents a Windows `.NET` assembly executable (`AvoidImpossible.exe`) running a retro invader-style arcade game. While the game requires surviving a 15-second timer and collecting bonus items, the real goal is to reverse-engineer the application logic, bypass execution checks, and solve four underlying mathematical/cryptographic puzzles.

---

## 🛠️ Tools & Methodology

| Tool | Purpose |
| :--- | :--- |
| **file / CLI** | Identified PE32 Intel 80386 Mono/.NET assembly architecture. |
| **dnSpy v6.1.8** | Decompiled MSIL bytecode back to C# source code and performed IL instruction patching. |
| **Python 3** | Developed custom automated solvers for all four puzzles and final XOR flag extraction. |
| **Hex Editor / Resources** | Extracted embedded assets (`extracted_soundtrack.mp3`). |

---

## 🧩 Solution Breakdown

### Step 1: Binary Decompilation & Patching
- Decompiled `AvoidImpossible.exe` using **dnSpy** to reveal C# source code structure (`Game`, `GameEngine`, `BonusObject`).
- Patched the game timer check inside `GameLoop()` (`this.elapsedTime.TotalSeconds >= 15.0`) down to `0.0` using IL instruction editing to bypass survival gameplay and trigger the `GOAL` state immediately.
- Uncovered the **Final Decryption Protocol**:
  $$\text{Flag} = \text{ENCRYPTED\_FLAG} \oplus \text{Key1} \oplus \text{Key2}$$
  * **Key1:** `bonus1_bonus2_bonus3_bonus4` (4 puzzle answers joined by underscores)
  * **Key2:** `SHA256(game_soundtrack.mp3)`

---

### Step 2: Puzzle Solvers

| Script | Strategy & Algorithm | Discovered Answer |
| :--- | :--- | :--- |
| `Puzzle1.py` | Brute-force over 6-character strings using polynomial rolling hash ($31$), weighted sum modulo $10000$, and pair products. | **`sacred`** |
| `Puzzle2.py` | Generates permutations of 6 distinct letters and checks SHA-256 big-endian byte unpack values (`struct.unpack`). | **`forest`** |
| `Puzzle3.py` | Fixed outer bounds (`t...e`), iterated SHA-256 key-stretching (1,000 rounds) with double salt constants (`salt1` & `salt2`). | **`temple`** |
| `Puzzle4.py` | Multi-layered arithmetic chain: sum check ($667$), running product modulo $65536$, powers of $137$ weighted sum $\oplus\text{0xDEADBEEF}$, pair relations (golden ratio constant $2654435769$), and sum of squares. | **`spirit`** |

---

### Step 3: Final Decryption (`flag.py`)
1. **Key1 Construction:** `sacred_forest_temple_spirit`
2. **Key2 Construction:** SHA-256 digest of the extracted asset `extracted_soundtrack.mp3` (`54bdce7e44be47e0...`).
3. **XOR Extraction:** Cyclic double-XOR decryption applied over the 44-byte static `ENCRYPTED_FLAG` array extracted from dnSpy.

```bash
$ python3 flag.py
MP3 loaded: 2212604 bytes
key2: 54bdce7e44be47e00a6fa3a565fb37af3169f83b19fe11842726544509ae1b0e
key1: sacred_forest_temple_spirit

Flag: ICTF26{FF6E45AC-2D3D-4F4C-A72C-03C50ECD5D5E}
