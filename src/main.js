import { startPomodoro } from "./apps/pomodorio/app.js";
import { display_date, updateTime } from "./utils/date.js";


startPomodoro();
display_date();

updateTime();
setInterval(updateTime, 1000);
