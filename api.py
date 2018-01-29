from flask import Flask, render_template, url_for
import RPi.GPIO as GPIO

app = Flask(__name__)

outputPin = [17, 18, 14, 4]
inputPin = [20,21]


@app.route("/turnOnAll")
def turnAllLightOn():
	for x in range(len(outputPin)):
		GPIO.output(outputPin[x], GPIO.HIGH)
	return render_template('index.html')

@app.route("/turnOffAll")
def turnAllLightOff():
	for x in range(len(outputPin)):
		GPIO.output(outputPin[x], GPIO.LOW)
	return render_template('index.html')

@app.route("/getdata")
def getdata():
	pin = []
	for x in range(len(outputPin)):
		if GPIO.input(outputPin[x]) == GPIO.HIGH : 
			pin.append(x)
	return json.dumps(pin)

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

for x in range(len(outputPin)):
	GPIO.setup(outputPin[x], GPIO.OUT)
	GPIO.setup(outputPin[x], GPIO.IN)

if __name__ == '__main__':
	app.run(debug=True)


#21, 20 input switch
