export function startPomodoro() {
    const workTime = 25 * 60; // 25 minutes
    const breakTime = 5 * 60; // 5 minutes
    let isWorkTime = true;
    let timeLeft = workTime;
    let newDiv = null;

    function updateTimer() {
        const mins = Math.floor(timeLeft / 60);
        const secs = timeLeft % 60;
        const timer = `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;

        document.querySelector('.timer').textContent = `${isWorkTime ? '' : ''} ${timer}`;

        if (timeLeft === 0) {
            isWorkTime = !isWorkTime;
            timeLeft = isWorkTime ? workTime : breakTime;

            if (!isWorkTime) {
                const navigatorBar = document.querySelector('.navigator-bar');
                newDiv = document.createElement('div');
                newDiv.classList.add('navigator-bar-notify');
                navigatorBar.appendChild(newDiv);
            } else {
                // Remove the appended div when it's work time again
                if (newDiv) newDiv.remove();
                newDiv = null;
            }
        } else {
            timeLeft--;
        }

        // Update the textContent of the newDiv every second during the break
        if (!isWorkTime && newDiv) {
            newDiv.textContent = `${timer}`;
        }
    }

    setInterval(updateTimer, 1000);
}
