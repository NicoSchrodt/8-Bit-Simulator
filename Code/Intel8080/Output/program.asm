Loop:
  ldax b
  cpi 0
  jz Done
  add d
  mov d, a
  inr c
  jmp Loop
Done:
  hlt
myArray:
  db 10h, 20h, 30h, 10h, 20h, 0