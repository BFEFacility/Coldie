# The Contribution Manual to Coldie

You'd make a big difference in a lone project. You will contribute to it's revival. 

## (some) Backstory...

Coldie is a project that has been started not in the hopes of earning money, it has been started in hopes of having a viable choice for it's kind (and to learn more about **Python**, **proxies**, **mitmproxy API** and **GitHub**). It was forked from the untouched project of Bombie which has been the true pioneer. After eventually 10 commits to the creation of README, a requirements.txt file and slight code improvements, it was deemed a stable fork. 

After some more committing, it was determined independent from it's old ghost and it left the fork network (and removed all traces of Bombie in the code)! It has all been made and connected by **sandStoop**, the creator, lead maintainer and the mastermind behind **Coldie**. I've been shadowbanned from GitHub the entire time I've made and have done 30+ commits while the project was being hosted there.

## Rules

1. No AI-generated code or content is allowed. This is a no-exception rule and it causes an instant ban from PR-ing. **YOU HAVE BEEN WARNED!** AI causes many problems, bugs and hallucinated text which is very bad. If it's not on English, translate it using a translation tool and we will try to handle the rest.
2. Don't intentionally try to push backdoors or viruses (like exec()-s or eval()-s) to cause harm to the users of this repository. This includes arbitrary command execution or backdoors. This will instantly cause an ban from PR-ing. *This should be obvious*
3. Do not try to lower the quality of our code. We don't aim for Python 2.x compatibility and our code should be new and good. Everything points to Python 3.x! This will not cause a ban but you will be warned!
4. **NO CHAINSAW PULL REQUESTS ALLOWED!** It isn't a good thing to be proud of, it's the ruining of code for open source projects in a tricky way to make testing work. This will cause an instant ban from PR-ing. This includes: many non-decodable characters by ASCII or Unicode or other problems.
5. Don't use the time library. It makes the script artificially slower, is a very unnecessary library for what this project does, includes more memory, bogs down the script and it is not for proxy scripts which are single-threaded. This will be pointed out on your code! This library is unnecessary, time.sleep(0) or time.sleep(0.01) is not awesome. It's useless, adds more lines and reduces code meaning and shames the code's culture and history.

## How to Contribute

1. Fork this GitHub repository using the **GitHub Web UI** or **git**. 
2. Edit the files that should be edited. Our main focus is the change of the main Python file, requirements.txt (if libraries were updated). You can focus on the README.md and INSTALLATION.md. Please do good changes to the Markdown files and not one liners to not waste time, it's recommended.
3. Open a new pull request to **Coldie** upstream, the repository you will contribute to is the main repository and compare it with your modified forks. Optionally, in the pull request compare the file before and after the change with a good title and nice description of all the changes and improvements.
5. You should argue with maintainers or others about why this iteration of the repository is better. This improves the chances of your PR being added, reduces work on our end and is overall more documented with more history.

You can also use **git** for the same task! *Please sign your commits if so with a PGP key or SSH key and help build a web of trust*!

**Coldie** would like to greatly thank you for your interest in this repository. A contribution can be a small grammatic improvement or a new feature.
