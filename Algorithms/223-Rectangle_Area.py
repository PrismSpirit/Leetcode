class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        overlap_area = 0
        
        if not (C < E or A > G or B > H or D < F):
            lux = max(A ,E)
            luy = max(B, F)
            rdx = min(C, G)
            rdy = min(D, H)
            
            w = rdx - lux
            h = rdy - luy
            
            overlap_area = w * h
            
        a1 = (C - A) * (D - B)
        a2 = (G - E) * (H - F)
        
        return a1 + a2 - overlap_area