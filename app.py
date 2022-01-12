from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from flask import Flask, send_from_directory
from pywebio.input import *
from pywebio.output import *
import argparse
from pywebio import start_server

from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('SVRModel.pkl', 'rb'))

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def h():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/HousingPropertyForm')
def HousingPropertyForm():
    return render_template('HousingPropertyForm.html')


@app.route('/pred', methods=['POST'])
def calc():
    Floor_area = request.form["Floor_area"]
    Land_Size = request.form["Land_Size(perches)"]
    Num_Baths = request.form["Num_Baths"]
    Num_Beds = request.form["Num_Beds"]
    Num_Stories = request.form["Num_Stories"]
    Time_to_Town = request.form["Time_to_Town"]
    Ava_Schools_yes = request.form["Ava_Schools_yes"]
    Ava_Hospitals_yes = request.form["Ava_Hospitals_yes"]
    Ava_Religious_yes = request.form["Ava_Religious_yes"]
    Decorations_NoDecorations = request.form["Decorations_NoDecorations"]
    ACNONAC_yes = request.form["AC/NONAC_yes"]
    Location = request.form["Location"]

    Floor_area=float(Floor_area)
    Land_Size=float(Land_Size)
    Num_Baths =float(Num_Baths)
    Num_Beds =float(Num_Beds)
    Num_Stories = float(Num_Stories)
    Time_to_Town =float(Time_to_Town)
    Ava_Schools_yes =float(Ava_Schools_yes)
    Ava_Hospitals_yes =float(Ava_Hospitals_yes)
    Ava_Religious_yes =float(Ava_Religious_yes)
    Decorations_NoDecorations =float(Decorations_NoDecorations)
    ACNONAC_yes =float(ACNONAC_yes)
    Location =float(Location)


    Floor_area = np.log(Floor_area)
    Land_Size = np.log(Land_Size)
    Time_to_Town = np.log(Time_to_Town)

    Located_City_athurugiriya = 0.0
    Located_City_boralesgamuwa = 0.0
    Located_City_dehiwala = 0.0
    Located_City_kottawa = 0.0
    Located_City_kotte = 0.0
    Located_City_malabe = 0.0
    Located_City_moratuwa = 0.0
    Located_City_nugegoda = 0.0
    Located_City_piliyandala = 0.0 
    Located_City_thalawathugoda = 0.0


    if Location == 1:
        Located_City_athurugiriya = 0.0
        Located_City_boralesgamuwa = 0.0
        Located_City_dehiwala = 0.0
        Located_City_kottawa = 0.0
        Located_City_kotte = 0.0
        Located_City_malabe = 0.0
        Located_City_moratuwa = 0.0
        Located_City_nugegoda = 0.0
        Located_City_piliyandala = 0.0 
        Located_City_thalawathugoda = 0.0
    elif Location == 2:
        Located_City_athurugiriya = 0.0
        Located_City_boralesgamuwa = 0.0
        Located_City_dehiwala = 0.0
        Located_City_kottawa = 0.0
        Located_City_kotte = 0.0
        Located_City_malabe = 0.0
        Located_City_moratuwa = 0.0
        Located_City_nugegoda = 0.0
        Located_City_piliyandala = 1.0 
        Located_City_thalawathugoda = 0.0
    elif Location == 3:
        Located_City_athurugiriya = 0.0
        Located_City_boralesgamuwa = 0.0
        Located_City_dehiwala = 0.0
        Located_City_kottawa = 1.0
        Located_City_kotte = 0.0
        Located_City_malabe = 0.0
        Located_City_moratuwa = 0.0
        Located_City_nugegoda = 0.0
        Located_City_piliyandala = 0.0 
        Located_City_thalawathugoda = 0.0
    elif Location == 4:
        Located_City_athurugiriya = 1.0
        Located_City_boralesgamuwa = 0.0
        Located_City_dehiwala = 0.0
        Located_City_kottawa = 0.0
        Located_City_kotte = 0.0
        Located_City_malabe = 0.0
        Located_City_moratuwa = 0.0
        Located_City_nugegoda = 0.0
        Located_City_piliyandala = 0.0 
        Located_City_thalawathugoda = 0.0
    elif Location == 5:
        Located_City_athurugiriya = 0.0
        Located_City_boralesgamuwa = 0.0
        Located_City_dehiwala = 0.0
        Located_City_kottawa = 0.0
        Located_City_kotte = 0.0
        Located_City_malabe = 1.0
        Located_City_moratuwa = 0.0
        Located_City_nugegoda = 0.0
        Located_City_piliyandala = 0.0 
        Located_City_thalawathugoda = 0.0
    elif Location == 6:
        Located_City_athurugiriya = 0.0
        Located_City_boralesgamuwa = 0.0
        Located_City_dehiwala = 0.0
        Located_City_kottawa = 0.0
        Located_City_kotte = 0.0
        Located_City_malabe = 0.0
        Located_City_moratuwa = 0.0
        Located_City_nugegoda = 0.0
        Located_City_piliyandala = 0.0 
        Located_City_thalawathugoda = 1.0
    elif Location == 7:
        Located_City_athurugiriya = 0.0
        Located_City_boralesgamuwa = 0.0
        Located_City_dehiwala = 0.0
        Located_City_kottawa = 0.0
        Located_City_kotte = 0.0
        Located_City_malabe = 0.0
        Located_City_moratuwa = 1.0
        Located_City_nugegoda = 0.0
        Located_City_piliyandala = 0.0 
        Located_City_thalawathugoda = 0.0
    elif Location == 8:
        Located_City_athurugiriya = 0.0
        Located_City_boralesgamuwa = 1.0
        Located_City_dehiwala = 0.0
        Located_City_kottawa = 0.0
        Located_City_kotte = 0.0
        Located_City_malabe = 0.0
        Located_City_moratuwa = 0.0
        Located_City_nugegoda = 0.0
        Located_City_piliyandala = 0.0 
        Located_City_thalawathugoda = 0.0
    elif Location == 9:
        Located_City_athurugiriya = 0.0
        Located_City_boralesgamuwa = 0.0
        Located_City_dehiwala = 1.0
        Located_City_kottawa = 0.0
        Located_City_kotte = 0.0
        Located_City_malabe = 0.0
        Located_City_moratuwa = 0.0
        Located_City_nugegoda = 0.0
        Located_City_piliyandala = 0.0 
        Located_City_thalawathugoda = 0.0
    elif Location == 10:
        Located_City_athurugiriya = 0.0
        Located_City_boralesgamuwa = 0.0
        Located_City_dehiwala = 0.0
        Located_City_kottawa = 0.0
        Located_City_kotte = 1.0
        Located_City_malabe = 0.0
        Located_City_moratuwa = 0.0
        Located_City_nugegoda = 0.0
        Located_City_piliyandala = 0.0 
        Located_City_thalawathugoda = 0.0
    else :
        Located_City_athurugiriya = 0.0
        Located_City_boralesgamuwa = 0.0
        Located_City_dehiwala = 0.0
        Located_City_kottawa = 0.0
        Located_City_kotte = 0.0
        Located_City_malabe = 0.0
        Located_City_moratuwa = 0.0
        Located_City_nugegoda = 1.0
        Located_City_piliyandala = 0.0 
        Located_City_thalawathugoda = 0.0

 
    arr = np.array([[Time_to_Town,Land_Size,Num_Stories,Floor_area,Num_Beds,Num_Baths,Located_City_athurugiriya,Located_City_boralesgamuwa,Located_City_dehiwala,Located_City_kottawa,Located_City_kotte,Located_City_malabe,Located_City_moratuwa,Located_City_nugegoda,Located_City_piliyandala,Located_City_thalawathugoda,Decorations_NoDecorations,Ava_Religious_yes,Ava_Schools_yes,Ava_Hospitals_yes,ACNONAC_yes]])
    pred = model.predict(arr)
    pr=pred[0]
    pr = np.exp(pr)
    answer = str(round(pr, 2))
    return render_template('test.html',data=answer)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", type=int, default=8080)
    args = parser.parse_args()

    start_server(predict, port=args.port)