class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        db = dict()
        lower_paragraph = paragraph.lower()
        tmp = ""

        for x in range(0, len(lower_paragraph)):
            if 96 < ord(lower_paragraph[x]) < 123:
                tmp += lower_paragraph[x]
            else:
                if tmp == "":
                    continue
                if not tmp in banned:
                    if tmp in db:
                        db[tmp] += 1
                    else:
                        db[tmp] = 1
                tmp = ""
            if x == len(lower_paragraph) - 1 and 96 < ord(lower_paragraph[x]) < 123:
                if not tmp in banned:
                    if tmp in db:
                        db[tmp] += 1
                    else:
                        db[tmp] = 1
        
        return max(db.items(), key=lambda x: x[1])[0]