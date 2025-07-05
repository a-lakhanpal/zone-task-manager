"""Logging configuration for Zone Task Manager."""
from __future__ import annotations

import logging
from typing import Any

from .const import DOMAIN

# Create loggers for different components
LOGGER_MAIN = logging.getLogger(f"{DOMAIN}")
LOGGER_CONFIG = logging.getLogger(f"{DOMAIN}.config_flow")
LOGGER_ZONE = logging.getLogger(f"{DOMAIN}.zone")
LOGGER_TASK = logging.getLogger(f"{DOMAIN}.task")
LOGGER_SCHEDULE = logging.getLogger(f"{DOMAIN}.schedule")
LOGGER_NOTIFICATION = logging.getLogger(f"{DOMAIN}.notification")
LOGGER_STORAGE = logging.getLogger(f"{DOMAIN}.storage")
LOGGER_SERVICE = logging.getLogger(f"{DOMAIN}.service")
LOGGER_SENSOR = logging.getLogger(f"{DOMAIN}.sensor")
LOGGER_CALENDAR = logging.getLogger(f"{DOMAIN}.calendar")


def log_entry_setup(entry_id: str, config_data: dict[str, Any]) -> None:
    """Log config entry setup details."""
    LOGGER_MAIN.debug(
        "Setting up config entry %s with notification_time: %s, notifications: %s",
        entry_id,
        config_data.get("notification_time", "Not set"),
        "Enabled" if config_data.get("notification_enabled", False) else "Disabled"
    )


def log_zone_operation(operation: str, zone_id: str, zone_name: str | None = None) -> None:
    """Log zone operations."""
    if zone_name:
        LOGGER_ZONE.debug("%s zone: %s (ID: %s)", operation, zone_name, zone_id)
    else:
        LOGGER_ZONE.debug("%s zone with ID: %s", operation, zone_id)


def log_task_operation(
    operation: str, 
    task_id: str, 
    task_title: str | None = None,
    zone_id: str | None = None
) -> None:
    """Log task operations."""
    details = [f"ID: {task_id}"]
    if task_title:
        details.append(f"Title: {task_title}")
    if zone_id:
        details.append(f"Zone: {zone_id}")
    
    LOGGER_TASK.debug("%s task - %s", operation, ", ".join(details))


def log_schedule_calculation(
    task_id: str, 
    schedule_type: str, 
    next_due: str | None = None
) -> None:
    """Log schedule calculations."""
    if next_due:
        LOGGER_SCHEDULE.debug(
            "Calculated next due date for task %s (%s): %s",
            task_id,
            schedule_type,
            next_due
        )
    else:
        LOGGER_SCHEDULE.debug(
            "Calculating schedule for task %s with type: %s",
            task_id,
            schedule_type
        )


def log_notification_sent(
    notification_type: str,
    task_count: int,
    recipient: str | None = None
) -> None:
    """Log notification events."""
    LOGGER_NOTIFICATION.info(
        "Sent %s notification with %d tasks%s",
        notification_type,
        task_count,
        f" to {recipient}" if recipient else ""
    )


def log_storage_operation(
    operation: str,
    data_type: str,
    count: int | None = None,
    success: bool = True
) -> None:
    """Log storage operations."""
    if success:
        if count is not None:
            LOGGER_STORAGE.debug(
                "%s %d %s items successfully",
                operation,
                count,
                data_type
            )
        else:
            LOGGER_STORAGE.debug("%s %s data successfully", operation, data_type)
    else:
        LOGGER_STORAGE.error("Failed to %s %s data", operation, data_type)


def log_service_call(
    service: str,
    service_data: dict[str, Any],
    user: str | None = None
) -> None:
    """Log service calls."""
    LOGGER_SERVICE.info(
        "Service '%s' called%s with data: %s",
        service,
        f" by {user}" if user else "",
        service_data
    )


def log_error(
    component: str,
    error: Exception,
    context: str | None = None
) -> None:
    """Log errors with context."""
    logger = logging.getLogger(f"{DOMAIN}.{component}")
    if context:
        logger.error("Error in %s: %s", context, error, exc_info=True)
    else:
        logger.error("Error: %s", error, exc_info=True)


# Example usage in configuration.yaml for debugging:
# logger:
#   default: info
#   logs:
#     custom_components.zone_task_manager: debug
#     custom_components.zone_task_manager.task: debug
#     custom_components.zone_task_manager.notification: info 