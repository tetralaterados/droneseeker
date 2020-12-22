from subprocess import call
while True:
    call(["python", "seekersKml.py"])
    call(["python", "splineConversor.py"])
    call(["python", "midPoint.py"])
    call(["python", "midPointPlot.py"])
    call(["python", "triangle.py"])