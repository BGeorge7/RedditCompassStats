import sys
sys.path.append(".")

from ideology import Ideology
from commentInfo import SubmissionCommentInfo
class ThreadStats:
    def __init__(self):
        self.noneCount = 0
        self.centristCount = 0
        self.authRightCount = 0
        self.authLeftCount = 0
        self.libLeftCount = 0
        self.libRightCount = 0
        self.authCenterCount = 0
        self.leftCount = 0
        self.libCenterCount = 0
        self.rightCount = 0

        self.noneAwardCount = 0
        self.centristAwardCount = 0
        self.authRightAwardCount = 0
        self.authLeftAwardCount = 0
        self.libLeftAwardCount = 0
        self.libRightAwardCount = 0
        self.authCenterAwardCount = 0
        self.leftAwardCount = 0
        self.libCenterAwardCount = 0
        self.rightAwardCount = 0

        self.noneScoreTotal = 0
        self.centristScoreTotal = 0
        self.authRightScoreTotal = 0
        self.authLeftScoreTotal = 0
        self.libLeftScoreTotal = 0
        self.libRightScoreTotal = 0
        self.authCenterScoreTotal = 0
        self.leftScoreTotal = 0
        self.libCenterScoreTotal = 0
        self.rightScoreTotal = 0

        self.allLeftCount = 0
        self.allRightCount = 0
        self.allCentristCount = 0

        self.countedUsers = []


    def ideology_score_increment(self, comment):
        if (comment.get_ideology() == Ideology.NONE): #None
            self.noneCount += 1
        elif (comment.get_ideology() == Ideology.CENTRIST): #Centrist
            self.centristCount += 1
        elif (comment.get_ideology() == Ideology.AUTHRIGHT): #Auth Right
            self.authRightCount += 1
        elif (comment.get_ideology() == Ideology.AUTHLEFT): #Auth Left
            self.authLeftCount += 1
        elif (comment.get_ideology() == Ideology.LIBLEFT): #Lib left
            self.libLeftCount += 1
        elif (comment.get_ideology() == Ideology.LIBRIGHT): #Lib Right
            self.libRightCount += 1
        elif (comment.get_ideology() == Ideology.AUTHCENTER): #Auth Center
            self.authCenterCount += 1
        elif (comment.get_ideology() == Ideology.LEFT): #Left
            self.leftCount += 1
        elif (comment.get_ideology() == Ideology.LIBCENTER): #Lib Center
            self.libCenterCount += 1
        elif (comment.get_ideology() == Ideology.RIGHT): #Right
            self.rightCount += 1
    
    def comment_score_increment(self, comment):
        if (comment.get_ideology() == Ideology.NONE): #None
            self.noneScoreTotal += 1
        elif (comment.get_ideology() == Ideology.CENTRIST): #Centrist
            self.centristScoreTotal += 1
        elif (comment.get_ideology() == Ideology.AUTHRIGHT): #Auth Right
            self.authRightScoreTotal += 1
        elif (comment.get_ideology() == Ideology.AUTHLEFT): #Auth Left
            self.authLeftScoreTotal += 1
        elif (comment.get_ideology() == Ideology.LIBLEFT): #Lib left
            self.libLeftScoreTotal += 1
        elif (comment.get_ideology() == Ideology.LIBRIGHT): #Lib Right
            self.libRightScoreTotal += 1
        elif (comment.get_ideology() == Ideology.AUTHCENTER): #Auth Center
            self.authCenterScoreTotal += 1
        elif (comment.get_ideology() == Ideology.LEFT): #Left
            self.leftScoreTotal += 1
        elif (comment.get_ideology() == Ideology.LIBCENTER): #Lib Center
            self.libCenterScoreTotal += 1
        elif (comment.get_ideology() == Ideology.RIGHT): #Right
            self.rightScoreTotal += 1

    def award_score_increment(self, comment):
        if (comment.get_ideology() == Ideology.NONE): #None
            self.noneAwardCount += 1
        elif (comment.get_ideology() == Ideology.CENTRIST): #Centrist
            self.centristAwardCount += 1
        elif (comment.get_ideology() == Ideology.AUTHRIGHT): #Auth Right
            self.authRightAwardCount += 1
        elif (comment.get_ideology() == Ideology.AUTHLEFT): #Auth Left
            self.authLeftAwardCount += 1
        elif (comment.get_ideology() == Ideology.LIBLEFT): #Lib left
            self.libLeftAwardCount += 1
        elif (comment.get_ideology() == Ideology.LIBRIGHT): #Lib Right
            self.libRightAwardCount += 1
        elif (comment.get_ideology() == Ideology.AUTHCENTER): #Auth Center
            self.authCenterAwardCount += 1
        elif (comment.get_ideology() == Ideology.LEFT): #Left
            self.leftAwardCount += 1
        elif (comment.get_ideology() == Ideology.LIBCENTER): #Lib Center
            self.libCenterAwardCount += 1
        elif (comment.get_ideology() == Ideology.RIGHT): #Right
            self.rightAwardCount += 1

    def left_right_increment(self,comment):
        if (comment.get_ideology() == Ideology.CENTRIST ): #None
            self.allCentristCount += 1
        if (comment.get_ideology() == Ideology.LEFT or comment.get_ideology() == Ideology.LIBLEFT or comment.get_ideology() == Ideology.AUTHLEFT): #Left
            self.allLeftCount += 1
        if (comment.get_ideology() == Ideology.AUTHRIGHT or comment.get_ideology() == Ideology.LIBRIGHT or comment.get_ideology() == Ideology.RIGHT ): #None
            self.allRightCount += 1


    def count_increment(self, comment, minimumScore = 0, maxScore = 999999, accountSameUserComments = False): #calls other incrementing functions

        if(not accountSameUserComments):
            if(comment.get_score() >= minimumScore and comment.get_score() <= maxScore):
                self.ideology_score_increment(comment)
                self.comment_score_increment(comment)
                self.award_score_increment(comment)
                self.left_right_increment(comment)
        else:
            if(comment.get_score() >= minimumScore and comment.get_score() <= maxScore and ((comment.get_authorUserName not in self.countedUsers) and accountSameUserComments )):
                #print("Got here")
                self.countedUsers.append(comment.get_authorUserName())
                self.ideology_score_increment(comment)
                self.comment_score_increment(comment)
                self.award_score_increment(comment)
                self.left_right_increment(comment)

        

    def ideology_breakdown(self):
        total = self.noneCount \
            + self.centristCount \
            + self.authRightCount \
            + self.authLeftCount \
            + self.libLeftCount \
            + self.libRightCount \
            + self.authCenterCount \
            + self.leftCount \
            + self.libCenterCount \
            + self.rightCount \

        print(f"Stats For Ideological Break Down")
        print(f"Out of a total of {total} comments The ideological break down was as follows")
        print(f"None's: {(self.noneCount / total) * 100:.2f}%")
        print(f"Centrist's: {(self.centristCount / total) * 100:.2f}%")
        print(f"Auth Right's: {(self.authRightCount / total) * 100:.2f}%")
        print(f"Lib Left's: {(self.libLeftCount / total) * 100:.2f}%")
        print(f"Lib Right's: {(self.libRightCount / total) * 100:.2f}%")
        print(f"Auth Center's: {(self.authCenterCount / total) * 100:.2f}%")
        print(f"Left's: {(self.leftCount / total) * 100:.2f}%")
        print(f"Lib Center's: {(self.libCenterCount / total) * 100:.2f}%")
        print(f"Right's: {(self.rightCount / total) * 100:.2f}%")

        print(f"\nBreak Down By Left and Right")
        print(f"Right Wing: {(self.allRightCount / total) * 100:.2f}")
        print(f"Left Wing: {(self.allLeftCount / total) * 100:.2f}")
        print(f"Centrist Wing: {(self.allCentristCount / total) * 100:.2f}")



