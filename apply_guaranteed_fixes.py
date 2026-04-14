import os
css_path = r'c:\Users\genna\.gemini\antigravity\scratch\eu-citizenship\assets\css\style.css'
js_path = r'c:\Users\genna\.gemini\antigravity\scratch\eu-citizenship\assets\js\main.js'

guaranteed_mobile_css = """

/* --- GUARANTEED MOBILE FIXES --- */
@media screen and (max-width: 1024px) {
    .hero-container {
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
    }
    .hero-content {
        width: 100% !important;
        margin-right: 0 !important;
        padding-right: 0 !important;
        text-align: center !important;
        margin-bottom: 30px !important;
    }
    .hero-form-wrapper {
        width: 100% !important;
        max-width: 400px !important;
        position: relative !important;
        right: auto !important;
        top: auto !important;
        margin: 0 auto !important;
        display: block !important;
    }
    .hero-form-box {
        width: 100% !important;
        transform: none !important;
    }
    .hero-bullets {
        justify-content: center !important;
    }
    .deco-passport {
        display: none !important; /* Hide floating passports on mobile to save space */
    }
    
    /* Strict Mobile Menu */
    .main-nav {
        display: none !important;
        width: 100% !important;
        position: absolute !important;
        top: 70px !important;
        left: 0 !important;
        background: #0B2046 !important;
        padding: 20px !important;
        z-index: 9999 !important;
        text-align: center !important;
    }
    .main-nav.active {
        display: block !important;
    }
    .main-nav ul {
        flex-direction: column !important;
    }
    .header-actions {
        display: none !important;
    }
    .header-actions.active {
        display: flex !important;
        position: absolute !important;
        top: 350px !important;
        left: 0 !important;
        width: 100% !important;
        justify-content: center !important;
        z-index: 9999 !important;
    }
}
"""

with open(css_path, 'a', encoding='utf-8') as f:
    f.write(guaranteed_mobile_css)

js_fix = """
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
"""

with open(js_path, 'a', encoding='utf-8') as f:
    f.write(js_fix)

print("Applied guaranteed fixes to CSS and JS")
