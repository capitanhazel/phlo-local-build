const invoke = window.__TAURI__.invoke
invoke('my_custom_command', { invokeMessage: 'Hello!' })