<div align="center">

# Simplebot
<p align="center">
    <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
    <img src="https://img.shields.io/badge/language-Python-blue" alt="Python">
</p>
Einfacher Chatbot um zu demonstrieren wie eine KI funktionieren würde.

---

### Voraussetzungen:

**Python-Version**: Python 3.6 oder höher.

---

### Installation:

#### **Python installieren**:
  Python 3.6 oder höher ist benötigt für diesen Projekt.
  
  Wenn du Python nicht hast, lade es hier herunter [python.org](https://www.python.org/downloads/)

#### **Repository klonen**:
Klone dieses Repository auf deinen lokalen Rechner:
  ```bash
git clone https://github.com/deinBenutzername/python-chatbot.git
  ```
Navigiere in das Verzeichnis des Projekts:
  ```bash
cd python-chatbot
  ```

#### **Chatbot ausführen**:
Starte den Chatbot mit dem folgenden Befehl:
  ```bash
python chatbot.py
  ```

---

### Verwendung:
Führe `chatbot.py` aus, um den Chatbot zu starten.

Gib eine Fragen ein, und der Chatbot wird antworten.

Wenn der Chatbot eine Frage nicht kennt, wird er dich nach der richtigen Antwort fragen und sie für zukünftige Interaktionen speichern.

Beende den Chat mit "bye".

---

</div>

> [!IMPORTANT]
> Der Chatbot speichert sein Antwortet in einer CSV-Datei (`ChatbotKnowledge.csv`).
>
> Ohne diese Datei kann der Chatbot kein neues Wissen speichern!

---

### Beispiel:
```
Chatbot: Hallo! Ich bin dein lernfähiger Chatbot. Wie kann ich dir helfen?
Du: Wie geht es dir?
Chatbot: Ich kenne die Antwort auf diese Frage noch nicht. Kannst du mir die Antwort sagen?
Antwort: Mir geht es gut, danke!
Chatbot: Danke, ich habe gelernt!
Du: Wie geht es dir?
Chatbot: Mir geht es gut, danke!
Du: bye
Chatbot: Tschüss! Bis zum nächsten Mal.
```
---

### Erweiterungsmöglichkeiten:
Da der Chatbot definitiv nicht fertig ist, gibt auch Erweiterungsmöglichkeiten:
- **Natürliche Sprachverarbeitung (NLP)**: Integriere Bibliotheken wie `spaCy` oder `NLTK`, um die Wortübereinstimmungen zu verbessern.
- **Mehrere Antworten**: Erlaube dem Chatbot, mehrere Antworten für dieselbe Frage zu speichern.
- **Datenbank**: Ersetze die CSV-Datei durch eine SQLite-Datenbank für bessere Skalierbarkeit.
- **find_best_match**: Ersetze find_best_match durch eine bessere funktion, um Antworten besser zu antworten.

---

### Lizenz:

Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen findest du in der `LICENSE`-Datei.

---

### Fazit:
Dieses Projekt sollte keine KI sein, sondern nur ein Demonstrationsprojekt sein, um zu zeigen wie Chatbots funktionieren.
