

def normalizePeriod(period,periodType):
  if(periodType == "months"):
    return period * 30
  elif(periodType == "weeks"):
    return period * 7
  else:
    return period 

def truncate(number):
  numStr = str(number)
  numStr = numStr.split('.')
  return int(numStr[0])


def estimator(data):
  normalizedPeriod  = normalizePeriod(data['timeToElapse'],data['periodType'])

  def getImpact():
    currentlyInfected = data["reportedCases"] * 10
    infectionsByRequestedTime = currentlyInfected  * ( 2 ** (normalizedPeriod/3))
    severCaseByRequestedTime = 0.15 * infectionsByRequestedTime

    hospitalBedsByRequestedTime = severCaseByRequestedTime -( 0.35 * data["totalHospitalBeds"])
    
    return {
      "currentlyInfected":currentlyInfected,
      "infectionsByRequestedTime": truncate(infectionsByRequestedTime),
      "severCaseByRequestedTime" : truncate(severCaseByRequestedTime),
      "hospitalBedsByRequestedTime" : truncate(hospitalBedsByRequestedTime)
    }


  def getSevereImpact():
    currentlyInfected = data["reportedCases"] * 50
    infectionsByRequestedTime = currentlyInfected  * ( 2 ** (normalizedPeriod/3))

    severCaseByRequestedTime = 0.15 * infectionsByRequestedTime
    presentBeds   = 0.95 * data['totalHospitalBeds']

    hospitalBedsByRequestedTime = severCaseByRequestedTime -( 0.35 * presentBeds)

    return {
      "currentlyInfected":currentlyInfected,
      "infectionsByRequestedTime": truncate(infectionsByRequestedTime),
      "severCaseByRequestedTime" : truncate(severCaseByRequestedTime),
      "hospitalBedsByRequestedTime" : truncate(hospitalBedsByRequestedTime)
    }


  

  result = {
    "data":data,
    "impact":getImpact(),
    "severeImpact":getSevereImpact()
  }
  return result
