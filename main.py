import cv2 as cv
import numpy as np
from exif import Image
from geopy.geocoders import Nominatim

def countInfraRed(n):
    infraRedCount = 0   
    for i in range(n.shape[0]):
        infraRedCount += sum(n[i])
    return infraRedCount

def countRed(r):
    redCount = 0
    for i in range(r.shape[0]):
        redCount += sum(r[i])
    return redCount

def countNDVI(img):
    n,_,r = cv.split(img)
    infraRedCount = countInfraRed(n)
    redCount = countRed(r)
    denom = int(infraRedCount) - int(redCount)
    numer = int(infraRedCount) + int(redCount)
    if(numer == 0):
        return 0
    return denom/numer 


def getLatitude(image):
    latitude = f'{int(image.gps_latitude[0])}.{int(image.gps_latitude[1])}'
    if(image.gps_latitude_ref == "S"):
        return f'-{latitude}'
    return latitude

def getLongitude(image):
    longitude = f'{int(image.gps_longitude[0])}.{int(image.gps_longitude[1])}'
    if(image.gps_longitude_ref == "W"):
        return f'-{longitude}'
    return longitude

def getCity(image_num):
    with open(f'../photos/img_{image_num}.jpg', 'rb') as image_file:
        image = Image(image_file)
        geoLocator = Nominatim(user_agent="geoapiExercises")
        latitude = getLatitude(image)
        longitude = getLongitude(image)
        location = geoLocator.reverse(latitude+","+longitude)
        return location
        

def main():
    for i in range(1, 731):
        with open("output.txt", 'a', encoding = 'utf-8', ) as f:
            index_length = len(str(i))
            image_number = "000" + str(i) if index_length == 1 else "00" + str(i) if index_length == 2 else "0" + str(i) if index_length == 3 else i
            img = cv.imread(f'../photos/img_{image_number}.jpg')
            ndvi = countNDVI(img)
            location = getCity(image_number)
            print(f'photo{image_number};{ndvi};{location}')
            f.write(f'photo{image_number};{ndvi};{location}\n')
            f.close()


main()