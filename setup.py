phab = None
LIMIT = 100


def setup_phab():
    import phabricator

    global phab
    phab = phabricator.Phabricator()
    phab.update_interfaces()


if __name__ == "__main__":
    setup_phab()
