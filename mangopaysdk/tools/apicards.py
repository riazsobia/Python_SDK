from mangopaysdk.tools.apibase import ApiBase
from mangopaysdk.entities.card import Card


class ApiCards (ApiBase):
    """Class to management MangoPay API for cards."""

    def Get(self, cardId):
        """Get card object
        param string Card identifier
        return Card Object returned from API
        """
        return self._getObject('card_get', cardId, 'Card')
