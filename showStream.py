from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json, time, sys
import datetime
import tweepy

api_key = 'nMx5ZaxM0MDYO34MB03sqKB99'
api_secret = '0VI6uVkPQN0GBq7fGn0oPG8815zZvuLDMzwlMLQh8fjKuFi5Iz'
access_token = '468144344-gKaGTGbv0lvzMISUjGhULnOFOEUDRd1AY8xfyojY'
access_token_secret = '9DATIGIOLG1WFnBfr0NgEzOtpwE1lHkkCREtsBekEEnWp'

auth = OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)


class StdOutListener(StreamListener):

    def __init__(self,api=None):
        super(StdOutListener, self).__init__()
        self.count = int(raw_input("Enter the number of tweets you would like to stream: "))
        print "How long this will stream is dependent on how many people are currently tweeting about House of Cards, Scandal, or Game of Thrones" 
        self.tweet_list = []
        self.GoT_list = []
        self.scandal_list = []
        self.HoC_list = []
        self.num_tweets = 0
        self.start_time = time.time()
        self.text_file = open('twitter_data.txt', 'w+')
        self.text_file.write("Tweet Data\n==========\n\n")
        self.GoT_tweets = 0
        self.scandal_tweets = 0
        self.HoC_tweets = 0

    def on_status(self, status):

        text = status.text.encode('utf-8')
        created = status.created_at
        self.num_tweets = self.num_tweets + 1
        self.tweet_list.append(text) 
        if self.num_tweets <= self.count:
            if "#GoT".lower() in text.lower():
                self.GoT_tweets = self.GoT_tweets + 1
                self.GoT_list.append(text)
            elif "#scandal".lower() in text.lower():
                self.scandal_tweets = self.scandal_tweets + 1
                self.scandal_list.append(text)
            elif "#HouseOfCards".lower() in text.lower():
                self.HoC_tweets = self.HoC_tweets + 1
                self.HoC_list.append(text)

            print str(self.num_tweets) + " tweet(s) out of " + str(self.count) + " have been gathered" 
            saveThis = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S') + '::' + text
            self.text_file.write(saveThis)
            self.text_file.write('\n')
            if self.num_tweets == self.count:
                print "Finished"
                print str(self.GoT_tweets) + " tweet(s) were about Game of Thrones."
                print str(self.scandal_tweets) + " tweet(s) were about Scandal."
                print str(self.HoC_tweets) + " tweet(s) were about House of Cards."
                total_time = time.time() - self.start_time
                print "It took " + str(total_time) + " seconds to finish streaming."
                self.text_file.write("\n\nIt took " + str(total_time) + " seconds to gather " + str(self.count) + " tweets about these shows.\n\n")
                self.text_file.write(str(self.GoT_tweets) + " out of " + str(self.count) + " tweets were about Game of Thrones.\n")
                self.text_file.write(str(self.scandal_tweets) + " out of " + str(self.count) + " tweets were about Scandal.\n")
                self.text_file.write(str(self.HoC_tweets) + " out of " + str(self.count) + " tweets were about House of Cards.\n")

                if self.GoT_tweets > self.scandal_tweets and self.GoT_tweets > self.HoC_tweets:
                    self.text_file.write("Game of Thrones is the most popular show on twitter as of " + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
                    print "Game of Thrones was the most popular show out of those " + str(self.count) + " tweet(s)"
                elif self.scandal_tweets > self.GoT_tweets and self.scandal_tweets > self.HoC_tweets:
                    self.text_file.write("Scandal is the most popular show on twitter as of " + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
                    print "Scandalwas the most popular show out of those " + str(self.count) + " tweet(s)"
                else:
                    self.text_file.write("House of Cards is the most popular show on twitter as of " + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
                    print "House of Cards was the most popular show out of those " + str(self.count) + " tweet(s)"

                length_of_all_tweets = map(len, self.tweet_list)
                print length_of_all_tweets
            


                self.text_file.close()
                return False
            else:
                return True
        """else:
            print "Finished"
            print str(self.GoT_tweets) + " tweet(s) were about Game of Thrones."
            print str(self.scandal_tweets) + " tweet(s) were about Scandal."
            print str(self.HoC_tweets) + " tweet(s) were about House of Cards."
            total_time = time.time() - self.start_time
            print "It took " + str(total_time) + " seconds to finish streaming."
            self.text_file.write("\n\nIt took " + str(total_time) + " seconds to gather " + str(self.count) + " tweets about these shows.\n\n")
            self.text_file.write(str(self.GoT_tweets) + " out of " + str(self.count) + " tweets were about Game of Thrones.\n")
            self.text_file.write(str(self.scandal_tweets) + " out of " + str(self.count) + " tweets were about Scandal.\n")
            self.text_file.write(str(self.HoC_tweets) + " out of " + str(self.count) + " tweets were about House of Cards.\n")

            if self.GoT_tweets > self.scandal_tweets and self.GoT_tweets > self.HoC_tweets:
                self.text_file.write("Game of Thrones is the most popular show on twitter as of " + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
                print "Game of Thrones was the most popular show out of those " + str(self.count) + " tweet(s)"
            elif self.scandal_tweets > self.GoT_tweets and self.scandal_tweets > self.HoC_tweets:
                self.text_file.write("Scandal is the most popular show on twitter as of " + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
                print "Scandalwas the most popular show out of those " + str(self.count) + " tweet(s)"
            else:
                self.text_file.write("House of Cards is the most popular show on twitter as of " + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
                print "House of Cards was the most popular show out of those " + str(self.count) + " tweet(s)"

            length_of_all_tweets = map(len, self.tweet_list)
            print length_of_all_tweets
            


            self.text_file.close()

            return False""" 

    def on_error(self, status):
        print 'Error on status', status

    def on_limit(self, status):
        print 'Limit threshold exceeded', status

    def on_timeout(self, status):
        print 'Stream disconnected; continuing...'



twitterStream = Stream(auth, StdOutListener())
twitterStream.filter(track=["#GoT", "#HouseOfCards","#Scandal"])

