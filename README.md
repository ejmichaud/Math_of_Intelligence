# Math_of_Intelligence

This is a submission for the challenge from [this](https://www.youtube.com/watch?v=xRJCOz3AfYY) video by [Siraj Raval](https://www.youtube.com/channel/UCWN3xxRkmTPmbKwht9FuE5A).

### Dependencies
-numpy
-matplotlib
Works with python 2 and 3

# Overview
This code helps to answer an essential question:
> **_What do people look for in a date_**?

To investigate, I used [this](https://www.kaggle.com/annavictoria/speed-dating-experiment) Kaggle dataset:
>Data was gathered from participants in experimental speed dating events from 2002-2004. During the events, the attendees would have a four minute "first date" with every other participant of the opposite sex. At the end of their four minutes, participants were asked if they would like to see their date again. They were also asked to rate their date on six attributes: Attractiveness, Sincerity, Intelligence, Fun, Ambition, and Shared Interests.

My code determines if there is a positive correlation between a date’s _perceived intelligence_ and how many matches they get by finding a **Linear Regression** using **Gradient Descent** on the data.

## Data Preparation

First, I removed all irrelevant columns (essentially everything but the intelligence rating and “see their date again” indicator) from the original Kaggle dataset, reducing the file size by about 98%. I then removed all rows containing missing data. In main.py, the code normalizes the intelligence and _match success_ scores for each participant to a gaussian distribution before executing the regression.

## Code Organization

All operations pertaining to initialization and fitting of the linear line are abstracted to a **Model** class. This organization, where a model’s parameters are stored in the same object

mimics the organization of more complex machine learning models, such as neural networks