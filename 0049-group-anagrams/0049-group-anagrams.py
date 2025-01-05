class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = []
        word_dict = dict()
        for word in strs :
            word_dict[word] = ''.join(sorted(word))

        sorted_dict = sorted(word_dict.items(), key= lambda item:item[1])

        anagrams = []
        vlist = list(word_dict.values())

        for item in sorted_dict : 
            if vlist.count(item[1]) > 1 : 
                anagrams.append(item[0])
                vlist.remove(item[1])
            else : 
                anagrams.append(item[0])
                answer.append(anagrams)
                anagrams=[]

        return answer