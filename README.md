# Flask Tweet To Video
## Main Exercise
Build a Flask app, Using the twitter feed, construct a daily video summarizing a twitter handle day.
## Process
  * Convert text into an image in a frame
  * Do a sequence of all texts and images in chronological order.
  * Display each video frame for 3 seconds
  * Deploy it on Flask
  
## High Level Intuition of the project
  * All of the requests go to the Queue. Each element is processed one by one.
  * Each User handle requests tweets by tweepy api.
  * The tweets are put in a list. Every tweet is processed and put in an image. In the end of this process every tweet would have unique images belong to the tweets.
  * After this the images would merge together and create a video. All videos belong to a specific file path called VideoSummary.
  * In addition to this all user handle will have files belong to the most recent tweets.
  * Build an AWS instance and transferred the files via scp command.
  * Run the Flask Script on Instance
  

## How to Use this API

The API object take 2 input arguments. The first one is the key. And the second one is the list of user_handles that we want to get the twitter feed from. The 'keys' file is the path to the api keys of the twitter.

![](https://github.com/BUEC500C1/video-Cagriyoruk/blob/With_Stub/Screenshots/How_TO.png)

The 'keys' file looks like this:

![](https://github.com/BUEC500C1/video-Cagriyoruk/blob/With_Stub/Screenshots/Auth.png)

The Keys can be obtained through tweepy api. In order to use this API, you need keys.

To be precise, we need to put user_handles in to a list. If we want to check only one person, still we need to put it into a list like ['Cagri_yoruk'].

## Input and Output
 * If there are correct authorization keys and path of the key with the correct input like this: VideoSummary('keys',['lexfridman', 'jomaoppa', 'elonmusk']). The API would return files and videos belongs to the user handles. 
 
 * The API would return the most frequent 30 tweets of the user handle as a video. Each user_handle would have a unique video based on their tweets.
 
 * In case of any wrong authorization or wrong path. If the user handle already has a files, the API will return that. The files are created after the succesful runs with the correct keys and path.

## Examples
### Home Page
<img width="1128" alt="2020-03-08" src="https://user-images.githubusercontent.com/55101879/76181491-aa19e080-6197-11ea-9cba-9226b390c1df.png">

### Download Page
<img width="1128" alt="2020-03-09 (1)" src="https://user-images.githubusercontent.com/55101879/76182101-eb12f480-6199-11ea-95c3-4c75e52b6ad7.png">

#### AWS Website
```
http://ec2-18-188-79-200.us-east-2.compute.amazonaws.com/
```



