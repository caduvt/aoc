file = open('input.txt', 'r')

reports = []

for line in file:
  reportNums = list(map(lambda x: int(x), line.strip().split()))
  reports.append(reportNums)
  
file.close()

def is_safe(report):
  is_ascending = report[0] < report[1]
  
  if is_ascending:
    for i in range(len(report)-1):
      diff = report[i+1] - report[i] 
      if diff < 1 or diff > 3:
        return False
    return True
  else:
    for i in range(len(report)-1):
      diff = report[i+1] - report[i] 
      if diff > -1 or diff < -3:
        return False
    return True
  
def is_safe_with_dampener(report):
  for i in range(len(report)):
    newReport = report.copy()
    newReport.pop(i)
    if is_safe(newReport):
      return True
  return False

  # A linha abaixo simplificaria a implementação da função acima.
  # É mais pythonic e mais eficiente, por não fazer cópias da lista.
  # return any(is_safe(report[:i] + report[i+1:]) for i in range(len(report)))
    
safeReports = sum(1 for report in reports if is_safe_with_dampener(report))
print(safeReports)