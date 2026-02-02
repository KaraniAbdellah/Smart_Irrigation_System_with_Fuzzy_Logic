# 🌱 Smart Irrigation System with Fuzzy Logic

## 📌 What is This Project?

This is an **automatic watering system** for plants that thinks like a smart gardener! 

It uses **Fuzzy Logic** (a type of AI) to decide:
- **When** to water your plants
- **How much** water they need

The Raspberry Pi acts as the "brain" that reads sensors and makes smart decisions automatically.

---

## 🎯 How Does It Work? (Simple Overview)

```
📊 Sensors Read Data → 🧠 Raspberry Pi Thinks → 💧 Pump Waters Plants → ☁️ Data Saved to Cloud → 📱 You See Results on App
```

---

## 🧩 System Components

| Component | What It Does |
|-----------|--------------|
| **Sensors** | Measure soil moisture, temperature, and air humidity |
| **Raspberry Pi** | The "brain" that makes watering decisions using fuzzy logic |
| **Water Pump** | Waters the plants based on the decision |
| **Relay** | Acts like a switch to turn the pump ON/OFF |
| **Cloud (Firebase)** | Stores all data online |
| **Mobile App** | Shows you what's happening with graphs and charts |

---

## 🔧 Step-by-Step: How the System Works

### Step 1️⃣: Sensors Measure the Environment

The system uses 3 sensors:

| Sensor | What It Measures | Why It Matters |
|--------|------------------|----------------|
| **Soil Moisture** | How wet or dry the soil is (0-100%) | Dry soil needs more water |
| **Temperature** | How hot or cold it is (0-50°C) | Hot weather means plants need more water |
| **Air Humidity** | How much moisture is in the air (0-100%) | Dry air means water evaporates faster |

### Step 2️⃣: Raspberry Pi Makes Smart Decisions (Fuzzy Logic)

The Raspberry Pi uses **fuzzy logic rules** to decide how much water is needed.

**Example Rules:**
- IF soil is **very dry** AND temperature is **very hot** → Water for a **very long time**
- IF soil is **wet** → **Don't water at all**
- IF air humidity is **high** → **Reduce watering** (water evaporates slowly)
- IF air humidity is **low** → **Increase watering** (water evaporates quickly)

### Step 3️⃣: The Pump Waters Your Plants

The Raspberry Pi:
1. Calculates exactly how much water is needed (in milliliters)
2. Turns ON the pump using a relay
3. Waits for the right amount of time
4. Turns OFF the pump

**Example:** If 300ml of water is needed and the pump flows at 100ml/second, the pump runs for 3 seconds.

### Step 4️⃣: Data is Sent to the Cloud

All information is sent to **Firebase/Firestore** (cloud storage):
- Soil moisture reading
- Temperature reading
- Air humidity reading
- Amount of water given
- Time and date

### Step 5️⃣: You Check the Mobile App

The mobile app shows you:
- Current sensor readings
- Watering history
- Graphs and charts
- Weather information

**Note:** The app does NOT make decisions. It only displays information. The Raspberry Pi does all the thinking!

---

## 📊 Fuzzy Logic Explained (Simple Version)

### What Are the Input Values?

#### 1. Soil Moisture Levels

| Level | Meaning | Range (%) |
|-------|---------|-----------|
| **Very Dry** | Soil is almost completely dry | 0-30% |
| **Dry** | Soil needs water soon | 25-55% |
| **Moist** | Soil is good, perfect condition | 50-80% |
| **Wet** | Soil has enough water | 75-100% |

#### 2. Temperature Levels

| Level | Meaning | Range (°C) |
|-------|---------|------------|
| **Very Cold** | Freezing or near freezing | 0-15°C |
| **Cold** | Cool weather | 12-26°C |
| **Normal** | Comfortable temperature | 24-36°C |
| **Hot** | Very warm | 34-46°C |
| **Very Hot** | Extremely hot | 44-50°C |

#### 3. Air Humidity Levels

| Level | Meaning | Range (%) |
|-------|---------|-----------|
| **Low** | Dry air, water evaporates fast | 0-45% |
| **Moderate** | Normal air moisture | 40-70% |
| **High** | Humid air, water evaporates slowly | 65-100% |

### What Are the Output Values?

