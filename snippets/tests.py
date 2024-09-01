from django.test import TestCase
from snippets.models import User, Snippet

class UserSnippetTestCase(TestCase):
    def setUp(self):
        """create a user and 3 snippets for this user"""
        self.user1 = User.objects.create(userName = "dhia")
        self.snippet1 = Snippet.objects.create(title="hello world", code="odjfois", owner = self.user1)
        self.snippet2 = Snippet.objects.create(title="hello world", code="odjfois", owner = self.user1)
        self.snippet3 = Snippet.objects.create(title="hello world", code="odjfois", owner = self.user1)

    def test_user(self):
        """creating a user"""
        user1 = User.objects.create(userName = "dhia")
        self.assertEqual(str(user1), str(self.user1))
    
    def test_snippets_of_user(self):
        """creating 3 snippet instances for a user"""
        user1 = User.objects.create(userName = "dhia")
        snippet1 = Snippet.objects.create(title="hello world", code="odjfois", owner = user1)
        snippet2 = Snippet.objects.create(title="hello world", code="odjfois", owner = user1)
        snippet3 = Snippet.objects.create(title="hello world", code="odjfois", owner = user1)
        print(user1.snippets.all().count(), self.user1.snippets.all().count())