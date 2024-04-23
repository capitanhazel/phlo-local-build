export function updateTime() {
    const now = new Date();
    const timeString = now.toLocaleTimeString('en-US', { weekday: 'long', hour: 'numeric', minute: 'numeric', hour12: true });
    document.getElementById('time').textContent = timeString;
}

export function display_date() {
    const now = new Date();
    const date_string = now.toISOString().slice(0, 10);
    document.querySelector('.date').textContent = date_string;
}
