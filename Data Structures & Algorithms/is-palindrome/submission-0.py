class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_chars = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        
        # Check if the filtered string is equal to its reverse
        return filtered_chars == filtered_chars[::-1]
