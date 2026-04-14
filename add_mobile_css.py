import os

css_path = r'c:\Users\genna\.gemini\antigravity\scratch\eu-citizenship\assets\css\style.css'

added_css = """

/* =========================================
   RESPONSIVE DESIGN (Tablets & Mobile)
   ========================================= */

.mobile-toggle {
    display: none;
    background: transparent;
    border: none;
    color: var(--gold-main);
    cursor: pointer;
    padding: 8px;
    z-index: 1000;
}

.mobile-toggle svg {
    transition: stroke 0.3s ease;
}

.mobile-toggle:hover svg {
    stroke: var(--blue-main);
}

@media (max-width: 1024px) {
    /* TABLET Fixes */
    .hero-content h1 { font-size: 3rem !important; }
    .hero-content p { font-size: 1.1rem !important; }
    
    .services-grid, .guarantees-grid, .program-grid, .reviews-grid, .contact-grid {
        grid-template-columns: 1fr 1fr !important;
        gap: 20px !important;
    }
    
    .main-nav ul.nav-list {
        gap: 15px !important;
    }
}

@media (max-width: 768px) {
    /* MOBILE Fixes */
    .mobile-toggle {
        display: block !important;
    }

    /* Mobile Header Stack */
    .main-header .container {
        flex-wrap: wrap !important;
        justify-content: space-between !important;
        padding: 10px 15px !important;
    }
    
    .main-nav {
        display: none;
        width: 100%;
        order: 3;
        margin-top: 15px;
        background: #FFFFFF;
        border-radius: 12px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        padding: 20px !important;
        text-align: center;
    }
    
    .main-nav.active {
        display: block !important;
        animation: fadeIn 0.3s ease;
    }

    .main-nav ul.nav-list {
        flex-direction: column !important;
        align-items: center !important;
        gap: 15px !important;
    }
    
    /* Header Actions under Mobile Nav */
    .header-actions {
        display: none;
        width: 100%;
        order: 4;
        justify-content: center !important;
        margin-top: 15px;
        flex-wrap: wrap;
        gap: 10px;
    }
    .header-actions.active {
        display: flex !important;
        animation: fadeIn 0.4s ease;
    }
    
    /* Grids to 1 column */
    .services-grid, .guarantees-grid, .program-grid, .timeline, .reviews-grid, .docs-grid, .contact-grid {
        grid-template-columns: 1fr !important;
    }
    
    /* Typography */
    .hero-content h1, .contact-hero h1, .faq-hero h1 {
        font-size: 2.2rem !important;
        line-height: 1.2 !important;
    }
    .section-header h2 {
        font-size: 1.8rem !important;
    }
    
    /* Section paddings */
    section, .hero, .contact-hero, .faq-hero {
        padding: 60px 20px !important;
    }
    
    /* Fix Hero Overlaps */
    .hero .container {
        flex-direction: column !important;
        text-align: center !important;
    }
    .hero-content {
        padding-right: 0 !important;
        margin-bottom: 40px !important;
        align-items: center !important;
    }
    .hero-bullets, .guarantee-labels {
        justify-content: center !important;
    }
    
    /* 3D Passports scaling fix */
    .passport-3d {
        transform: scale(0.8) !important;
        right: 0 !important;
    }
    .passport-1, .passport-2, .passport-3 {
        position: relative !important;
        right: auto !important;
        top: auto !important;
        margin: -20px 0 !important;
    }
    .hero-form-wrapper {
        margin-top: 20px;
    }
    
    /* Footer */
    .footer-top .container {
        flex-direction: column !important;
        gap: 30px !important;
    }
    .footer-col {
        text-align: center !important;
        border-right: none !important;
        padding-right: 0 !important;
    }
    .social-icons, .footer-contact, .footer-col ul {
        justify-content: center !important;
        text-align: center !important;
    }
}

@media (max-width: 480px) {
    .container {
        padding: 0 15px !important;
    }
    .hero-content h1 {
        font-size: 1.9rem !important;
    }
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(-10px); }
    to { opacity: 1; transform: translateY(0); }
}
"""

with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

if 'RESPONSIVE DESIGN (Tablets & Mobile)' not in css_content:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write(added_css)
    print("Added responsive CSS successfully.")
else:
    print("Responsive CSS already exists.")
