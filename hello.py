# import cv2
# import numpy as np
# from flask import Flask, Response, render_template, request
# # from hand_gesture2 import *
# # from hand_gesture2.final import hand_gesture
# # from llm.quiz import quiz


# app = Flask(__name__)

# camera = cv2.VideoCapture(0)



# def generate_frames():
#     while True:
#         success, frame = camera.read()
#         if not success:
#             break
#         else:
#             ret, buffer = cv2.imencode('.jpg', frame)
#             frame = buffer.tobytes()
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# def gesture():
#     while True:
#         frame = hand_gesture(camera)  # Call the hand_gesture function to process the frame
#         ret, buffer = cv2.imencode('.jpg', frame)
#         frame = buffer.tobytes()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# def cur(num, cur_num):
#     if num == cur_num:
#         return True
#     return False


# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/video_feed')
# def video_feed():
#     return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# @app.route('/video_feed1')
# def gesture_recog():
#     return Response(gesture(), mimetype='multipart/x-mixed-replace; boundary=frame')

# @app.route('/quiz')
# def display_quiz():
#     prompt = "environment"  # Replace this with the desired topic or prompt for the quiz
#     question, correct, wrong, ans, num = quiz(prompt)
#     return render_template('quiz.html', question=question, ans=ans, num=num)

# @app.route('/answer', methods=['POST'])
# def check_answer():
#     user_answer = request.form['answer']
#     correct_num = int(request.form['correct_num'])

#     # Check if the user's answer is correct
#     is_correct = cur(correct_num, int(user_answer))

#     # You can add further logic here to handle user responses, score keeping, etc.

#     return f"Your answer is {'correct' if is_correct else 'wrong'}."



# if __name__ == '__main__':
#     app.run(debug=True)


from sklearn import *




