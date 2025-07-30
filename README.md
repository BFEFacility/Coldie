# The new era of Bomber Friends cheating

**Coldie** is a maintained and updated version of **bombie**, the original Bomber Friends proxy-based cheat. This is a entirely new vector for this game's cheating that has firstly been created by **bombie**. Unlike other cheaters who have tried to modify the game's binary or inject their own Java code which have been banned many times before... They have been getting weaker and weaker with new anti-cheat updates and due to many other factors. The introduction of the checksum will totally wipe this era and the methods used by it. Talking about the last blow: the failure of their anti-ban which has been wiping cheaters left and right. However, there has been one vector of cheating that hasn't been tried nor fully secured by the game's servers since it was unexpected. That's proxy cheating. 

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
12. Recommended Version (**Stable**), always sets your version as the latest version allowing you to play in older versions of the game (new features won't be there, crashes and problems may be caused due to faulty code in other versions!) (**Unbannable**) (**Safe**) (**Not Tested Yet**)
    
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
5. Recommended Version (If you turn this on, you can keep any version of your choice freely)
6. **ANTI-BAN!** (If you turn this on, it will always unban you of all previous bans (even bans when turned off!) and will keep you that)

Let's talk more about the script and it's proxy. For all of these features to be granted, it modifies the server response to include all of these features for the client. The server is always smart and this bug abuses a very specific bug: giving a fake response to the client which is always trusted, so **some of the features** are granted and can be used/exist. Unlike some games, Hyperkani servers always keep a log of all server request of every user which is instantly used for every logon. This simply makes the client see a different state than the server. The server knows best so when not using the proxy, it returns the actual response and not the spoofed response that Coldie returns that the server has no idea of. 

**Recommended Version** is a feature which tricks the client that their game version is the latest one, allowing the client to play anywhere. This is extremely safe to do since there's no probable reason to ban a user (and they never will) for an out-of-date version. It doesn't trick the server, it tricks the client. An out-of-date version will lead to an updating prompt which blocks all play and that's client-side. This bypasses it which allows all play to resume on older versions too! When you turn this off, it will show the prompt and when you turn it on, you can still play.

Let's talk about what happens when the proxy is turned off: For features such as Season Pass or XP, the feature gets revoked and a ban isn't granted to your account since the anti-cheat doesn't account for that. **Always Bots** gets revoked. **All Costumes** get out. However, when turning off **Anti-Ban**, you get banned if you have already gotten banned. Coldie's **Anti-Ban** abuses a very particular flaw: a ban is simply a block from playing, it still remains in the server (Coldie tricks the client, not the server)! **Anti-Ban** modifies the server's response that literally can be anything (banned...) and simply tells the client: they're not banned. Because of this, no matter if the servers think they're banned, they can still play and behave like a normal unbanned player. Keep in mind that while **Anti-Ban** can bypass all account bans, it should still always be turned on when playing to ensure further security against bans and for DNS leaks to not happen. A ban is a restriction upon the account which this feature bypasses. It cannot erase server logs or legit server-mandated responses due to the server-sided verification and possible logging features of previous requests.

These trick the client and not always the server. Those that trick the server don't need the proxy on at all times, those that trick the client need the proxy for their magic. The proxy is what has everything for the client. It doesn't matter if you need to play the game 1,000 times, for the features that need the proxy **on**, you need to have it enabled. For those that need it for one-time, they need the proxy to be **on for one time, not always on**.

The proxy acts as the middleman between you and Hyperkani. Think of it as some dude between the connection that Hyperkani has no idea exists (**SSL pinning** is not implemented). When you tell Hyperkani that you entered the fashion show and got **3 points**, the dude in the middle tells it without it barely caring for your request: "**I entered the fashion show and got 100 fashion points, watched the ad (set to a True boolean, not "1" like other specific requests/responses) and got 200 fashion points)**", Hyperkani accepts that because it was a value from the client, it wasn't malformed and it was on range (0-200), so the points are granted. The same thing happens for literally every feature, for every visual feature, the server trusts it's own values further or it requires many other modifications of other requests/responses of other buying flows.

## Is this project being maintained? Will any other feature be implemented?

It is being maintained and it adds on to bombie's amazing legacy. Many other features, testcases or code improvements such as the usage of ternary operators (plans are going to make the code 10x shorter and more lightweight) are being tried. The reason why features are added less unlike code improvements or docs (easier but time consuming) is because the API endpoint needs to be tracked, the cloud script name needs to be found, the modifiable code needs to be found and every new feature is always tested and tried in new accounts. This simple explanation doesn't include the time it takes to write the code, the time it takes to write the relevant docs for it, the time it takes to check if it is bannable or safe and many other factors such as code breakage. In other words: like any other cheat but for this cheat, it's a more special case: it takes a lot of time to make and test more cheats and features.

## Are there any other features/things this project would like to achieve?

There are a few other things this project would like to complete, apart from small things specified in some of the code comments, this talks about the big stuff:

1. Have a **stable release**, it's in alpha even after some time due to the long time it takes to test existing features and the time it takes to make new features.
2. Include a **good tutorial** on how to set this script up
3. **Add many more cheats**. Due to the current state of cheating in the modern day, the cheats Coldie can do mostly range from visual. However, attempts are being made to have visual scripts work and add more cheats (visual or non-visual). However, we can modify the metadata (less important data), for example: modify the game's version so that you can play it on any version, more visual cheats etc. 
4. *Improve* the code.

## What's so different about this form of cheating?

The special thing is that it has never been tried before. Every other cheat has included Java script injection, hex editing, game file modification, texture modification and things that have modified the game **inside of it**. Other attempted cheats such as memory editors don't work due to server side validation. This form of cheating is new to the game and in fact, it's a very new form of cheating (programmatically using the mitmproxy API instead of manual proxy cheating). 

One of our main arguments is that: "since this script and approach has never been tried before, they haven't fully validated the server against it; they have been fighting against the most obvious forms of cheaters using their valuable time, resources and funding and not this type of it". This approach has never been seen before so it has never been fought. Also, fighting against this type of cheating is harder than fighting their cheats which can be easily patched with the introduction of **checksums** and with more complicated server logging. This is way harder to patch since it modifies the server's response and keeps the client's request in bound.

If you have heard of a better cheat, tell the maintainers in GitHub Discussions. **Unlimited Nukes** and such are a thing of the past. Not every cheat can be implemented or added due to the differences of this type of cheat compared to that type of cheat.

### Benefits

1. The best anti-ban as of now; it relies on server modifications to make it impossible to be banned and remain playing. It is literally not possible to be banned! Banned accounts can play using Coldie's anti-ban technology.
2. A wider variety of cheats than all other Bomber Friends cheats!
3. Isn't based off the version of the game unlike standard APKs or IPAs that are cheated, it can exploit any version that can be exploited!
4. Open source and customizable: the code is open source meaning that you don't have to worry about malware (the primary concern of modified games) and you can simply customize variables to cheat how you want, not how they want.
5. Harder to patch and more stable compared to other mods which can easily cause kicks, the only feature which causes a **kickloop** (known as a 10x worse ban) is disabled and not recommended. The game puts more efforts into patching the other types of modding which are easier-to-patch and fought everyday unlike this type of modding!

## Drawbacks

1. Harder to setup than usual; unlike other mods which require a simple installation, it requires the setup of a whole proxy (and the installation of a programming language, libraries). Coldie has tried to simplify such a big step with the introduction of requirements.txt, easy code structure and other measures, however it will never be enough.
2. Requires a computer, laptop or another machine to host the proxy. That machine should be always open with the proxy in case you wanna play. You need to be connected to the computer's malicious proxy instead of another proxy. If you use adblocking proxies, use an adblocking DNS instead.

## What is this project licensed under?

This project is licensed under the **GPL** license. For a full breakdown of the license, see the **LICENSE** file.

## Coldie would like to thank...

**bombie** is an amazing Python script which was the base of the entire project. It had many features that became the essentials of the proxy-based cheating, the proxy cheating era and Coldie itself. For that, Coldie would like you to star the project to show your appreciation! *The maintainer and owner of that project was me in a lost account, so I'm thanking my own project.*

**mitmproxy** is the entire project summarized in one word, both for **bombie** and **Coldie**. I'd like to thank the **mitmproxy API** which made it possible to modify traffic flow programmatically. The API made this process smoother with it's great documentation, simple naming scheme and the small learning curve of the project which allowed **bombie** to be completed while learning the API (that's how the amazing and quick the API is). The maintainers and owners of each dependency **mitmproxy** uses are also thanked.

**bombie** would like to thank some of the people on iOSGods for providing **bombie** for good motivation and giving answers to some of it's questions. The project was eventually moved to GitHub to ensure more stable hold of the code and it's maintainer, but it will eventually be posted to iOSGods.
