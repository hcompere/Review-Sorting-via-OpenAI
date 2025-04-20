import matplotlib.pyplot as plt


def make_plot(sentiments: list) -> list:
    """
    make_plot is a function that takes sentiments from reviews and displays them as a bar graph

    sentiments: takes in a list of sentiments containing counts of positive, negative, neutral and irrelvant reviews

    returns: a bar graph displaying how many reviews were positive, negative, neutral or irrelevant. 
    """
    #create categories for the bar chart
    sentiment = ["Positive", "Negative", "Neutral", "Irrelevant"]   
    #create a list of counts for each category     
    counts = [sentiments.count("positive"), sentiments.count("negative"), sentiments.count("neutral"), sentiments.count("irrelevant")]
    
    #create a bar graph showing the sentiment counts and store it as an image in the images\ folder
    plt.bar(sentiment, counts)                     
    plt.title("Review Sentiments")
    plt.xlabel("Review Type")
    plt.ylabel("Count")
    graph = plt.savefig("images/sentiments.png")        
    return graph




