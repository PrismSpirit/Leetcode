class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        db = dict()
        output = list()

        for cpdomain in cpdomains:
            tmp = cpdomain.split(" ")
            count = int(tmp[0])
            domain = tmp[1]
            tmp = domain.split(".")

            for x in range(0, len(tmp)):
                tmp_list = list()
                for y in range(x, len(tmp)):
                    tmp_list.append(tmp[y])
                subdomain = ".".join(tmp_list)
                if subdomain in db:
                    db[subdomain] += count
                else:
                    db[subdomain] = count

        for k in db.keys():
            output.append(str(db[k]) + " " + k)

        return output