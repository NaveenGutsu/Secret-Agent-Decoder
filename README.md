# Secret Agent Message Scrambler

A beginner-friendly Python program that scrambles secret messages using a Caesar cipher. It takes any text, shifts each letter forward in the alphabet using a `for` loop, and outputs an encoded message.

---

# Features

* **Letter-by-letter encryption:** Uses a clean `for` loop to inspect and shift characters.
* **Wrap-around handling:** Uses modulo arithmetic (`% 26`) so letters past `z` loop neatly back to `a`.
* **Preserves formatting:** Keeps spaces and punctuation intact.

---

# How It Works

Think of the `for` loop like an assembly line:
1. Picks each character from the secret message one by one.
2. Finds its position in the alphabet (0 to 25).
3. Slides it forward by the secret shift key (e.g., $+3$ steps: $A \rightarrow D$).
4. Glues the new scrambled letter into the final secret code.

---

# Quick Start

1. **Clone the repository:**
   ```bash
