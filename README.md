# 🌡️ AI Weather Advisor — ESP32 + DHT22 + Ollama

### 🧠 What if your sensor data could talk back?

This project connects **IoT and AI** to create a smart assistant that “understands” sensor readings.

Your **ESP32** reads live **temperature and humidity** from a **DHT22 sensor**,  
and your **AI model (Ollama)** responds in natural language — giving advice like:

It's 31°C and 75% humidity.

AI says: It's quite humid today! You should probably turn on a fan.

## 🚀 Overview

**AI + IoT = Understanding the Environment**

- 🌡️ ESP32 measures temperature & humidity  
- ⚙️ Python bridges the sensor and AI  
- 🧠 Ollama interprets the data and speaks in natural language  

This project is great for students learning how **data sensing** and **AI interpretation** combine to create smart systems like weather assistants or smart homes.

---

## 🪛 Hardware Setup

**You’ll need:**
- 1 × ESP32 board  
- 1 × DHT22 sensor  
- Jumper wires  
- Breadboard  
- USB cable  

**Connections:**

| DHT22 Pin | Connects To | Description |
|------------|-------------|-------------|
| VCC        | 3.3V        | Power supply |
| DATA       | GPIO 4      | Data pin (can be changed) |
| GND        | GND         | Ground |

*(Remember to use a 10kΩ pull-up resistor between DATA and 3.3V if your module doesn’t have one built-in.)*

---
