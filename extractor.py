import cv2
import numpy as np

class Extractor():
    def __init__(self):
        self.orb = cv2.ORB_create(100)
        self.bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        self.last = None 
    def extract(self, img):
        # detection
        features = cv2.goodFeaturesToTrack(np.mean(img,axis=2).astype(np.uint8), qualityLevel=0.01, minDistance=3, maxCorners=3000)
        
        # extraction 
        kps = [cv2.KeyPoint(x=f[0][0], y=f[0][1], size=20) for f in features]
        kps, des = self.orb.compute(img, kps)
        
        # matching
        matches = None
        if self.last is not None:
            matches = self.bf.match(des, self.last["des"])
            matches = zip([kps[m.queryIdx] for m in matches], [self.last['kps'][m.trainIdx] for m in matches])
        
        self.last = {"kps": kps, "des": des}
        return matches