# Meal Planner Agent (Lakto-ovo vegetarian)

Detta projekt innehåller en AI-agent byggd med LangChain som hjälper användaren att planera måltider.

Agenten är anpassad för en **lakto-ovo vegetarisk kost**, vilket innebär att ägg och mejeriprodukter är tillåtna, men inte kött eller fisk.

---

## Funktionalitet

Agenten kan:

* Föreslå måltider (frukost, lunch, middag)
* Anpassa förslag efter användarens preferenser
* Ge pedagogiska förklaringar till sina val
* Hålla kontext i en konversation (minne under körning)

---

## Systemprompt (sammanfattning)

Agenten:

- Är pedagogisk och förklarande
- Svarar alltid på svenska
- Tar hänsyn till variation, enkelhet och näring
- Följer strikt lakto-ovo vegetarisk kost

---

## Installation

### 1. Klona repot

```bash
git clone https://github.com/BigLurch/meal-planner-agent.git
cd meal-planner-agent
```

### 2. Installera beroenden med uv

```bash
uv sync
```

### 3. Skapa `.env`

Kopiera `.env.example` och fyll i dina värden:

```bash
cp .env.example .env
```

---

## Kör agenten

```bash
python examples/agent_lecture/meal_planner_agent.py
```

---

## Exempel på användning

```text
Jag vill ha en enkel vegetarisk middag
Gör den billig
Jag gillar inte svamp
Kan du ge mig en plan för hela veckan?
```

---

## Projektstruktur

```text
meal-planner-agent/
│
├── examples/
│   └── agent-lecture/
│       ├── meal_planner_agent.py
│       └── meal_planner_prompt.py
│
├── util/
│   ├── models.py
│   ├── streaming_utils.py
│   ├── tools.py
│   └── pretty_print.py
│
├── README.md
├── requirements.txt
├── .gitignore
└── .env.example
```

---

## Teknologi

* Python
* LangChain
* LangGraph (via kursens repo)
* uv (pakethantering)

---

## Syfte

Detta projekt är en del av en uppgift där tre olika AI-agenter ska utvecklas med olika funktionalitet.

Denna agent fokuserar på:
- Matplanering för lakto-ovo vegetarianer

---

## Författare

Skapad av BigLurch som en del av kursprojekt.
