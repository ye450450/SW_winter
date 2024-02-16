from byte_buffer2 import *
from superblock import *
from FatArea import *
from directoryEntry import *

class Node:
    def __init__(self, file) :
        self.name = " "
        self.size = 0
        self.source = file
        self.extents = [] #(40000,1000)
    
    def export_to(self, path) :
        with open(path, 'wb') as f:
            for extent in self.extents:
                addr, size = extent
                self.source.seek(addr)
                b = self.source.read(size)
                f.write(b)

class FAT32:
    def __init__(self, input_file):
        self.sb = None
        self.fat0 = None
        self.file = None
        self.node = None
        self.node_list = []
        
        buffer = None
        self.file = open(input_file, 'rb')
        
        #superblock
        buffer = self.file.read(0x200)
        bb = ByteBuffer2(buffer)
        self.sb = Superblock(bb)
        
        # FAT
        self.file.seek(self.sb.start_fat_pos)
        buffer2 = self.file.read(self.sb.fat_size)
        bb2 = ByteBuffer2(buffer2)
        self.fat = FatArea(bb2)
    
    def build(self):
        self.file.seek(self.sb.start_cluster_pos+0x4040)
        buffer3 = self.file.read(0x20)
        bb3 = ByteBuffer2(buffer3)
        leaf = directoryEntry(bb3)
        self.node = self.toNode(leaf)
        
    def build(self, pos, prev_name):
        
        start_pos = pos
                
        while start_pos < 0x4000A0:
            self.file.seek(start_pos)
            buffer = self.file.read(0x20)
            bb = ByteBuffer2(buffer)
            de = directoryEntry(bb)
            
            if de.is_file:
                dir_name = prev_name + "/" + de.name
                self.node_list.append({dir_name : self.toNode(de)})
            if de.is_dir:
                self.build("/" + dir_name)

    def get_node(self, input_path):
        return self.node_list[input_path]
    
    def to_Extents(self, clusters):
        extents = []
        for cluster in clusters:
            Addr = self.sb.start_cluster_pos + (cluster-self.sb.root_inode) * self.sb.cluster_size
            extents.append((Addr, self.sb.cluster_size))
        
        return extents
       
    def toNode(self, dir_entry):
        node = Node(self.file)
        node.name = dir_entry.name
        node.size = dir_entry.size
        clusters = self.fat.all_clusters(dir_entry.cluster_no)
        node.extents = self.to_Extents(clusters)
        
        return node