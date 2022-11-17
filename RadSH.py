import os,base64

# RadSH PKG Format:
# -----------------
#   RadSH Package
# -----------------
# directory:base64

def CompileDir(directory):
    pkg = "-----------------\n  RadSH Package  \n-----------------\n".encode("utf-8")
    for root, dirs, files in os.walk(directory):
        if root == directory:
            continue
        
        r = root.replace(directory,"")
        if files != []:
            for file in files:
                path = os.path.join(r,file)
                path = path.encode("utf-8")
                f = open(os.path.join(root,file),"rb")
                data = f.read()
                data = base64.b64encode(data)
                f.close()
                pkg += path + b":" + data + "\n".encode("utf-8")
    with open(f"{directory}.radsh","wb") as f:
        f.write(pkg)
                
class PKGReader():
    def __init__(self, filename):
        with open(filename+".radsh","rb") as f:
            self.data = f.read()
        self.vdir = {}
        for line in self.data.split(b"\n"):
            if line.startswith(b"/"):
                data = line.split(b":")
                vdir[data[0]] = base64.b64decode(data[1])
    
    def get(self,dir):
        if dir in self.vdir:
            return self.vdir[dir]
        else:
            raise KeyError("not a valid key")