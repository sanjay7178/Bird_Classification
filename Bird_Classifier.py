from keras.models import load_model
import tensorflow as tf
import requests

loaded_model = load_model("deep_learning_model/Trained_model2.h5")

token = '5670119365:AAHkaefzKJ09qp3yoKGqvg2n-j0JpVig1AE'
userID = -813050596


fname = "deep_learning_model/birds.txt"
with open(fname ,"r") as f:
    BirdClasses = sorted(set([word for line in f for word in line.split()]))

def sendMessage(message) :

    # Create url
    url = f'https://api.telegram.org/bot{token}/sendMessage'

    # Create json link with message
    data = {'chat_id': userID, 'text': message}

    # POST the message
    requests.post(url, data)

def sendPhoto(filepath):
    url = "https://api.telegram.org/bot{}/sendPhoto?chat_id={}".format(token, userID)

    data =  { 
        'photo':open(filepath, 'rb')
    }

    requests.post(url, files=data)

def load_and_prep_image(filename, img_shape = 224):
    img = tf.io.read_file(filename) #read image
    img = tf.image.decode_image(img) # decode the image to a tensor
    img = tf.image.resize(img, size = [img_shape, img_shape]) # resize the image
    img = img/255. # rescale the image
    return img

# predict function
def predict(filename):

    # Import the target image and preprocess it
    img = load_and_prep_image(filename)
    
    # Make a prediction
    pred = loaded_model.predict(tf.expand_dims(img, axis=0))

    # Get the predicted class
    pred_class = BirdClasses[pred.argmax()]

    return pred_class


if __name__ == '__main__' : 
    filepath = 'images/birds.png'
    result = predict(filepath)
    # sendMessage(result)
    # sendPhoto(filepath)
    print('result : ', result)