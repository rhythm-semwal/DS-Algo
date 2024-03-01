from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        hash_set = set()

        for email in emails:
            name, domain = email.split('@')

            original_email = name.split('+')[0].replace('.', '') + '@' + domain

            if original_email not in hash_set:
                hash_set.add(original_email)

        return len(hash_set)

