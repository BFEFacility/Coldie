#!/usr/bin/env python3
# Coldie v1.0.0-beta
# Python script that utilizes the mitmproxy API to cheat on Bomber Friends! It handles many cloud functions and abuses requests and responses.
# It's not just actual hacks... it's visual ones! An anti-ban is paired too! This is the peak of Bomber Friends cheating!

from json import dumps, loads 
from json.decoder import JSONDecodeError

try:
    from mitmproxy import http, ctx
except ModuleNotFoundError:
    raise SystemExit("The mitmproxy module wasn't found. The cause is likely attributed to the fact that mitmproxy isn't installed")
    
# This script works by modifying the response of many different cloud scripts (requested cloud scripts to do many things)
# Keep in mind that this script may be broken by API URL changes, API endpoint changes or the smallest changes to the JSON!

# Variables which make the modification of the script easier
# Putting values at -1 doesn't modify them and puts them as the same values. Holds true and should be done mostly for visual or unneeded values. The script simply checks if the value is -1 and discards the changes if that is true to ensure script safety
# Keep in mind the game accepts 0 as an unset bit and 1 as a set bit, it can also accept boolean values and integers however request/response flow has been modified to fit the used data type.
# TODO: Change values from -1 to False. Apart from representing the state of an unset bit (0), -1 doesn't represent an unset bit nor a set bit creating confusing. This change will be done in beta at maximum!

apiURL = "https://e1e6.playfabapi.com" # The URL of the API
apiCloudScriptURL = apiURL + "/Client/ExecuteCloudScript" # The cloud script's API endpoint which manages the execution of essential scripts

retrieveData = "getInitialData" # The only cloud script function which gets the initial data of the game (account included) which spans to a lot of hard-to-decode JSON full of metadata
bomberium = False # Amount of bomberium (visual)
freespins = False # Amount of free (non-VIP) spins (visual)
vipspins = False # Amount of 150 gem (VIP) spins (visual)
XP = False # XP which determines the level (not the rank) which gives you pretty good multiplayer benefits
gems = False # Gems (known as EL) (visual)
seasonPass = False # Is season pass enabled? (cannot claim rewards, fashion show rewards doubled and VIP icon is shown)
medals = False # Medals, also known as trophies in the game code (visual, chests can't be claimed (visual unless you've reached that medal range), matchmaking changes (unconfirmed), not on leaderboard) 
alwaysBots = False # Always match with bots; no match or medal limitations -> TODO: Test it in higher medal range
costumes = False # Get all costumes (it's a string value by design and requirement), this has been disabled since it has an extremely high chance of a kickloop (instant kick from any type of play, different from a ban) (AFFECTED, UNRECOMMENDED)
recommendedVersion = True # Always sets your version of the game to the recommended version of the game which allows you to play the game in any version of Bomber Friends (does not bring back features, just allows play)

fashionPointHandler = "addFashionPoints" # The cloud function which handles fashion show point claiming after an entry has been made.
fashionPoints = 100 # The number of fashion points (maximum: 100, smart server-side validation refuses bad values and causes kick)
ad = True # Doubles the number of fashion points

# NEW PLAYER EXCLUSIVE STUFF :(

tutorialWon = "tutorialWon" # The cloud function which handles if the tutorial is won
injectedTutorialWon = False # Determines if the rewards of the tutorial will be injected (visual)
injectedTutorialWonBO = 999999 # Determines the BO (bomberium, coins) won by the injected tutorial (visual)
injectedTutorialWonMedals = 999999 # Medals won by injected tutorial (visual)

