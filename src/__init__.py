from estimator import estimator

data ={
    "region":{
        "name":"Africa",
        "avgAge":19.7,
        "avgDailyIncomeUSD":5,
        "avgDailyIncomePopulation":0.71
    },
    "periodType":"days",
    "timeToElapse":58,
    "reportedCases":674,
    "population":6663987,
    "totalHospitalBeds":1380614
}


def loopThrough(data,name):
    print("\n\n"+name)
    for (key,value) in data.items():
        print(key+" - ",value)


result = estimator(data)
loopThrough(result['data'],"Data")
loopThrough(result['impact'],"Impact")
loopThrough(result['severeImpact'],"Severe Impact")

