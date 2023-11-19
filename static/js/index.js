const deleteModal = document.querySelector('#delete-goal-modal');

function createModalHTML(title, url, txt) {
    return `
  <div class="modal-dialog">
    <div class="modal-content">

      <!-- Modal Header -->
      <div class="modal-header">
        <h4 class="modal-title">Delete your ${txt}</h4>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
      </div>

      <!-- Modal body -->
      <div class="modal-body h3 text-center">
        Are you sure you want to delete <strong>${title}</strong>?
      </div>

      <!-- Modal footer -->
      <div class="modal-footer">
        <button type="button" class="btn btn-outline-dark" data-bs-dismiss="modal">Cancel</button>
        <a class="btn btn-danger" href="${url}">Confirm</a>
      </div>

    </div>
  </div>
`;
}

function confirmDelete(title, url, txt) {
  deleteModal.innerHTML = createModalHTML(title, url, txt);
  const myModal = new bootstrap.Modal(deleteModal);
  myModal.show();
}

document.body.addEventListener('click', (e) => {
    if(e.target.classList.contains('delete-icon')) {
      confirmDelete(e.target.dataset.title, e.target.dataset.url, e.target.dataset.txt);
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
