import { startPomodoro } from "./apps/pomodorio/app.js";
import { display_date, updateTime } from "./utils/date.js";
import './apps/qapqom/app.js'

startPomodoro();
display_date();
updateTime();
setInterval(updateTime, 1000);