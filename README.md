# MQTT System Monitoring

![MIT License](https://img.shields.io/badge/license-MIT-green)

## Overview

**MQTT System Monitoring** is a lightweight Python application designed for Raspberry Pi devices to monitor system resource usage (CPU, memory, disk, and temperature) and send the data to a ThingsBoard instance using MQTT. This program is intended for production environments where reliable telemetry reporting and logging are crucial. It is structured for maintainability and extensibility, with a focus on clean code, unit testing, and systemd deployment.

## Features

- Sends system telemetry to ThingsBoard
- Sends static machine attributes (device name, IP, MAC address)
- Local rotating log files for debugging and traceability
- Unit tested with Pytest
- Python 3.11+ support
- Easily configurable via `.env` and `config.json`
- Production-ready with systemd service example

## Project Structure

```
mqtt_system_monitoring/
├── monitoring_service/
│   ├── agent.py
│   ├── attributes.py
│   ├── config_loader.py
│   ├── logging_setup.py
│   ├── telemetry.py
│   └── TBClientWrapper.py
├── tests/
│   └── test_*.py
├── config.json
├── .env
└── requirements.txt
```

## Getting Started

### Prerequisites

- Raspberry Pi OS (or any Linux-based OS)
- Python 3.11+
- ThingsBoard instance
- MQTT device access token

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Ryan-Atkinson87/mqtt_pi_monitoring.git mqtt_system_monitoring
cd mqtt_system_monitoring
```

2. Set up the Python virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Configure your `.env` file and `config.json`:
- `.env`:
    ```
    ACCESS_TOKEN=your_thingsboard_access_token
    THINGSBOARD_SERVER=your_thingsboard_server_url_or_ip
    ```
- `config.json`:
    ```json
    {
      "poll_period": 60,
      "device_name": "your_device_name",
      "mount_path": "/",
      "log_level": "INFO"
    }
    ```

### Running the Application

Run directly:
```bash
python main.py
```

Or deploy with systemd for production:
```bash
sudo cp mqtt_system_monitoring.service /etc/systemd/system/
sudo systemctl enable mqtt_system_monitoring.service
sudo systemctl start mqtt_system_monitoring.service
```

### Testing

```bash
pytest tests/
```

## License

This project is licensed under the [MIT License](LICENSE).

## Contributing

Contributions welcome! Please fork the repo, create a feature branch, and submit a pull request.

---

Built with ❤️ to provide reliable system telemetry monitoring.
