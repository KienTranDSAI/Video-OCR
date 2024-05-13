from ocr import *
from tracking import *
from merge_box import *
import json
import os
from visual import *
import cv2
def pipeline(video_dir):
    file_name = os.listdir(video_dir)
    file_name = [i.split('.')[0] for i in file_name]
    for vid_name in file_name:
        #Get numframe
        video = cv2.VideoCapture(video_dir + f'/{vid_name}.mp4')
        num_frames = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
        video.release()

        with open(f"/home/kientran/Code/Work/OCR/pipeline/raw_results/{vid_name}.json", 'r') as file:
            result = json.load(file)
        # ##Remove low score
        remove_low_score_from_raw(result,vid_name)
        ##Tracking
        with open(f"/home/kientran/Code/Work/OCR/pipeline/remove_low_score/{vid_name}.json", 'r') as file:
            myDict = json.load(file)
        test = tracking(myDict)
        with open(f"/home/kientran/Code/Work/OCR/pipeline/tracking_results/{vid_name}.json", 'w') as file:
            json.dump(test, file)
        ##Merge boxes
        do_merge(vid_name, num_frame = num_frames)
        #Visual
        visualize(vid_name)
        print(vid_name)
        break

if __name__ == "__main__":

    pipeline("/home/kientran/Code/Work/OCR/Video")