The system decides how much water to give:

| Watering Level | Meaning | Approximate Amount |
|----------------|---------|-------------------|
| **None** | Don't water | 0 ml |
| **Very Short** | Just a little water | 50-100 ml |
| **Short** | Small amount | 100-200 ml |
| **Medium** | Moderate watering | 200-300 ml |
| **Long** | Good amount of water | 300-400 ml |
| **Very Long** | Lots of water | 400-500 ml |

---

## 🤖 Decision-Making Examples

Here are some real examples of how the system thinks:

| Soil Moisture | Temperature | Air Humidity | Decision |
|---------------|-------------|--------------|----------|
| Very Dry | Very Hot | Low | **Very Long watering** (plants desperately need water!) |
| Dry | Hot | Low | **Long watering** (plants need good watering) |
| Moist | Normal | Moderate | **Short watering** (just a little water) |
| Wet | Any | Any | **No watering** (soil already has enough water) |
| Dry | Normal | High | **Short watering** (humid air means less evaporation) |

---

## ⚡ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Raspberry Pi** | The computer that runs the fuzzy logic system |
| **Soil Moisture Sensor** | Measures how wet the soil is |
| **Temperature Sensor** | Measures the temperature |
| **Air Humidity Sensor** | Measures moisture in the air |
| **ADC (Analog-to-Digital Converter)** | Converts sensor signals to numbers the Raspberry Pi can read |
| **Relay Module** | Controls the water pump (turns it on/off) |
| **Water Pump** | Delivers water to the plants |
| **Python (scikit-fuzzy)** | Programming language and fuzzy logic library |
| **Firebase/Firestore** | Cloud database to store all data |
| **Mobile App** | Displays data and graphs to the user |

---

## 🚀 Complete Data Flow

```
┌─────────────┐
│   Sensors   │ ← Measure soil, temperature, humidity
└──────┬──────┘
       │
       ▼
┌─────────────────────┐
│   Raspberry Pi      │ ← Read sensor data
│   (Fuzzy Logic AI)  │ ← Apply smart rules
│                     │ ← Calculate water amount
└──────┬──────────────┘
       │
       ├──────────────────┐
       │                  │
       ▼                  ▼
┌─────────────┐    ┌──────────┐
│ Water Pump  │    │  Cloud   │ ← Save all data
│   (Relay)   │    │ Firebase │
└─────────────┘    └────┬─────┘
                        │
                        ▼
                  ┌──────────┐
                  │ Mobile   │ ← Display data
                  │   App    │ ← Show graphs
                  └──────────┘
```

---

## 🎓 Why Fuzzy Logic?

Traditional systems use simple rules: "IF soil < 30% THEN water"

**Fuzzy Logic is smarter** because:
- It handles "in-between" situations (like soil at 50% - not too dry, not too wet)
- It considers **multiple factors at once** (soil + temperature + humidity)
- It makes smooth, gradual decisions (not just on/off)
- It thinks like a human gardener would!

---

## 📚 Learn More

This project is based on:
- **Mamdani Fuzzy Logic** - A method for making smart decisions
- **FAO Crop Guidelines** - International standards for watering crops
- **Scikit-Fuzzy Library** - Python tool for fuzzy logic

---

## 👨‍💻 Author

**Made With Love By Abdellah Karani** 💚

---

## 🆘 Need Help Understanding?

**Key Terms Explained:**

| Term | Simple Explanation |
|------|-------------------|
| **Fuzzy Logic** | A way for computers to make decisions like humans (not just yes/no, but "maybe" too) |
| **Sensor** | A device that measures something (like a thermometer measures temperature) |
| **Raspberry Pi** | A small, cheap computer (size of a credit card) |
| **Relay** | An electronic switch that turns things on and off |
| **Cloud** | Storing data on the internet instead of on your device |
| **Firebase** | A Google service for storing data online |
| **ADC** | Converts real-world measurements into numbers a computer can understand |

---

## 🌟 Project Benefits

✅ Saves water by watering only when needed  
✅ Keeps plants healthy automatically  
✅ You can check your garden from anywhere using the app  
✅ No need to remember to water your plants  
✅ Smart decisions based on weather conditions  

---

**Happy Gardening! 🌿💧**
