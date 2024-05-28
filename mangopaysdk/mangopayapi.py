from mangopaysdk.tools import apioauth, apiclients, apiusers, apiwallets, apitransfers, apipayins, apipayouts, apievents
from mangopaysdk.tools import apirefunds, apicardregistrations, apicards
from mangopaysdk.configuration import Configuration
from mangopaysdk.tools.storages.authorizationtokenmanager import AuthorizationTokenManager


class MangoPayApi:

    """MangoPay API main entry point.
    Provides managers to connect, send and read data from MangoPay API
    as well as holds configuration/authorization data.
    """

    def __init__(self):

        #########################################
        # Config/authorization related fields
        #########################################

        # Configuration instance with default settings (to be reset if required).
        self.Config = Configuration()
        self.OAuthTokenManager = AuthorizationTokenManager(self);

        #########################################
        # API managers fields
        #########################################

        self.authenticationManager = apioauth.ApiOAuth(self)
        self.clients = apiclients.ApiClients(self)
        self.users = apiusers.ApiUsers(self)
        self.wallets = apiwallets.ApiWallets(self)
        self.transfers = apitransfers.ApiTransfers(self)
        self.payIns = apipayins.ApiPayIns(self)
        self.payOuts = apipayouts.ApiPayOuts(self)
        self.refunds = apirefunds.ApiRefunds(self)
        self.cardRegistrations = apicardregistrations.ApiCardRegistrations(self)
        self.cards = apicards.ApiCards(self)
        self.events = apievents.ApiEvents(self)