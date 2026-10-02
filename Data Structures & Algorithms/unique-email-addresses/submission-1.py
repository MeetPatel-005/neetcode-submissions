class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()

        for email in emails:
            localName,domain = email.split("@") 
            localName = localName.replace(".","").split("+")
            seen.add(localName[0]+domain)

        return len(seen)