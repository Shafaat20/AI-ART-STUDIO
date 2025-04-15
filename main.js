
document.addEventListener("DOMContentLoaded", () => {
  // Mobile menu toggle
  const mobileMenuButton = document.querySelector(".mobile-menu-button")
  const mobileMenu = document.querySelector(".mobile-menu")

  if (mobileMenuButton && mobileMenu) {
    mobileMenuButton.addEventListener("click", () => {
      mobileMenu.classList.toggle("active")

      // Change icon
      const icon = mobileMenuButton.querySelector("i")
      if (mobileMenu.classList.contains("active")) {
        icon.classList.remove("fa-bars")
        icon.classList.add("fa-times")
      } else {
        icon.classList.remove("fa-times")
        icon.classList.add("fa-bars")
      }
    })
  }

  // Close flash messages
  const closeButtons = document.querySelectorAll(".flash-message .close-button")

  closeButtons.forEach((button) => {
    button.addEventListener("click", () => {
      const flashMessage = button.closest(".flash-message")
      flashMessage.style.opacity = "0"
      setTimeout(() => {
        flashMessage.remove()
      }, 300)
    })
  })

  // Auto-hide flash messages after 5 seconds
  const flashMessages = document.querySelectorAll(".flash-message")

  flashMessages.forEach((message) => {
    setTimeout(() => {
      message.style.opacity = "0"
      setTimeout(() => {
        message.remove()
      }, 300)
    }, 5000)
  })
})
document.addEventListener('DOMContentLoaded', function() {
// Close flash messages
const closeButtons = document.querySelectorAll('.flash-message .close-button');
closeButtons.forEach(button => {
  button.addEventListener('click', function() {
    const flashMessage = this.parentElement;
    flashMessage.style.opacity = '0';
    setTimeout(() => {
      flashMessage.remove();
    }, 300);
  });
});

// Auto-hide flash messages after 5 seconds
const flashMessages = document.querySelectorAll('.flash-message');
flashMessages.forEach(message => {
  setTimeout(() => {
    message.style.opacity = '0';
    setTimeout(() => {
      message.remove();
    }, 300);
  }, 5000);
});

// Mobile sidebar toggle
const sidebarToggle = document.querySelector('.sidebar-toggle');
if (sidebarToggle) {
  sidebarToggle.addEventListener('click', function() {
    const sidebar = document.querySelector('.chat-sidebar');
    sidebar.classList.toggle('collapsed');
    
    // Update toggle icon
    const icon = this.querySelector('i');
    if (sidebar.classList.contains('collapsed')) {
      icon.classList.remove('fa-times');
      icon.classList.add('fa-bars');
    } else {
      icon.classList.remove('fa-bars');
      icon.classList.add('fa-times');
    }
  });
}

// Auto-resize textarea
const chatInput = document.querySelector('.chat-input');
if (chatInput) {
  chatInput.addEventListener('input', function() {
    this.style.height = 'auto';
    this.style.height = (this.scrollHeight) + 'px';
  });
}

// Scroll to bottom of chat messages
const chatMessages = document.querySelector('.chat-messages');
if (chatMessages) {
  chatMessages.scrollTop = chatMessages.scrollHeight;
}
});
document.addEventListener("DOMContentLoaded", () => {
// Mobile menu toggle
const mobileMenuButton = document.querySelector(".mobile-menu-button")
const mobileMenu = document.querySelector(".mobile-menu")

if (mobileMenuButton && mobileMenu) {
  mobileMenuButton.addEventListener("click", () => {
    mobileMenu.classList.toggle("active")

    // Change icon
    const icon = mobileMenuButton.querySelector("i")
    if (mobileMenu.classList.contains("active")) {
      icon.classList.remove("fa-bars")
      icon.classList.add("fa-times")
    } else {
      icon.classList.remove("fa-times")
      icon.classList.add("fa-bars")
    }
  })
}

// Close flash messages
const closeButtons = document.querySelectorAll(".flash-message .close-button")

closeButtons.forEach((button) => {
  button.addEventListener("click", () => {
    const flashMessage = button.closest(".flash-message")
    flashMessage.style.opacity = "0"
    setTimeout(() => {
      flashMessage.remove()
    }, 300)
  })
})

// Auto-hide flash messages after 5 seconds
const flashMessages = document.querySelectorAll(".flash-message")

flashMessages.forEach((message) => {
  setTimeout(() => {
    message.style.opacity = "0"
    setTimeout(() => {
      message.remove()
    }, 300)
  }, 5000)
})
})









// document.addEventListener("DOMContentLoaded", () => {
//     // Mobile menu toggle
//     const mobileMenuButton = document.querySelector(".mobile-menu-button")
//     const mobileMenu = document.querySelector(".mobile-menu")
  
//     if (mobileMenuButton && mobileMenu) {
//       mobileMenuButton.addEventListener("click", () => {
//         mobileMenu.classList.toggle("active")
  
//         // Change icon
//         const icon = mobileMenuButton.querySelector("i")
//         if (mobileMenu.classList.contains("active")) {
//           icon.classList.remove("fa-bars")
//           icon.classList.add("fa-times")
//         } else {
//           icon.classList.remove("fa-times")
//           icon.classList.add("fa-bars")
//         }
//       })
//     }
  
//     // Close flash messages
//     const closeButtons = document.querySelectorAll(".flash-message .close-button")
  
//     closeButtons.forEach((button) => {
//       button.addEventListener("click", () => {
//         const flashMessage = button.closest(".flash-message")
//         flashMessage.style.opacity = "0"
//         setTimeout(() => {
//           flashMessage.remove()
//         }, 300)
//       })
//     })
  
//     // Auto-hide flash messages after 5 seconds
//     const flashMessages = document.querySelectorAll(".flash-message")
  
//     flashMessages.forEach((message) => {
//       setTimeout(() => {
//         message.style.opacity = "0"
//         setTimeout(() => {
//           message.remove()
//         }, 300)
//       }, 5000)
//     })
//   })
  
  