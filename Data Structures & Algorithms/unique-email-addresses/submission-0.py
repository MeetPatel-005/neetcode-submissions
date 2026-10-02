class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()

        for email in emails:
            prefix,suffix = email.split("@") 

            prefix = prefix.replace(".","")
            start = prefix.find('+')

            if start == -1: final = prefix + suffix 
            else: final = prefix[:start] + suffix
            seen.add(final)
            
        return len(seen)