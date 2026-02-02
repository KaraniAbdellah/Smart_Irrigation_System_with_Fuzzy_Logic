# 🌱 Smart Irrigation System with Fuzzy Logic (Raspberry Pi)

## 📌 Description
This project is an intelligent irrigation system based on **Fuzzy Logic**.  
The Raspberry Pi makes automatic decisions from sensor data, without waiting for the mobile app.

---

## 🔄 General Architecture
**Sensors → Raspberry Pi (Fuzzy Logic) → Water Pump + Cloud → Mobile App**

---

## 🧩 System Steps

### 1️⃣ Data Collection and Conversion (Hardware)
- Sensors used:
  - Soil moisture  
  - Temperature  
  - Air humidity  
- Sensors measure physical values.
- Raspberry Pi reads these values via an **analog-to-digital converter (ADC)**.

---

### 2️⃣ AI Brain – Fuzzy Logic
- Raspberry Pi collects sensor data (inputs).
- Data is processed by the fuzzy logic engine.
- Rules are applied, for example:  
  **IF soil moisture is low AND temperature is high THEN strong watering**.
- The exact **water volume** is calculated automatically.

---

### 3️⃣ Action and Storage (Cloud)
- The water pump is activated via a relay according to the decision.
- Sensor data + water volume are sent in real-time to the **Cloud** (Firebase/Firestore).

---

### 4️⃣ Visualization (Mobile App)
- The mobile app displays data stored on the Cloud.
- Shows graphs, weather, and current system status.
- No calculations are done in the app; it only reads and displays the data.

---

## ⚡ Technologies Used
- **Raspberry Pi**  
- **Sensors**: moisture, temperature, air humidity  
- **Fuzzy Logic**  
- **Relay for water pump**  
- **Cloud**: Firebase / Firestore  
- **Mobile App**: data reading and visualization

---

## 🚀 Data Flow

```bash
Sensors → Raspberry Pi (Fuzzy Logic) → Action (Pump) + Send to Cloud → Mobile App
```


## 👨‍💻 Author

**Made With Love By Abdellah Karani**

