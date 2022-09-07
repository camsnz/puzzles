# https://leetcode.com/problems/pacific-atlantic-water-flow/

from lib2to3.pgen2.token import AT
from typing import List

PACIFIC = 'PACIFIC'
ATLANTIC = 'ATLANTIC'

# def drainToAnyAdjacent

class Cell:
    def __init__(self, x:int, y:int, h:int):
        self.x = x
        self.y = y
        self.h = h
        self.pacific = False
        self.atlantic = False
        self.walked = ""
    def isOcean(self, ocean:str) -> bool:
        return (ocean == PACIFIC and self.pacific) or (ocean == ATLANTIC and self.atlantic)
    def setOcean(self, ocean:str, val:bool):
        if(ocean == PACIFIC):
            self.pacific = val
        if(ocean == ATLANTIC):
            self.atlantic = val

def getAdjCoords(i:int, j:int, l:int) -> List[List[int]]:
    result = []
    if(i-1 >= 0):
        result.append([i-1,j])
    if(i+1 < l):
        result.append([i+1,j])
    if(j-1 >= 0):
        result.append([i,j-1])
    if(j+1 < l):
        result.append([i,j+1])
    return result

class Solution:

# identify pacific starting tiles
# walk each tile, one at a time. If a tile has pacific true, it's walked.
# >> list neighbours, higher and not walked? Add Walk.

    def walk(cells: List[List[Cell]], cell: Cell, ocean:str) -> List[Cell]:
        # get each adj, test hasOcean and height, setOcean and add to be walked
        coords = getAdjCoords(cell.x, cell.y, len(cells))
        result = []
        for coord in coords:
            c = cells[coord[0]][coord[1]]
            if(c.h >= cell.h and c.walked != ocean):
                result.append(c)
        cell.walked = ocean
        cell.setOcean(ocean, True)
        print(f"walk [{cell.x},{cell.y}] coords: {coords} results: {formatCells(result)}",)
        return result

    # def walkAll

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # shape(heights)
        # cells = [ [Cell()]*len(heights) for i in range(len(heights)) ]
        cells = []
        pacificWalk = []
        atlanticWalk = []

        for i, iv in enumerate(heights):
            cells.append([])
            for j, jv in enumerate(iv):
                cell = Cell(i, j, jv)
                cells[i].append(cell)
                cell.x = i
                cell.y = j
                cell.h = jv

        for i, iv in enumerate(cells):
            for j, cell in enumerate(iv):

                if(i==0 or j==0):
                    cell.pacific = True
                    pacificWalk.extend(self.walk(cells, cell, PACIFIC))

                if(i+1==len(heights) or j+1==len(heights)):
                    cell.atlantic = True
                    atlanticWalk.extend(self.walk(cells, cell, ATLANTIC))

        # print("pacificWalk",len(pacificWalk))
        # print("atlanticWalk",len(atlanticWalk))
        while(len(pacificWalk) > 0):
            pacificWalk.extend(self.walk(cells, pacificWalk.pop(), PACIFIC))
            # print("pacificWalk",len(pacificWalk))

        while(len(atlanticWalk) > 0):
            atlanticWalk.extend(self.walk(cells, atlanticWalk.pop(), ATLANTIC))
            # print("atlanticWalk",len(atlanticWalk))
            
        # print("pacific")
        # print(pacific)
        # print("atlantic")
        # print(atlantic)
        result = []
        for i, iv in enumerate(cells):
            for j, jv in enumerate(iv):
                str = ""
                if(jv.atlantic and jv.pacific):
                    str = "BOTH"
                elif(jv.atlantic):
                    str = ATLANTIC
                elif(jv.pacific):
                    str = PACIFIC
                print(f"[{jv.x},{jv.y}] {str}")

                if(jv.atlantic and jv.pacific):
                    result.append(jv)
        return result

heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

def formatCells(cells:List[Cell]) -> str:
    return ",".join(map(lambda c: f"[{c.x},{c.y}]", cells))

def printCells(cells:List[Cell]):
    print("[" + formatCells(cells) + "]")

printCells(Solution.pacificAtlantic(Solution, heights))