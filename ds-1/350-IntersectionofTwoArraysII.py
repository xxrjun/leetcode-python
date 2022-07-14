# 350. Intersection of Two Arrays II
# Idea:
#     1. 把第一個 array 依 (number, times) 放入 hash table
#     2. 另一個 list 去比較 hash table 並且 update times，有找到的話放入 returnResult

class Solution:
		def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
			returnResult = []
			hashTable = {}	# (number, times)

			hashTable = self.getHashTable(nums1)
			returnResult = self.findInterSection(nums2, hashTable)

			return returnResult
		

		# Helper funciton to get hash table from a List
		def getHashTable(self, numList: List[int]):
				returnHashTable = {}
				
				for n in numList:
					if n not in returnHashTable.keys():
						returnHashTable[n] = 1
					elif n in returnHashTable.keys():
						returnHashTable[n] += 1

				return returnHashTable


		# Helper function to find intersection from a list and hashTable
		def findInterSection(self, numList: List[int], hashTable: Dict):
				returnResult = []

				for n in numList:
					if n in hashTable.keys() and hashTable[n] > 0:
						returnResult.append(n)
						hashTable[n] -= 1

				return returnResult