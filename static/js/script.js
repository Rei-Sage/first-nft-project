// const mobileMenuToggle = document.getElementById('mobile-menu-toggle');
// const mobileMenu = document.getElementById('mobile-menu');
// const navMenu = document.getElementById('nav-menu');

// mobileMenuToggle.addEventListener('click', () => {
//     mobileMenu.classList.toggle('hidden');
// });

// document.addEventListener('click', (event) => {
//     const isClickInsideMenu = mobileMenu.contains(event.target) || 
//                               mobileMenuToggle.contains(event.target);
    
//     if (!isClickInsideMenu && !mobileMenu.classList.contains('hidden')) {
//         mobileMenu.classList.add('hidden');
//         navMenu.classList.remove('hidden');
//     }
// });


const mobileMenuToggle = document.getElementById('mobile-menu-toggle');
const mobileMenu = document.getElementById('mobile-menu');

mobileMenuToggle.addEventListener('click', () => {
    if (mobileMenu.classList.contains('hidden')) {
        mobileMenu.classList.remove('hidden');
        mobileMenu.classList.remove('translate-y-full');
        mobileMenu.classList.add('translate-y-0');
    } else {
        mobileMenu.classList.add('translate-y-full');
        setTimeout(() => {
            mobileMenu.classList.add('hidden');
        }, 0); 
    }
});

document.addEventListener('click', (event) => {
    const isClickInsideMenu = mobileMenu.contains(event.target) || 
                              mobileMenuToggle.contains(event.target);
    if (!isClickInsideMenu && !mobileMenu.classList.contains('hidden')) {
        mobileMenu.classList.add('translate-y-full');
        setTimeout(() => {
            mobileMenu.classList.add('hidden');
        }, 0);
    }
});





document.querySelectorAll('.tab').forEach(tab => {
    tab.addEventListener('click', () => {
      document.querySelector('.tab.active').classList.remove('active', 'text-red-500', 'border-blue-500');
      tab.classList.add('active', 'text-white', 'border-blue-500');
    });
  });
  