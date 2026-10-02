class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()

        for email in emails:
            localName,domain = email.split("@") 
            localName = localName.replace(".","").split("+")[0]
            seen.add(localName+"@"+domain)

        return len(seen)