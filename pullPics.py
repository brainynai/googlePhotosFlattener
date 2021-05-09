import os

class Settings:
    outdir = r"C:\Users\Nai\Documents\Python\pullPics\pics" #Change as needed

    #All relevant file extensions to move
    ext = ['ase', 'art', 'bmp', 'blp', 'cd5', 'cit', 'cpt', 'cr2', 'cut', 'dds',
           'dib', 'djvu', 'egt', 'exif', 'gif', 'gpl', 'grf', 'icns', 'ico', 'iff',
           'jng', 'jpeg', 'jpg', 'jfif', 'jp2', 'jps', 'lbm', 'max', 'miff', 'mng', 'msp',
           'nitf', 'ota', 'pbm', 'pc1', 'pc2', 'pc3', 'pcf', 'pcx', 'pdn', 'pgm', 'PI1', 'PI2', 'PI3',
           'pict', 'pct', 'pnm', 'pns', 'ppm', 'psb', 'psd', 'pdd', 'psp', 'px', 'pxm', 'pxr', 'qfx',
           'raw', 'rle', 'sct', 'sgi', 'rgb', 'int', 'bw', 'tga', 'tiff', 'tif', 'vtf', 'xbm', 'xcf',
           'xpm', '3dv', 'amf', 'ai', 'awg', 'cgm', 'cdr', 'cmx', 'dxf', 'e2d', 'egt', 'eps', 'fs',
           'gbr', 'odg', 'svg', 'stl', 'vrml', 'x3d', 'sxd', 'v2d', 'vnd', 'wmf', 'emf', 'art', 'xar',
           'png', 'webp', 'jxr', 'hdp', 'wdp', 'cur', 'ecw', 'iff', 'lbm', 'liff', 'nrrd', 'pam', 'pcx',
           'pgf', 'sgi', 'rgb', 'rgba', 'bw', 'int', 'inta', 'sid', 'ras', 'sun', 'tga',
           '3g2', '3gp', 'aaf', 'asf', 'avchd', 'avi', 'drc', 'flv', 'm2v', 'm4p', 'm4v', 'mkv', 'mng',
           'mov', 'mp2', 'mp4', 'mpe', 'mpeg', 'mpg', 'mpv', 'mxf', 'nsv', 'ogg', 'ogv', 'qt', 'rm',
           'rmvb', 'roq', 'svi', 'vob', 'webm', 'wmv', 'yuv']

    #Check if two files contain the same data (mods req'd for very large files)
    def compareFiles(filePath1, filePath2):
        with open(filePath1, 'rb') as f:
            data1 = f.read()

        with open(filePath2, 'rb') as f:
            data2 = f.read()

        return hash(data1) == hash(data2)

def main():
    sourcePath = input("Enter path: ")
    if not os.path.exists(sourcePath):
        print('Path not reachable.')
        input('Enter to exit')
        exit()
        
    for thisPath, dirs, files in os.walk(sourcePath):
        for file in files:
            if any(file.lower().endswith(i) for i in Settings.ext):
                #print(f'Found file: {os.path.join(thisPath,file)}')
                try:
                    os.rename(os.path.join(thisPath, file), os.path.join(Settings.outdir, file))
                except FileExistsError as e:
                    if Settings.compareFiles(os.path.join(thisPath, file), os.path.join(Settings.outdir, file)):
                        #print('Duplicate file found')
                        #print(str(e))
                        continue
                    else:
                        print('These files have the same name, but are different.')
                        print(str(e))
                        exit() #In theory, change the destination name to something that doesn't exist, but I never encountered this case


if __name__ == "__main__":
    main()
