import os.path as paths
class PyProps:
    @staticmethod
    def replaceStringsInPlace(strings: dict, sourceFilePath: str):
        with open(sourceFilePath,"r") as f:
            lines=f.readlines()

        newLines =[]
        for line in lines:
            for key in strings:
                if key in line:
                    originalValue = line.split("=")[1]
                    line=line.replace(originalValue,strings[key]+"\n")
            newLines.append(line)

        with open(sourceFilePath,"w") as f:
            for line in newLines:
                f.write(line)

    @staticmethod
    def replaceStringsIntoNewFile(strings: dict, sourceFilePath: str, targetFilePath: str ):
        """Check if write is allowed into the target path"""
        lines=[]
        newlines=[]
        with open(sourceFilePath,"r") as f:                
            lines = f.readlines()

        for line in lines:
            for key in strings:
                if key in line:
                    originalValue = line.split("=")[1]
                    line.replace(originalValue,strings[key]+"\n")
            newlines.append(line)

        with open(targetFilePath,"w") as f:
            f.writelines(newlines)

    @staticmethod
    def getKeyValuePairs(sourceFilePath: str) -> dict:
        properties={}
        with open(sourceFilePath,"r") as f:
            lines=f.readlines()
        
        for line in lines:
            key = line.split("=")[0]
            value = line.split("=")[1].replace("\n","")
            properties[key]=value
        return properties
