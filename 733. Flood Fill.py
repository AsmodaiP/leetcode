# https://leetcode.com/problems/flood-fill/
class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        def add_neighbor_to_stack(stack, image, c_sr, c_sc):
            if len(image) > c_sr + 1:
                stack.append((c_sr+1, c_sc))
            if len(image[0]) > c_sc + 1:
                stack.append((c_sr, c_sc+1))

            if c_sr > 0:
                stack.append((c_sr-1, c_sc))
            if c_sc > 0:
                stack.append((c_sr, c_sc-1))

        stack = [(sr, sc)]
        initial_color = image[sr][sc]
        if initial_color == color:
            return image
        while stack:
            c_sr, c_sc = stack.pop()

            if image[c_sr][c_sc] == initial_color:
                image[c_sr][c_sc] = color
                image[c_sr][c_sc] == color
                add_neighbor_to_stack(stack, image, c_sr, c_sc)
        return image


sol = Solution()
sol.floodFill(
    [[0, 0, 0], [0, 0, 0]],
    0, 0, 0
)
