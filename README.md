# Inflation Report Austria

Ein Python-basiertes Tool zur Analyse und Vergleich der Inflationsraten zwischen Österreich, Deutschland und der Eurozone. Dieses Projekt ruft Echtzeit-Daten von Eurostat ab und generiert umfassende Berichte mit professionellen Visualisierungen.

## Features

- **Echtzeit-Daten**: Ruft die neuesten HICP (Harmonisierter Verbraucherpreisindex) Inflationsdaten von Eurostat ab
- **Umfassende Analyse**: 
  - Statistische Analyse (Durchschnitt, Median, Min, Max, Standardabweichung)
  - Jahr-für-Jahr Vergleich zwischen Österreich, Deutschland und Eurozone
  - Identifikation von Trends und Extremwerten
  - Historische Analyse seit 2002
  
- **12-Monats-Prognose**: 
  - Machine Learning basierte Vorhersage (Linear Regression)
  - 95% Konfidenzintervalle für Unsicherheitsabschätzung
  - Integration der Prognose in die Hauptvisualisierung

- **EZB-Leitzinsen**:
  - Hauptrefinanzierungssatz (Main Refinancing Rate)
  - Einlagefazilität (Deposit Facility Rate)
  - Historische Daten seit 2000

- **Professionelle Visualisierungen** (plotnine/ggplot2-Stil):
  - Inflationsvergleich mit integrierter 6-Monats-Prognose
  - EZB-Leitzinsen-Entwicklung
  - Inflationsdifferenz zwischen Ländern
  - Statistische Vergleichscharts
  - Langfristige historische Entwicklung seit 2002 mit kritischen Events (Finanzkrise, COVID-19, Ukraine-Krieg)
  - EU-weite Heatmap mit Ländernamen
  - Alle Plots mit Punktmarkern, professioneller Farbpalette und gestrichelten Gridlines

- **Interaktiver HTML-Report**: 
  - Modern gestalteter, responsiver HTML-Bericht
  - Eingebettete Visualisierungen
  - Übersichtliche Statistik-Karten
  - Prognose-Tabellen
  - Druckoptimiert

- **Text-Report**: Klassischer Textbericht für schnelle Übersicht

## Requirements

- Python 3.8 oder höher
- Abhängigkeiten in `requirements.txt`

## Installation

1. Repository klonen:
```bash
git clone https://github.com/jstreitberger03/inflation-report-austria.git
cd inflation-report-austria
```

