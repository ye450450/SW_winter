
from byte_buffer2 import *
from superblock import *

class directoryEntry:
    def __init__(self, bb):
        self.read_attributes(bb)
        self.read_cluster_info(bb)


    def read_attributes(self, bb):
        bb.offset(0xb)
        self.attr = bb.get_uint1_le()

        self.is_file = self.attr == 0x20
        self.is_dir = self.attr == 0x10

    def read_cluster_info(self, bb):
        
        bb.m_offset = 0; bb.offset(0)
        name = bb.get_ascii(8)
        name = name.replace(" ","")
        bb.m_offset = 0; bb.offset(0x8)
        ext = bb.get_ascii(3)
        ext = ext.replace(" ","")
        self.name = name +"."+ ext
        
        bb.m_offset = 0; bb.offset(0x20-4)
        self.size = bb.get_uint4_le()
        
        bb.m_offset = 0
        bb.offset(0x10 + 4)
        self.cluster_hi = bb.get_uint2_le()
        bb.offset(4)
        self.cluster_lo = bb.get_uint2_le()

        self.cluster_no = (self.cluster_hi << 16) | self.cluster_lo
    
    
    
    def export_to(self, source, path, sb):
        with open(path, 'wb') as file:
            for cluster in self.clusters:
                physical_Add = sb.start_cluster_pos + (cluster-sb.root_inode) * sb.cluster_size
                source.seek(physical_Add)
                b = source.read(sb.cluster_size)
                file.write(b)
                
                