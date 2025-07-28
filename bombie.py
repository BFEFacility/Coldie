#!/usr/bin/env python3
# bombie v1.0-alpha
# Python script that utilizes the mitmproxy API to cheat on Bomber Friends! It handles many cloud functions and abuses requests and responses.
# It's not just actual hacks... it's visual ones! An anti-ban is paired too! This is the peak of Bomber Friends cheating!

from mitmproxy import http, ctx
from time import sleep
from json import dumps, loads
from json.decoder import JSONDecodeError

# This script works by modifying the response of many different cloud scripts (requested cloud scripts to do many things)
# Keep in mind that this script may be broken by API URL changes, API endpoint changes or the smallest changes to the JSON!

# Variables which make the modification of the script easier
# Putting values at -1 doesn't modify them and puts them as the same values. Holds true and should be done mostly for visual or unneeded values

apiURL = "https://e1e6.playfabapi.com" # The URL of the API
apiCloudScriptURL = apiURL + "/Client/ExecuteCloudScript" # The cloud script's API endpoint which manages the execution of essential scripts

retrieveData = "getInitialData" # The only cloud script function which gets the initial data of the game (account included) which spans to a lot of hard-to-decode JSON full of metadata
bomberium = -1 # Amount of bomberium (visual)
freespins = -1 # Amount of free (non-VIP) spins (visual)
vipspins = -1 # Amount of 150 gem (VIP) spins (visual)
seasonPass = False # Is season pass enabled? (cannot claim rewards, fashion show rewards doubled and VIP icon is shown)
XP = -1 # XP which determines the level (not the rank) which gives you pretty good multiplayer benefits
gems = -1 # Gems (known as EL) (visual)
medals = -1 # Medals, also known as trophies in the game code (visual, chests can't be claimed (visual unless you've reached that medal range), matchmaking changes (unconfirmed), not on leaderboard) 
alwaysBots = True # Always match with bots; no match or medal limitations -> TODO: Test it in higher medal range
costumes = "0" # Get all costumes (it's a string value by design and requirement), this has been disabled since it has an extremely high chance of a kickloop (instant kick from any type of play, different from a ban) (AFFECTED, UNRECOMMENDED)

fashionPointHandler = "addFashionPoints" # The cloud function which handles fashion show point claiming after an entry has been made.
fashionPoints = 100 # The number of fashion points (maximum: 100, smart server-side validation refuses bad values)
ad = True # Doubles the number of fashion points

# NEW PLAYER EXCLUSIVE STUFF :(

tutorialWon = "tutorialWon" # The cloud function which handles if the tutorial is won
injectedTutorialWon = True # Determines if the rewards of the tutorial will be injected (visual)
injectedTutorialWonBO = 999999 # Determines the BO (bomberium, coins) won by the injected tutorial (visual)
injectedTutorialWonMedals = 999999 # Medals won by injected tutorial (visual)

