# Network Device Scanner and Report Generator

This project is a Network Device Scanner that detects active devices connected to a local network and generates a detailed report of these devices. The report includes the device's name, IP address, MAC address, manufacturer, status (online/offline), and last seen time. The report can be exported as a PDF for record-keeping or analysis purposes.

# Project Overview
This web-based application allows users to scan their local network for active devices and generate a PDF report. The project is built using Flask (a lightweight web framework), and Scapy (for network scanning). The web interface provides a visually appealing design, and the report includes key details about each device found during the scan.

Users can view the status of devices (online/offline), their last seen time, and other important information such as the device's manufacturer and MAC address. The device details are displayed in a table, and the report can be exported as a PDF file.

# Features
* Network Scanning: Detects all active devices connected to the local network.
* Device Information: Displays the IP address, MAC address, manufacturer, online/offline status, and last seen time.
* Report Generation: Generates a PDF report with all scanned devices and their details.
* Export Option: Users can export the device details as a PDF for further reference.
* Dynamic User Interface: Visually appealing and responsive UI with centered tables, hover effects, and device status indicators.
* Interactive Device Details: Click on any device card to enlarge details and view additional information.

# Programming Languages
* Python: Core programming language used to develop the backend logic and handle network scanning.
* HTML/CSS: Frontend development for designing the user interface.
# Frameworks:
* Flask: Used as the web framework to create the backend and handle the user interface.
* Jinja2: Templating engine used with Flask to dynamically inject device data into the HTML.
# Libraries:
* Scapy: A Python library used for network scanning to find active devices and retrieve their IP addresses, MAC addresses, and manufacturer.
* WeasyPrint: Converts HTML files into PDFs, used for exporting device information into a report.

# Setup Instructions

Step 1: Clone the Repository

```git clone https://github.com/PramodAdhav/Network-Device-Scanner.git```

```cd network-scanner```

Step 2: Install the Required Libraries
You can install all the necessary libraries using pip. Open your terminal and run the following command:

```pip install flask scapy weasyprint```

Step 3: Run the Application
After installing the required libraries, run the Flask app using the following command:

Step 4: Access the Application
Open your web browser and visit:

```http://127.0.0.1:5000```

* Important Note

Change the IP Address:

To correctly scan the network, you need to modify the IP address in the scanner.py file. Ensure the IP address matches the IP range of the network you are scanning. Here's how you can change it:

Open the ```scanner.py``` file.

Locate the section where the IP range is defined. It will look something like this:
```target_ip = "192.168.0.1/24"```

Replace the IP address (192.168.0.1/24) with the appropriate IP address range for your local network.

License

This project is licensed under the MIT License - see the LICENSE file for details.


Developed by: Pramod Adhav

Contact: Pramodadhav111@gmail.com
