from StockDataAnalyzer import

#Write Unit Tests for Project 3 Inputs
#symbol: capitalized, 1-7 alpha characters
def capitalizer_tester(value):
  while True:
        try:
            value = input(prompt)
            if validation_func(value):
              value.upper()
              print("Input:" + value)
              return value
            else:
                print("error")
        except ValueError:
            print("Incorrect value type\n")

#chart type: 1 numeric character, 1 or 2
def chartType_tester(chart_type):
  if chart_type = 1:
    print("input 1")
  else if chart_type = 2:
    print("input 2")
  else:
    print("Bad input")

#time series: 1 numeric character, 1 - 4
def time_tester(time_series):
  if time_series = (1 or 2 or 3 or 4):
    print("good input")
  else:
    print("Bad input")

#start date: date type YYYY-MM-DD
def startdate_tester(start_date):
  if start_date = datetime.strptime(start_date, '%Y-%m-%d'):
    print("good input")
  else:
    print("Bad input")

#end date: date type YYYY-MM-DD
def enddate_tester(end_date):
  if end_date = datetime.strptime(end_date, '%Y-%m-%d'):
    print("good input")
  else:
    print("Bad input")

