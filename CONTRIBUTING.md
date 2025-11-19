# The Contribution Manual to Coldie

You'd make a big difference in a lone project. You will contribute to it's revival. 

## (some) Backstory...

Coldie is a project that has been started not in the hopes of earning money, it has been started in hopes of having a viable choice for it's kind (and to learn more about **Python**, **proxies**, **mitmproxy API** and **GitHub**). It was forked from the untouched project of Bombie which has been the true pioneer. After eventually 10 commits to the creation of README, a requirements.txt file and slight code improvements, it was deemed a stable fork. After some more committing, it was determined independent from it's old ghost and it left the fork network (and removed all traces of Bombie in the code). As of the time of writing this, there have been *32* commits! (33 in the untested branch). That's (nearly) one third of 100 commits in the span of a week (more correctly, 5-6 days)! It has all been made and connected by **sandStoop**, the creator, lead maintainer and the mastermind behind **Coldie**. No money, no big achievements, no awards and no fame (I've been shadowbanned from GitHub the entire time I've made and have done 30+ commits!).

## Rules

1. No AI-generated code, content or content is allowed. This is a no-exception rule and it causes an instant ban from PR-ing. **YOU HAVE BEEN WARNED!** AI causes many problems, bugs and hallucinated text which is very bad for **Coldie**. If it's not on English, translate it and we will try to handle the rest though it's not recommended.
2. Don't intentionally try to push backdoors or viruses (like exec()-s or eval()-s) to cause harm to the users of this repository. This includes arbitrary command execution or suspicious behavior. This will instantly cause an ban from PR-ing.
3. Do not try to lower the quality of our code intentionally or unintentionally, such as adding very old features that maintainers do not agree with that have no or very little benefit. We don't aim for Python 2.x compatibility! Everything points to Python 3.x! This will not cause a ban but you will be warned!
4. **NO CHAINSAW PULL REQUESTS ALLOWED!** It isn't a cool thing to be proud of, it's the ruining of code for open source projects in a tricky way to make testing work. This will cause an instant ban from PR-ing. This includes: many non-decodable characters, too many or very weird comments and weaker or slower code (and algorithms).
5. Don't use the time library. It makes the script artificially slower, is a very unnecessary library for what this project does, includes more memory, bogs down the script and it is not for proxy scripts which are single-threaded. This will be pointed out on (and very likely stripped out of) your code! This library is unnecessary, time.sleep(0) or time.sleep(0.01) is not awesome. It's useless, adds more lines and reduces code meaning and shames the code's culture and history.

## How to Contribute

**This tutorial uses the GitHub Web UI!**

1. Fork this GitHub repository using the **GitHub Web UI** or **git**. The **GitHub Web UI** is recommended since it's the used format for this project and code is edited with a seperate text editor and not **GitHub Web UI**.
2. Edit the files that should be edited. Our main focus is the change of the main Python file, requirements.txt (if library versions or libraries were changed, added or removed). You can focus on the README.md and INSTALLATION.md. Please do good changes to the Markdown files, it's recommended.
3. Open a new PR (pull request) to **Coldie**, the repository you will contribute to is the main repository and compare it with your modified forks.
4. Compare them carefully (you likely have!) and create a pull request of it with a good title and nice description of all the changes and improvements.
5. You should argue with maintainers or others about why this iteration of the repository is better. This improves the chances of your PR being added, reduces work on our end (and we will be nicer to you!) and is overall more documented with more history.

You can also use **git** for the same task! Please sign your commits if so.

**Coldie** would like to greatly thank you for your interest in this repository. A contribution can be a small typo fix (there are a lot of them, please add more typo fixes or better changes to reduce PR checking and other factors) or a new feature.
