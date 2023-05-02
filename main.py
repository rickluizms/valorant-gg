import services

americas = "americas"
emea = "emea"
pacific = "pacific"


def get_overview():

    services.scrap.get_overview(americas)

    services.scrap.get_overview(emea)
    
    services.scrap.get_overview(pacific)

def get_stats():

    services.scrap.get_stats(americas)

    services.scrap.get_stats(emea)

    services.scrap.get_stats(pacific)

def get_matches():

    services.scrap.get_matches(americas)

    services.scrap.get_matches(emea)

    services.scrap.get_matches(pacific)

def get_agents():
    
    services.scrap.get_agents(americas)

    services.scrap.get_agents(emea)

    services.scrap.get_agents(pacific)

#get_overview()
#get_stats()
get_matches()
get_agents()


