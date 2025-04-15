from openai import OpenAI

client = OpenAI()

def get_sentiment(text: list) -> list:

    if text == []:
        return "Wrong input. text must be an array of strings."
    
    for item in text:
            if type(item) != str:
                return "Wrong input. text must be an array of strings."
    
    else:
        """
        defining a funtcion that takes an input of a list of reviews and returns a list of 
        sentiments for each review. 
        """
        system_prompt = f""""
        You are an expert at understanding human emotion and have spent years reading 
        online reviews as a review intepretor. You can easily catergorize based on relevance and tone. 
        """

        prompt = f"""
        For each line of text in the string below, please categorize the review
        as either positive, neutral, negative, or irrelevant.

        Use only a one-word response per line. Do not include any numbers.
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
  

