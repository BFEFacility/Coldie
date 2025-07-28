# The new era of Bomber Friends cheating

**Coldie** is a fork of **Bombie**, the original Bomber Friends proxy-based cheat. This is a entirely new vector for this game's cheating that has been created by **bombie**. Unlike other cheaters who have tried to modify the game's binary or inject their own Java code which have been banned many times before... They have been getting weaker and weaker with new anti-cheat update and due to many other factors. The introduction of the checksum will wipe this era in a total way. Talking about the last blow: the failure of their anti-ban which has been wiping cheaters left and right. However, there has been one vector of cheating that hasn't been tried nor secured enough. That's proxy cheating. 

## What's proxy cheating?

**Proxy cheating** (or *MITM cheating*, *MITM*) is a unique type of cheating that doesn't involve app modifications, hex editors, memory editors nor any special type of patches. It simply modifies the app's (or game's) traffic to make the client or server communicate to themselves in modified and patched ways. A **proxy** is the machine your traffic goes through, it can be modified or seen through a proxy. **Traffic** is a way to describe how machines talk to each other in technological ways. This type of cheat uses a **proxy** which modifies the client's request and the server's response to cheat. Unlike manual and hassling proxy cheating, it uses a *script* to automate the whole process!

## What does this script use? What proxy it uses?

This script uses the **mitmproxy API** to programmatically act as a proxy and modify the request/response flow handsomely. It uses **mitmproxy** programmatically. This script requires manual script modification (very easy, guided, simple) and it can run forever to serve you.

## What features does it have?

One thing that sets this cheat from other cheats is the fact that it has **visual and non-visual cheats in one**. This sets it's variety of features ahead of other scripts which try to implement all the non-visual features, leading to more time wasted for an update and less cheats in one. Here are all the features this script offers (Ordered by first to last in the script):

(∞ represents Infinity, 0-∞ represents the currency/item can be set to any amount by modifying the script, kickloop is a repeated kick from the servers when attempting to play; this is worse than a ban and unbypassable)

1. 0-∞ Bomberium (**Visual**)
2. 0-∞ Free Spins (**Visual**)
3. 0-∞ VIP Spins (**Visual**)
4. Season Pass (**Partial**), contains all the benefits of the season pass (double fashion points, event lives etc.) however claiming the tiers will return an error (impossible) (**Unbannable**) (**Safe**)
5. XP (**Working**), specifies the XP of the account (XP = level), 99999 XP is level 10, this gives you good multiplayer benefits (**Unbannable**) (**Safe**)
6. Gems (**Visual**)
7. Medals (**Visual**)
8. Always Bots (**Working**), makes you always play with bots no matter the matches played nor the medal range (**Not Tested Enough**) (**Safe**)
9. All Costumes (**Working**), always gives you every costume (capped at 3,000 items which is enough for now, can be increased), this feature is extremely likely to cause an kickloop (**Very Unsafe**) 
10. Maximum Fashion Points (**Working**), always gives you (100*2) = 200 fashion points in every fashion show entry, nothing matters, always keep it on everytime you apply for the fashion show (**Unbannable**) (**Very Safe**)
11. Anti-Ban (**Working**), always keeps your account unbanned and removes all ban reasons if there is, this is the most *stable* and *best* feature that only Coldie has implemented (**UNBANNABLE**) (**Safe**) (**DON'T TURN OFF**)

There are also some features about the new player's tutorial (visual features that inject into the tutorial):

12. 0-∞ Bomberium After Completing Tutorial (**Visual**)
13. 0-∞ Medals After Completing Tutorial (**Visual**)

More features are being added!

### After setup, is it OK to turn off the proxy?

**Never turn off the proxy**! This is such an **important topic**, it was chosen to be put in it's whole subsection and not in a few sentences! Let's look at when it is OK to turn off the proxy and when it is absolutely **NOT OK** to turn off the proxy:

#### It's OK to turn off the proxy!

1. Every Visual Feature (after you've taken a photo of it and flexed it *;)*)
2. Maximum Fashion Points (after you've applied for the fashion show)

#### It's NOT OK to turn off the proxy!

1. Season Pass
2. XP 
3. Always Bots
4. All Costumes (if you're using it!)
5. **ANTI-BAN!**

Let's talk more about the script and it's proxy. For all of these features to be granted, it modifies the server response to include all of these features for the client. The server is always smart and this bug abuses a very specific bug: giving a fake response to the client which is always trusted, so **some of the features** are granted and can be used/exist. Unlike some games, Hyperkani servers always keep a log of all server request of every user which is instantly used for every logon. This simply makes the client see a different state than the server. The server knows best so when not using the proxy, it returns the actual response and not the spoofed response that Coldie returns that the server has no idea of. 

Let's talk about what happens when the proxy is turned off: For features such as Season Pass or XP, the feature gets revoked and a ban isn't granted to your account since the anti-cheat doesn't account for that. **Always Bots** gets revoked. **All Costumes** get out. However, when turning off **Anti-Ban**, you get banned if you have already gotten banned. Bombie's **Anti-Ban** abuses a very particular flaw: a ban is simply a block from playing, it still remains in the server (no issue unless you turn the proxy off, the server will see you were banned and do it). **Anti-Ban** modifies the server's response that literally can be anything (banned...) and simply tells the client: they're not banned. Because of this, no matter if the servers think they're banned, they can still play and behave like a normal unbanned player. A ban is a restriction upon the account which this feature bypasses. It cannot erase server logs or legit server-mandated responses due to the server-sided verification and possible logging features of previous requests.

The proxy acts as the middleman between you and Hyperkani. Think of it as some dude between the connection that Hyperkani has no idea exists (**SSL pinning** is not implemented). When you tell Hyperkani that you entered the fashion show and got **3 points**, the dude in the middle tells it without it barely caring for your request: "**I entered the fashion show and got 100 fashion points, watched the ad (set to a True boolean, not "1" like other specific requests/responses) and got 200 fashion points)**", Hyperkani accepts that because it was a value from the client, it wasn't malformed and it was on range (0-200), so the points are granted. The same thing happens for literally every feature, for every visual feature, the server trusts it's own values further or it requires many other modifications of other requests/responses of other buying flows.

## Is this project being maintained? Will any other feature be implemented?

It is being maintained and it adds on to bombie's amazing legacy. Many other features, testcases or code improvements such as the usage of ternary operators (plans are going to make the code 10x shorter and more lightweight) are being tried. The reason why features are added less unlike code improvements or docs (easier but time consuming) is because the API endpoint needs to be tracked, the cloud script name needs to be found, the modifiable code needs to be found and every new feature is always tested and tried in new accounts. This simple explanation doesn't include the time it takes to write the code, the time it takes to write the relevant docs for it, the time it takes to check if it is bannable or safe and many other factors such as code breakage. In other words: like any other cheat but for this cheat, it's a more special case: it takes a lot of time to make and test more cheats and features.

## Coldie would like to thank...

**bombie** is an amazing Python script which was the base of the entire project. It had many features that became the essentials of the proxy-based cheating, the proxy cheating era and Coldie itself. For that, Coldie would like you to star the project to show your appreciation! *The maintainer and owner of that project was me in a lost account, so I'm thanking my own project.*

**mitmproxy** is the entire project summarized in one word, both for **bombie** and **Coldie**. I'd like to thank the **mitmproxy API** which made it possible to modify traffic flow programmatically. The API made this process smoother with it's great documentation, simple naming scheme and the small learning curve of the project which allowed **bombie** to be completed while learning the API (that's how the amazing and quick the API is).

**bombie** would like to thank some of the people on iOSGods for providing **bombie** for good motivation and giving answers to some of it's questions. The project was eventually moved to GitHub to ensure more stable hold of the code and it's maintainer, but it will eventually be posted to iOSGods.
