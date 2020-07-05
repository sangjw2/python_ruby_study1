arr = [1, 2 ,321, 31, 5, 312, 313, 563, 8]

arr.delete_if{|v| v > 7} # 여러 줄이면 do end 사용 권장
print arr