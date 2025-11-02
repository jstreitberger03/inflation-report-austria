"""
Module for generating HTML reports from inflation analysis.
"""
from datetime import datetime
import os


def generate_html_report(df, stats, comparison, trends, forecast_df, output_dir='output'):
    """
    Generate a comprehensive HTML report of the inflation analysis.
    
    Args:
        df (pd.DataFrame): Processed inflation data
        stats (dict): Statistics dictionary
        comparison (pd.DataFrame): Month-by-month comparison
        trends (dict): Trends and extremes data
        forecast_df (pd.DataFrame): Forecast data
        output_dir (str): Directory to save the report
        
    Returns:
        str: Path to the saved report
    """
    
    # Get data range
    years = sorted(df['year'].unique())
    
    html_content = f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inflationsbericht Österreich {years[-1]}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #f5f5f5;
            min-height: 100vh;
            padding: 20px;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            overflow: hidden;
        }}
        
        header {{
            background: #2c3e50;
            color: white;
            padding: 40px;
            border-bottom: 3px solid #34495e;
        }}
        
        header h1 {{
            font-size: 2.2em;
            margin-bottom: 10px;
            font-weight: 600;
        }}
        
        header p {{
            font-size: 1.1em;
            color: #ecf0f1;
        }}
        
        .content {{
            padding: 40px;
        }}
        
        .section {{
            margin-bottom: 40px;
        }}
        
        .section-title {{
            font-size: 1.6em;
            color: #2c3e50;
            margin-bottom: 20px;
            padding-bottom: 10px;
            border-bottom: 2px solid #bdc3c7;
            font-weight: 600;
        }}
        
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}
        
        .card {{
            background: #fafafa;
            padding: 25px;
            border: 1px solid #e0e0e0;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }}
        
        .card h3 {{
            color: #2c3e50;
            font-size: 1.3em;
            margin-bottom: 15px;
            font-weight: 600;
        }}
        
        .stat {{
            display: flex;
            justify-content: space-between;
            padding: 8px 0;
            border-bottom: 1px solid #dee2e6;
        }}
        
        .stat:last-child {{
            border-bottom: none;
        }}
        
        .stat-label {{
            font-weight: 600;
            color: #666;
        }}
        
        .stat-value {{
            font-weight: bold;
            color: #2c3e50;
        }}
        
        .highlight-box {{
            background: #34495e;
            color: white;
            padding: 30px;
            margin-bottom: 30px;
            border-left: 4px solid #2c3e50;
        }}
        
        .highlight-box h3 {{
            font-size: 1.4em;
            margin-bottom: 15px;
            font-weight: 600;
        }}
        
        .highlight-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }}
        
        .highlight-item {{
            text-align: center;
            padding: 15px;
            background: rgba(255,255,255,0.15);
            border: 1px solid rgba(255,255,255,0.2);
        }}
        
        .highlight-value {{
            font-size: 2.2em;
            font-weight: 600;
            display: block;
            margin-bottom: 5px;
        }}
        
        .highlight-label {{
            font-size: 1em;
            color: #ecf0f1;
        }}
        
        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
            background: white;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            border-radius: 8px;
            overflow: hidden;
        }}
        
        th {{
            background: #2c3e50;
            color: white;
            padding: 15px;
            text-align: left;
            font-weight: 600;
        }}
        
        td {{
            padding: 12px 15px;
            border-bottom: 1px solid #dee2e6;
        }}
        
        tr:hover {{
            background: #f8f9fa;
        }}
        
        .positive {{
            color: #e74c3c;
            font-weight: bold;
        }}
        
        .negative {{
            color: #27ae60;
            font-weight: bold;
        }}
        
        .images-grid {{
            display: grid;
            grid-template-columns: 1fr;
            gap: 30px;
            margin-top: 30px;
        }}
        
        .image-container {{
            background: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}
        
        .image-container h3 {{
            color: #2c3e50;
            margin-bottom: 15px;
            font-size: 1.2em;
            font-weight: 600;
        }}
        
        .image-container object {{
            width: 100%;
            height: auto;
            border: 1px solid #e0e0e0;
        }}
        
        footer {{
            background: #2c3e50;
            color: #ecf0f1;
            text-align: center;
            padding: 25px;
            font-size: 0.9em;
            border-top: 1px solid #34495e;
        }}
        
        .forecast-box {{
            background: #f8f9fa;
            border-left: 4px solid #34495e;
            padding: 20px;
            margin: 20px 0;
        }}
        
        .forecast-box h4 {{
            color: #2c3e50;
            margin-bottom: 10px;
            font-weight: 600;
        }}
        
        @media print {{
            body {{
                background: white;
                padding: 0;
            }}
            
            .container {{
                box-shadow: none;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Inflationsbericht Österreich</h1>
            <p>Analyse der Inflationsentwicklung {years[0]} - {years[-1]}</p>
            <p style="font-size: 0.9em; margin-top: 10px; color: #bdc3c7;">Erstellt am {datetime.now().strftime('%d.%m.%Y')}</p>
        </header>
        
        <div class="content">
            <!-- Executive Summary -->
            <div class="highlight-box">
                <h3>Aktuelle Inflationsraten (Stand: {stats['Österreich']['latest_date'].strftime('%B %Y').encode('latin1').decode('utf-8', errors='replace')})</h3>
                <div class="highlight-grid">
"""
    
    # Add current inflation rates
    for country in ['Österreich', 'Deutschland', 'Eurozone']:
        if country in stats:
            html_content += f"""                    <div class="highlight-item">
                        <span class="highlight-value">{stats[country]['latest']:.2f}%</span>
                        <span class="highlight-label">{country}</span>
                    </div>
"""
    
    html_content += """                </div>
            </div>
            
            <!-- Key Statistics -->
            <div class="section">
                <h2 class="section-title">Statistische Kennzahlen</h2>
                <div class="grid">
"""
    
    # Add statistics cards
    for country in ['Österreich', 'Deutschland', 'Eurozone']:
        if country in stats:
            html_content += f"""                    <div class="card">
                        <h3>{country}</h3>
                        <div class="stat">
                            <span class="stat-label">Durchschnitt:</span>
                            <span class="stat-value">{stats[country]['mean']:.2f}%</span>
                        </div>
                        <div class="stat">
                            <span class="stat-label">Median:</span>
                            <span class="stat-value">{stats[country]['median']:.2f}%</span>
                        </div>
                        <div class="stat">
                            <span class="stat-label">Maximum:</span>
                            <span class="stat-value">{stats[country]['max']:.2f}%</span>
                        </div>
                        <div class="stat">
                            <span class="stat-label">Minimum:</span>
                            <span class="stat-value">{stats[country]['min']:.2f}%</span>
                        </div>
                        <div class="stat">
                            <span class="stat-label">Standardabweichung:</span>
                            <span class="stat-value">{stats[country]['std']:.2f}%</span>
                        </div>
                    </div>
"""
    
    html_content += """                </div>
            </div>
"""
    
    # Add forecast section
    if forecast_df is not None and len(forecast_df) > 0:
        # Filter to March 2026
        import pandas as pd
        forecast_df_filtered = forecast_df[forecast_df['date'] <= '2026-03-31'].copy()
        
        html_content += """            <!-- Forecast -->
            <div class="section">
                <h2 class="section-title">Inflationsprognose</h2>
                <div class="forecast-box">
                    <h4>Prognose bis März 2026 mit 95% Konfidenzintervall</h4>
                    <p>Basierend auf linearer Regression der letzten 12 Monate unter Verwendung des HCPI (Harmonisierter Verbraucherpreisindex).</p>
                </div>
                
                <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 20px;">
"""
        
        # Group by country and create side-by-side tables
        for country in ['Österreich', 'Deutschland', 'Eurozone']:
            country_forecast = forecast_df_filtered[forecast_df_filtered['country'] == country].sort_values('date')
            if len(country_forecast) > 0:
                html_content += f"""                    <div>
                        <h4 style="text-align: center; margin-bottom: 10px; color: #2c3e50;">{country}</h4>
                        <table style="width: 100%; font-size: 0.9em;">
                            <thead>
                                <tr>
                                    <th>Monat</th>
                                    <th>Prognose</th>
                                    <th>Bereich</th>
                                </tr>
                            </thead>
                            <tbody>
"""
                
                for _, row in country_forecast.iterrows():
                    # Format date properly for German month names
                    month_names = {
                        1: 'Jan', 2: 'Feb', 3: 'Mär', 4: 'Apr', 5: 'Mai', 6: 'Jun',
                        7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Okt', 11: 'Nov', 12: 'Dez'
                    }
                    month_str = f"{month_names[row['date'].month]} {row['date'].year}"
                    html_content += f"""                                <tr>
                                    <td>{month_str}</td>
                                    <td><strong>{row['inflation_rate']:.2f}%</strong></td>
                                    <td style="font-size: 0.85em; color: #666;">{row['lower_bound']:.2f}% - {row['upper_bound']:.2f}%</td>
                                </tr>
"""
                
                html_content += """                            </tbody>
                        </table>
                    </div>
"""
        
        html_content += """                </div>
            </div>
"""
    
    # Add trends section
    html_content += """            <!-- Trends and Extremes -->
            <div class="section">
                <h2 class="section-title">Höchst- und Tiefstwerte</h2>
                <div class="grid">
"""
    
    for country in ['Österreich', 'Deutschland', 'Eurozone']:
        if country in trends:
            # Format dates properly for German month names
            month_names = {
                1: 'Januar', 2: 'Februar', 3: 'März', 4: 'April', 5: 'Mai', 6: 'Juni',
                7: 'Juli', 8: 'August', 9: 'September', 10: 'Oktober', 11: 'November', 12: 'Dezember'
            }
            highest_month = f"{month_names[trends[country]['highest_date'].month]} {trends[country]['highest_date'].year}"
            lowest_month = f"{month_names[trends[country]['lowest_date'].month]} {trends[country]['lowest_date'].year}"
            
            html_content += f"""                    <div class="card">
                        <h3>{country}</h3>
                        <div class="stat">
                            <span class="stat-label">Höchster Wert:</span>
                            <span class="stat-value positive">{trends[country]['highest_rate']:.2f}%</span>
                        </div>
                        <div class="stat">
                            <span class="stat-label">Zeitpunkt:</span>
                            <span class="stat-value">{highest_month}</span>
                        </div>
                        <div class="stat">
                            <span class="stat-label">Niedrigster Wert:</span>
                            <span class="stat-value negative">{trends[country]['lowest_rate']:.2f}%</span>
                        </div>
                        <div class="stat">
                            <span class="stat-label">Zeitpunkt:</span>
                            <span class="stat-value">{lowest_month}</span>
                        </div>
                    </div>
"""
    
    html_content += """                </div>
            </div>
            
            <!-- Visualizations -->
            <div class="section">
                <h2 class="section-title">Visualisierungen</h2>
                <div class="images-grid">
                    <div class="image-container">
                        <h3>Inflationsrate im Vergleich mit Prognose</h3>
                        <object data="inflation_comparison.svg" type="image/svg+xml" style="width:100%; height:500px;">
                            <p>SVG wird nicht unterstützt.</p>
                        </object>
                    </div>
                    <div class="image-container">
                        <h3>EZB-Leitzinsen</h3>
                        <object data="ecb_interest_rates.svg" type="image/svg+xml" style="width:100%; height:500px;">
                            <p>SVG wird nicht unterstützt.</p>
                        </object>
                    </div>
                    <div class="image-container">
                        <h3>Inflationsdifferenz</h3>
                        <object data="inflation_difference.svg" type="image/svg+xml" style="width:100%; height:450px;">
                            <p>SVG wird nicht unterstützt.</p>
                        </object>
                    </div>
                    <div class="image-container">
                        <h3>Statistische Vergleiche</h3>
                        <object data="statistics_comparison.svg" type="image/svg+xml" style="width:100%; height:550px;">
                            <p>SVG wird nicht unterstützt.</p>
                        </object>
                    </div>
                    <div class="image-container">
                        <h3>Langfristige Entwicklung seit 2002</h3>
                        <object data="historical_comparison.svg" type="image/svg+xml" style="width:100%; height:500px;">
                            <p>SVG wird nicht unterstützt.</p>
                        </object>
                    </div>
                    <div class="image-container">
                        <h3>EU-weiter Vergleich (Heatmap)</h3>
                        <object data="eu_inflation_heatmap.svg" type="image/svg+xml" style="width:100%; height:600px;">
                            <p>SVG wird nicht unterstützt.</p>
                        </object>
                    </div>
                </div>
            </div>
            
            <!-- Analysis Summary -->
            <div class="section">
                <h2 class="section-title">Zusammenfassung</h2>
                <div class="card">
"""
    
    if 'Difference (AT - EA)' in comparison.columns:
        # Filter to 2020 onwards for summary
        comparison_filtered = comparison[comparison.index.year >= 2020] if hasattr(comparison.index, 'year') else comparison[comparison.index >= 2020]
        avg_diff = comparison_filtered['Difference (AT - EA)'].mean()
        years_higher = (comparison_filtered['Difference (AT - EA)'] > 0).sum()
        total_years = len(comparison_filtered)
        
        html_content += f"""                    <p style="font-size: 1.1em; margin-bottom: 15px;">
                        Die durchschnittliche Differenz zwischen österreichischer und Eurozone-Inflation beträgt 
                        <strong>{avg_diff:.2f} Prozentpunkte</strong> seit 2020.
                    </p>
                    <p style="font-size: 1.1em;">
                        Österreich hatte in <strong>{years_higher} von {total_years} Monaten</strong> eine höhere 
                        Inflation als die Eurozone.
                    </p>
"""
    
    html_content += """                </div>
            </div>
        </div>
        
        <footer>
            <p><strong>Datenquelle:</strong> Eurostat - Harmonisierter Verbraucherpreisindex (HICP)</p>
            <p style="margin-top: 5px;">Generiert mit Python, plotnine, pandas und scikit-learn</p>
            <p style="margin-top: 15px; font-size: 0.95em;">&copy; {0} Julian Streitberger</p>
        </footer>
    </div>
</body>
</html>""".format(datetime.now().year)
    
    # Save HTML file
    output_path = os.path.join(output_dir, 'inflation_report.html')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Saved HTML report to {output_path}")
    return output_path
