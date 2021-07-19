import phabricator
import time
import typing
import json


LIMIT = 100
phab = None
stories = dict()
user_queue: typing.List[str] = []


def setup_phab():
    global phab
    phab = phabricator.Phabricator(timeout=10)
    phab.update_interfaces()


def fetch_new_items():
    global phab, stories
    # num_stories = LIMIT
    new_stories = phabricator.Result(phab.feed.query(limit=LIMIT, view="data"))
    if len(new_stories.items()) > 0:
        stories.update(new_stories)


def filter_stories():
    global stories, user_queue
    for story in stories.values():
        if "transactionPHIDs" not in story["data"]:
            continue
        if story["authorPHID"] == story["data"]["objectPHID"]:
            transactionPHID = list(story["data"]["transactionPHIDs"].keys())[0]
            if "PHID-XACT-USER" in transactionPHID:
                user_queue.append(story["authorPHID"])


def get_user_urls():

   
   
    global user_queue, phab
    while len(user_queue) > 0:
        ln = min(len(user_queue), LIMIT)
        user_data = phab.user.search(
            constraints={"phids": user_queue[:ln], "isDisabled": False}, limit=LIMIT)
        user_queue = user_queue[ln:]
        f = open("logs.md", "r")
        safe = open("safe.md", "r")

        for phab_data in user_data["data"]:
            data = "https://developer.blender.org/p/" + phab_data["fields"]["username"]
            if data not in f.read():
                if data not in safe.read():
                    print(json.dumps(data))
        time.sleep(6)


if __name__ == '__main__':
    setup_phab()
    fetch_new_items()
    filter_stories()
    get_user_urls()
    # Make sure there's always something to commit.
    print(" ")
