# EX:
# "/home/" ⇒ "/home"
# "/../" ⇒ "/"
# "/home//foo/" ⇒ "/home/foo"


def solution(path):
    chunks = path.split("/")
    # 實現相鄰消消樂的容器
    newChunks = []

    for chunk in chunks:
        if chunk == "." or chunk == "":
            continue
        elif chunk == "..":
            if newChunks:
                newChunks.pop()
        else:
            newChunks.append(chunk)
    newResult = "/".join(newChunks)
    return "/" + newResult
