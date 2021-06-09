import phabricator
import setup
import time
import typing
import json
from setup import LIMIT

user_queue: typing.List[str] = []


def user_url():
    """
    Return user profile URL given a `PHID-USER` ID.
    """
    global user_queue
    phab = setup.phab
    while len(user_queue) > 0:
        ln = min(len(user_queue), LIMIT)
        user_data = phab.user.search(
            constraints={"phids": user_queue[:ln]}, limit=LIMIT
        )

        user_queue = user_queue[ln:]
        for phab_data in user_data["data"]:
            data = {
                "url": "https://developer.blender.org/people/manage/"
                + str(phab_data["id"]),
                "phid": phab_data["phid"],
                "username": phab_data["fields"]["username"],
            }

            f = open("logs.json", "r")
            if "https://developer.blender.org/people/manage/" + str(phab_data["id"] not in f.read():
               print(json.dumps(data))
        time.sleep(6)


if __name__ == "__main__":
    pass
