import os
import json

file_name = os.listdir("/home/kientran/Code/Work/OCR/pipeline/merge")
for name in file_name:
    full_path = os.path.join("/home/kientran/Code/Work/OCR/pipeline/merge", name)
    try:
        with open(full_path, 'r') as file:
            frameDict = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading {full_path}: {e}")
        continue

    for frameCount in frameDict.keys():
        for key in frameDict[frameCount]:
            tmp = frameDict[frameCount][key]['text_origin']
            if tmp.isupper():
                frameDict[frameCount][key]['Capitalization'] = 'all_caps'
            elif tmp.istitle():
                frameDict[frameCount][key]['Capitalization'] = 'start'
            elif tmp.islower():
                frameDict[frameCount][key]['Capitalization'] = 'no_caps'
            else:
                frameDict[frameCount][key]['Capitalization'] = 'standard'
    with open(f"/home/kientran/Code/Work/OCR/pipeline/features/{name}", 'w') as file:
        json.dump(frameDict, file)
