# Balance Changes

As you may have heard, the recent XP balance changes break the "*Level 10*" barrier. As of 3 November 2025, this balance change still remains. According to the developers:

## The Changes

* More chests and resources for everybody which will indirectly boost the average player's **bomberium** (possibly *gem*, *card* and *other resources*) making the game more fair against the card epidemic
* There are more rewards when achieving newer and higher levels, ***levels are higher than 10 and to infinity***. *Due to a period of inactivity, I cannot confirm whether this barrier has been entirely removed or not*

## The Experiments

*Experimenting against Bomber Friends is a tiring process*. Fuzzing it is unclear and hard since it takes a long time to load and won't return the data of success. The only *potentially useful fuzzing* would apply to checking if the game crashes or overflows. However, **that is also very time consuming both to test and try**! I have made a few attempts to fuzz the XP and these are the results:

### The Results

Let's get the question out of the room and clarify that: *Levels are not up to infinity, eventually they end up overflowing back to 10*. When trying to modify the server response and set it to ***millions of XP***, you will get *level 10*. Setting it to a range like *200,000 or 485,000* will yield you something like *level 40-82*.

It's ***unclear why this has happened*** because it seems very counterproductive and it's likely the thought of a developer that nobody will pass the level, right? ;)

According to my investigations, the maximum level is somewhere between 80-90. More specifically, it's *82*. We hope that somebody on the developer team will get to the root of this issue!
