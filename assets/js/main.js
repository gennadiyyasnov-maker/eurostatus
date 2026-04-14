import './lang.js';
window.initEuroStatusApp = function() {
    // Logic for sticky header - check to prevent duplicate listeners
    if (!window.headerScrollInitialized) {
        window.addEventListener('scroll', () => {
            const header = document.querySelector('.main-header');
            if (!header) return;
            if (window.scrollY > 50) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        });
        window.headerScrollInitialized = true;
    }

    // Carousel Logic
    const track = document.querySelector('.reviews-track');
    const prevBtn = document.querySelector('.prev-btn');
    const nextBtn = document.querySelector('.next-btn');

    if (track && prevBtn && nextBtn) {
        let currentIndex = 0;

        const updateCarousel = () => {
            const card = track.querySelector('.review-card');
            if (!card) return;

            // Calculate cards visible right now
            const cardsVisible = Math.max(1, Math.round(track.parentElement.offsetWidth / card.offsetWidth));
            const totalCards = track.querySelectorAll('.review-card').length;
            const actualMax = Math.max(0, totalCards - cardsVisible);

            if (currentIndex > actualMax) currentIndex = actualMax;
            if (currentIndex < 0) currentIndex = 0;

            const gap = parseInt(window.getComputedStyle(track).gap) || 0;
            const transformValue = currentIndex * (card.offsetWidth + gap);
            
            track.style.transform = `translateX(-${transformValue}px)`;

            prevBtn.disabled = currentIndex === 0;
            nextBtn.disabled = currentIndex >= actualMax;
        };

        // Remove old listeners to avoid duplicates if re-initialized
        const newNextBtn = nextBtn.cloneNode(true);
        nextBtn.parentNode.replaceChild(newNextBtn, nextBtn);
        const newPrevBtn = prevBtn.cloneNode(true);
        prevBtn.parentNode.replaceChild(newPrevBtn, prevBtn);

        newNextBtn.addEventListener('click', () => {
            currentIndex++;
            updateCarousel();
        });

        newPrevBtn.addEventListener('click', () => {
            currentIndex--;
            updateCarousel();
        });

        if (!window.carouselResizeInitialized) {
            window.addEventListener('resize', updateCarousel);
            window.carouselResizeInitialized = true;
        }
        setTimeout(updateCarousel, 100);
    }
    
    // Custom Dropdown Initialization (if exists)
    // Removed old inline HTML onclicks and moving to JS logic if necessary,
    // but right now they are inline so they don't duplicate.

    // Modal click-outside logic
    const modal = document.getElementById('serviceModal');
    if (modal) {
        // Clone to remove old listeners
        const newModal = modal.cloneNode(true);
        modal.parentNode.replaceChild(newModal, modal);
        
        newModal.addEventListener('click', (e) => {
            if (e.target === newModal) {
                closeServiceModal();
            }
        });
    }

    console.log('EU Citizenship App initialized.');
};

// Global modal functions
window.openServiceModal = function(serviceName) {
    const modal = document.getElementById('serviceModal');
    if (!modal) return;
    
    const badge = document.getElementById('modal-service-name');
    if (badge) badge.innerText = serviceName;
    
    const formInput = modal.querySelector('input[name="service_type"]'); 
    if (formInput) formInput.value = serviceName;
    
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
};

window.closeServiceModal = function() {
    const modal = document.getElementById('serviceModal');
    if (!modal) return;
    modal.classList.remove('active');
    document.body.style.overflow = 'auto';
};

// Unif Dropdown function for forms
window.customSelectOptionUnif = function(hiddenId, textId, menuId, wrapperId, value, text) {
    document.getElementById(hiddenId).value = value;
    const txtEl = document.getElementById(textId);
    txtEl.innerText = text;
    txtEl.style.color = '#fff';
    document.getElementById(menuId).classList.remove('show');
    document.getElementById(wrapperId).querySelector('.custom-select-trigger').classList.remove('active');
};

document.addEventListener('DOMContentLoaded', window.initEuroStatusApp);


// Mobile Menu Toggle logic
function toggleMobileMenu() {
    const nav = document.querySelector('.main-nav');
    const actions = document.querySelector('.header-actions');
    const toggleBtn = document.querySelector('.mobile-toggle');
    
    if (nav) nav.classList.toggle('active');
    if (actions) actions.classList.toggle('active');
    if (toggleBtn) toggleBtn.classList.toggle('active');
}

// Close mobile menu on anchor clicks
document.addEventListener('DOMContentLoaded', () => {
    const navLinks = document.querySelectorAll('.main-nav a');
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            const nav = document.querySelector('.main-nav');
            const actions = document.querySelector('.header-actions');
            const toggleBtn = document.querySelector('.mobile-toggle');
            if (nav && nav.classList.contains('active')) {
                nav.classList.remove('active');
                if(actions) actions.classList.remove('active');
                if(toggleBtn) toggleBtn.classList.remove('active');
            }
        });
    });
});

// Expose for inline onclick
window.toggleMobileMenu = toggleMobileMenu;

// Hard override mobile toggle
window.toggleMobileMenu = function() {
    var nav = document.querySelector('.main-nav');
    var actions = document.querySelector('.header-actions');
    if (nav) {
        if (nav.classList.contains('active')) {
            nav.classList.remove('active');
            nav.setAttribute('style', 'display: none !important');
        } else {
            nav.classList.add('active');
            nav.setAttribute('style', 'display: block !important');
        }
    }
    if (actions) {
        if (actions.classList.contains('active')) {
            actions.classList.remove('active');
            actions.setAttribute('style', 'display: none !important');
        } else {
            actions.classList.add('active');
            actions.setAttribute('style', 'display: flex !important');
        }
    }
};


// Morphing Hero Country Animation
document.addEventListener("DOMContentLoaded", () => {
  const countries = ["Евросоюза", "Румынии", "Болгарии", "Словении", "Польши", "Турции", "Австрии", "Израиля", "Германии", "Венгрии", "Армении", "Испании"];
  let currentIndex = 0;
  const morphEl = document.querySelector(".morphing-country");
  
  if(morphEl) {
    setInterval(() => {
      morphEl.classList.add("fade-out");
      
      setTimeout(() => {
        currentIndex = (currentIndex + 1) % countries.length;
        morphEl.textContent = countries[currentIndex];
        
        morphEl.classList.remove("fade-out");
        morphEl.classList.add("fade-in");
        
        // force reflow
        void morphEl.offsetWidth;
        
        morphEl.classList.remove("fade-in");
      }, 500); 
    }, 3500); 
  }
});
