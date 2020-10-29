import ideology

class SubmissionCommentInfo:
    def __init__(self, ideology, score, authorUserName, permalink, controversiality, totalAwards):
        self.ideology = ideology
        self.authorUserName = authorUserName
        self.score = score
        self.permalink = permalink
        self.controversiality = controversiality
        self.totalAwards = totalAwards

    def get_ideology(self):
        return self.ideology

    def get_authorUserName(self):
        return self.authorUserName

    def get_score(self):
        return self.score

    def get_permalink(self):
        return self.permalink

    def get_controversiality(self):
        return self.controversiality

    def get_totalAwards(self):
        return self.totalAwards

    