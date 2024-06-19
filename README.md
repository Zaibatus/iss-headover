# ISS Satellite Overhead Notifier

This Python-based ISS Satellite Overhead Notifier informs users when the International Space Station (ISS) is passing overhead and sends an email notification to prompt users to look up and observe it. Key features include:

Real-Time ISS Tracking: Utilizes real-time data to monitor the current position of the ISS.
Overhead Detection: Calculates when the ISS will be directly overhead based on the user’s location.
Email Notifications: Automatically sends an email alert to the user with the exact time and duration when the ISS will be visible in their sky.
User-Friendly Configuration: Allows users to input their geographical coordinates and email addresses easily.
API Integration: Integrates with APIs like Open Notify and Sunrise-Sunset to fetch live positional data of the ISS and local sunrise/sunset times.

**Usage**

The script checks the ISS position every minute.
If the ISS is overhead and it is nighttime at your location, it sends an email notification.
Customize the email settings and frequency as needed.
This tool is perfect for space enthusiasts who don't want to miss the opportunity to view the ISS. Its accurate predictions and timely email alerts make it a convenient tool for staying informed about ISS sightings.
