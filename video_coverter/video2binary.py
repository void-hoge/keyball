#!/usr/bin/env python3

import cv2
import sys
import time
import numpy as np

def main():
    path = sys.argv[1]
    video = cv2.VideoCapture(path)
    count = 0
    frames = []
    while (frame := video.read())[0] and (count := count + 1) <= 24:
        if count % 3 in [1, 2]:
            continue
        _, image = frame
        width, height, channel = image.shape
        resized = cv2.resize(image, (64, 36), interpolation=cv2.INTER_AREA)
        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
        binarized = np.where(gray >= 128, 255, 0).astype(np.uint8)
        clipped = binarized[2:2+32, 16:16+32]
        # cv2.imshow('video', clipped)
        frames.append(clipped)
    binframes = [np.where(frame == 255, 0, 1).astype(np.uint8) for frame in frames]
    binframes[0][14][23] = 0
    binframes[0][13][23] = 1
    binframes[1][11][22] = 1
    binframes[2][10][21] = 1
    binframes[3][13][9] = 1
    binframes[3][14][9] = 0
    binframes[4][13][9] = 1
    binframes[6][11][11] = 1
    binframes[7][13][23] = 1
    for frame in binframes:
        page = []
        tframe = frame.T
        for raw in range(0, 32, 8):
            for col in range(0, 32):
                num = 0
                for i in range(8):
                    num |= tframe[raw + i][col] << i
                page.append(f'0x{num:02x}')
        print(f'{{{", ".join(page)}}},')
    while True:
        for frame in frames:
            cv2.imshow('video', frame)
            if cv2.waitKey(80) & 0xff == ord('q'):
                return

if __name__ == '__main__':
    main()
