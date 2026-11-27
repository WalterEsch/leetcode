class Twitter:
    def __init__(self):
        self.t = 0
        self.tweets = []
        self.follows = collections.defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.t += 1
        self.tweets.append((self.t, userId, tweetId))

    def getNewsFeed(self, userId):
        who = self.follows[userId] | {userId}
        return [tid for _, u, tid in sorted(self.tweets, reverse=True) if u in who][:10]

    def follow(self, followerId, followeeId):
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.follows[followerId].discard(followeeId)
