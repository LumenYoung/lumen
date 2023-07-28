# Lumeny

This is lumeny, a cli project that I used for my own daily usage.

There are several aspects that I want my cli app grows:

1. Connect to caldav so that it can reminds me of my events, or add new events in cli convinently. Pushing notification to the KDE desktop is also a important part to remind me of the events.
2. Connect to my RSS reader miniflux and filter the most important feeds using ChatGPT (A small recommendation system).
3. A TUI based on textual to help me manage several aspects of point 1 and 2, like inspect upcoming events or get general statistic of my feeds, and help me gradually improve the recommandation algorithm.

## Functions

This is a amalgamation of interesting feature for my personal use, they are not necessarily corelated.

### Caldav integrator

Connect to caldav so that it can reminds me of my events, or add new events in cli convinently. Pushing notification to the KDE desktop is also a important part to remind me of the events.

### Miniflux filter

There are several thousands of feeds in my miniflux, which I sometimes not able to process them all. I would like to make it more automated by using LLM to find the interesting feeds for me.

### Random tasks picker

Through times I accumulated a list of interesting project/subject. I would like to have a command to help me randomly select a project exists in my task page and make it a bonus to my day after finishing the main goal of the day.

