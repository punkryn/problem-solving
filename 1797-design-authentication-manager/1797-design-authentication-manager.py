class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokenMap = dict()

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokenMap[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        if tokenId not in self.tokenMap:
            return
        
        expireTime = self.tokenMap[tokenId]

        if expireTime <= currentTime:
            return
        
        self.tokenMap[tokenId] = currentTime + self.timeToLive

    def countUnexpiredTokens(self, currentTime: int) -> int:
        cnt = 0
        for key in self.tokenMap:
            if self.tokenMap[key] > currentTime:
                cnt += 1
        return cnt


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)