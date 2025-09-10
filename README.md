### Steps to make own mappings:
1. Export all .ubulk (raw data) files from the audio folders in PAYDAY 3 using [FModel](https://fmodel.app/). You can right click folders to do this.
    - `PAYDAY3/Content/WwiseAudio/Media`, `PAYDAY3/Content/WwiseAudio/Localized/English_US_/Media`
2. Change the folders in `id_mapper.py` and run it.
3. Upload the resulting JSON files to GitHub or elsewhere.
4. Open PD3AudioModder, click the settings icon, advanced, and then change the URLs for "Wwise ID Mappings". Make sure the URL you are using links to the raw file, and ends in .json
     - For example: `https://raw.githubusercontent.com/Snoozeds/PD3WwiseMappings/refs/heads/main/media.json`
     - You can get this on GitHub by clicking the "Raw" button when viewing a file.