def request(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_url.endswith(apiCloudScriptURL):
        ctx.log.info("bombie: found request!")
        sleep(0.25)
        ctx.log.info("checking the request's cloud script...")
        try:
            apiCloudScriptURLRequest = loads(flow.request.get_text())
        except JSONDecodeError:
            ctx.log.warn("bombie: this endpoint has returned undecodable JSON. this is a very weird and uncommon issue which has been caused due to API breakages, trying workaround...")
            sleep(0.25)
            try:
                apiCloudScriptURLRequest = loads(dumps(flow.response.get_text()))
            except JSONDecodeError:
                ctx.log.error("bombie: nothing about this request is right and bombie cannot intercept it!")
                flow.kill() # Kills the flow
            except Exception as e:
                ctx.log.error(e)
        except Exception as e:
            ctx.log.error(e)
        if apiCloudScriptURLRequest["FunctionName"] == fashionPointHandler: # If the request's script is the fashion point giver...
            try:
                if fashionPoints != -1:
                    apiCloudScriptURLRequest["FunctionParameter"]["points"] = fashionPoints
                else:
                    pass 
                if ad != False:
                    apiCloudScriptURLRequest["FunctionParameter"]["ad"] = bool(ad)
                else:
                    pass
                ctx.log.info("bombie: VALUE INJECTION SUCCESSFUL! [1/2]")
            except KeyError:
                ctx.log.error("bombie: the API has been changed and the result of the initial data cannot be found")
            except Exception as e:
                ctx.log.error(e)
            flow.request.text = dumps(apiCloudScriptURLRequest)
            ctx.log.info("bombie: INJECTED REQUEST SENT TO SERVER! [2/2] :D")
        else: # TODO: Add more requests to hook...
            ctx.log.warn("bombie: as of now, bombie doesn't support other exploitable functions!")

def response(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_url.endswith(apiCloudScriptURL):
        ctx.log.info("bombie: found api endpoint!")
        sleep(0.25)
        ctx.log.info("bombie: checking the entire cloud script...")
        try:
            apiCloudScriptURLResponse = loads(flow.response.get_text())
        except JSONDecodeError:
            ctx.log.warn("bombie: this endpoint has returned undecodable JSON. this is a very common issue due to bad return value however there's a workaround...")
            sleep(0.25)
            try:
                apiCloudScriptURLResponse = loads(dumps(flow.response.get_text())) # Workaround for the currently bad JSON for Python's json.loads()
            except JSONDecodeError:
                ctx.log.error("bombie: nothing works!")
                flow.kill() # kills the entire flow and nothing is sent!
            except Exception as e:
                ctx.log.error(e)
                flow.kill() # if the workaround doesn't work... why should it keep going? if no approach works... why bother?
        except Exception as e:
            ctx.log.error(e)
        if flow.response.status_code == int(200): # If the response doesn't reject or decline the value, should be checked via the status code not from the request!
            if apiCloudScriptURLResponse["data"]["FunctionName"] == retrieveData:
                try:
                    if isinstance(apiCloudScriptURLResponse["data"]["FunctionResult"], str):
                        apiCloudScriptURLResponse["data"]["FunctionResult"] = loads(apiCloudScriptURLResponse["data"]["FunctionResult"])
                    
                    if bomberium != -1:
                        apiCloudScriptURLResponse["data"]["FunctionResult"]["BO"] = int(bomberium)
                    else:
                        pass

                    if freespins != -1:
                        apiCloudScriptURLResponse["data"]["FunctionResult"]["rewardwheel"]["rewardspins"] = int(freespins)
                    else:
                        pass

                    if vipspins != -1:
                        apiCloudScriptURLResponse["data"]["FunctionResult"]["rewardwheel"]["vipspins"] = int(vipspins)
                    else:
                        pass

                    if gems != -1:
                        apiCloudScriptURLResponse["data"]["FunctionResult"]["EL"] = int(gems)
                    else:
                        pass

                    if medals != -1:
                        apiCloudScriptURLResponse["data"]["FunctionResult"]["trophies"] = int(medals)
                    else:
                        pass

                    if seasonPass != False:
                        apiCloudScriptURLResponse["data"]["FunctionResult"]["seasonD"]["seasonPass"] = seasonPass
                    else:
                        pass

                    if XP != -1:
                        apiCloudScriptURLResponse["data"]["FunctionResult"]["xp"] = XP
                    else:
                        pass

                    apiCloudScriptURLResponse["data"]["FunctionResult"]["custItems"] = str(costumes) * 3000 # Responsible for all costumes injection, adds 3,000 set/unset bits which ensures the user will get all 3,000 items (AFFECTED, DON'T USE)

                    # ANTI-BAN 
                    apiCloudScriptURLResponse["data"]["FunctionResult"]["banned"] = 0 # 0 is the same as False, this uses an integer since an integer is expected by the server
                    apiCloudScriptURLResponse["data"]["FunctionResult"]["banReason"] = ""
                    apiCloudScriptURLResponse["data"]["FunctionResult"]["banExtraInfo"] = ""
                    apiCloudScriptURLResponse["data"]["FunctionResult"]["banInfo"] = ""

                    # ALWAYS BOTS; EASY MEDAL FARMING
                    if alwaysBots != False:
                        apiCloudScriptURLResponse["data"]["FunctionResult"]["botMatch"]["trophyLimit"] = int(999999) # If you're below 999,999 medals, only bots!
                        apiCloudScriptURLResponse["data"]["FunctionResult"]["botMatch"]["dailyGameLimit"] = int(999999) # You can play with bots 999,999 games a day!
                        apiCloudScriptURLResponse["data"]["FunctionResult"]["botMatch"]["maxLimit"] = int(999999) # You can play 999,999 games of bots before no bots!
                        apiCloudScriptURLResponse["data"]["FunctionResult"]["botMatchPlayerData"]["dailyGamesPlayed"] = int(0) # You have played no games with bots... keep playing!
                    else:
                        pass

                    ctx.log.info("bombie: VALUE INJECTION SUCCESSFUL! [1/2]")
                except KeyError:
                    ctx.log.error("bombie: the API has been changed and the result of the initial data cannot be found")
                except Exception as e:
                    ctx.log.error(e)
                try:
                    flow.response.text = dumps(apiCloudScriptURLResponse)
                    ctx.log.info("bombie: INJECTED RESPONSE SENT TO CLIENT! [2/2] :D")
                except Exception as e:
                    ctx.log.error(e)
            elif apiCloudScriptURLResponse["data"]["FunctionName"] == tutorialWon:
                if isinstance(apiCloudScriptURLResponse["data"]["FunctionResult"], str):
                    apiCloudScriptURLResponse["data"]["FunctionResult"] = loads(apiCloudScriptURLResponse["data"]["FunctionResult"])
                if bool(injectedTutorialWon) != False:
                    try:
                        apiCloudScriptURLResponse["data"]["FunctionResult"]["BO"] = int(injectedTutorialWonBO) # The injected bomberium is the bomberium you earn visually after spoofed tutorial completion
                        apiCloudScriptURLResponse["data"]["FunctionResult"]["trophies"] = int(injectedTutorialWonMedals) # The injected medals is the medals you earn visually in the spoofed tutorial match
                        ctx.log.info("bombie: VALUE INJECTION SUCCESSFUL! [1/2]")
                    except KeyError:
                        ctx.log.error("bombie: the API has been changed and the result of the initial data cannot be found")
                    except Exception as e:
                        ctx.log.error(e)
                else:
                    pass
            try:
                flow.response.text = dumps(apiCloudScriptURLResponse)
                ctx.log.info("bombie: INJECTED RESPONSE SENT TO CLIENT! [2/2] :D")
            except Exception as e:
                ctx.log.error(e)
            else: # TODO: Implement many more cloud scripts (every cloud script require it's function name and data to setup)
                ctx.log.warn("bombie: as of now, bombie doesn't support other exploitable functions!")

        else:
            ctx.log.error("bombie: non-ok status code has been returned pre-modification!")
