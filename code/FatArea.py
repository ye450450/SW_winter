from byte_buffer2 import *

class FatArea:
    def __init__(self,bb):
        self.fat = []
        entry_count  = int(len(bb.m_data) / 4)
        for i in range(entry_count):
            self.fat.append(bb.get_uint4_le())
            
    def all_clusters(self, start):
        clusters = []
        next = start
        while next != 0xfffffff:
            clusters.append(next)
            next = self.fat[next]
        return clusters