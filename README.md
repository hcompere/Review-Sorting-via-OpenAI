# Review Processing
This project implements a sentiment classification pipeline for customer reviews using OpenAI’s GPT-4o-mini model. The tool analyzes textual reviews and assigns one of four sentiment labels:

* positive: *I love this ring, I use it all the time when working out.*
* neutral: *It's an ok ring. Some features could be better but for the price it's fine.*
* negative: *Absolutely terrible ring. The green light that the ring emitted kept attracting mosquitos.*
* irrelevant: *I like strawberry ice cream because its the best.* 

This is the first milestone in developing a production-ready sentiment analysis tool at Bernardino Group, a Vancouver-based analytics consulting firm.

You are tasked with creating a minimal pipeline that reads a JSON file of reviews and generates an output file that contains one of these sentiment labels for each respective review.

For example, if your input file contains the following array of reviews:
```
[
 "this ring smells weird, don't recomend",
 "I love this ring, I use it all the time when working out.",
 "I will never buy another brand again, I love this ring",
 "It's an ok ring. Some features could be better but for the price its fine.",
 "its a ring",
 "Bought this ring and it came broken. rip-off."
]
```
Returns labeled output as a list of sentiment tags.

```
["negative", "positive", "positive", "neutral", "irrelevant", "negative"]
```


🚀 Project Overview
This project demonstrates a complete data pipeline that:

Ingests review data from a JSON file.

Classifies each review's sentiment using OpenAI’s gpt-4o-mini model.

Visualizes sentiment distribution as a chart.

The raw dataset used in this project (`reviews.json`) includes real customer feedback on coconut water products from 1999–2012. While the examples above are synthetic, the actual model will be evaluated on this historical data.


Your company has also provided you an API key **(which you must keep secret)** to interface with this API. You will again utilize test-driven development to complete this project.

**Note** To limit cost anomalies throughout this project, we've set up API restrictions that limit the entire data science cohort to 1500 requests-per-day, 100 requests-per-minute, and 40,000 tokens-per-minute. If you encounter a `429` error when you run your code, this could either mean that your prompt is over the allotted 40,000 tokens or there have been too many requests within the same minute. Please read the section titled **API Limitations** to find out how to work around these limitations.


### label.py

Implements label_reviews(), a function that:

* Accepts a list of strings.
* Uses the OpenAI Chat Completions API to classify sentiment.
* Returns a list of labels or an error message for invalid input.

Note: Only gpt-4o-mini is supported. API calls will fail with other models.

Run tests:
```
python test_label.py
```

**Note**: You are limited to working with the `gpt-4o-mini` model. If you utilize any other model, your API call will not function correctly.

### visualize.py

Implements a function to count label occurrences and generate a visualization (e.g., bar chart).
Images are saved to the images/ directory.

Run tests:
```
python test_visualize.py
```

**Note**: Ensure that any images this function generates are saved within the `images/` folder.

### main.py

mplements the run() function to:

* Load input JSON
* Call the sentiment classifier
* Generate and save sentiment distribution plot

Run tests:
```
python test_run.py
```

### writeup.md

This file contains 3 analytical questions based on the visualizations the code generates.

🧠 Note: This project emphasizes test-driven development and cost-conscious API usage, simulating constraints in a production environment (e.g., token budgets, API limits).

