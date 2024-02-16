from byte_buffer2 import *

class Superblock:
    def __init__(self, bb):
        bb.offset(0xb)
        self.sec_byte = bb.get_uint2_le()
        self.clus_sec = bb.get_uint1_le()
        self.cluster_size = self.sec_byte*self.clus_sec
        self.reserve_num_sec = bb.get_uint2_le()
        
        #FAT 시작부분
        self.start_fat_pos = self.sec_byte * self.reserve_num_sec
        self.num_fat = bb.get_uint1_le()
        
        bb.m_offset = 0
        bb.offset(0x20+4)
        self.num_fat_sec = bb.get_uint4_le()
        #FAT SIZE
        self.fat_size = self.num_fat_sec*self.sec_byte
        bb.offset(4)
        self.root_inode = bb.get_uint4_le()
        #데이터 시작부분
        self.start_cluster_pos = self.start_fat_pos + self.num_fat*self.num_fat_sec*self.sec_byte