def request(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_url.endswith(apiCloudScriptURL):
        ctx.log.info("Coldie: found request!")
        ctx.log.info("checking the request's cloud script...")
        try:
            apiCloudScriptURLRequest = loads(flow.request.get_text())
        except JSONDecodeError:
            ctx.log.warn("Coldie: this endpoint has returned undecodable JSON. this is a very weird and uncommon issue which has been caused due to API breakages, trying workaround...")
            try:
                apiCloudScriptURLRequest = loads(dumps(flow.response.get_text()))
            except JSONDecodeError:
                ctx.log.error("Coldie: nothing works!")
                flow.kill() # Kills the flow
            except Exception as e:
                ctx.log.error(e)
        except Exception as e:
            ctx.log.error(e)
        if apiCloudScriptURLRequest["FunctionName"] == fashionPointHandler: # If the request's script is the fashion point giver...
            try:
                apiCloudScriptURLRequest["FunctionParameter"]["points"] = fashionPoints if fashionPoints else apiCloudScriptURLRequest["FunctionParameter"]["points"] 
                apiCloudScriptURLRequest["FunctionParameter"]["ad"] = bool(ad) if ad else apiCloudScriptURLRequest["FunctionParameter"]["ad"]
                ctx.log.info("Coldie: VALUE INJECTION SUCCESSFUL! [1/2]")
            except KeyError:
                ctx.log.error("Coldie: the API has been changed and the result of the initial data cannot be found")
            except Exception as e:
                ctx.log.error(e)
            flow.request.text = dumps(apiCloudScriptURLRequest)
            ctx.log.info("Coldie: INJECTED REQUEST SENT TO SERVER! [2/2] :D")
        else: # TODO: Add more requests to hook...
            ctx.log.warn("Coldie: as of now, Coldie doesn't support other exploitable functions!")

def response(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_url.endswith(apiCloudScriptURL):
        ctx.log.info("Coldie: found api endpoint!")
        ctx.log.info("Coldie: checking the entire cloud script...")
        try:
            apiCloudScriptURLResponse = loads(flow.response.get_text())
        except JSONDecodeError:
            ctx.log.warn("Coldie: this endpoint has returned undecodable JSON. this is a very common issue due to bad return value however there's a workaround...")
            try:
                apiCloudScriptURLResponse = loads(dumps(flow.response.get_text())) # Workaround for the currently bad JSON for Python's json.loads()
            except JSONDecodeError:
                ctx.log.error("Coldie: nothing works!")
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

                    if bomberium:
                         apiCloudScriptURLResponse["data"]["FunctionResult"]["BO"] = int(bomberium)

                    if freespins:
                         apiCloudScriptURLResponse["data"]["FunctionResult"]["rewardwheel"]["rewardspins"] = int(freespins) 
                    
                    if vipspins:
                        apiCloudScriptURLResponse["data"]["FunctionResult"]["rewardwheel"]["vipspins"] = int(vipspins)
                        
                    if gems:
                        apiCloudScriptURLResponse["data"]["FunctionResult"]["EL"] = int(gems)

                    if seasonPass:
                        apiCloudScriptURLResponse["data"]["FunctionResult"]["seasonP"]["seasonPass"] = True # This fixes the API changes, using seasonP instead of seasonD.
                        
                    if medals:
                        apiCloudScriptURLResponse["data"]["FunctionResult"]["trophies"] = int(medals) 

                    if XP:
                        apiCloudScriptURLResponse["data"]["FunctionResult"]["xp"] = XP 

                    if costumes:
                        apiCloudScriptURLResponse["data"]["FunctionResult"]["custItems"] = "1" * 3000 # Maybe, make this more reliable when the game ages beyond 3000 items?

                    if recommendedVersion:
                         apiCloudScriptURLResponse["data"]["FunctionResult"]["version"] = apiCloudScriptURLResponse["data"]["FunctionResult"]["recommended"] # Make the version become the version if the feature is not on

                    # ANTI-BAN 
                    apiCloudScriptURLResponse["data"]["FunctionResult"]["banned"] = 0 # 0 is the same as False, this uses an integer since an integer is expected by the server
                    apiCloudScriptURLResponse["data"]["FunctionResult"]["banReason"] = ""
                    apiCloudScriptURLResponse["data"]["FunctionResult"]["banExtraInfo"] = ""
                    apiCloudScriptURLResponse["data"]["FunctionResult"]["banInfo"] = ""

                    # ALWAYS BOTS; EASY MEDAL FARMING
                    if alwaysBots:
                        apiCloudScriptURLResponse["data"]["FunctionResult"]["botMatch"]["trophyLimit"] = int(999999) # If you're below 999,999 medals, only bots!
                        apiCloudScriptURLResponse["data"]["FunctionResult"]["botMatch"]["dailyGameLimit"] = int(999999) # You can play with bots 999,999 games a day!
                        apiCloudScriptURLResponse["data"]["FunctionResult"]["botMatch"]["maxLimit"] = int(999999) # You can play 999,999 games of bots before no bots!
                        apiCloudScriptURLResponse["data"]["FunctionResult"]["botMatchPlayerData"]["dailyGamesPlayed"] = int(0) # You have played no games with bots... keep playing!
                    else:
                        pass

                    ctx.log.info("Coldie: VALUE INJECTION SUCCESSFUL! [1/2]")
                except KeyError:
                    ctx.log.error("Coldie: the API has been changed and the result of the initial data cannot be found")
                except Exception as e:
                    ctx.log.error(e)
                try:
                    flow.response.text = dumps(apiCloudScriptURLResponse)
                    ctx.log.info("Coldie: INJECTED RESPONSE SENT TO CLIENT! [2/2] :D")
                except Exception as e:
                    ctx.log.error(e)
            elif apiCloudScriptURLResponse["data"]["FunctionName"] == tutorialWon:
                if isinstance(apiCloudScriptURLResponse["data"]["FunctionResult"], str):
                    apiCloudScriptURLResponse["data"]["FunctionResult"] = loads(apiCloudScriptURLResponse["data"]["FunctionResult"])
                if bool(injectedTutorialWon) != False:
                    try:
                        apiCloudScriptURLResponse["data"]["FunctionResult"]["BO"] = int(injectedTutorialWonBO) # The injected bomberium is the bomberium you earn visually after spoofed tutorial completion
                        apiCloudScriptURLResponse["data"]["FunctionResult"]["trophies"] = int(injectedTutorialWonMedals) # The injected medals is the medals you earn visually in the spoofed tutorial match
                        ctx.log.info("Coldie: VALUE INJECTION SUCCESSFUL! [1/2]")
                    except KeyError:
                        ctx.log.error("Coldie: the API has been changed and the result of the initial data cannot be found")
                    except Exception as e:
                        ctx.log.error(e)
                else:
                    pass
            try:
                flow.response.text = dumps(apiCloudScriptURLResponse)
                ctx.log.info("Coldie: INJECTED RESPONSE SENT TO CLIENT! [2/2] :D")
            except Exception as e:
                ctx.log.error(e)
            else: # TODO: Implement many more cloud scripts (every cloud script require it's function name and data to setup)
                ctx.log.warn("Coldie: as of now, Coldie doesn't support other exploitable functions!")

        else:
            ctx.log.error("Coldie: non-ok status code has been returned pre-modification!")
