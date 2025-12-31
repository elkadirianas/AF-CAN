import pandas as pd
import os


matches_file = "afcon_matches.csv" 
events_file = "afcon_events.csv"                
output_dir = "split_data"


os.makedirs(output_dir, exist_ok=True)


print(" Loading Master Files...")
df_matches = pd.read_csv(matches_file)
df_events = pd.read_csv(events_file, low_memory=False)

stages_map = {
    "Group Stage": "1_group_stage",
    "Round of 16": "2_round_of_16",
    "Quarter-finals": "3_quarter_finals",
    "Semi-finals": "4_semi_finals",
    "3rd Place Final": "5_3rd_place",
    "Final": "6_final"
}

print(" Splitting files...")

for stage_name, file_prefix in stages_map.items():
    print(f"   Processing: {stage_name}...")
    
    stage_matches = df_matches[df_matches['competition_stage.name'] == stage_name]
    
    if stage_matches.empty:
        print(f"   ⚠️ No matches found for {stage_name}")
        continue

    match_ids = stage_matches['match_id'].unique()
    stage_events = df_events[df_events['match_id'].isin(match_ids)]
    
    match_filename = f"{file_prefix}_matches.csv"
    event_filename = f"{file_prefix}_events.csv"
    
    stage_matches.to_csv(f"{output_dir}/{match_filename}", index=False)
    stage_events.to_csv(f"{output_dir}/{event_filename}", index=False)
    
    print(f"     -> Saved {match_filename} & {event_filename}")

print("\n DONE! Upload the 'split_data' folder to your GitHub.")