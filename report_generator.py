"""
Module for generating text reports from inflation analysis.
"""
from datetime import datetime


def generate_text_report(df, stats, comparison, trends, output_dir='output'):
    """
    Erstellt einen umfassenden Textbericht der Inflationsanalyse.
    
    Args:
        df (pd.DataFrame): Verarbeitete Inflationsdaten.
        stats (dict): Wörterbuch mit Statistiken.
        comparison (pd.DataFrame): Monatlicher Vergleich.
        trends (dict): Daten zu Trends und Extremwerten.
        output_dir (str): Verzeichnis zum Speichern des Berichts.
        
    Returns:
        str: Pfad zum gespeicherten Bericht.
    """
    report_lines = []
    
    # Kopfzeile
    report_lines.append("=" * 80)
    report_lines.append("INFLATIONSBERICHT: ÖSTERREICH IM EUROPÄISCHEN VERGLEICH")
    report_lines.append("=" * 80)
    report_lines.append(f"Erstellt am: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report_lines.append("")
    
    # Zusammenfassung
    report_lines.append("ZUSAMMENFASSUNG")
    report_lines.append("-" * 80)
    
    # Datenbereich
    years = sorted(df['year'].unique())
    report_lines.append(f"Analysezeitraum: {years[0]} - {years[-1]}")
    report_lines.append("")
    
    # Aktuelle Inflationsraten
    for country in stats.keys():
        latest_rate = stats[country]['latest']
        latest_date = stats[country]['latest_date']
        report_lines.append(f"{country} - Aktuelle Inflationsrate ({latest_date.strftime('%B %Y')}): {latest_rate:.2f}%")
    report_lines.append("")
    
    # Statistische Kennzahlen
    report_lines.append("STATISTISCHE KENNZAHLEN (SEIT 2020)")
    report_lines.append("-" * 80)
    
    for country in stats.keys():
        report_lines.append(f"\n{country}:")
        report_lines.append(f"  Durchschnittliche Inflation: {stats[country]['mean']:.2f}%")
        report_lines.append(f"  Median der Inflation:      {stats[country]['median']:.2f}%")
        report_lines.append(f"  Minimale Inflation:        {stats[country]['min']:.2f}%")
        report_lines.append(f"  Maximale Inflation:        {stats[country]['max']:.2f}%")
        report_lines.append(f"  Standardabweichung:        {stats[country]['std']:.2f}")
    
    report_lines.append("")
    
    # Trends und Extremwerte
    report_lines.append("TRENDS UND EXTREMWERTE")
    report_lines.append("-" * 80)
    
    for country in trends.keys():
        report_lines.append(f"\n{country}:")
        report_lines.append(f"  Höchste Inflation: {trends[country]['highest_rate']:.2f}% im {trends[country]['highest_date'].strftime('%B %Y')}")
        report_lines.append(f"  Niedrigste Inflation: {trends[country]['lowest_rate']:.2f}% im {trends[country]['lowest_date'].strftime('%B %Y')}")
    
    report_lines.append("")
    
    # Jährlicher Vergleich
    report_lines.append("MONATLICHER VERGLEICH")
    report_lines.append("-" * 80)
    report_lines.append(f"{'Monat':<12} {'Österreich':<15} {'Deutschland':<15} {'Eurozone':<15} {'Differenz (AT-EA)':<20}")
    report_lines.append("-" * 80)
    
    # Letzte 12 Monate anzeigen
    for date in comparison.index[-12:]:
        austria_val = comparison.loc[date, 'Österreich']
        germany_val = comparison.loc[date, 'Deutschland']
        euro_val = comparison.loc[date, 'Eurozone']
        diff_val = comparison.loc[date, 'Difference (AT - EA)']
        
        report_lines.append(
            f"{date.strftime('%Y-%m'):<12} {austria_val:>8.2f}%      "
            f"{germany_val:>8.2f}%      {euro_val:>8.2f}%      "
            f"{diff_val:>8.2f} PP"
        )
    
    report_lines.append("")
    
    # Analyse-Zusammenfassung
    report_lines.append("ANALYSE-ZUSAMMENFASSUNG")
    report_lines.append("-" * 80)
    
    if 'Difference (AT - EA)' in comparison.columns:
        avg_diff = comparison['Difference (AT - EA)'].mean()
        months_higher = (comparison['Difference (AT - EA)'] > 0).sum()
        total_months = len(comparison)
        
        report_lines.append(f"Durchschnittliche Differenz (Österreich - Eurozone): {avg_diff:.2f} Prozentpunkte.")
        report_lines.append(f"Österreich hatte in {months_higher} von {total_months} Monaten ({months_higher/total_months:.1%}) eine höhere Inflation als die Eurozone.")
        
        if avg_diff > 0.1:
            report_lines.append("Im Durchschnitt war die Inflation in Österreich tendenziell höher als im Euroraum.")
        elif avg_diff < -0.1:
            report_lines.append("Im Durchschnitt war die Inflation in Österreich tendenziell niedriger als im Euroraum.")
        else:
            report_lines.append("Im Durchschnitt entsprach die Inflation in Österreich weitgehend der des Euroraums.")
    
    report_lines.append("")
    report_lines.append("=" * 80)
    report_lines.append("ENDE DES BERICHTS")
    report_lines.append("=" * 80)
    
    # In Datei schreiben
    import os
    output_path = os.path.join(output_dir, 'inflation_report.txt')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(report_lines))
    
    print(f"Textbericht gespeichert unter: {output_path}")
    return output_path


def print_summary(stats, trends):
    """
    Gibt eine kurze Zusammenfassung auf der Konsole aus.
    
    Args:
        stats (dict): Wörterbuch mit Statistiken.
        trends (dict): Daten zu Trends.
    """
    print("\n" + "=" * 80)
    print("ZUSAMMENFASSUNG DER INFLATIONSANALYSE")
    print("=" * 80)
    
    for country in stats.keys():
        print(f"\n{country}:")
        print(f"  Aktuell: {stats[country]['latest']:.2f}% ({stats[country]['latest_date'].strftime('%B %Y')})")
        print(f"  Durchschnitt (seit 2020): {stats[country]['mean']:.2f}%")
        print(f"  Spitzenwert: {trends[country]['highest_rate']:.2f}% ({trends[country]['highest_date'].strftime('%B %Y')})")
    
    print("\n" + "=" * 80)
