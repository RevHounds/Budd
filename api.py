from flask import Flask, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

url_for('static', filename='style/style.css')
url_for('static', filename='style/botstrap.css')

outputPin = [17, 18, 14, 4]

@app.route("/")
def hello():
	return render_template('index.html')

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

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

for x in range(len(outputPin)):
	GPIO.setup(outputPin[x], GPIO.OUT)

if __name__ == '__main__':
	app.run(debug=True)