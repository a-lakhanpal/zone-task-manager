"""Constants for the Zone Task Manager integration."""
from datetime import timedelta
from typing import Final

# Domain
DOMAIN: Final = "zone_task_manager"

# Platforms
PLATFORM_CALENDAR: Final = "calendar"
PLATFORM_SENSOR: Final = "sensor"

# Configuration Keys
CONF_ZONES: Final = "zones"
CONF_TASKS: Final = "tasks"
CONF_NOTIFICATIONS: Final = "notifications"
CONF_NOTIFICATION_TIME: Final = "notification_time"
CONF_NOTIFICATION_ENABLED: Final = "notification_enabled"
CONF_WEEKLY_SUMMARY: Final = "weekly_summary"
CONF_MONTHLY_SUMMARY: Final = "monthly_summary"

# Zone Keys
ZONE_ID: Final = "id"
ZONE_NAME: Final = "name"
ZONE_DESCRIPTION: Final = "description"
ZONE_HA_AREA_ID: Final = "ha_area_id"
ZONE_ENABLED: Final = "enabled"
ZONE_CUSTOM: Final = "custom"
ZONE_ICON: Final = "icon"

# Task Keys
TASK_ID: Final = "id"
TASK_TITLE: Final = "title"
TASK_DESCRIPTION: Final = "description"
TASK_NOTES: Final = "notes"
TASK_ZONE_ID: Final = "zone_id"
TASK_SCHEDULE: Final = "schedule"
TASK_STATUS: Final = "status"
TASK_CREATED_AT: Final = "created_at"
TASK_COMPLETED_AT: Final = "completed_at"
TASK_COMPLETED_BY: Final = "completed_by"
TASK_NEXT_DUE: Final = "next_due"
TASK_COMPLETION_HISTORY: Final = "completion_history"

# Task Status Values
STATUS_PENDING: Final = "pending"
STATUS_COMPLETED: Final = "completed"
STATUS_OVERDUE: Final = "overdue"
STATUS_CANCELLED: Final = "cancelled"

# Schedule Keys
SCHEDULE_TYPE: Final = "type"
SCHEDULE_INTERVAL: Final = "interval"
SCHEDULE_UNIT: Final = "unit"
SCHEDULE_DAYS_OF_WEEK: Final = "days_of_week"
SCHEDULE_DAY_OF_MONTH: Final = "day_of_month"
SCHEDULE_MONTHS: Final = "months"
SCHEDULE_START_DATE: Final = "start_date"
SCHEDULE_END_DATE: Final = "end_date"

# Schedule Types
SCHEDULE_TYPE_ONCE: Final = "once"
SCHEDULE_TYPE_DAILY: Final = "daily"
SCHEDULE_TYPE_WEEKLY: Final = "weekly"
SCHEDULE_TYPE_MONTHLY: Final = "monthly"
SCHEDULE_TYPE_YEARLY: Final = "yearly"
SCHEDULE_TYPE_CUSTOM: Final = "custom"

# Schedule Units
UNIT_DAYS: Final = "days"
UNIT_WEEKS: Final = "weeks"
UNIT_MONTHS: Final = "months"
UNIT_YEARS: Final = "years"

# Storage Keys
STORAGE_VERSION: Final = 1
STORAGE_KEY: Final = f"{DOMAIN}.storage"
STORAGE_ZONES_KEY: Final = "zones"
STORAGE_TASKS_KEY: Final = "tasks"
STORAGE_SETTINGS_KEY: Final = "settings"

# Default Values
DEFAULT_NOTIFICATION_TIME: Final = "09:00"
DEFAULT_NOTIFICATION_ENABLED: Final = True
DEFAULT_WEEKLY_SUMMARY_DAY: Final = "sunday"
DEFAULT_MONTHLY_SUMMARY_DAY: Final = 1
DEFAULT_SCAN_INTERVAL: Final = timedelta(minutes=5)
DEFAULT_OVERDUE_THRESHOLD: Final = timedelta(days=1)

# Service Names
SERVICE_CREATE_TASK: Final = "create_task"
SERVICE_COMPLETE_TASK: Final = "complete_task"
SERVICE_UPDATE_TASK: Final = "update_task"
SERVICE_DELETE_TASK: Final = "delete_task"
SERVICE_CREATE_ZONE: Final = "create_zone"
SERVICE_UPDATE_ZONE: Final = "update_zone"
SERVICE_DELETE_ZONE: Final = "delete_zone"
SERVICE_BACKUP_DATA: Final = "backup_data"
SERVICE_RESTORE_DATA: Final = "restore_data"
SERVICE_SEND_SUMMARY: Final = "send_summary"

# Attributes
ATTR_ZONE_ID: Final = "zone_id"
ATTR_TASK_ID: Final = "task_id"
ATTR_TASK_COUNT: Final = "task_count"
ATTR_OVERDUE_COUNT: Final = "overdue_count"
ATTR_TODAY_COUNT: Final = "today_count"
ATTR_COMPLETED_TODAY: Final = "completed_today"
ATTR_COMPLETION_RATE: Final = "completion_rate"

# Events
EVENT_TASK_CREATED: Final = f"{DOMAIN}_task_created"
EVENT_TASK_COMPLETED: Final = f"{DOMAIN}_task_completed"
EVENT_TASK_OVERDUE: Final = f"{DOMAIN}_task_overdue"
EVENT_ZONE_CREATED: Final = f"{DOMAIN}_zone_created"
EVENT_ZONE_UPDATED: Final = f"{DOMAIN}_zone_updated"

# Icons
ICON_TASK: Final = "mdi:clipboard-check"
ICON_ZONE: Final = "mdi:home-floor-plan"
ICON_OVERDUE: Final = "mdi:alert-circle"
ICON_COMPLETED: Final = "mdi:check-circle"
ICON_PENDING: Final = "mdi:clock-outline"

# Limits
MAX_TASK_TITLE_LENGTH: Final = 100
MAX_TASK_DESCRIPTION_LENGTH: Final = 500
MAX_TASK_NOTES_LENGTH: Final = 1000
MAX_ZONE_NAME_LENGTH: Final = 50
MAX_ZONE_DESCRIPTION_LENGTH: Final = 200 