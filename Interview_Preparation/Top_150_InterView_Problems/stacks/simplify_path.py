#todo Important
def simplifyPath(path:str)->str:
    if len(path)==1:
        return path
    canonical_path = ['/']
    CURRENT_PATH='.'
    PREVIOUS_PATH='../'
    pass