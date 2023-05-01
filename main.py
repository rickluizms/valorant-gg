import services

americas = "americas"
emea = "emea"
pacific = "pacific"


def get_overview():

    services.scrap.get_score(americas)

    services.scrap.get_score(emea)
    
    services.scrap.get_score(pacific)


def get_stats():
    
    services.scrap.get_stats(americas)

    services.scrap.get_stats(emea)

    services.scrap.get_stats(pacific)


get_overview()
get_stats()


