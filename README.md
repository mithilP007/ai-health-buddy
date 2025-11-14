# 🌟 AI Health Buddy

> Your personal AI assistant for health tracking and digital wellness

## 👋 Overview

AI Health Buddy is a comprehensive personal health and phone usage tracking application that helps you:
- **Track junk food intake** and calculate money saved on healthy days
- **Monitor phone usage** with customizable daily limits
- **Get motivational quotes** to stay on track
- **View detailed statistics** of your progress over time

## ✨ Features

### Health Tracking
- 🍔 Daily junk food logging
- 💰 Automatic savings calculator
- 📊 Visual progress dashboard
- 📅 Historical data tracking

### Phone Usage Monitoring
- 📱 Track daily phone usage in minutes
- ⏰ Set custom usage limits
- 🚨 Over-limit day tracking
- 📈 Average usage statistics

### AI Features
- 🤖 Motivational quote generator
- 📝 Notes and observations
- 🎯 Goal tracking

## 🛠️ Tech Stack

- **Backend:** FastAPI (Python)
- **Frontend:** HTML5, CSS3, JavaScript
- **Data Storage:** JSON file-based storage
- **API:** RESTful API design

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Steps

1. **Clone the repository**
```bash
git clone https://github.com/mithilP007/ai-health-buddy.git
cd ai-health-buddy
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python app.py
```

4. **Access the app**
Open your browser and navigate to:
```
http://localhost:8000
```

## 💻 API Endpoints

### Junk Food Tracking
- `POST /api/junk-food` - Log junk food entry
- `GET /api/entries` - Get all entries

### Phone Usage
- `POST /api/phone-usage` - Log phone usage
- `GET /api/today` - Get today's status

### Statistics
- `GET /api/summary` - Get overall statistics
- `GET /api/motivational-quote` - Get random motivational quote

## 📄 Project Structure

```
ai-health-buddy/
├── app.py                 # FastAPI backend application
├── index.html             # Frontend interface
├── requirements.txt       # Python dependencies
├── health_data.json       # Data storage (auto-generated)
├── README.md              # Documentation
└── LICENSE                # MIT License
```

## 🎯 Usage Guide

### Logging Junk Food
1. Select whether you ate junk food today
2. Enter the approximate cost
3. Add optional notes
4. Click "Save Junk Food Entry"

### Tracking Phone Usage
1. Enter your phone usage in minutes
2. Set your daily limit
3. Add optional notes
4. Click "Save Phone Usage"

### Viewing Statistics
The dashboard automatically updates to show:
- Total healthy days
- Money saved
- Average phone usage
- Days exceeding limit

## 💡 Use Cases

- **Personal Health Goals:** Track and maintain healthy eating habits
- **Financial Savings:** Monitor money saved by avoiding junk food
- **Digital Wellness:** Control and reduce phone usage
- **Habit Formation:** Build consistent healthy routines
- **Progress Tracking:** Visualize your health journey over time

## 🔧 Customization

You can customize:
- Default junk food cost
- Phone usage limit
- Motivational quotes
- Visual theme and colors

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Abishek** (mithilP007)
- GitHub: [@mithilP007](https://github.com/mithilP007)
- Project Link: [AI Health Buddy](https://github.com/mithilP007/ai-health-buddy)

## 🚀 Future Enhancements

- [ ] Mobile app version (Android/iOS)
- [ ] Integration with fitness trackers
- [ ] Advanced AI recommendations
- [ ] Social features and challenges
- [ ] Data export and analytics
- [ ] Voice input support
- [ ] Notification reminders
- [ ] Multi-user support

## 🔗 Links

- [Live Demo](#) (Coming soon)
- [Documentation](#)
- [Report Bug](https://github.com/mithilP007/ai-health-buddy/issues)
- [Request Feature](https://github.com/mithilP007/ai-health-buddy/issues)

---

<p align="center">Made with ❤️ by Abishek</p>
<p align="center">
  <i>Your health is your wealth. Track it, improve it, live it! 🌟</i>
</p>
