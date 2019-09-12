def countingValleys(n, s):
  valleys = level = 0

      for i in range(n):
          if s[i] == 'D':
              level -= 1
          elif s[i] == 'U':
              level += 1
              if level == 0:
                  valleys += 1
      return(valleys)
