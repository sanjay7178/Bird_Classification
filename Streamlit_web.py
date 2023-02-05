from streamlit_webrtc import webrtc_streamer, RTCConfiguration
from labels import label
import Recognition
import cv2
import av

model = Recognition.load_model()

class VideoProcessor:
    def recv(self, frame):
        frm = frame.to_ndarray(format="bgr24")

        idxs, conf, bboxs = model.detect(frm, 0.6)
        if len(idxs) != 0:
            for idx, _, bbox in zip(idxs.flatten(), conf, bboxs):
                class_name = label.get(idx, 'unknown')

                cv2.rectangle(frm, bbox, color=(255, 0, 0), thickness=2)
                cv2.putText(frm, class_name, (bbox[0]+10, bbox[1]+30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), thickness=2)

        return av.VideoFrame.from_ndarray(frm, format='bgr24')

webrtc_streamer(key="key", video_processor_factory=VideoProcessor)