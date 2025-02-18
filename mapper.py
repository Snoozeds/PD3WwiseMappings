import os
import json

# Folders
media_folder = r"F:\PD3 Modding\Tools\FModel\Output\Exports\PAYDAY3\Content\WwiseAudio\Media"
localized_folder = r"F:\PD3 Modding\Tools\FModel\Output\Exports\PAYDAY3\Content\WwiseAudio\Localized\English_US_\Media"

# Find ubulk files, return names without extension
def get_ubulk_file_names(folder):
    file_names = []
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith('.ubulk'):
                file_names.append(os.path.splitext(file)[0])  # Remove extension
    return file_names

media_ubulk_files = get_ubulk_file_names(media_folder)
localized_ubulk_files = get_ubulk_file_names(localized_folder)

# Save results to json files
def save_to_json(file_path, data):
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

save_to_json(r"media.json", media_ubulk_files)
save_to_json(r"localized.json", localized_ubulk_files)

print("JSON files have been created successfully.")
