import pyrebase

config={
    "apiKey": "AIzaSyCapvaTuwCidEhJA6E-CDOH5DyOfiAfKUg",
    "authDomain": "uniduetraffic.firebaseapp.com",
    "projectId": "uniduetraffic",
    "storageBucket": "uniduetraffic.appspot.com",
    "messagingSenderId": "125639716972",
    "appId": "1:125639716972:web:8c683acf95558085fa2849",
    "measurementId": "G-64PB0776YR"
}

firebase = pyrebase.initialize_app(config)

storage = firebase.storage()