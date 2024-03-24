class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        foods_set = set()
        tables = dict()
        
        for _, table, food in orders:
            if table not in tables:
                tables[table] = dict()
            
            if food not in tables[table]:
                tables[table][food] = 0
            
            foods_set.add(food)
            tables[table][food] += 1
        
        sorted_foods_set = sorted(foods_set)
        answer = []
        answer.append(["Table"] + sorted_foods_set)

        for table in sorted(tables, key=lambda x:int(x)):
            cur = [table]

            for food in sorted_foods_set:
                if food not in tables[table]:
                    cur.append("0")
                    continue

                cur.append(str(tables[table][food]))
            
            answer.append(cur)

        return answer