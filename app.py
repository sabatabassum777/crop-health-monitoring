from __future__ import division, print_function
import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Flask utils
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename

# from gevent.pywsgi import WSGIServer

# Define a flask app
app = Flask(__name__)

# Model saved with Keras model.save()
MODEL_PATH = 'model2_vgg19.h5'

# Load your trained model
model = load_model(MODEL_PATH)


def model_predict(img_path, model):
    img = image.load_img(img_path, target_size=(256, 256))

    # Preprocessing the image
    x = image.img_to_array(img)
    # x = np.true_divide(x, 255)
    ## Scaling

    x = np.expand_dims(x, axis=0)
    x = x * 1.0 / 255

    # Be careful how your trained model deals with the input
    # otherwise, it won't make correct prediction!
    # x = preprocess_input(x)

    preds = model.predict(x)
    preds = np.argmax(preds, axis=1)
    # preds = np.argmax(preds, axis=1)
    print("The prediction is: ", preds)
    if preds == 0:
        return render_template('index.html', preds='Rice_BrownSpot',mes='Remove Weeds , Use balanced nutrients',pest=' Iprodione, propiconazole, azoxystrobin',link='https://www.amazon.com/Iprodione-2F-Select-Gallon-Compare/dp/B07D828P3Z')
    elif preds == 1:
        return render_template('index.html', preds='Rice_Healthy',mes='No Measures',pest='No Pesticides',link="https://www.amazon.in/s?k=organic+fertilizer+for+plants&hvadid=82944601526132&hvbmt=bp&hvdev=c&hvqmt=p&tag=msndeskstdin-21&ref=pd_sl_7j96q2uswp_p")
    elif preds == 2:
        return render_template('index.html', preds='Rice_Hispa',mes='Avoid over fertilizing, cutting shoot tips',pest='Lambda-cyhalothrin',link="https://www.flipkart.com/search?q=Lambda-cyhalothrin&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
    elif preds == 3:
        return render_template('index.html', preds='Rice_LeafBlast',mes='Adjust planting time,Flood the fields in often',pest='UPL SAAF AVANCER GLOW',link="https://www.flipkart.com/upl-saaf-avancer-glow-8-3-azoxystrobin-66-7-wg-mancozeb-150/p/itm3a418fb00be27")
    elif preds == 4:
        return render_template('index.html', preds='Strawberry_healthy',mes='No Measures',pest='No Pesticide',link="https://www.amazon.in/s?k=organic+fertilizer+for+plants&hvadid=82944601526132&hvbmt=bp&hvdev=c&hvqmt=p&tag=msndeskstdin-21&ref=pd_sl_7j96q2uswp_p")
    elif preds == 5:
        return render_template('index.html', preds='Strawberry_leaf scorch',mes='Proper plant spacing,Use Drip irrigation',pest='Bayer Melody Duo',link='https://www.flipkart.com/bayer-melody-duo-fungicide-100-gm/p/itme4d9b9c1feada?pid=IRPGYRNSX7DYHSZS&lid=LSTIRPGYRNSX7DYHSZSMKGC6P&marketplace=FLIPKART&q=MELODY+DUO+&store=search.flipkart.com&srno=s_1_3&otracker=search&otracker1=search&fm=Search&iid=ef3a0ffc-446e-4cbe-9ad3-b0d80a226eb3.IRPGYRNSX7DYHSZS.SEARCH&ppt=sp&ppn=sp&ssid=yd8i8lzmdc0000001666194767373&qH=04e786cf2ee13573')
    elif preds == 6:
        return render_template('index.html', preds='corn_cercospora leaf spot gray leaf spot',mes='Remove all damaged material,Rotational of crops',pest='Delaro® 325 SC',link='https://www.fbn.com/direct/product/delaro-325-sc-fungicide')
        #preds = 'corn_cercospora leaf spot gray leaf spot'
    elif preds == 7:
        return render_template('index.html', preds='corn common rust',mes='Use resistant maize hybrids,Timely plantation of corn',pest='syngenta Kavach ',link='https://www.amazon.in/dp/B08RY71PZC/ref=cm_sw_r_awdo_0R0TYZVK8WZBYR4W4279_0')
        #preds = 'corn common rust'
    elif preds == 8:
        return render_template('index.html', preds='corn healthy',mes='No Measures',pest='No Pesticide',link="https://www.amazon.in/s?k=organic+fertilizer+for+plants&hvadid=82944601526132&hvbmt=bp&hvdev=c&hvqmt=p&tag=msndeskstdin-21&ref=pd_sl_7j96q2uswp_p")
        #preds = 'corn healthy'
    elif preds == 9:
        return render_template('index.html', preds='corn_northern leaf blight',mes='Manage Weeds,keep space evenly',pest='foliar',link='https://www.arbico-organics.com/category/foliar-fungicides')
        #preds = 'corn_northern leaf blight'
    elif preds == 10:
        return render_template('index.html', preds='grape_black rot',mes='Pruning of vines plant in open area,plant in open area',pest='lime sulfur',link='https://dir.indiamart.com/impcat/lime-sulphur.html')
        #preds = 'grape_black rot'
    elif preds == 11:
        return render_template('index.html', preds='grape_esca (black measles)',mes='Cross sectional cuts through trunks',pest='lime sulfur',link='https://dir.indiamart.com/impcat/lime-sulphur.html')
        #preds = 'grape_esca (black measles)'
    elif preds == 12:
        return render_template('index.html', preds='grape_healthy',mes='No Measures',pest='No Pesticide',link="https://www.amazon.in/s?k=organic+fertilizer+for+plants&hvadid=82944601526132&hvbmt=bp&hvdev=c&hvqmt=p&tag=msndeskstdin-21&ref=pd_sl_7j96q2uswp_p")
        #preds = 'grape_healthy'
    elif preds == 13:
        return render_template('index.html', preds='grape_leaf blight (isariopsis leaf spot)',mes='Keep the grass Height at 2.5-3 inches',pest='Bordeaux mixture',link='https://dir.indiamart.com/impcat/bordeaux-mixture.html')
        #preds = 'grape_leaf blight (isariopsis leaf spot)'
    elif preds == 14:
        return render_template('index.html', preds='orange_haunglongbing (citrus greening)',mes='Apply aqueous dilution of trees, Replace infected trees',pest='Foliar and Sevin',link='https://www.arbico-organics.com/category/foliar-fungicides')
        #preds = 'orange_haunglongbing (citrus greening)'
    elif preds == 15:
        return render_template('index.html', preds='potato_early blight',mes='Harvest late maturing ones,Avoid Overhead irrigation',pest='Potato Blight Control',link='https://mcparlands.ie/product/protect-garden-potato-blight-control/')
        #preds = 'potato_early blight'
    elif preds == 16:
        return render_template('index.html', preds='potato_healthy',mes='No Measures',pest='No Pesticides',link="https://www.amazon.in/s?k=organic+fertilizer+for+plants&hvadid=82944601526132&hvbmt=bp&hvdev=c&hvqmt=p&tag=msndeskstdin-21&ref=pd_sl_7j96q2uswp_p")
        #preds = 'potato_healthy'
    elif preds == 17:
        return render_template('index.html', preds='potato_late blight',mes='Use only disease free seed,Water in early morning hours',pest='Mancozeb',link='https://www.amazon.in/AD-45-Mancozeb-75-WP-Fungicide/dp/B07JDSJY6C/ref=sr_1_1?crid=F3LT3XCCLH3U&keywords=mancozeb+pesticide&qid=1666196835&qu=eyJxc2MiOiIxLjc4IiwicXNhIjoiMC4wMCIsInFzcCI6IjAuMDAifQ%3D%3D&sprefix=mancozab+pesticide%2Caps%2C200&sr=8-1')
        #preds = 'potato_late blight'
    else:
        return render_template('index.html', preds='tomato_bacterial spot',mes='Using pathogen-free seed,Avoid Sprinkler irrigation',pest='Mancozeb',link='https://www.amazon.in/AD-45-Mancozeb-75-WP-Fungicide/dp/B07JDSJY6C/ref=sr_1_1?crid=F3LT3XCCLH3U&keywords=mancozeb+pesticide&qid=1666196835&qu=eyJxc2MiOiIxLjc4IiwicXNhIjoiMC4wMCIsInFzcCI6IjAuMDAifQ%3D%3D&sprefix=mancozab+pesticide%2Caps%2C200&sr=8-1')
        #preds = 'tomato_bacterial spot'
    return preds


@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path, model)
        result = preds
        return result
    return None


if __name__ == '__main__':
    app.run(debug=True)