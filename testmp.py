import cv2
import mediapipe as mp
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils
import math
# For static images:
IMAGE_FILES = ['WIN_20220528_00_22_16_Pro.jpg']
with mp_face_detection.FaceDetection(

    model_selection=1, min_detection_confidence=0.5) as face_detection:
	for idx, file in enumerate(IMAGE_FILES):

  
		image = cv2.imread(file)
		# Convert the BGR image to RGB and process it with MediaPipe Face Detection.
		results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

		# Draw face detections of each face.
		if not results.detections:

			continue
		annotated_image = image.copy()
		i=0
		
			
		for detection in results.detections:
			# print('Nose tip:')
			# print(mp_face_detection.get_key_point(
			# 	detection, mp_face_detection.FaceKeyPoint.NOSE_TIP))
			
			x = detection.location_data.relative_bounding_box.xmin
			y = detection.location_data.relative_bounding_box.ymin
			w = detection.location_data.relative_bounding_box.width
			h = detection.location_data.relative_bounding_box.height
			x_p = min(math.floor(x * annotated_image.shape[1]), annotated_image.shape[1] -1)
			y_p = min(math.floor(y * annotated_image.shape[0]), annotated_image.shape[1] -1)
			w_p = min(math.floor(w * annotated_image.shape[1]), annotated_image.shape[1] -1)
			h_p = min(math.floor(h * annotated_image.shape[0]), annotated_image.shape[1] -1)
			path_file = "found_faces/images"+str(i)+".jpg"
			i+=1
			newim = annotated_image[y_p:y_p+h_p,x_p:x_p+w_p]
			cv2.imwrite(path_file,newim)
			# mp_drawing.draw_detection(annotated_image, detection)


			cv2.imshow('image',newim)
			cv2.waitKey(0)
	cv2.destroyAllWindows()
	# For webcam input:
	# cap = cv2.VideoCapture(0)
	# with mp_face_detection.FaceDetection(
	#     model_selection=0, min_detection_confidence=0.5) as face_detection:
	#   while cap.isOpened():
	#     success, image = cap.read()
	#     if not success:
	#       print("Ignoring empty camera frame.")
	#       # If loading a video, use 'break' instead of 'continue'.
	#       continue

	#     # To improve performance, optionally mark the image as not writeable to
	#     # pass by reference.
	#     image.flags.writeable = False
	#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
	#     results = face_detection.process(image)

	#     # Draw the face detection annotations on the image.
	#     image.flags.writeable = True
	#     image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
	#     if results.detections:
	#       for detection in results.detections:
	#         mp_drawing.draw_detection(image, detection)
		# Flip the image horizontally for a selfie-view display.
		# cv2.imshow('MediaPipe Face Detection', cv2.flip(image, 1))
		# if cv2.waitKey(5) & 0xFF == 27:
		#   break
	# cap.release()