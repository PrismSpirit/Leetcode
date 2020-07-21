class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        m_angle = 6 * minutes
        h_angle = 0.5 * minutes + (hour % 12) * 30
        
        return abs(m_angle - h_angle) if abs(m_angle - h_angle) < 180 else 360 - abs(m_angle - h_angle)