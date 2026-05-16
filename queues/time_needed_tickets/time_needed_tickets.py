class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        time = 0
        for i, ticket_count in enumerate(tickets):
            if i <= k: time +=  min(ticket_count, tickets[k])
            else: time += min(ticket_count, tickets[k] - 1)

        return time
