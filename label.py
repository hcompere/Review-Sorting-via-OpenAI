from openai import OpenAI

client = OpenAI()

def get_sentiment(text: list) -> list:
    """
    get_sentiment is a function that uses OpenAI to go through a list of reviews and interpret them into simple cateorgies; 
    positive, negative, neutal or irrlevant

    text: takes in an input of a list containing reviews in an array of strings

    returns: a list of one word sentiments for each review; positive, negative, neutral or irrelevant
    """

    if text == []:
        return "Wrong input. text must be an array of strings."
    
    for item in text:
            if type(item) != str:
                return "Wrong input. text must be an array of strings."
    
    else:
        
        system_prompt = f""""
        You are an expert at understanding human emotion and have spent years reading 
        online reviews as a review intepretor. You can easily catergorize based on relevance and tone. 
        """

        prompt = f"""
        For each line of text in the string below, please categorize the review
        as either positive, neutral, negative, or irrelevant. Use irrelevant for any reviews that
        are not about the water.

        Use only a one-word response per line. Do not include any numbers. 
        Make sure that each review returns exactly one category and there are no repeats.
        There are 50 reviews, and you will return 50 one-word sentiments.
        {text}
        """
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                { "role": "developer",  "content": system_prompt },
                { "role": "user",  "content":  prompt }
            ]
        )
        return completion.choices[0].message.content.split()
  

