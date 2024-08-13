import os
import pandas as pd
from llama_index.experimental.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str

data_dir = "csv"

all_stats_df = pd.DataFrame()

# Liste zum Speichern einzelner Bundesliga DataFrames
dataframes_list = []

# Durchlaufen aller Dateien im Verzeichnis "data_dir"
for filename in os.listdir(data_dir):
    # Überprüfen, ob die Datei eine CSV-Datei ist und "bundesliga" im Dateinamen enthält
    if filename.endswith(".csv") and "2-bundesliga" in filename.lower():
        file_path = os.path.join(data_dir, filename)
        
        # Extrahieren von Liga und Saison aus dem Dateinamen
        parts = filename.replace(".csv", "").split("_")
        league = parts[0]
        season = parts[-1]
        
        # Laden der CSV-Datei in einen DataFrame
        single_df = pd.read_csv(file_path)
        # Hinzufügen der Saison- und Liga-Informationen als neue Spalten
        single_df['Season'] = season
        single_df['League'] = league
        
        # Hinzufügen des DataFrames zur Liste
        dataframes_list.append(single_df)
        
        # Hinzufügen des DataFrames zum all_stats_df
        all_stats_df = pd.concat([all_stats_df, single_df], ignore_index=True)

print(all_stats_df.head()) 
        
secondBundesliga_query_engine = PandasQueryEngine(df=all_stats_df, verbose=True, instruction_str=instruction_str)
secondBundesliga_query_engine.update_prompts({"pandas_prompt": new_prompt})