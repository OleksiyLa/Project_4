const elementsDOM = {
  prevMonthBtn: document.getElementById("prev-month"),
  nextMonthBtn: document.getElementById("next-month"),
  todayBtn: document.getElementById("today"),
  calendar: document.getElementById("calendar-table"),
  tasks: document.getElementById("scheduled-tasks-body"),
  selected_date: document.getElementById("selected-date"),
};

const weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
const months = [
  'January', 'February', 'March', 'April',
  'May', 'June', 'July', 'August',
  'September', 'October', 'November', 'December'
];

const date = new Date();
let calendarData;

elementsDOM.prevMonthBtn.addEventListener("click", () => {
  date.setMonth(date.getMonth() - 1);
  renderCalendar(date, calendarData);
});
elementsDOM.nextMonthBtn.addEventListener("click", () => {
  date.setMonth(date.getMonth() + 1);
  renderCalendar(date, calendarData);
});
elementsDOM.todayBtn.addEventListener("click", () => {
  renderCalendar(new Date(), calendarData);
});
elementsDOM.calendar.addEventListener("click", (e) => {
  if(e.target.getAttribute('data-date')) {
    elementsDOM.tasks.innerHTML = getTasksHTML(e.target.getAttribute('data-date'))
  }
})

fetchData()
renderCalendar(date, calendarData);

function renderCalendar(date, data) {
  let scheduledDates;
  if(data) {
    let scheduled_tasks = data.map(item => item.schedule).flat().map(item => new Date(item.date))
    scheduledDates = scheduled_tasks.map(item => item.toLocaleDateString())
  }
  const diplayedDate = date;
  const firstDay = new Date(diplayedDate.getFullYear(), diplayedDate.getMonth(), 1);
  const startingDay = firstDay.getDay();
  const daysInMonth = new Date(diplayedDate.getFullYear(), diplayedDate.getMonth() + 1, 0).getDate();
  const tbody = document.querySelector("table tbody");
  tbody.innerHTML = "";
  let row = document.createElement("tr");

  row.innerHTML += getPreviousMonthHTML(diplayedDate, startingDay);

  for (let day = 1; day <= daysInMonth; day++) {
    row.innerHTML += `<td class='text-center' data-date='${new Date(diplayedDate.getFullYear(), diplayedDate.getMonth(), day).toLocaleDateString()}'>${day}</td>`;
    if(day === daysInMonth && (startingDay + day) % 7 !== 0) {
      let nextMonthDay = 1;
      for(let i = (startingDay + day) % 7; i < 7; i++) {
        row.innerHTML += `<td class='text-center next-month-day'>${nextMonthDay++}</td>`;
      }
    }
    if (day === diplayedDate.getDate() && diplayedDate.getMonth() === new Date().getMonth() && diplayedDate.getFullYear() === new Date().getFullYear()) {
      row.lastChild.classList.add("today");
    }
    if(data && scheduledDates.includes(row.lastChild.getAttribute('data-date'))) {
      row.lastChild.classList.add("scheduled-date");
    }
    if ((day + startingDay) % 7 === 0 || day === daysInMonth) {
      tbody.appendChild(row);
      row = document.createElement("tr");
    }
  }

  const currentMonthYear = document.getElementById("current-month-year");
  currentMonthYear.innerHTML = `<h2>${diplayedDate.toLocaleString("default", { month: "long" })} ${diplayedDate.getFullYear()}</h2>`;
}

function getPreviousMonthHTML(today, startingDay) {
  const daysInPreviousMonth = new Date(today.getFullYear(), today.getMonth(), 0).getDate();
  const prevMonthDate = []
  for (let i = 0; i < startingDay; i++) {
    const day = daysInPreviousMonth - i;
    prevMonthDate.push(`<td class='text-center prev-month-day'>${day}</td>`);
  }
  return prevMonthDate.reverse().join("");
}

function fetchData() {
  fetch('http://127.0.0.1:8000/api/calendar_data/')
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      return data
    })
    .then(data => {
      calendarData = processData(data)
      renderCalendar(date, calendarData);
      getTasksHTML(new Date().toLocaleDateString())
    })
    .catch(error => {
      console.error('Fetch error:', error);
    });
}

function processData(data) {
  const processedData = data.map(item => ({title: item.task_title, description: item.task_description, slug: item.task_slug, schedule: item.schedule_list.map(schedule => schedule.scheduled_dates).flat()}))
  return processedData
}

function getTasksHTML(date){
  const tasks = calendarData.filter(item => item.schedule.map(schedule => new Date(schedule.date).toLocaleDateString()).includes(date))
  date = new Date(date)
  const tasksArrHTML = [];
  elementsDOM.selected_date.innerHTML = `<h2>${date.getDate()} ${months[date.getMonth()]} ${date.getFullYear()}</h2>`
  tasks.map(item => {
    const schedule = item.schedule.filter(schedule => new Date(schedule.date).toLocaleDateString() === date.toLocaleDateString())
    for(let i = 0; i < schedule.length; i++) {
      tasksArrHTML.push(`
      <div class="card mb-3 bg-light">
        <div class="card-body p-3">
          <img src="/static/svg/delete_icon.svg" alt="delete-icon" class="float-end delete-icon" data-txt="task" data-title="${item.title}" data-url="${item.url}">
          <h3 class="h4 text-center my-2">${item.title}</h3>
          <h3 class="h4 text-center my-2">From <span>${schedule[i].start_time}</span> To <span>${schedule[i].end_time}</span></h3>
          <p class="text-center">${item.description}</p>
          <p class="text-center">Done</p>
          <div class="mt-3">
            <a class="btn btn-outline-primary w-100" href="">Edit</a>
            <a class="btn btn-outline-primary w-100" href="">Reschedule</a>
          </div>
        </div>
      </div>`)
    }
    return 
  })
  return tasksArrHTML.join("")
}