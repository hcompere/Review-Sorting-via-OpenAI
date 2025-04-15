from label import get_sentiment
from visualize import make_plot

import json


def run(filepath: str):
    """
    INSERT DOCSTRING HERE
    """
    # open the json object
    ...
    with open('data/raw/reviews.json') as j:
        d = json.load(j)
    # extract the reviews from the json file
    ...
    reviews = list(d["results"])
   
   

    # get a list of sentiments for each line using get_sentiment
    ...
    get_sentiment(reviews)
    # plot a visualization expressing sentiment ratio
    ...
    make_plot(get_sentiment(reviews))
    # return sentiments
    return get_sentiment(reviews)
    ...


if __name__ == "__main__":
    print(run("data/raw/reviews.json"))
