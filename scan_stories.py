import sched_user
import sched_feed
from sched_feed import stories
from sched_user import user_queue


def scan_stories():

    for story in stories.values():
        if "transactionPHIDs" not in story["data"]:
            continue
        if story["authorPHID"] == story["data"]["objectPHID"]:
            transactionPHID = list(story["data"]["transactionPHIDs"].keys())[0]
            if "PHID-XACT-USER" in transactionPHID:
                user_queue.append(story["authorPHID"])


while True:
    sched_feed.fetch_new_items()
    scan_stories()
    sched_user.user_url()
    # Make sure there's always something to commit.
    print(" ")
    break
