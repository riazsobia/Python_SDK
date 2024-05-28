import random, string, time
from tests.testbase import TestBase
from mangopaysdk.mangopayapi import MangoPayApi
from mangopaysdk.types.pagination import Pagination
from mangopaysdk.types.exceptions.responseexception import ResponseException
from mangopaysdk.entities.userlegal import UserLegal
from mangopaysdk.entities.bankaccount import BankAccount
from mangopaysdk.entities.kycdocument import KycDocument
from mangopaysdk.entities.kycpage import KycPage
from mangopaysdk.tools.enums import *


class Test_ApiUsers(TestBase):

    def test_Users_CreateNatural(self):
        john = self.getJohn()
        self.assertTrue(int(john.Id) > 0)
        self.assertEqual(john.PersonType, PersonType.Natural)

    def test_Users_CreateLegal(self):
        matrix = self.getMatrix()
        self.assertTrue(int(matrix.Id) > 0)
        self.assertEqual(matrix.PersonType, PersonType.Legal)

    def test_Users_CreateLegal_FailsIfRequiredPropsNotProvided(self):
        user = UserLegal()
        with self.assertRaises(ResponseException) as cm:
            self.sdk.users.Create(user)
        self.assertEqual(400, cm.exception.Code)
        self.assertTrue('One or several required parameters are missing or incorrect' in cm.exception.Message)

    def test_Users_CreateLegal_PassesIfRequiredPropsProvided(self):
        user = UserLegal()
        user.Name = "SomeOtherSampleOrg"
        user.LegalPersonType = "BUSINESS"
        user.Email = "john.doe@sample.org"
        user.LegalPersonType = "BUSINESS"
        user.LegalRepresentativeFirstName = 'Piter'
        user.LegalRepresentativeLastName = 'Doe'
        user.LegalRepresentativeBirthday = int(time.mktime((1979, 11, 21, 0,0,0, -1, -1, -1)))
        user.LegalRepresentativeNationality = 'FR'
        user.LegalRepresentativeCountryOfResidence = 'FR'
        ret = self.sdk.users.Create(user)

        self.assertTrue(int(ret.Id) > 0, "Created successfully after required props set")
        self.assertEqualInputProps(user, ret)

    def test_Users_GetNatural(self):
        john = self.getJohn()

        user1 = self.sdk.users.Get(john.Id)
        user2 = self.sdk.users.GetNatural(john.Id)

        self.assertEqual(user1.Id, john.Id)
        self.assertEqual(user2.Id, john.Id)
        self.assertEqualInputProps(user1, john)
        self.assertEqualInputProps(user2, john)

    def test_Users_GetNatural_FailsForLegalUser(self):
        matrix = self.getMatrix()
        with self.assertRaises(Exception) as cm:
            user = self.sdk.users.GetNatural(matrix.Id)
        self.assertEqual(404, cm.exception.Code)
        self.assertTrue('The ressource does not exist' in cm.exception.Message)

    def test_Users_GetLegal_FailsForNaturalUser(self):
        john = self.getJohn()
        with self.assertRaises(Exception) as cm:
            user = self.sdk.users.GetLegal(john.Id)
        self.assertEqual(404, cm.exception.Code)
        self.assertTrue('The ressource does not exist' in cm.exception.Message)

    def test_Users_GetLegal(self):
        matrix = self.getMatrix()

        user1 = self.sdk.users.Get(matrix.Id)
        user2 = self.sdk.users.GetLegal(matrix.Id)

        self.assertEqual(user1.Id, matrix.Id)
        self.assertEqual(user2.Id, matrix.Id)
        self.assertEqualInputProps(user1, matrix)
        self.assertEqualInputProps(user2, matrix)

    def test_Users_UpdateNatural(self):
        john = self.getJohn()
        john.LastName += " - CHANGED"

        userUpdated = self.sdk.users.Update(john)
        userFetched = self.sdk.users.Get(john.Id)

        self.assertEqualInputProps(userUpdated, john)
        self.assertEqualInputProps(userFetched, john)

    def test_Users_UpdateLegal(self):
        matrix = self.getMatrix()
        matrix.LegalRepresentativeLastName += " - CHANGED"

        userUpdated = self.sdk.users.Update(matrix)
        userFetched = self.sdk.users.Get(matrix.Id)

        self.assertEqualInputProps(userUpdated, matrix)
        self.assertEqualInputProps(userFetched, matrix)

    def test_Users_CreateBankAccount(self):
        john = self.getJohn()
        account = self.getJohnsAccount()
        
        self.assertTrue(int(account.Id) > 0)
        self.assertEqual(account.UserId, john.Id)

    def test_Users_BankAccount(self):
        john = self.getJohn()
        account = self.getJohnsAccount()

        accountFetched = self.sdk.users.GetBankAccount(john.Id, account.Id)
        self.assertEqualInputProps(account, accountFetched)

    def test_Users_BankAccounts(self):
        john = self.getJohn()
        account = self.getJohnsAccount()
        pagination = Pagination(1, 12)

        list = self.sdk.users.GetBankAccounts(john.Id, pagination)

        self.assertIsInstance(list[0], BankAccount)
        self.assertEqual(account.Id, list[0].Id)
        self.assertEqualInputProps(account, list[0])
        self.assertEqual(pagination.Page, 1)
        self.assertEqual(pagination.ItemsPerPage, 12)
        self.assertTrue(pagination.TotalPages > 0)
        self.assertTrue(pagination.TotalItems > 0)

    def test_Users_CreateKycDocument(self):
        kycDoc = self.getUserKycDocument()
        self.assertNotEqual(kycDoc.Id, None)
        self.assertNotEqual(kycDoc.Id, 0)
        self.assertNotEqual(kycDoc.CreationDate, None)
        self.assertEqual(kycDoc.Status, KycDocumentStatus.CREATED)

    def test_Users_GetKycDocument(self):
        john = self.getJohn()
        kycDoc = self.getUserKycDocument()
        kycDocRes = self.sdk.users.GetUserKycDocument(kycDoc.Id, john.Id)
        self.assertEqual(kycDoc.Id, kycDocRes.Id)
        self.assertEqual(kycDoc.Tag, kycDocRes.Tag)
        self.assertEqual(kycDoc.Type, kycDocRes.Type)
        self.assertEqual(kycDoc.Status, kycDocRes.Status)   
        
    def test_Users_UpdateKycDocument(self):
        john = self.getJohn()
        kycDoc = self.getUserKycDocument()
        kycDoc.Status = KycDocumentStatus.VALIDATION_ASKED
        kycDocRes = self.sdk.users.UpdateUserKycDocument(kycDoc, john.Id, kycDoc.Id)
        self.assertEqual(kycDocRes.Status, KycDocumentStatus.VALIDATION_ASKED) 

    def test_Users_CreateKycDocumentPage(self):
        john = self.getJohn()
        kycDoc = self.getUserKycDocument()
        kycPage = KycPage().LoadDocumentFromFile('D:/7tapeta.jpg')
        kycDocRes = self.sdk.users.CreateUserKycPage(kycPage, john.Id, kycDoc.Id)
        self.assertEqual(kycDocRes, None)