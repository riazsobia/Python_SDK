from mangopaysdk.entities.entitybase import EntityBase
from mangopaysdk.entities.user import User
from mangopaysdk.tools.enums import PersonType


class UserLegal (User):

    def __init__(self, id = None):
        super(UserLegal, self).__init__(id)
        self._setPersonType(PersonType.Legal)

        self.Name = None
        # Required  LegalPersonType: BUSINESS, ORGANIZATION
        self.LegalPersonType = None
        self.HeadquartersAddress = None
        # Required
        self.LegalRepresentativeFirstName = None
        # Required
        self.LegalRepresentativeLastName = None
        self.LegalRepresentativeAddress = None
        self.LegalRepresentativeEmail = None
        # Required
        self.LegalRepresentativeBirthday = None
        # Required
        self.LegalRepresentativeNationality = None
        # Required
        self.LegalRepresentativeCountryOfResidence = None
        self._statute = None
        self._proofOfRegistration = None
        self._shareholderDeclaration = None

    def GetReadOnlyProperties(self):
        properties = super().GetReadOnlyProperties()
        properties.append('Statute' )        
        properties.append('ProofOfRegistration' )        
        properties.append('ShareholderDeclaration' )        
        return properties
