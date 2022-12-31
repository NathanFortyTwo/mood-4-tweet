import re
import configparser
import tweepy
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import pickle
import csv
import time

def auth():
    global api
    config = configparser.ConfigParser()
    config.read("config.ini")

    api_key = config['twitter']["api_key"]
    api_key_secret = config['twitter']["api_key_secret"]
    access_token = config['twitter']["access_token"]
    access_token_secret = config['twitter']["access_token_secret"]


    auth = tweepy.OAuthHandler(api_key,api_key_secret)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth)
    return api


def get_tweets(username, count):
    return api.user_timeline(screen_name=username,count=count,tweet_mode='extended')

def valid_text_from_tweets(tweets):
    res = []
    for t in tweets:    
        text = t.full_text
        if text.__contains__(":"):
            text = text.split(":",1)[1] # remove RT info

        text=re.sub(r'https\S+', '', text) #remove links
        text=re.sub(r'http\S+', '', text) # remove links
        text=re.sub(r'//t.co\S+', '', text) # remove image links

        text=re.sub(r"\n",'',text) # remove newlines
        
        if not any(c.isalpha() for c in text):
            text = "xyz" # if no text then dummy text because we cant know mood
        res.append(text)
        
    return res

def load_vect_layer():
    from_disk = pickle.load(open("mymodel_soft/tv_layer.pkl", "rb"))
    new_v = tf.keras.layers.TextVectorization.from_config(from_disk['config'])
    # You have to call `adapt` with some dummy data (BUG in Keras)
    new_v.adapt(tf.data.Dataset.from_tensor_slices(["xyz"]))
    new_v.set_weights(from_disk['weights'])
    return new_v

def model_predict_multiple(texts):   
    vect_texts = vect_layer(texts)
    return model.predict(vect_texts)



vect_layer = load_vect_layer()
model = tf.keras.models.load_model('mymodel_soft')   
tweet_count = 1000
usernames = ["JoeBiden"]
header = ["id","author","date_published","fav_count","full_text","mood"]

def main():
    api = auth()
    timestamp = time.time().__str__().split(".")[0]
    filename = f"dataset-{timestamp}.csv"
    with open(filename,'w',newline="") as csvfile:
        writer = csv.writer(csvfile,delimiter=" ")
        writer.writerow(header)
        for username in usernames:
            tweets = get_tweets(username,count=tweet_count)
            texts = valid_text_from_tweets(tweets)
            results=model_predict_multiple(texts)
            for index,tweet in enumerate(tweets):
                if texts[index]!="xyz": # if text is valid
                    row = [tweet.id,tweet.author.screen_name,tweet.created_at,tweet.favorite_count,texts[index],results[index][0]]
                    writer.writerow(row)

if __name__=="__main__":
    main()