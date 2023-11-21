const deleteModal = document.querySelector('#delete-goal-modal');

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



// function createModalHTML(title, url, txt) {
//   return `
//   <div class="modal fade" id="exampleModalCenter" tabindex="-1" role="dialog" aria-labelledby="exampleModalCenterTitle" aria-hidden="true">
//   <div class="modal-dialog modal-dialog-centered" role="document">
//     <div class="modal-content">
//       <div class="modal-header">
//         <h5 class="modal-title" id="exampleModalLongTitle">Modal title</h5>
//         <button type="button" class="close" data-dismiss="modal" aria-label="Close">
//           <span aria-hidden="true">&times;</span>
//         </button>
//       </div>
//       <div class="modal-body">
//         ...
//       </div>
//       <div class="modal-footer">
//         <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
//         <button type="button" class="btn btn-primary">Save changes</button>
//       </div>
//     </div>
//   </div>
// </div>
// `;
// }