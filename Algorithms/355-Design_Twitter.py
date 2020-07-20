class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.post = list()
        self.follow_dict = dict()

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.post.append([userId, tweetId])
        if not userId in self.follow_dict:
            self.follow_dict[userId] = [userId]

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        if not userId in self.follow_dict:
            self.follow_dict[userId] = [userId]
        newsfeed = list()
        for x in self.post:
            if x[0] in self.follow_dict.get(userId):
                if len(newsfeed) == 10:
                    del newsfeed[0]
                    newsfeed.append(x[1])
                else:
                    newsfeed.append(x[1])
        newsfeed.reverse()
        return newsfeed
        
    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if not followerId in self.follow_dict:
            self.follow_dict[followerId] = [followerId]
        self.follow_dict[followerId].append(followeeId)
            
    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId and self.follow_dict.get(followerId) != None and self.follow_dict.get(followerId).count(followeeId):
            self.follow_dict.get(followerId).remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)