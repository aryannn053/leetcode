class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs, letter_logs = [], []
        
        for log in logs:
            id, words = log.split(maxsplit=1)
            
            if words[0].isnumeric():
                digit_logs += [log]    
            else:
                letter_logs += [log]

        letter_logs.sort(key=lambda log: (log.split(maxsplit=1)[1], log.split(maxsplit=1)[0]))

        return letter_logs + digit_logs