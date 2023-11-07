const date = new Date();
function renderCalendar(date) {
  // Get the current date
  const today = date;
  // Get the first day of the current month
  const firstDay = new Date(today.getFullYear(), today.getMonth(), 1);
  // Determine the day of the week for the first day (0 = Sunday, 1 = Monday, etc.)
  const startingDay = firstDay.getDay();

  // Get the number of days in the current month
  const daysInMonth = new Date(today.getFullYear(), today.getMonth() + 1, 0).getDate();

  // Get the tbody element to populate
  const tbody = document.querySelector("table tbody");

  // Clear the tbody
  tbody.innerHTML = "";

  // Create rows and cells for the calendar
  let row = document.createElement("tr");

  row.innerHTML += getPreviousMonthHTML(today, startingDay);

  for (let day = 1; day <= daysInMonth; day++) {
    row.innerHTML += `<td class='text-center'>${day}</td>`;
    if(day === daysInMonth && (startingDay + day) % 7 !== 0) {
      let nextMonthDay = 1;
      for(let i = (startingDay + day) % 7; i < 7; i++) {
        row.innerHTML += `<td class='text-center next-month-day'>${nextMonthDay++}</td>`;
      }
    }
    if ((day + startingDay) % 7 === 0 || day === daysInMonth) {
      tbody.appendChild(row);
      row = document.createElement("tr");
    }
    if (day === today.getDate() && today.getMonth() === new Date().getMonth() && today.getFullYear() === new Date().getFullYear()) {
      row.lastChild.classList.add("today");
    }
  }




  const currentMonthYear = document.getElementById("current-month-year");
  currentMonthYear.innerHTML = `<h2>${today.toLocaleString("default", { month: "long" })} ${today.getFullYear()}</h2>`;
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

const prevMonthBtn = document.getElementById("prev-month");
const nextMonthBtn = document.getElementById("next-month");
const todayBtn = document.getElementById("today");

prevMonthBtn.addEventListener("click", () => {
  date.setMonth(date.getMonth() - 1);
  renderCalendar(date);
});
nextMonthBtn.addEventListener("click", () => {
  date.setMonth(date.getMonth() + 1);
  renderCalendar(date);
  console.log(date);
});
todayBtn.addEventListener("click", () => {
  // date.setMonth(new Date().getMonth());
  renderCalendar(new Date());
});
renderCalendar(date);