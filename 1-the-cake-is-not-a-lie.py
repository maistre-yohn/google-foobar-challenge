def solution(s):
  # counts s until repeat 
    return[s.count(s[:i]) for i in range(1, len(s)+1) if s.count(s[:i])*len(s[:i])-len(s) == 0][0]
