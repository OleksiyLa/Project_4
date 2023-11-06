const deleteModal = document.querySelector('#delete-goal-modal');

function createModalHTML(title, url, goal) {
    return `
  <div class="modal-dialog">
    <div class="modal-content">

      <!-- Modal Header -->
      <div class="modal-header">
        <h4 class="modal-title">Delete your ${goal}</h4>
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

// const goalsBoard = document.querySelector('#goals-board');
// goalsBoard.addEventListener('click', (e) => {
//     if(e.target.classList.contains('delete-icon')) {
//       confirmDelete(e.target.dataset.title, e.target.dataset.url, 'goal');
//     }
// });

const tasksContainer = document.querySelector('#tasks-container');
tasksContainer.addEventListener('click', (e) => {
    if(e.target.classList.contains('delete-icon')) {
      confirmDelete(e.target.dataset.title, e.target.dataset.url, 'task');
    }
});