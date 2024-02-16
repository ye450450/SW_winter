from FAT32 import *
        
if __name__ == "__main__":
    
    fat32 = FAT32('./FAT32_simple.mdf')
    fat32.build()
    # leaf = fat32.get_node("/DIR1/LEAF.jpg")
    fat32.node.export_to("./leaf.jpg")
