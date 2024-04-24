export function updateTime() {
    const now = new Date();
    const timeString = now.toLocaleTimeString('en-US', { hour: 'numeric', minute: 'numeric', hour12: true });
    document.querySelector('.time').textContent = timeString;
}

export function display_date() {
    const now = new Date();
    const date_string = now.toLocaleDateString('en-US', { weekday: 'long'});
    document.querySelector('.date').textContent = date_string;
}
