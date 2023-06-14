#!/bin/python3 
import numpy as np
import cv2

def black_white(cap, median):
    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    grayMedianFrame = cv2.cvtColor(median, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Cinza', grayMedianFrame)
    cv2.imwrite('ACINZENTADO.jpg', grayMedianFrame)
    cv2.waitKey(0)

def get_src(src):
    import os # So serao usadas nessa funcao
    import sys # Depois removidas da memoria
    #print(f'{os.getcwd()}{sys.argv[0][1:]}')   Outra forma de fazer kk
    return os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), src) if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), src)) else 0

def reuse_StoredData(file, bw=False, cap=None):
    try:
        data = np.load(get_src(file))
        if bw and cap:
            black_white(cap, data)
        else:
            cv2.imshow('MEDIAN FRAME', data)
            cv2.waitKey(0)           
    except:
        print(f'O arquivo: {file} nao existe!')
        pass

if get_src('data.npy') != 0:
    #video = get_src('PEOPLE.mp4')
    video = get_src('fish.mp4')
    c = cv2.VideoCapture(video)
    reuse_StoredData('data.npy')
    cv2.waitKey(0)
    exit(0)

# -----------------  SOMENTE SE NAO JA TIVER SIDO PROCESSADO OS DADOS ANTES ---------------------->

def main():
    video = get_src('PEOPLE.mp4')
    #video = get_src('fish.mp4')
    if video == 0:
        print('O VIDEO NAO EXISTE!')
        exit(0)
    
    cap = cv2.VideoCapture(video)
    hasFrame, frame = cap.read()
    
    frames_ids = cap.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=72)
    
    frames = []
    for fid in frames_ids:
        cap.set(cv2.CAP_PROP_POS_FRAMES, fid)
        hasFrame, frame = cap.read()
        frames.append(frame)
    
    median = np.median(frames, axis=0).astype(dtype=np.uint8)
    print(median)
    
    np.save('data.npy', median)
    cv2.imshow('Median Frame', median)
    cv2.waitKey(0)

if __name__ == '__main__':
    main()
