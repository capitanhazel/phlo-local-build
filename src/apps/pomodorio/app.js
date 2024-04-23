export function startPomodoro() {
    const workTime = 25 * 60; // 25 minutes
    const breakTime = 5 * 60; // 5 minutes
    let isWorkTime = true;
    let timeLeft = workTime;

    function updateTimer() {
        const mins = Math.floor(timeLeft / 60);
        const secs = timeLeft % 60;
        const timer = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;

        document.getElementById('timer').textContent = `${isWorkTime ? 'Work Time:' : 'Break Time:'} ${timer}`;

        if (timeLeft === 0) {
            isWorkTime = !isWorkTime;
            timeLeft = isWorkTime ? workTime : breakTime;
        } else {
            timeLeft--;
        }
    }

    setInterval(updateTimer, 1000);
}
