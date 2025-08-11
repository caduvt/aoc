# Código terrivelmente pouco legível
# Seria bom refatorar

file = open('input.txt', 'r')

reports = []

for line in file:
  reports.append(line.strip().split())
  
file.close()

safeReports = 0

for stringReport in reports:
  report = [int(level) for level in stringReport]
  sortedReport = sorted(report)
  reversedReport = list(reversed(report))
  if sortedReport == report or reversedReport == sortedReport:
    for i in range(len(report)-1):
      diff = abs(report[i] - report[i+1])
      if diff < 1 or diff > 3:
        break
    else:
      safeReports += 1
    
print(safeReports)