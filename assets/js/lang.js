/* Simple Google Translate Auto-Localization */

function setTranslateCookie(lang) {
    document.cookie = `googtrans=/ru/${lang}; path=/`;
    document.cookie = `googtrans=/ru/${lang}; domain=${location.hostname}; path=/`;
}

function removeTranslateCookie() {
    document.cookie = "googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
    document.cookie = `googtrans=; expires=Thu, 01 Jan 1970 00:00:00 UTC; domain=${location.hostname}; path=/;`;
}

document.addEventListener('DOMContentLoaded', () => {
    // 1. Inject hidden translator
    const style = document.createElement('style');
    style.innerHTML = `
        /* Hide the banner frame */
        .goog-te-banner-frame { display: none !important; }
        .goog-te-banner-frame.skiptranslate { display: none !important; }
        iframe.goog-te-banner-frame { display: none !important; }
        
        /* Stop the body from being pushed down */
        body, html { top: 0px !important; position: static !important; min-height: 100vh !important; }
        
        /* Hide hovering translation tooltips and highlight boxes */
        .goog-text-highlight { background-color: transparent !important; box-shadow: none !important; }
        #goog-gt-tt, .goog-te-balloon-frame, .VIpgJd-ZVi9od-ORHb-OEVmcd { display: none !important; }
        
        /* Prevent inline box fragmentation for pill buttons when translated */
        .lang-switch a { display: inline-block !important; white-space: nowrap; }
        
        /* Hide the main dropdown block just in case */
        #google_translate_element { display: none !important; }
        body > .skiptranslate { display: none !important; }
        
        /* Force body not to have marginTop which google sometimes applies */
        body { margin-top: 0 !important; }
    `;
    document.head.appendChild(style);

    const gtContainer = document.createElement('div');
    gtContainer.id = 'google_translate_element';
    document.body.appendChild(gtContainer);

    window.googleTranslateElementInit = function() {
        new google.translate.TranslateElement({
            pageLanguage: 'ru',
            includedLanguages: 'en,ru',
            autoDisplay: false
        }, 'google_translate_element');
    };

    // Only load the script if the cookie asks for English
    const currentLang = document.cookie.includes('googtrans=/ru/en') ? 'en' : 'ru';
    
    if (currentLang === 'en') {
        const script = document.createElement('script');
        script.src = "https://translate.google.com/translate_a/element.js?cb=googleTranslateElementInit";
        document.body.appendChild(script);
    }
    
    // 2. Setup Buttons
    const langLinks = document.querySelectorAll('.lang-switch a');
    langLinks.forEach(link => {
        link.classList.remove('active');
        if (link.textContent.trim().toLowerCase() === currentLang) {
            link.classList.add('active');
        }
    });

    document.body.addEventListener('click', (e) => {
        const langLink = e.target.closest('.lang-switch a');
        if (langLink) {
            e.preventDefault();
            const text = langLink.textContent.trim().toLowerCase();
            
            if (text === 'en' && currentLang !== 'en') {
                setTranslateCookie('en');
                window.location.reload();
            } else if (text === 'ru' && currentLang !== 'ru') {
                setTranslateCookie('ru'); removeTranslateCookie();
                window.location.reload();
            }
        }
    });

    // Anti-FOUC (Flash of Untranslated Content) Unhide Logic
    if (currentLang === 'en') {
        const showContent = () => {
            if (document.documentElement.style.visibility) {
                // Set opacity to 0 BEFORE unhiding to prevent any 1-frame flashes
                document.documentElement.style.opacity = '0';
                document.documentElement.style.visibility = '';
                
                // Double rAF ensures the browser has painted the invisible state
                requestAnimationFrame(() => {
                    requestAnimationFrame(() => {
                        document.documentElement.style.transition = 'opacity 0.4s ease';
                        document.documentElement.style.opacity = '1';
                    });
                });
            }
        };

        const observer = new MutationObserver((mutations) => {
            if (document.documentElement.className.includes('translated-ltr') || document.documentElement.lang === 'en') {
                // GT adds the class *before* finishing text replacement. Wait 300ms for text to parse.
                setTimeout(showContent, 300);
                observer.disconnect();
            }
        });
        
        // Wait for class injection or language switch
        observer.observe(document.documentElement, { attributes: true, attributeFilter: ['class', 'lang'] });
        
        // Failsafe if translation takes too long or fails completely
        setTimeout(showContent, 1500);
    }
});
