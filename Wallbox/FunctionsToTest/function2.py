import os

size14MB = (14*(2**20))

def findFirstAdminExecutableLessthan14MB(path):
    if (not os.path.isdir(path)):
        raise Exception("Invalid Path")
    else:
        content = os.scandir(path)
        for item in content:
            userPermission = os.stat(item.path).st_uid
            if item.is_file() and os.access(item.path, os.X_OK) and os.path.getsize(item.path) < size14MB and userPermission == 0:
                return item.path
        return("File not found")