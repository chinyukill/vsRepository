
import csv

data = [
    {
        "job": "job1",
        "company": "company1",
        "position": "position1",
        "salary": "salary1",
        "publish_time": "time1",
    },
    {
        "job": "job2",
        "company": "company2",
        "position": "position2",
        "salary": "salary2",
        "publish_time": "time2",
    },
    {
        "job": "job3",
        "company": "company3",
        "position": "position3",
        "salary": "salary3",
        "publish_time": "time3",
    },
    {
        "job": "job4",
        "company": "company4",
        "position": "position4",
        "salary": "salary4",
        "publish_time": "time4",
    }
]
with open("test.csv", "w") as testFile:
    # testWriter = csv.writer(testFile)
    testWriter=csv.DictWriter(testFile, fieldnames=['job','company','position','salary','publish_time'])
    # testWriter.writerow(["1", 2])
    testWriter.writeheader()
    testWriter.writerows(data)
    # for i in data:
    #     for key,item in i.items():
    #         testWriter.writerow([item])
