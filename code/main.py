from deepface import DeepFace
import cv2
from threading import Thread
import time
import Grafik


def Camera():
  global df
  time.clock()
  cap = cv2.VideoCapture(1)
  while True:
    success, img = cap.read()
    if success:
      cv2.imshow('rez', img)
      df = DeepFace.analyze(img, actions=['emotion'])
      # cv2.waitKey()
      if cv2.waitKey(1) & 0xff == ord('q'):
        break
    else:
      break

def main():
  global df
  Gra = Grafik.Grafik()
  tim = time.clock()
  while True:
    time.sleep(0.01)
    if df!={}:
      Emo_data = df["emotion"]
      if Emo_data != 0:
        Gra.update(time.clock()-tim, Emo_data)



if __name__=="__main__":
  df ={}
  th = Thread(target=Camera)
  th.start()
  main()
