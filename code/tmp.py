

# buffer = None
    # superblock
    # with open('./FAT32_simple.mdf', 'rb') as file:
        
    #     # superblock
    #     buffer = file.read(0x200)
    #     bb = ByteBuffer2(buffer)
    #     sb = Superblock(bb)
    
    #     # FAT
    #     file.seek(sb.start_fat_pos)
    #     buffer2 = file.read(sb.fat_size)
    #     bb2 = ByteBuffer2(buffer2)
    #     ft = FatArea(bb2)

    #     # directory entry
    #     start_pos = sb.start_cluster_pos
    #     # while True:
    #     file.seek(start_pos+0x4040)
    #     buffer3 = file.read(0x20)
    #     bb3 = ByteBuffer2(buffer3)
    #     de = directoryEntry(bb3,ft.fat)
    #     de.export_to(file,"./test.jpg",sb)
        
    #     file.seek(start_pos+0x4060)
    #     buffer3 = file.read(0x20)
    #     bb3 = ByteBuffer2(buffer3)
    #     de = directoryEntry(bb3,ft.fat)
    #     de.export_to(file,"./port.jpg",sb)