from roboflow import Roboflow
rf = Roboflow(api_key="JSZlqImP83L1s9dhT5nN")
project = rf.workspace().project("car_detection-dorjn")
model = project.version(1).model

# infer on a local image
#print(model.predict("9.jpg", confidence=40, overlap=30).json())

# visualize your prediction
model.predict("3.jpeg", confidence=40, overlap=30).save("yolov7.jpg")

# infer on an image hosted elsewhere
# print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())