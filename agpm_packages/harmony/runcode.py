import ESDLang
import os

def main(extension, filename):
    match extension:
        case ".esdla":
            ESDLang.main(filename)
        case ".py":
            os.system("python3 "+filename)
        case ".java":
            os.system("java "+filename)
