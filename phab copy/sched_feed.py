import phabricator
import setup
import time
from setup import LIMIT

stories = dict()


def update_queue(new_stories):
    """
    Add new items to the story checking queue.
    """

    global stories
    stories.update(new_stories)


def fetch_new_items():
    """
    Fetch new items since last epoch.
    """
    setup.setup_phab()
    phab = setup.phab
    # num_stories = LIMIT
    new_stories = phabricator.Result(phab.feed.query(limit=LIMIT, view="data"))
    num_stories = len(new_stories.items())
    if num_stories > 0:
        update_queue(new_stories)
