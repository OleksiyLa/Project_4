const deleteModal = document.querySelector('#delete-goal-modal');
const goBackAddAnchor = document.getElementById("go_back_arrow_add");

function createModalHTML(url, txt) {
    return `
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">

      <div class="modal-header">
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>

      <div class="modal-body h3 text-center">
        Are you sure you want to delete your ${txt}?
      </div>

      <div class="modal-footer">
        <button type="button" class="btn btn-outline-dark" data-bs-dismiss="modal">Cancel</button>
        <a class="btn btn-danger" href="${url}">Confirm</a>
      </div>

    </div>
  </div>
`;
}

function confirmDelete(url, txt) {
  deleteModal.innerHTML = createModalHTML(url, txt);
  const myModal = new bootstrap.Modal(deleteModal);
  myModal.show();
}

document.body.addEventListener('click', (e) => {
    if(e.target.classList.contains('delete-icon')) {
      confirmDelete(e.target.dataset.url, e.target.dataset.txt);
    }
});

document.body.addEventListener('click', (e) => {
  const target = e.target;
  let toggleChevron;
  if(target.classList.contains('tasks-toggler')) {
    if(target.classList.contains('card-title')) {
      toggleChevron = target.children[0];
    } else if(e.target.classList.contains('tasks-toggler-svg')) {
      toggleChevron = target;
    } else {
      toggleChevron = target.parentElement;
    }
    if(toggleChevron.style.transform === "rotate(180deg)") {
      toggleChevron.style.transform = "rotate(0deg)"
      return
    }
    toggleChevron.style.transform = "rotate(180deg)"
  } 
});

if(goBackAddAnchor) {
  const previousUrl = document.referrer;
  const currentUrl = window.location.href;
  if(new URL(previousUrl).hostname === new URL(currentUrl).hostname) {
    const urlFromCookie = getCookie("go_back");
    if(urlFromCookie === "tasks") {
      const baseURL = window.location.origin;
      const fullUrl = `${baseURL}/${urlFromCookie}`;
      goBackAddAnchor.href = fullUrl;
      deleteCookie("go_back")
    }
  }
}

function getCookie(cookieName) {
  const name = cookieName + "=";
  const decodedCookie = decodeURIComponent(document.cookie);
  const cookieArray = decodedCookie.split(';');

  for (let i = 0; i < cookieArray.length; i++) {
    let cookie = cookieArray[i];
    while (cookie.charAt(0) === ' ') {
      cookie = cookie.substring(1);
    }
    if (cookie.indexOf(name) === 0) {
      return cookie.substring(name.length, cookie.length);
    }
  }
  return "";
}

function deleteCookie(name) {
  document.cookie = name + '=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
}
