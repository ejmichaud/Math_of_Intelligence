# Math_of_Intelligence

This is a submission for the challenge from [this](https://www.youtube.com/watch?v=xRJCOz3AfYY) video by [Siraj Raval](https://www.youtube.com/channel/UCWN3xxRkmTPmbKwht9FuE5A).

### Dependencies
- numpy
- matplotlib

Works with Python 2 and 3

# Overview
This code helps to answer an essential question:
> **_What do people look for in a date_**?

To investigate, I used [this](https://www.kaggle.com/annavictoria/speed-dating-experiment) Kaggle dataset:
>Data was gathered from participants in experimental speed dating events from 2002-2004. During the events, the attendees would have a four minute "first date" with every other participant of the opposite sex. At the end of their four minutes, participants were asked if they would like to see their date again. They were also asked to rate their date on six attributes: Attractiveness, Sincerity, Intelligence, Fun, Ambition, and Shared Interests.

My code determines if there is a positive correlation between a date’s _perceived intelligence_ and how many matches they get by finding a **Linear Regression** using **Gradient Descent** on the data.

## Data Preparation

First, I removed all irrelevant columns (essentially everything but the intelligence rating and “see their date again” indicator) from the original Kaggle dataset, reducing the file size by about 98%. I then removed all rows containing missing data. In main.py, the code normalizes the intelligence and _match success_ scores for each participant to a gaussian distribution before executing the regression.

## Code Organization

All operations pertaining to initialization and fitting of the linear line are abstracted to a **Model** class. This organization, where the model’s parameters and training methods are grouped together cleans things up and scales well when the complexity of the model increases (such as in neural networks).

# Results

First off, the standard deviation for the intelligence scores and positive match rate worked out to be about **1.0**, and **0.15** respectively. Now here’s what the regression produced:

![Alt text](https://www.dropbox.com/s/6wsp1k7go2oo240/Screen%20Shot%202017-06-21%20at%207.39.59%20PM.png?raw=true)

Now frankly that looks a bit nebulous to me, but we still get a result! The slope of that line is about **0.18**, which is _very interesting_. There does indeed seem to be some positive correlation between a person’s perceived intelligence and their speed-dating success. More specifically, that a 1 standard deviation improvement in your perceived intelligence corresponds with over a 1 standard deviation increase in your speed-dating success!

So people _do_ seem to look for intelligence, more or less, in prospective partners. Aggressively extrapolating on this correlation, it becomes obvious that the most desirable man to have ever lived, ladies and gentleman, is…

##### John von Neumann
![Alt text](https://upload.wikimedia.org/wikipedia/commons/thumb/7/78/HD.3F.191_%2811239892036%29.jpg/220px-HD.3F.191_%2811239892036%29.jpg?raw=true)
