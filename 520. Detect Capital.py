def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word.isupper() or word.islower() or word==word.title():
            return True
        else:
            return False
