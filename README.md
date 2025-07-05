# Zone Task Manager for Home Assistant

[![GitHub Release][releases-shield]][releases]
[![GitHub Activity][commits-shield]][commits]
[![License][license-shield]](LICENSE)
[![hacs][hacsbadge]][hacs]

_A comprehensive task management system for Home Assistant that helps you organize and track home maintenance tasks by zones/areas._

## 🎯 Features

- **Zone-Based Organization**: Automatically integrates with Home Assistant areas and supports custom zones
- **Flexible Scheduling**: Create one-time or recurring tasks (daily, weekly, monthly, yearly, custom intervals)
- **Smart Notifications**: Daily task summaries, weekly/monthly reports via Home Assistant notifications
- **Task Management**: Create, update, complete, and delete tasks with notes and completion history
- **Dashboard Integration**: Beautiful dashboard card showing today's tasks and quick completion actions
- **Data Backup**: Export and import your tasks and zones in JSON format
- **Service Integration**: Full automation support with 10 custom services
- **Multi-User Support**: Track who completed tasks in households with multiple users

**This integration will set up the following platforms:**

Platform | Description
-- | --
`sensor` | Task statistics (total, pending, overdue, completion rate)
`calendar` | Task calendar showing scheduled maintenance

## 📋 Prerequisites

- Home Assistant 2023.1.0 or newer
- HACS (for easy installation)
- Home Assistant areas configured (optional but recommended)

## 🚀 Installation

### HACS (Recommended)

1. Open HACS in your Home Assistant instance
2. Go to "Integrations" section
3. Click the three dots in the top right corner
4. Select "Custom repositories"
5. Add this repository URL: `https://github.com/yourusername/zone-task-manager`
6. Select "Integration" as the category
7. Click "Add"
8. Search for "Zone Task Manager" and install it
9. Restart Home Assistant

### Manual Installation

1. Download the `custom_components/zone_task_manager` folder from this repository
2. Copy it to your `custom_components` directory
3. Restart Home Assistant

## ⚙️ Configuration

### Initial Setup

1. Go to **Settings** → **Devices & Services**
2. Click **+ Add Integration**
3. Search for "Zone Task Manager"
4. Follow the configuration wizard:
   - Set your preferred daily notification time
   - Enable/disable notification types
   - Select which Home Assistant areas to use as zones

### Options

After setup, you can adjust settings by clicking **Configure** on the integration:
- Daily notification time
- Weekly/monthly summary preferences
- Overdue task threshold

## 📱 Usage

### Dashboard Card

Add the Zone Task Manager card to your dashboard:

```yaml
type: custom:zone-task-manager-card
entity: sensor.zone_task_manager_today_tasks
```

### Creating Tasks

#### Via UI:
1. Open the Zone Task Manager from the sidebar
2. Select a zone
3. Click "Add Task"
4. Fill in task details and schedule

#### Via Service:
```yaml
service: zone_task_manager.create_task
data:
  zone_id: "living_room"
  title: "Clean windows"
  notes: "Use glass cleaner from garage"
  schedule_type: "monthly"
```

### Task Examples

**Monthly HVAC Filter Change:**
```yaml
service: zone_task_manager.create_task
data:
  zone_id: "utility_room"
  title: "Replace HVAC Filter"
  description: "Change the 20x25x1 filter"
  notes: "Warranty expires March 2025"
  schedule_type: "monthly"
```

**Quarterly Gutter Cleaning:**
```yaml
service: zone_task_manager.create_task
data:
  zone_id: "outdoor"
  title: "Clean gutters"
  schedule_type: "custom"
  schedule_interval: 90
```

## 🔧 Services

The integration provides the following services:

Service | Description
-- | --
`zone_task_manager.create_task` | Create a new task
`zone_task_manager.complete_task` | Mark a task as completed
`zone_task_manager.update_task` | Update task details
`zone_task_manager.delete_task` | Delete a task
`zone_task_manager.create_zone` | Create a custom zone
`zone_task_manager.update_zone` | Update zone settings
`zone_task_manager.delete_zone` | Delete a custom zone
`zone_task_manager.backup_data` | Export all data to JSON
`zone_task_manager.restore_data` | Import data from JSON
`zone_task_manager.send_summary` | Manually trigger a summary notification

## 📊 Sensors

The integration creates the following sensors:

Sensor | Description
-- | --
`sensor.zone_task_manager_total_tasks` | Total number of tasks
`sensor.zone_task_manager_pending_tasks` | Tasks waiting to be completed
`sensor.zone_task_manager_overdue_tasks` | Tasks past their due date
`sensor.zone_task_manager_today_tasks` | Tasks due today
`sensor.zone_task_manager_completed_today` | Tasks completed today
`sensor.zone_task_manager_completion_rate` | 7-day completion percentage

## 🤖 Automations

### Example: Morning Task Reminder
```yaml
automation:
  - alias: "Morning Task Check"
    trigger:
      - platform: time
        at: "08:00:00"
    condition:
      - condition: numeric_state
        entity_id: sensor.zone_task_manager_today_tasks
        above: 0
    action:
      - service: tts.google_say
        data:
          entity_id: media_player.living_room
          message: "You have {{ states('sensor.zone_task_manager_today_tasks') }} tasks due today"
```

### Example: Overdue Task Alert
```yaml
automation:
  - alias: "Overdue Task Alert"
    trigger:
      - platform: state
        entity_id: sensor.zone_task_manager_overdue_tasks
    condition:
      - condition: numeric_state
        entity_id: sensor.zone_task_manager_overdue_tasks
        above: 0
    action:
      - service: notify.mobile_app
        data:
          title: "Overdue Tasks"
          message: "You have {{ states('sensor.zone_task_manager_overdue_tasks') }} overdue tasks!"
```

## 🐛 Troubleshooting

### Debug Logging

Add to your `configuration.yaml`:

```yaml
logger:
  default: info
  logs:
    custom_components.zone_task_manager: debug
    custom_components.zone_task_manager.task: debug
    custom_components.zone_task_manager.notification: info
```

### Common Issues

**No zones appearing:**
- Ensure you have areas configured in Home Assistant
- Check that the integration has permission to access areas

**Notifications not working:**
- Verify the `persistent_notification` integration is enabled
- Check notification time settings
- Enable debug logging for `zone_task_manager.notification`

**Tasks not rescheduling:**
- Ensure task has a valid schedule type
- Check logs for scheduling errors
- Verify task completion is being recorded

## 📝 Data Backup

### Creating a Backup
```yaml
service: zone_task_manager.backup_data
data:
  include_completed: true
```

The backup will be saved to your config directory.

### Restoring from Backup
```yaml
service: zone_task_manager.restore_data
data:
  backup_data: "{{ backup_json_content }}"
  merge: false
```

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Credits

- Built for the Home Assistant community
- Inspired by the need for better home maintenance tracking
- Thanks to all contributors and testers

---

[zone-task-manager]: https://github.com/yourusername/zone-task-manager
[commits-shield]: https://img.shields.io/github/commit-activity/y/yourusername/zone-task-manager.svg?style=for-the-badge
[commits]: https://github.com/yourusername/zone-task-manager/commits/main
[hacs]: https://github.com/hacs/integration
[hacsbadge]: https://img.shields.io/badge/HACS-Custom-orange.svg?style=for-the-badge
[license-shield]: https://img.shields.io/github/license/yourusername/zone-task-manager.svg?style=for-the-badge
[releases-shield]: https://img.shields.io/github/release/yourusername/zone-task-manager.svg?style=for-the-badge
[releases]: https://github.com/yourusername/zone-task-manager/releases 