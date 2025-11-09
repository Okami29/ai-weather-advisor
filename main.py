from langchain_ollama import OllamaLLM
import serial
import time

# === SETUP ===
# Replace COM3 with your actual port (e.g. /dev/ttyUSB0 on macOS/Linux)
ser = serial.Serial('COM3', 9600, timeout=1)
time.sleep(2)

llm = OllamaLLM(model="llama3.1:8b")

print("🌡️ AI Weather Advisor is running...")
print("Reading sensor data and asking AI for advice.\n")

def interpret_data(sensor_text):
    prompt = f"""
    You are an AI assistant that interprets temperature and humidity data
    from a DHT22 sensor and gives friendly, useful advice.

    Example inputs:
    - Temperature:28.5,Humidity:60.1 → "It's a pleasant day!"
    - Temperature:32.0,Humidity:80.0 → "It's hot and humid, maybe turn on a fan."
    - Temperature:18.0,Humidity:40.0 → "It's cool and dry, wear something warm."

    The user input: {sensor_text}
    Respond in one short natural sentence as a friendly AI assistant.
    """
    return llm.invoke(prompt).strip()

while True:
    line = ser.readline().decode().strip()
    if line.startswith("Temperature"):
        print(f"📟 Sensor: {line}")
        response = interpret_data(line)
        print(f"🤖 AI says: {response}\n")
        print("-" * 40)