2. Virtuelle Umgebung erstellen (empfohlen):
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux
```

3. Abhängigkeiten installieren:
```bash
pip install -r requirements.txt
```

## Verwendung

Führe das Hauptskript aus, um den kompletten Inflationsbericht zu generieren:

```bash
python main.py
```

## Output

Das Skript generiert folgende Dateien im `output/` Verzeichnis:

### Visualisierungen (SVG):
1. **inflation_comparison.svg** - Inflationsvergleich mit integrierter Prognose bis März 2026 und Konfidenzintervallen
2. **ecb_interest_rates.svg** - EZB-Leitzinsen (Hauptrefinanzierungssatz und Einlagefazilität)
3. **inflation_difference.svg** - Balkendiagramm der jährlichen Differenzen
4. **statistics_comparison.svg** - Statistische Kennzahlen im Vergleich
5. **historical_comparison.svg** - Langfristige Entwicklung seit 2002 mit markierten kritischen Events
6. **eu_inflation_heatmap.svg** - EU-weite Heatmap mit Ländernamen (Quartalsdurchschnitt)

### Berichte:
7. **inflation_report.html** - Interaktiver, modern gestalteter HTML-Bericht mit allen Visualisierungen und Analysen
8. **inflation_report.txt** - Klassischer Textbericht für schnelle Übersicht

## Technologie-Stack

- **plotnine** - ggplot2-ähnliche Syntax für professionelle statische Visualisierungen
- **pandas** - Datenmanipulation und -analyse
- **scikit-learn** - Machine Learning für Inflationsprognosen
- **eurostat** - API-Zugriff auf offizielle EU-Statistiken
- **numpy** - Numerische Berechnungen

### Warum plotnine statt plotly?

**plotnine** eignet sich hervorragend für:
- Statische, publikationsreife Grafiken
- Konsistente, professionelle Ästhetik
- Einfache Integration in Berichte und Papers
- ggplot2 Grammar of Graphics

**plotly** wäre besser für:
- Interaktive Dashboards
- Echtzeit-Updates
- User-Interaktion (Zoom, Hover, etc.)

Für diesen Anwendungsfall (statischer Report) ist plotnine die optimale Wahl.

## Datenquelle

Dieses Projekt nutzt die Eurostat-API für offizielle Inflationsdaten:
- **Dataset**: `prc_hicp_manr` (HCPI - monatliche Änderungsraten)
- **Regionen**: Österreich (AT), Deutschland (DE), Eurozone (EA20)
- **Zeitraum**: 2002 - heute (historisch), 2020 - heute (Hauptvisualisierungen)
- **EZB-Zinsen**: `irt_st_m` mit synthetischem Fallback

## Projektstruktur

```
inflation-report-austria/
├── main.py                      # Hauptskript für die Analyse
├── data_fetcher.py              # Modul zum Abrufen von Eurostat-Daten und Prognose
├── analysis.py                  # Statistische Analysefunktionen
├── visualization.py             # Generierung aller Visualisierungen (plotnine)
├── report_generator.py          # Textbericht-Generierung
├── html_report_generator.py     # Interaktiver HTML-Bericht
├── requirements.txt             # Python-Abhängigkeiten
├── README.md                    # Diese Datei
└── output/                      # Generierte Berichte (wird beim ersten Lauf erstellt)
    ├── *.svg                    # Alle Visualisierungen
    ├── inflation_report.html    # HTML-Bericht
    └── inflation_report.txt     # Text-Bericht
```

## Features im Detail

### Inflationsprognose
- Verwendet **Linear Regression** auf den letzten 12 Monaten
- Berechnet **95% Konfidenzintervalle**
- Unsicherheit wächst mit zunehmendem Prognosehorizont
- In Hauptvisualisierung integriert (gestrichelte Linie mit Schattierung)

### Kritische Events
Die historische Visualisierung markiert wichtige wirtschaftliche Ereignisse:
- **Finanzkrise 2008** (Lehman Brothers, 15. September 2008)
- **COVID-19 Pandemie** (WHO-Erklärung, 11. März 2020)
- **Ukraine-Krieg** (Invasionsbeginn, 24. Februar 2022)
- **Liberation Day** (Trump-Zölle, 20. Januar 2025)

### Visualisierungs-Stil
- **Farbpalette**: Professionell (#2E86AB, #A23B72, #F18F01)
- **Gridlines**: Gestrichelt (dotted) für bessere Lesbarkeit
- **Y-Achse**: 1.0% Schritte mit dichter Beschriftung
- **X-Achse**: 3-Monats-Intervalle mit deutschen Monatsnamen
- **Punktmarker**: Alle historischen Datenpunkte sichtbar
- **Hintergrund**: Helles Grau (#FAFAFA) für sanften Kontrast

## Beispiel-Output

Die Analyse liefert Einblicke wie:
- Aktuelle Inflationsraten für alle Regionen
- Historische Trends und Muster
- Jahre mit höchster/niedrigster Inflation
- Durchschnittliche Differenzen zwischen Regionen
- Kumulative Inflation über den Analysezeitraum
- Prognose bis März 2026 mit Unsicherheitsintervallen

## Lizenz

Dieses Projekt ist Open Source und steht für Bildungs- und Analysezwecke zur Verfügung.

## Mitwirken

Beiträge sind willkommen! Öffnen Sie gerne Issues oder reichen Sie Pull Requests ein.

## Autor
Julian Streitberger
Erstellt zur Analyse von Inflationstrends in Österreich im Vergleich zur Eurozone.