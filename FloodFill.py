def dfs(image, r, c, color, initial):
    if image[r][c] == initial and image[r][c] != color:
        image[r][c] = color
        
    else:
        return
    if r-1 >= 0:
        dfs(image, r-1, c, color, initial)
    if r+1 < len(image):
        dfs(image, r+1, c, color, initial)
    if c-1 >= 0:
        dfs(image, r, c-1, color, initial)
    if c+1 < len(image[0]):
        dfs(image, r, c+1, color, initial)


image = [[0, 0, 0], [0, 1, 1]]
sr = 1
sc = 1
newColor = 1
dfs(image, sr, sc, newColor, image[sr][sc])
print(image)
