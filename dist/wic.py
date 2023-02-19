import sys as _s

from PIL import Image
from pathlib import Path
import glob

def run(targetPath,targetFormat):
    webpFiles = glob.glob(f'{targetPath}\\*.webp')
    for webpFile in webpFiles:
        pathName = Path(webpFile).name
        newFile = webpFile.replace(pathName,pathName[:-4] + targetFormat)
        image = Image.open(webpFile).convert("RGB")
        image.save(newFile,format=targetFormat,optimize=True)


valid_formats = ['jpeg','png']

if __name__ == "__main__":
    targetPath = None
    targetFormat = 'jpeg'

    for arg in _s.argv:
        if(arg.startswith("-t")):
            targetPath = arg.split("=")[1]
        elif(arg.startswith("-f")):
            targetFormat = arg.split("=")[1]

    if(targetPath is None):            
        raise Exception('The target folder path should be specified.')
    
    if(not targetFormat.lower() in valid_formats):
        raise Exception('The specified format is not valid. Please set png or jpeg.')

    run(targetPath,targetFormat)