from mangopaysdk.tools.apibase import ApiBase
from mangopaysdk.entities.wallet import Wallet


class ApiWallets(ApiBase):
    """MangoPay API methods for wallets."""

    def Create(self, wallet):
        """Create new wallet.
        param Wallet wallet with fields: Owners, Descriptio, Currency, Tag
        return Wallet object returned from API
        """
        return self._createObject('wallets_create', wallet, 'Wallet')

    def Get(self, walletId):
        """Get wallet by Id.
        param int/GUID walletId identifier
        return Wallet object returned from API
        """
        return self._getObject('wallets_get', walletId, 'Wallet')

    def Update(self, wallet):
        """Update wallet.
        param Wallet wallet with fields: Id, Owners, Descriptio, Tag
        return Wallet object returned from API
        """
        return self._saveObject('wallets_save', wallet, 'Wallet')


    def GetTransactions(self, walletId, pagination = None, filter = None):
        """Get transactions for the wallet.
        param type walletId Wallet identifier
        param Pagination pagination object
        param FilterTransactions filter Object to filter data
        return Transaction[] Transactions for wallet returned from API
        """
        return self._getList('wallets_alltransactions', pagination, 'Transaction', walletId, filter)
