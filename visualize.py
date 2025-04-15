import matplotlib.pyplot as plt


def make_plot(sentiments: list) -> list:
    """
    defines a function that takes sentiments from reviews and displays them as a bar graph
    """
    sentiment = {                                   #define a dictionary that catergorizes sentiments into 4 groups
        "positive": sentiments.count("positive"),   #the sentiments are stored as keys and the number of values 
        "negative": sentiments.count("negative"),   #matching those sentiments are stored as values. 
        "neutral": sentiments.count("neutral"),
        "irrelevant": sentiments.count("irrelevant")
    }
    x_values = list(sentiment.keys())               #create x and y values, each x will represent a sentiment and each 
    y_values = list(sentiment.values())             #y is the count for the respective sentiment
    plt.bar(x_values, y_values)                     #create a bar graph
    plt.title("Review Sentiments")
    plt.xlabel("Review Type")
    plt.ylabel("Count")
    graph = plt.savefig("images/sentiments.png")        
    return(graph)




