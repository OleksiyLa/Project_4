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
let selectedDate;

elementsDOM.prevMonthBtn.addEventListener("click", () => {
  date.setMonth(date.getMonth() - 1);
  renderCalendar(date, calendarData);
  selectDate(selectedDate)
});
elementsDOM.nextMonthBtn.addEventListener("click", () => {
  date.setMonth(date.getMonth() + 1);
  renderCalendar(date, calendarData);
  selectDate(selectedDate)
});
elementsDOM.todayBtn.addEventListener("click", () => {
  renderCalendar(new Date(), calendarData);
  selectDate(new Date().toDateString())
  getTasksHTML(new Date().toDateString())
});
elementsDOM.calendar.addEventListener("click", (e) => {
  if(e.target.getAttribute('data-date')) {
    selectDate(e.target.getAttribute('data-date'))
    elementsDOM.tasks.innerHTML = getTasksHTML(e.target.getAttribute('data-date'))
  }
})

fetchData()
renderCalendar(date, calendarData);

function renderCalendar(date, data) {
  let scheduledDates;
  if(data) {
    let scheduled_tasks = data.map(item => item.schedule).flat().map(item => new Date(item.date))
    scheduledDates = scheduled_tasks.map(item => item.toDateString())
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
    row.innerHTML += `<td class='text-center' data-date='${new Date(diplayedDate.getFullYear(), diplayedDate.getMonth(), day).toDateString()}'>${day}</td>`;
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
  fetch('https://task-manager-planner-app-ca416dc67970.herokuapp.com/api/calendar_data/')
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
      calendarData = data
      console.log(calendarData)
      renderCalendar(date, data);
      selectDate(new Date().toDateString())
      getTasksHTML(new Date().toDateString())
    })
    .catch(error => {
      console.error('Fetch error:', error);
    });
}

function selectDate(date) {
  const removeSelector = `td[data-date="${selectedDate}"]`;
  const elementToRemoveClass = document.querySelector(removeSelector);
  if (elementToRemoveClass && elementToRemoveClass.classList.contains('selected-date')) {
    elementToRemoveClass.classList.remove('selected-date');
  }
  
  const addSelector = `td[data-date="${date}"]`;
  const element = document.querySelector(addSelector);
  if (element){
    element.classList.add('selected-date');
  }
  selectedDate = date;
}

function getTasksHTML(date){
  console.log(date)
  const tasks = calendarData.filter(item => {
    return item.schedule.some(schedule => {
      const scheduleDate = new Date(schedule.date);
      return scheduleDate.toDateString() === new Date(selectedDate).toDateString();
    });
  });
  console.log(tasks)
  // const tasks = calendarData.filter(item => item.schedule.map(schedule => new Date(schedule.date).toDateString()).includes(date))
  date = new Date(date)
  console.log(date)
  const tasksArrHTML = [];
  elementsDOM.selected_date.innerHTML = `<h2>${date.getDate()} ${months[date.getMonth()]} ${date.getFullYear()}</h2>`
  tasks.map(item => {
    const schedule = item.schedule.filter(schedule => new Date(schedule.date).toDateString() === date.toDateString())
    console.log(schedule)
    for(let i = 0; i < schedule.length; i++) {
      tasksArrHTML.push([schedule[i].start_time, `
      <div class="card mb-3 bg-light">
        <div class="card-body p-3">
        <img src="/static/svg/delete_icon.svg" alt="delete-icon" class="float-end delete-icon" data-txt="scheduled task" data-title="${item.title}" data-url="${schedule[i].url}">
          <h3 class="h4 text-center my-2">${item.title}</h3>
          <h3 class="h4 text-center my-2">From <span>${schedule[i].start_time.slice(0, -3)}</span> To <span>${schedule[i].end_time.slice(0, -3)}</span></h3>
          <p class="text-center">${item.description}</p>
          <p class="text-center">Done</p>
          <div class="mt-3">
            <a class="btn btn-outline-primary w-100" href="">Edit</a>
            <a class="btn btn-outline-primary w-100" href="">Reschedule</a>
          </div>
        </div>
      </div>`])
    }
    return
  })
  tasksArrHTML.sort((a, b) => a[0] > b[0] ? 1 : -1)
  return tasksArrHTML.map(item => item.pop()).join("")
}
