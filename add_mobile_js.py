import os

js_path = r'c:\Users\genna\.gemini\antigravity\scratch\eu-citizenship\assets\js\main.js'

with open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

if 'function toggleMobileMenu' not in js_content:
    added_js = """

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
"""
    with open(js_path, 'a', encoding='utf-8') as f:
        f.write(added_js)
    print("Added toggleMobileMenu to main.js")
else:
    print("toggleMobileMenu already exists")
