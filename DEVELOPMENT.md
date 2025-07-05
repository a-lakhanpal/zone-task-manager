# Development Guide for Your Home Assistant Integration

## Overview

This guide will help you develop and customize your Home Assistant integration for distribution via HACS.

## Project Structure

```
your_integration/
├── custom_components/your_integration/
│   ├── __init__.py          # Main integration setup
│   ├── manifest.json        # Integration metadata
│   ├── const.py            # Constants and configuration
│   ├── config_flow.py      # UI configuration flow
│   ├── sensor.py           # Sensor platform (example)
│   └── strings.json        # UI translations
├── hacs.json               # HACS configuration
├── README.md               # User documentation
├── LICENSE                 # MIT License
└── DEVELOPMENT.md          # This file
```

## Key Components

### 1. manifest.json
Contains metadata about your integration:
- `domain`: Unique identifier (must match folder name)
- `name`: Display name in UI
- `codeowners`: GitHub usernames responsible for the code
- `config_flow`: Enable UI configuration
- `documentation`: Link to documentation
- `issue_tracker`: Link to issue tracker
- `iot_class`: How the integration communicates
- `requirements`: Python dependencies
- `version`: Integration version

### 2. __init__.py
Main integration file that handles:
- Setup and teardown of the integration
- Platform loading (sensors, switches, etc.)
- Data coordination between platforms

### 3. config_flow.py
Handles the UI configuration flow:
- User input validation
- Connection testing
- Configuration storage

### 4. Platform files (sensor.py, switch.py, etc.)
Implement specific entity types:
- Sensor entities for data display
- Switch entities for control
- Binary sensor entities for on/off states

## Development Steps

### 1. Customize Your Integration

1. **Change the domain name**:
   - Rename folder from `your_integration` to your desired name
   - Update `DOMAIN` in `const.py`
   - Update `domain` in `manifest.json`

2. **Update metadata**:
   - Edit `manifest.json` with your details
   - Update `hacs.json` with your integration name
   - Modify `README.md` with your documentation

3. **Implement your logic**:
   - Add API client code for your service
   - Implement data fetching in `__init__.py`
   - Create appropriate sensor/switch entities

### 2. Testing Locally

1. **Install in Home Assistant**:
   ```bash
   # Copy to your Home Assistant custom_components directory
   cp -r custom_components/your_integration /config/custom_components/
   ```

2. **Restart Home Assistant**

3. **Add integration via UI**:
   - Go to Settings > Devices & Services
   - Click "Add Integration"
   - Search for your integration

### 3. Prepare for HACS Distribution

1. **Create GitHub repository**
2. **Add required files**:
   - All files from this template
   - Proper README.md
   - LICENSE file
   - hacs.json configuration

3. **Repository requirements**:
   - Public repository on GitHub
   - Repository description
   - Repository topics/tags
   - Proper folder structure

### 4. HACS Requirements

Your integration must meet these requirements:

1. **Repository structure**:
   - Only one integration per repository
   - All files in `custom_components/INTEGRATION_NAME/`

2. **manifest.json requirements**:
   - `domain`, `documentation`, `issue_tracker`, `codeowners`, `name`, `version`

3. **Home Assistant Brands**:
   - Add your integration to [home-assistant/brands](https://github.com/home-assistant/brands)

4. **Optional but recommended**:
   - GitHub releases for version management
   - Proper semantic versioning

## API Integration Patterns

### Data Update Coordinator Pattern

```python
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

class YourDataUpdateCoordinator(DataUpdateCoordinator):
    def __init__(self, hass, api_client):
        super().__init__(
            hass,
            _LOGGER,
            name="Your Integration",
            update_interval=timedelta(seconds=30),
        )
        self.api_client = api_client

    async def _async_update_data(self):
        """Fetch data from API."""
        try:
            return await self.api_client.get_data()
        except Exception as err:
            raise UpdateFailed(f"Error communicating with API: {err}")
```

### Entity Implementation

```python
class YourSensorEntity(CoordinatorEntity, SensorEntity):
    def __init__(self, coordinator, description):
        super().__init__(coordinator)
        self.entity_description = description
        self._attr_unique_id = f"{DOMAIN}_{description.key}"

    @property
    def native_value(self):
        """Return the state of the sensor."""
        return self.coordinator.data.get(self.entity_description.key)
```

## Common Integration Types

### Cloud Polling
- Fetches data from cloud API periodically
- Uses `DataUpdateCoordinator` for efficient updates
- Set `iot_class: "cloud_polling"` in manifest

### Local Polling
- Connects to local device/service
- Similar to cloud polling but local network
- Set `iot_class: "local_polling"` in manifest

### Push Updates
- Receives real-time updates via webhooks/websockets
- More efficient than polling
- Set `iot_class: "cloud_push"` or `"local_push"`

## Best Practices

1. **Error Handling**:
   - Always handle API errors gracefully
   - Provide meaningful error messages
   - Use proper exception types

2. **Configuration**:
   - Use config flow for UI configuration
   - Validate user input
   - Store sensitive data securely

3. **Entity Management**:
   - Use unique IDs for all entities
   - Implement proper device info
   - Handle entity availability

4. **Performance**:
   - Use DataUpdateCoordinator for shared data
   - Implement proper update intervals
   - Avoid blocking the event loop

## Publishing to HACS

1. **Create GitHub repository**
2. **Add your integration to HACS**:
   - Users can add custom repositories manually
   - Or submit to HACS default repositories

3. **For default HACS inclusion**:
   - Meet all quality requirements
   - Submit PR to HACS/default repository
   - Maintain active development

## Resources

- [Home Assistant Developer Documentation](https://developers.home-assistant.io/)
- [HACS Documentation](https://hacs.xyz/docs/publish/integration/)
- [Integration Examples](https://github.com/home-assistant/core/tree/dev/homeassistant/components)
- [Home Assistant Brands](https://github.com/home-assistant/brands)

## Support

- Create issues in your GitHub repository
- Join Home Assistant Discord for community support
- Check Home Assistant forums for integration development discussions 