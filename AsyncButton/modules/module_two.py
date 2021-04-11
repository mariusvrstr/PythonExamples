


async def start():    
    sensor_manager.register_available()
    sensor_manager.start_monitoring()    
    
    trigger_manager.register_available()
    device_manager = DeviceManager()

    integration_adapter.start_monitoring(sensor_manager.sensor_list)

    await device_manager.start_device_dashboard(sensor_manager, trigger_manager, integration_adapter) 