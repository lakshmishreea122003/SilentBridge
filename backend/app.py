from flask import Flask, render_template, Response, request, jsonify
import cv2


from hand_gesture2.final import hand_gesture
from llm.quiz import quiz
from llm.doubt import doubt


app = Flask(__name__)

cap = cv2.VideoCapture(0)

# functions
def quiz_cv():
     prompt = "save water"
     question,answer= quiz(prompt)
     return question,answer

def gesture_recognition():
    while True:
        frame,gesture = hand_gesture(cap)  # Call the hand_gesture function to process the frame
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def generate_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


# Responses
@app.route('/get_doubt', methods=['POST'])
def get_doubt_from_user():
    topic = request.form['topic']
    doubt_result = doubt(topic)
    return jsonify(doubt_result) 

@app.route('/video_feed')
def video_feed():
    return Response(gesture_recognition(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(debug=True)
